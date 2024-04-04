# PDF to MP3 Converter

This script converts PDF documents into MP3 audio files using OpenAI's text-to-speech API. It's designed to help users listen to written content on-the-go, making it particularly useful for those who prefer auditory learning or for visually impaired users.

## Features

- Converts PDF text to speech using a high-quality voice model.
- Splits large documents into manageable parts for processing.
- Combines audio segments into a single MP3 file for easy listening.

## Requirements

- Python 3.x
- OpenAI API Key
- [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/)
- [pydub](https://pypi.org/project/pydub/)
- [OpenAI Python Client](https://github.com/openai/openai-python)

## Installation

1. Clone this repository or download the script to your local machine.
2. Install the required Python packages:

```bash
pip install PyMuPDF pydub openai
```

3. Make sure you have [ffmpeg](https://ffmpeg.org/) installed on your system as `pydub` relies on it for audio file processing.

## Usage

1. Ensure you have your OpenAI API key ready. If not, obtain one from [OpenAI](https://openai.com/).

2. Use the script from the command line by providing the PDF file, the output MP3 file name, and your OpenAI API key:

```bash
python pdf_to_mp3.py <path/to/your/document.pdf> <output_file_name.mp3> <your_openai_api_key>
```

The script will process the PDF, convert its text to speech, and output an MP3 file.

## License

[MIT License](LICENSE)

This project is open-source and freely available for modification and distribution, subject to the terms of the MIT License.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or have identified any bugs.

## Acknowledgments

- OpenAI for providing the text-to-speech API.
- The developers of the libraries this script depends on: PyMuPDF, pydub, and the OpenAI Python client.

