# AI Writing Assistant & Audio Optimizer ✍️🤖

A specialized production-grade Python toolset designed for high-accuracy local audio transcription, optimized for execution on consumer hardware (such as Intel-based MacBooks). This repository combines a smart execution menu for writers with an automated audio pre-processing utility.

## 📦 Included Tools

* **Main Assistant (`scripts/main.py`)**: Integrates the `faster-whisper` engine using the 'Medium' AI model. Features a dynamic terminal menu to select recording files and seamlessly append transcriptions directly into new or existing text documents.
* **Audio Optimizer (`scripts/audio_optimizer.py`)**: A background utility utilizing FFmpeg to standardize raw audio recordings into standard WAV specifications (16kHz, mono, PCM 16-bit). This guarantees maximum speech-to-text recognition accuracy.

## 📁 Project Structure

* `scripts/` - Contains execution scripts (`main.py`, `audio_optimizer.py`).
* `recordings/` - Place your raw audio files here (input).
* `transcriptions/` - Where your transcribed text files will be saved (output).
* `requirements.txt` - List of necessary Python libraries.

## 🚀 Key Features

* **Hardware Optimized**: Specifically tuned with optimized threading (`OMP_NUM_THREADS=1`) and `int8` quantization to ensure stable, safe execution on 1.4 GHz CPUs without overheating.
* **VAD Filtering**: Employs Voice Activity Detection (VAD) to filter out background noise, long pauses, and silence.
* **Portable Codebase**: Built entirely with relative paths, making it easily deployable across different local environments.

## 🛠 Tech Stack

* **Language**: Python 3.x
* **Core Libraries**: Faster-Whisper, Asyncio, Logging
* **External Dependencies**: FFmpeg (for audio normalization)

---

## 💻 Getting Started

### 1. Prerequisites

Ensure you have **FFmpeg** installed on your system.

* **macOS**: `brew install ffmpeg`
* **Windows**: Download from ffmpeg.org and add to PATH.

### 2. Installation

Clone this repository and navigate to the project folder:

```bash
git clone https://github.com/wiktoria-spytek/StoryAI.git
cd StoryAI

```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

Install the dependencies:

```bash
pip install -r requirements.txt

```

> **Note for macOS users:** If you encounter a `Failed to build 'av'` error during installation, run: `pip install av --only-binary :all:` to bypass the local compilation issue.

### 3. Usage

1. Place your audio recordings in the `recordings/` folder.
2. Run the main assistant:

```bash
python scripts/main.py

```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
