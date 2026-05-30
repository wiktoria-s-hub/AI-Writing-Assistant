"""
AI WRITING ASSISTANT - TRANSCRIPTION ENGINE
-------------------------------------------
Author: Wiktoria Spytek
Description: 
A high-efficiency transcription tool designed for writers. 
Utilizes the 'faster-whisper' model (Medium) to convert local audio 
recordings into text drafts. 

Key Features:
- Local execution optimized for consumer hardware (Intel Macs).
- Dynamic file selection menu.
- VAD (Voice Activity Detection) for silence removal.
- Standardized text output for creative writing workflows.
"""


import os
import sys
import asyncio

# 1. FIX LIBRARY CONFLICT FOR INTEL CPUs
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1" 

import logging
from faster_whisper import WhisperModel

# Disable unnecessary logs, keep only errors
logging.basicConfig(level=logging.ERROR)

print("⌛ Initializing AI Companion (Model: Medium)...")

try:
    # Settings for 1.4 GHz processor - safe and stable
    model = WhisperModel(
        "medium", 
        device="cpu", 
        compute_type="int8", 
        cpu_threads=1, 
        num_workers=1
    )
    print("✅ AI Companion ready for work!")
except Exception as e:
    print(f"❌ CRITICAL STARTUP ERROR: {e}")
    sys.exit(1)

def transcribe_audio(audio_path):
    print(f"\n[AI WORKING] Listening to recording... (This may take a while ;)))) )")
    
    # vad_filter helps with long recordings and silence
    segments, info = model.transcribe(
        audio_path, 
        beam_size=5, 
        vad_filter=True, 
        vad_parameters=dict(min_silence_duration_ms=500)
    )

    full_text = []
    for segment in segments:
        # Displaying progress in real-time
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        full_text.append(segment.text)

    return " ".join(full_text).strip()

async def main_menu():
    print("\n=== YOUR PERSONAL WRITING ASSISTANT ===")
    
    # --- PATH DEFINITIONS ---
    # Using relative path for portability[cite: 7]
    project_root = "./"
    
    # Subdirectories (ensure these match your local folder structure!)
    audio_folder = os.path.join(project_root, "recordings")
    text_folder = os.path.join(project_root, "transcripts")

    # 1. SEARCH FOR RECORDINGS
    if not os.path.exists(audio_folder):
        print(f"❌ Recording folder not found: {audio_folder}")
        return

    files = [f for f in os.listdir(audio_folder) if f.endswith(".wav")]
    
    if not files:
        print(f"❌ 'Recordings' folder is empty.")
        return

    print("\n--- WHICH RECORDING DO YOU WANT TO TRANSCRIBE? ---")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    try:
        wybor = int(input("\nSelect recording number: ")) - 1
        audio_file = os.path.join(audio_folder, files[wybor])
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    # 2. SEARCH FOR TEXT FILES
    if not os.path.exists(text_folder):
        print(f"⚠️ 'Texts' folder not found, looking in root directory...")
        text_folder = project_root # Fallback: search in the main project folder if subfolder is missing

    txt_files = [f for f in os.listdir(text_folder) if f.endswith(".txt")]
    
    print("\n--- WHICH FILE SHOULD I APPEND THE TEXT TO? ---")
    for i, file in enumerate(txt_files, 1):
        print(f"{i}. {file}")
    print(f"{len(txt_files) + 1}. [CREATE NEW FILE IN TEXTS FOLDER]")

    try:
        choice_txt = int(input("\nSelect file number: ")) - 1
        if choice_txt == len(txt_files):
            new_name = input("Enter new file name: ")
            if not new_name.endswith(".txt"): new_name += ".txt"
            file_path = os.path.join(text_folder, new_name)
        else:
            file_path = os.path.join(text_folder, txt_files[choice_txt])
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    # --- START TRANSCRIPTION ---
    transcription_result = transcribe_audio(audio_file)
    
    if transcription_result:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n\n" + result_text)
        print(f"\n✅ Done! Text appended to: {os.path.basename(file_path)}")
    else:
        print("\n❌ Failed to generate text.")

if __name__ == "__main__":
    try:
        asyncio.run(main_menu()) 
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")        
