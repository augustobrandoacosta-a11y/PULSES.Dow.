import numpy as np
from scipy.io import wavfile

def generate_pulsar_tone(filename, frequency_hz, duration_sec=5, sample_rate=44100):
    """Generates a rhythmic 'click' based on pulsar rotation frequency."""
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    
    # Create a pulse train (a series of sharp peaks)
    # The pulsar 'ticks' at a specific frequency (Hz)
    signal = np.sin(2 * np.pi * frequency_hz * t)
    
    # Sharpen the sine wave into a narrow pulse (simulating the 'beam' hitting Earth)
    signal = np.where(signal > 0.98, 1.0, 0.0)
    
    # Soften the click slightly so it doesn't hurt your ears
    signal = np.convolve(signal, np.ones(10)/10, mode='same')
    
    # Normalize to 16-bit PCM range
    audio_data = (signal * 32767).astype(np.int16)
    
    wavfile.write(filename, sample_rate, audio_data)
    print(f"Generated: {filename}")

# Pulsar Data (Rotational Frequencies)
# Vela Pulsar (PSR B0833-45): Rotates ~11.19 times per second
# Crab Pulsar (PSR B0531+21): Rotates ~30.2 times per second

generate_pulsar_tone("vela_pulsar.wav", frequency_hz=11.19)
generate_pulsar_tone("crab_pulsar.wav", frequency_hz=30.2)
