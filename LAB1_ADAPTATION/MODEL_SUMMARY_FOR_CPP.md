# Audio CNN Model Summary for C++ Implementation

## Input Mel-Spectrogram Dimensions

### Input Specifications
- **Height**: 128 (mel frequency bands)
- **Width**: 128 (time frames)
- **Channels**: 1 (single-channel grayscale spectrogram)
- **Full Input Shape**: `(128, 128, 1)`
- **Data Type**: `float32`
- **Value Range**: [0.0, 1.0] (normalized)

### Audio Processing Parameters
- **Sample Rate**: 22,050 Hz
- **Duration**: 3.0 seconds (fixed)
- **FFT Size (N_FFT)**: 2048
- **Hop Length**: 512 samples
- **Number of Mel Bands**: 128
- **Preprocessing**: Power-to-dB conversion, min-max normalization to [0,1]

---

## Model Architecture Summary

### Layer-by-Layer Breakdown

| Layer # | Layer Name | Type | Input Shape | Output Shape | Parameters |
|---------|------------|------|-------------|--------------|------------|
| 0 | conv1_1 | Conv2D | (128, 128, 1) | (124, 124, 32) | 832 |
| 1 | conv1_2 | Conv2D | (124, 124, 32) | (120, 120, 32) | 25,632 |
| 2 | pool1 | MaxPool2D | (120, 120, 32) | (60, 60, 32) | 0 |
| 3 | conv2_1 | Conv2D | (60, 60, 32) | (58, 58, 64) | 18,496 |
| 4 | conv2_2 | Conv2D | (58, 58, 64) | (56, 56, 64) | 36,928 |
| 5 | pool2 | MaxPool2D | (56, 56, 64) | (28, 28, 64) | 0 |
| 6 | conv3_1 | Conv2D | (28, 28, 64) | (26, 26, 64) | 36,928 |
| 7 | conv3_2 | Conv2D | (26, 26, 64) | (24, 24, 128) | 73,856 |
| 8 | pool3 | MaxPool2D | (24, 24, 128) | (12, 12, 128) | 0 |
| 9 | flatten | Flatten | (12, 12, 128) | (18,432) | 0 |
| 10 | fc1 | Dense | (18,432) | (256) | 4,718,848 |
| 11 | dropout | Dropout | (256) | (256) | 0 |
| 12 | fc2 | Dense | (256) | (10) | 2,570 |

**Total Parameters**: 4,914,090

---

## Exported Weight Files (Binary Format)

### File Format Specifications
- **Data Type**: 32-bit floating point (float32)
- **Byte Order**: Little-endian (platform default)
- **Layout**: Row-major order (C-style)
- **No Header**: Raw binary data only

### Weight Files Exported

#### Convolutional Layers
1. **conv1_1_weights.bin**
   - Shape: `(5, 5, 1, 32)` → Kernel: 5×5, Input channels: 1, Output channels: 32
   - Size: 800 floats = 3,200 bytes
   - Layout: `[kernel_h, kernel_w, in_channels, out_channels]`

2. **conv1_1_bias.bin**
   - Shape: `(32,)`
   - Size: 32 floats = 128 bytes

3. **conv1_2_weights.bin**
   - Shape: `(5, 5, 32, 32)` → Kernel: 5×5, Input: 32, Output: 32
   - Size: 25,600 floats = 102,400 bytes

4. **conv1_2_bias.bin**
   - Shape: `(32,)`
   - Size: 32 floats = 128 bytes

5. **conv2_1_weights.bin**
   - Shape: `(3, 3, 32, 64)` → Kernel: 3×3, Input: 32, Output: 64
   - Size: 18,432 floats = 73,728 bytes

6. **conv2_1_bias.bin**
   - Shape: `(64,)`
   - Size: 64 floats = 256 bytes

7. **conv2_2_weights.bin**
   - Shape: `(3, 3, 64, 64)` → Kernel: 3×3, Input: 64, Output: 64
   - Size: 36,864 floats = 147,456 bytes

8. **conv2_2_bias.bin**
   - Shape: `(64,)`
   - Size: 64 floats = 256 bytes

9. **conv3_1_weights.bin**
   - Shape: `(3, 3, 64, 64)` → Kernel: 3×3, Input: 64, Output: 64
   - Size: 36,864 floats = 147,456 bytes

10. **conv3_1_bias.bin**
    - Shape: `(64,)`
    - Size: 64 floats = 256 bytes

11. **conv3_2_weights.bin**
    - Shape: `(3, 3, 64, 128)` → Kernel: 3×3, Input: 64, Output: 128
    - Size: 73,728 floats = 294,912 bytes

12. **conv3_2_bias.bin**
    - Shape: `(128,)`
    - Size: 128 floats = 512 bytes

#### Fully Connected Layers
13. **fc1_weights.bin**
    - Shape: `(18432, 256)` → Input: 18,432, Output: 256
    - Size: 4,718,592 floats = 18,874,368 bytes (≈18 MB)

14. **fc1_bias.bin**
    - Shape: `(256,)`
    - Size: 256 floats = 1,024 bytes

15. **fc2_weights.bin**
    - Shape: `(256, 10)` → Input: 256, Output: 10 classes
    - Size: 2,560 floats = 10,240 bytes

16. **fc2_bias.bin**
    - Shape: `(10,)`
    - Size: 10 floats = 40 bytes

---

## C++ Implementation Notes

### Reading Binary Files in C++

```cpp
// Example: Reading a weight file
std::vector<float> loadWeights(const std::string& filename, size_t expected_size) {
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        throw std::runtime_error("Cannot open file: " + filename);
    }
    
    std::vector<float> weights(expected_size);
    file.read(reinterpret_cast<char*>(weights.data()), 
              expected_size * sizeof(float));
    
    if (!file) {
        throw std::runtime_error("Error reading file: " + filename);
    }
    
    return weights;
}

// Usage example for conv1_1
auto conv1_1_weights = loadWeights("conv1_1_weights.bin", 5*5*1*32);  // 800 floats
auto conv1_1_bias = loadWeights("conv1_1_bias.bin", 32);              // 32 floats
```

### Weight Tensor Layout (TensorFlow/Keras Convention)
- **Conv2D Weights**: `[kernel_height, kernel_width, input_channels, output_channels]`
- **Dense Weights**: `[input_features, output_features]`
- **Biases**: `[output_channels]` or `[output_features]`

### Important Considerations for C++

1. **Data Layout**: TensorFlow uses row-major order, which matches C++ arrays
2. **Convolution Padding**: All conv layers use "valid" padding (no padding)
3. **Activation Functions**: 
   - Conv layers: ReLU → `max(0, x)`
   - Final layer: Softmax → for classification output
4. **Pooling**: MaxPooling2D with 2×2 kernel and stride 2
5. **Dropout**: Only used during training, skip in inference

### Validation Strategy

The `feature_maps/` directory contains intermediate outputs from each layer:
- Use these to validate your C++ implementation layer-by-layer
- Compare C++ layer outputs with Python outputs (tolerance: ±1e-5)

---

## Output Classes (10 Instruments)

| Index | Instrument Code | Full Name |
|-------|----------------|-----------|
| 0 | cel | Cello |
| 1 | cla | Clarinet |
| 2 | flu | Flute |
| 3 | gac | Acoustic Guitar |
| 4 | gel | Electric Guitar |
| 5 | org | Organ |
| 6 | pia | Piano |
| 7 | sax | Saxophone |
| 8 | tru | Trumpet |
| 9 | vio | Violin |

---

## Verification Checklist

- [x] Input dimensions: 128 × 128 × 1
- [x] All weight files exported as float32 binary
- [x] Weight shapes documented
- [x] Intermediate feature maps exported for validation
- [x] Total of 16 weight/bias files (6 conv layers + 2 dense layers)
- [x] Largest file: fc1_weights.bin (≈18 MB)
- [x] No compression or encoding applied
- [x] Little-endian byte order (standard for x86/x64)

---

## Quick File Size Verification

Run this to verify all weight files are correctly sized:

```bash
# PowerShell
Get-ChildItem model_weights/*.bin | Select-Object Name, Length | Format-Table
```

Expected total size: **≈19.5 MB** for all weight files combined.
