# Academic Articles to Podcast

A Python project that converts academic articles from PDF to podcast audio. This project uses AI technology to automatically extract PDF content, generate academic summaries, and convert text to speech.

## Features

- 📄 **PDF Text Extraction**: Automatically extract text content from PDF files using `pdfplumber`
- 🤖 **AI-Powered Summarization**: Integrated with Qwen large language model for structured academic article summaries
- 🎙️ **Text-to-Speech**: Convert summaries to podcast-style audio using advanced TTS technology
- 🎯 **Academic Focus**: Optimized for academic articles in Economics, Sociology, Political Science and related fields

## Project Structure

```
project/
├── main.py                 # Main program entry point
├── ai_summary.py          # AI summarization module
├── text_to_audio.py       # Text-to-speech module
├── requirements.txt       # Project dependencies
├── output.wav            # Generated audio file
├── articles_example/     # Sample academic articles directory
│   ├── civic-responses-to-police-violence.pdf
│   └── contested-killings-the-mobilizing-effects-of-community-contact-with-police-violence.pdf
└── __pycache__/          # Python cache files
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nanawanzii/academic_articles_to_podcast.git
cd academic_articles_to_podcast
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or on Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Configure your Alibaba Cloud Qwen API key in `ai_summary.py`:

```python
api_key = "your-api-key-here"
```

## Usage

### Basic Usage

1. Place your academic PDF articles in the `articles_example/` directory
2. Run the main program:

```bash
python main.py
```

3. The program will automatically:
   - Scan PDF files in the directory
   - Extract text content
   - Generate AI summaries
   - Convert to audio files

### Generated Summary Content Includes

- **Research Question**: The core research question and its significance
- **Literature Review**: Theoretical background and current research status
- **Research Design & Methodology**: Detailed data sources, research design, and analytical methods
- **Conclusions & Contributions**: Main findings and their academic and policy implications

## Core Modules

### ai_summary.py
- Uses Qwen large language model for text summarization
- Specialized prompts optimized for academic articles
- Generates podcast-style summary content

### text_to_audio.py
- High-quality speech synthesis based on Tacotron2 model
- Supports natural pronunciation of English academic content
- Generates podcast-suitable audio format

### main.py
- Batch processing of PDF files
- Coordinates workflow between modules
- Automates the entire conversion process

## Tech Stack

- **Python 3.8+**
- **pdfplumber**: PDF text extraction
- **OpenAI API**: Qwen model via Alibaba Cloud compatible interface
- **TTS (Text-to-Speech)**: Deep learning-based speech synthesis
- **PyTorch**: Deep learning framework

## System Requirements

- Python 3.8 or higher
- At least 4GB RAM
- Internet connection (for API calls)
- GPU acceleration recommended (optional)

## Contributing

Welcome to submit Issues and Pull Requests to improve this project!

### Development Setup

1. Fork this repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact us through:

- GitHub Issues: [Project Issues Page](https://github.com/nanawanzii/academic_articles_to_podcast/issues)
- Email: your-email@example.com

## Changelog

### v1.0.0 (2025-09-03)
- Initial release
- PDF text extraction support
- AI summarization integration
- Text-to-speech implementation

---

**Note**: Please ensure compliance with relevant copyright laws and API usage terms when using this project.
