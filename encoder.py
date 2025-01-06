import base64
import time 
import numpy as np
import wave
import imageio
import os
import moviepy
import moviepy.editor
from moviepy.editor import AudioFileClip, ImageClip

start = time.perf_counter()
print("Hello World!")


with open('file.bin', 'rb') as file:
    # Read file :D
    binary_content = file.read()
    
    # bin converter >:)
    binary = ''.join(format(byte, '08b') for byte in binary_content)




#file conversion from .bin

def generate_tone(frequency, duration_ms, sample_rate=44100):
    duration_s = duration_ms / 1000  # Convert ms to seconds
    t = np.linspace(0, duration_s, int(sample_rate * duration_s), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t) * 32767  # 16-bit PCM format
    return tone.astype(np.int16)

# .wav creation
output_file = "file.wav"
sample_rate = 44100  
with wave.open(output_file, 'wb') as wf:
    wf.setnchannels(1)  
    wf.setsampwidth(2) 
    wf.setframerate(sample_rate)


    for i in binary:
        if i == "0":
            tone = generate_tone(4000, 5) 
        elif i == "1":
            tone = generate_tone(6000, 5) 
        
       
        wf.writeframes(tone.tobytes())
        
        
        

print(f"Binary sound sequence saved as {output_file}.")
#convert to video
image = ImageClip("83f1c636c6ab4d892a94b1c27a6ab54e.webp", duration=1)  
audio = AudioFileClip(output_file)
video = image.set_audio(audio)
video = video.set_duration(audio.duration)


video.write_videofile("binary_sound.mp4", codec="libx264", fps=24)

print("Audio has been converted to an MP4 file.")
os.remove(output_file)

#time end
end = time.perf_counter()
time = end-start

print(time*1000, "ms")
#pip install moviepy==1.0.3 numpy>=1.18.1 imageio>=2.5.0 decorator>=4.3.0 tqdm>=4.0.0 Pillow>=7.0.0 scipy>=1.3.0 pydub>=0.23.0 audiofile>=0.0.0 opencv-python>=4.5