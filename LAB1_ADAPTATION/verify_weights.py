"""
Weight File Verification Script
Validates exported binary weight files for C++ compatibility
"""

import os
import numpy as np
from tensorflow.keras.models import load_model

def verify_weight_files(model_path='audio_classifier_irmas.h5', 
                       weights_dir='model_weights'):
    """
    Verify that exported weight files match the model's actual weights
    """
    print("="*70)
    print("WEIGHT FILE VERIFICATION FOR C++ IMPLEMENTATION")
    print("="*70)
    
    # Load the model
    print(f"\nLoading model from: {model_path}")
    model = load_model(model_path)
    
    print("\n" + "-"*70)
    print("LAYER-BY-LAYER WEIGHT VERIFICATION")
    print("-"*70)
    
    total_size_bytes = 0
    verification_results = []
    
    for i, layer in enumerate(model.layers):
        if len(layer.get_weights()) > 0:
            weights = layer.get_weights()
            layer_name = layer.name
            layer_type = layer.__class__.__name__
            
            print(f"\nLayer {i}: {layer_name} ({layer_type})")
            print("-" * 50)
            
            # Verify weights
            if len(weights) > 0:
                weight_array = weights[0]
                weight_file = os.path.join(weights_dir, f'{layer_name}_weights.bin')
                
                if os.path.exists(weight_file):
                    # Read binary file
                    loaded_weights = np.fromfile(weight_file, dtype=np.float32)
                    expected_size = np.prod(weight_array.shape)
                    file_size = os.path.getsize(weight_file)
                    
                    print(f"  Weights File: {weight_file}")
                    print(f"    Shape: {weight_array.shape}")
                    print(f"    Elements: {expected_size:,}")
                    print(f"    File Size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
                    print(f"    Expected Size: {expected_size * 4:,} bytes")
                    
                    # Verify size
                    if len(loaded_weights) == expected_size:
                        print(f"    ✓ Size match!")
                    else:
                        print(f"    ✗ SIZE MISMATCH! Got {len(loaded_weights)}, expected {expected_size}")
                    
                    # Verify values (sample check)
                    loaded_weights_reshaped = loaded_weights.reshape(weight_array.shape)
                    max_diff = np.max(np.abs(loaded_weights_reshaped - weight_array))
                    
                    if max_diff < 1e-6:
                        print(f"    ✓ Values match (max diff: {max_diff:.2e})")
                        verification_results.append(("✓", layer_name, "weights"))
                    else:
                        print(f"    ✗ VALUE MISMATCH! Max difference: {max_diff:.2e}")
                        verification_results.append(("✗", layer_name, "weights"))
                    
                    total_size_bytes += file_size
                else:
                    print(f"  ✗ Weights file NOT FOUND: {weight_file}")
                    verification_results.append(("✗", layer_name, "weights - FILE MISSING"))
            
            # Verify biases
            if len(weights) > 1:
                bias_array = weights[1]
                bias_file = os.path.join(weights_dir, f'{layer_name}_bias.bin')
                
                if os.path.exists(bias_file):
                    loaded_bias = np.fromfile(bias_file, dtype=np.float32)
                    expected_size = np.prod(bias_array.shape)
                    file_size = os.path.getsize(bias_file)
                    
                    print(f"  Bias File: {bias_file}")
                    print(f"    Shape: {bias_array.shape}")
                    print(f"    Elements: {expected_size:,}")
                    print(f"    File Size: {file_size:,} bytes")
                    
                    # Verify size
                    if len(loaded_bias) == expected_size:
                        print(f"    ✓ Size match!")
                    else:
                        print(f"    ✗ SIZE MISMATCH! Got {len(loaded_bias)}, expected {expected_size}")
                    
                    # Verify values
                    max_diff = np.max(np.abs(loaded_bias - bias_array))
                    
                    if max_diff < 1e-6:
                        print(f"    ✓ Values match (max diff: {max_diff:.2e})")
                        verification_results.append(("✓", layer_name, "bias"))
                    else:
                        print(f"    ✗ VALUE MISMATCH! Max difference: {max_diff:.2e}")
                        verification_results.append(("✗", layer_name, "bias"))
                    
                    total_size_bytes += file_size
                else:
                    print(f"  ✗ Bias file NOT FOUND: {bias_file}")
                    verification_results.append(("✗", layer_name, "bias - FILE MISSING"))
    
    # Summary
    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    
    passed = sum(1 for r in verification_results if r[0] == "✓")
    total = len(verification_results)
    
    print(f"\nTotal Files Verified: {total}")
    print(f"Passed: {passed} / {total}")
    print(f"Failed: {total - passed} / {total}")
    print(f"\nTotal Weight Data Size: {total_size_bytes:,} bytes ({total_size_bytes/1024/1024:.2f} MB)")
    
    if total - passed == 0:
        print("\n✓✓✓ ALL WEIGHT FILES VERIFIED SUCCESSFULLY! ✓✓✓")
        print("Your binary files are ready for C++ implementation.")
    else:
        print("\n✗ VERIFICATION FAILED - Please check the errors above")
    
    print("\n" + "="*70)
    
    return verification_results, total_size_bytes


def print_cpp_loading_code():
    """
    Generate C++ code snippets for loading each weight file
    """
    print("\n" + "="*70)
    print("C++ CODE SNIPPETS FOR LOADING WEIGHTS")
    print("="*70)
    
    weight_specs = [
        ("conv1_1_weights.bin", 5*5*1*32, "(5, 5, 1, 32)"),
        ("conv1_1_bias.bin", 32, "(32,)"),
        ("conv1_2_weights.bin", 5*5*32*32, "(5, 5, 32, 32)"),
        ("conv1_2_bias.bin", 32, "(32,)"),
        ("conv2_1_weights.bin", 3*3*32*64, "(3, 3, 32, 64)"),
        ("conv2_1_bias.bin", 64, "(64,)"),
        ("conv2_2_weights.bin", 3*3*64*64, "(3, 3, 64, 64)"),
        ("conv2_2_bias.bin", 64, "(64,)"),
        ("conv3_1_weights.bin", 3*3*64*64, "(3, 3, 64, 64)"),
        ("conv3_1_bias.bin", 64, "(64,)"),
        ("conv3_2_weights.bin", 3*3*64*128, "(3, 3, 64, 128)"),
        ("conv3_2_bias.bin", 128, "(128,)"),
        ("fc1_weights.bin", 18432*256, "(18432, 256)"),
        ("fc1_bias.bin", 256, "(256,)"),
        ("fc2_weights.bin", 256*10, "(256, 10)"),
        ("fc2_bias.bin", 10, "(10,)"),
    ]
    
    print("\n// Function to load weights from binary file")
    print("std::vector<float> loadWeights(const std::string& filename, size_t expected_size) {")
    print("    std::ifstream file(filename, std::ios::binary);")
    print("    if (!file) {")
    print("        throw std::runtime_error(\"Cannot open file: \" + filename);")
    print("    }")
    print("    ")
    print("    std::vector<float> weights(expected_size);")
    print("    file.read(reinterpret_cast<char*>(weights.data()), expected_size * sizeof(float));")
    print("    ")
    print("    if (!file) {")
    print("        throw std::runtime_error(\"Error reading file: \" + filename);")
    print("    }")
    print("    ")
    print("    return weights;")
    print("}")
    print("\n// Load all weights")
    
    for filename, size, shape in weight_specs:
        var_name = filename.replace('.bin', '').replace('-', '_')
        print(f"auto {var_name} = loadWeights(\"model_weights/{filename}\", {size});  // Shape: {shape}")


def print_input_spec():
    """
    Print detailed input specification
    """
    print("\n" + "="*70)
    print("INPUT SPECIFICATION FOR C++ IMPLEMENTATION")
    print("="*70)
    
    print("\nInput Mel-Spectrogram Dimensions:")
    print("  Height:       128 pixels (mel frequency bands)")
    print("  Width:        128 pixels (time frames)")
    print("  Channels:     1 (grayscale)")
    print("  Data Type:    float32")
    print("  Value Range:  [0.0, 1.0] (normalized)")
    print("  Total Size:   128 × 128 × 1 × 4 bytes = 65,536 bytes (64 KB)")
    print("\nMemory Layout:")
    print("  Row-major order (C-style): [row][col][channel]")
    print("  For pixel at (h, w, c): index = (h * 128 + w) * 1 + c")
    print("\nAudio Processing Parameters:")
    print("  Sample Rate:  22,050 Hz")
    print("  Duration:     3.0 seconds")
    print("  FFT Size:     2048")
    print("  Hop Length:   512 samples")
    print("  Mel Bands:    128")


if __name__ == "__main__":
    # Verify weight files
    results, total_size = verify_weight_files()
    
    # Print input specification
    print_input_spec()
    
    # Generate C++ code
    print_cpp_loading_code()
    
    print("\n" + "="*70)
    print("VERIFICATION COMPLETE")
    print("="*70)
    print("\nNext Steps:")
    print("1. Review MODEL_SUMMARY_FOR_CPP.md for complete documentation")
    print("2. Use the C++ code snippets above to load weights")
    print("3. Validate C++ implementation against feature_maps/*.bin files")
    print("="*70)
