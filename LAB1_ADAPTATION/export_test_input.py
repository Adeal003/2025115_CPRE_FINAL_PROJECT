"""
Export Test Input for C++ Implementation
Generates test_input.bin - a mel-spectrogram for C++ validation
"""

import os
import numpy as np
import librosa

# Same parameters as in the notebook
SAMPLE_RATE = 22050
N_FFT = 2048
HOP_LENGTH = 512
N_MELS = 128
DURATION = 3.0
TARGET_SHAPE = (128, 128, 1)

def audio_to_melspectrogram(audio_path, sr=SAMPLE_RATE, n_mels=N_MELS, 
                           duration=DURATION, target_shape=TARGET_SHAPE):
    """
    Convert audio file to mel-spectrogram (same as notebook)
    """
    # Load audio file
    y, sr_actual = librosa.load(audio_path, sr=sr, duration=duration)
    
    # Pad if too short
    target_length = int(sr * duration)
    if len(y) < target_length:
        y = np.pad(y, (0, target_length - len(y)), mode='constant')
    
    # Generate mel-spectrogram
    mel_spec = librosa.feature.melspectrogram(
        y=y, 
        sr=sr, 
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        n_mels=n_mels
    )
    
    # Convert to log scale (dB)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    # Normalize to [0, 1]
    mel_spec_norm = (mel_spec_db - mel_spec_db.min()) / (mel_spec_db.max() - mel_spec_db.min())
    
    # Resize to target shape if needed
    if mel_spec_norm.shape != target_shape[:2]:
        from scipy.ndimage import zoom
        zoom_factors = (target_shape[0] / mel_spec_norm.shape[0], 
                       target_shape[1] / mel_spec_norm.shape[1])
        mel_spec_norm = zoom(mel_spec_norm, zoom_factors, order=1)
    
    # Add channel dimension
    mel_spec_norm = np.expand_dims(mel_spec_norm, axis=-1)
    
    return mel_spec_norm.astype(np.float32)


def export_test_input(audio_file_path, output_file='test_input.bin'):
    """
    Export a test mel-spectrogram for C++ validation
    """
    print("="*70)
    print("EXPORTING TEST INPUT FOR C++ IMPLEMENTATION")
    print("="*70)
    
    print(f"\nAudio File: {audio_file_path}")
    
    if not os.path.exists(audio_file_path):
        print(f"ERROR: Audio file not found: {audio_file_path}")
        return False
    
    # Generate mel-spectrogram
    print("Generating mel-spectrogram...")
    mel_spec = audio_to_melspectrogram(audio_file_path)
    
    print(f"\nMel-Spectrogram Shape: {mel_spec.shape}")
    print(f"Data Type: {mel_spec.dtype}")
    print(f"Value Range: [{mel_spec.min():.4f}, {mel_spec.max():.4f}]")
    print(f"Total Elements: {mel_spec.size}")
    print(f"Total Size: {mel_spec.nbytes} bytes ({mel_spec.nbytes/1024:.2f} KB)")
    
    # Export as binary file
    print(f"\nExporting to: {output_file}")
    mel_spec.tofile(output_file)
    
    # Verify export
    file_size = os.path.getsize(output_file)
    print(f"✓ File created successfully!")
    print(f"  File size: {file_size} bytes ({file_size/1024:.2f} KB)")
    
    # Verify by reading back
    print("\nVerifying export...")
    loaded = np.fromfile(output_file, dtype=np.float32)
    loaded = loaded.reshape(mel_spec.shape)
    
    if np.allclose(loaded, mel_spec):
        print("✓ Verification successful - file matches original data")
    else:
        print("✗ WARNING: Verification failed - file doesn't match original")
        return False
    
    print("\n" + "="*70)
    print("EXPORT COMPLETE")
    print("="*70)
    print(f"\nYou can now use '{output_file}' with your C++ implementation")
    print("Place it in the 'data/' directory for your C++ program to load")
    
    return True


if __name__ == "__main__":
    # Define paths
    IRMAS_PATH = r"U:\cpre_587\2025115_CPRE_FINAL_PROJECT\LAB1_ADAPTATION\irmas_dataset"
    TRAIN_PATH = os.path.join(IRMAS_PATH, "IRMAS-TrainingData")
    
    # Try to find a test audio file
    instrument_classes = ['cel', 'cla', 'flu', 'gac', 'gel', 'org', 'pia', 'sax', 'tru', 'vio']
    
    test_audio_file = None
    
    # Search for the first available audio file
    for inst in instrument_classes:
        inst_path = os.path.join(TRAIN_PATH, inst)
        if os.path.exists(inst_path):
            audio_files = [f for f in os.listdir(inst_path) if f.endswith('.wav')]
            if audio_files:
                test_audio_file = os.path.join(inst_path, audio_files[0])
                print(f"Found test audio: {test_audio_file}")
                print(f"Instrument class: {inst}")
                break
    
    if test_audio_file:
        # Export test input
        success = export_test_input(test_audio_file, output_file='test_input.bin')
        
        if success:
            print("\n" + "="*70)
            print("NEXT STEPS")
            print("="*70)
            print("1. Move 'test_input.bin' to your C++ project's 'data/' directory")
            print("2. Run your C++ program to test inference")
            print("3. Compare C++ outputs with feature_maps/*.bin for validation")
    else:
        print("\nERROR: No audio files found in IRMAS dataset!")
        print(f"Please check that the dataset exists at: {TRAIN_PATH}")
        print("\nYou can manually specify an audio file:")
        print("  python export_test_input.py /path/to/audio.wav")
