import os
import subprocess

# --- PATH CONFIGURATION ---
# Using the standardized relative path for the repository
RECORDINGS_FOLDER = "./recordings/"

def optimize_audio_files():
    print("=== AUTOMATIC AUDIO OPTIMIZER ===")
    
    # Check if directory exists before scanning
    if not os.path.exists(RECORDINGS_FOLDER):
        print(f"❌ Target directory not found: {RECORDINGS_FOLDER}")
        return

    files = [f for f in os.listdir(RECORDINGS_FOLDER) if f.endswith('.wav')]
    
    if not files:
        print("ℹ️ No .wav files found in the recordings folder.")
        return
    
    for file in files:
        file_path = os.path.join(RECORDINGS_FOLDER, file)
        temp_file_path = os.path.join(RECORDINGS_FOLDER, f"fixed_{file}")
        
        print(f"Checking and processing: {file}...")
        
        # FFmpeg command to enforce standard WAV specifications (16kHz, mono, PCM 16-bit)
        # This optimal configuration ensures maximum transcription accuracy for AI engines.
        cmd = [
            'ffmpeg', '-y', '-i', file_path, 
            '-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le', 
            temp_file_path
        ]
        
        try:
            # Run the conversion process silently
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            # Replace the original file with the optimized version
            os.replace(temp_file_path, file_path)
            print(f"✅ {file} successfully optimized for AI processing!")
        except Exception as e:
            print(f"❌ Failed to process {file}: {e}")
            # Clean up temp file if conversion failed
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

if __name__ == "__main__":
    optimize_audio_files()
