# AI Writing Assistant & Audio Optimizer

A specialized production-grade Python toolset designed for high-accuracy local audio transcription, optimized for execution on consumer hardware (such as Intel-based MacBooks). This repository combines a smart execution menu for writers with an automated audio pre-processing utility.

## 📦 Included Tools

* **Main Assistant (`main.py`):** Integrates the `faster-whisper` engine using the 'Medium' AI model. Features a dynamic terminal menu to select recording files and seamlessly append transcriptions directly into new or existing text documents.
* **Audio Optimizer (`audio_optimizer.py`):** A background utility utilizing FFmpeg to standardize raw audio recordings into standard WAV specifications (16kHz, mono, PCM 16-bit). This guarantees maximum speech-to-text recognition accuracy.

## 🚀 Key Features

* **Hardware Optimized:** Specifically tuned with optimized threading (`OMP_NUM_THREADS=1`) and `int8` quantization to ensure stable, safe execution on 1.4 GHz CPUs without overheating.
* **VAD Filtering:** Employs Voice Activity Detection (VAD) to filter out background noise, long pauses, and silence.
* **Portable Codebase:** Built entirely with relative paths, making it easily deployable across different local environments.

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Core Libraries:** Faster-Whisper, Asyncio, Logging
* **External Dependencies:** FFmpeg (for audio normalization)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
