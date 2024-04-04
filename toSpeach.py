from openai import AsyncOpenAI
import asyncio
from pathlib import Path
import argparse
import os
import fitz
from pydub import AudioSegment
import re


def sort_key(filename):
    match = re.match(r"(\d+)", filename)
    if match:
        return int(match.group())
    return 0


def sort_fileList(fileList):
    return sorted(fileList, key=sort_key)


def combine_audio_files(audio_files, output_file):
    combined = AudioSegment.empty()
    for audio_file in audio_files:
        combined += AudioSegment.from_file(audio_file)
    combined.export(output_file, format="mp3")


def pdf_to_text(pdf_file):
    pdf_document = fitz.open(pdf_file)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text


def split_text(text, max_length=4000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


async def text_to_speech(text, fileName, apikey):
    client = AsyncOpenAI(api_key=apikey)
    speech_file_path = Path(__file__).parent / f"{fileName}.mp3"
    response = await client.audio.speech.create(
        model="tts-1", voice="nova", input=text)

    await asyncio.to_thread(response.stream_to_file, speech_file_path)
    return str(speech_file_path)


async def main(pdf_file, output_file, apikey):
    text = pdf_to_text(pdf_file)
    text_parts = split_text(text)
    audio_file_futures = []
    for i, text_part in enumerate(text_parts):
        fileName = f"part_{i}"
        audio_file_futures.append(text_to_speech(text_part, fileName, apikey))
    audio_files = await asyncio.gather(*audio_file_futures)
    combine_audio_files(sort_fileList(audio_files), output_file)
    for audio_file in audio_files:
        os.remove(audio_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a PDF to an MP3 file")
    parser.add_argument("pdf_file", type=str, help="The PDF file to convert")
    parser.add_argument("output_file", type=str, help="The output MP3 file")
    parser.add_argument("apikey", type=str, help="OpenAI API key")
    args = parser.parse_args()

    asyncio.run(main(args.pdf_file, args.output_file, args.apikey))
