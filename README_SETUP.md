# CPRE 587 Audio Classification Project Setup

## Virtual Environment Created Successfully! 🎉

**Environment Name:** `cpre587_env`  
**Location:** `U:\cpre_587\2025115_CPRE_FINAL_PROJECT\cpre587_env`  
**Jupyter Kernel:** "CPRE587 Audio Classification"

## ✅ Installed Packages Summary

### Core Scientific Computing
- numpy (2.3.4)
- pandas (2.3.3) 
- scipy (1.16.3)
- matplotlib (3.10.7)
- scikit-learn (1.7.2)

### Deep Learning
- tensorflow (2.20.0)
- keras (3.11.3)

### Audio Processing  
- librosa (0.11.0)
- soundfile (0.13.1)
- audioread (3.1.0)

### Jupyter & Development
- jupyter (1.1.1)
- jupyterlab (4.4.10)
- ipykernel (7.1.0)
- ipython (9.7.0)

## 🚀 How to Use Your Environment

### Method 1: VS Code Jupyter Kernel Selection
1. Open your notebook in VS Code
2. Click **"Select Kernel"** in the top-right corner
3. Choose **"CPRE587 Audio Classification"** from the dropdown
4. Start running cells!

### Method 2: Activate in Terminal (PowerShell)
```powershell
# Navigate to project directory
Set-Location "U:\cpre_587\2025115_CPRE_FINAL_PROJECT"

# Activate virtual environment
.\cpre587_env\Scripts\Activate.ps1

# Now you're in the environment - run jupyter or python commands
jupyter lab
```

### Method 3: Direct Python Execution
```powershell
# Run Python scripts directly with the virtual environment
.\cpre587_env\Scripts\python.exe your_script.py
```

## 📁 Project Structure
```
U:\cpre_587\2025115_CPRE_FINAL_PROJECT\
├── cpre587_env/                    # Virtual environment
├── LAB1_ADAPTATION/
│   ├── week1_audio_classifier.ipynb  # Main notebook
│   ├── requirements.txt              # Package list
│   └── irmas_dataset/               # Audio dataset
└── README_SETUP.md                 # This file
```

## 🔧 Quick Verification Test

Run this in your notebook to verify everything works:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import tensorflow as tf

print("✅ All packages loaded successfully!")
print(f"TensorFlow: {tf.__version__}")
print(f"Librosa: {librosa.__version__}")
print(f"NumPy: {np.__version__}")
```

## 💡 Pro Tips

1. **Persistent Environment:** Your virtual environment will persist between sessions on the virtual lab computer.

2. **Kernel Selection:** Always select "CPRE587 Audio Classification" kernel when opening notebooks.

3. **Package Management:** To install additional packages:
   ```powershell
   .\cpre587_env\Scripts\Activate.ps1
   pip install package_name
   ```

4. **Backup:** Your environment is in your U: drive, so it should be backed up automatically.

## 🆘 Troubleshooting

**Problem:** Can't see the kernel in VS Code
**Solution:** 
- Close and reopen VS Code
- Use Ctrl+Shift+P → "Python: Select Interpreter" → Choose the cpre587_env python.exe

**Problem:** Import errors
**Solution:**
- Make sure you selected the correct kernel
- Restart the kernel (Kernel → Restart)

**Problem:** Environment not activating
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\cpre587_env\Scripts\Activate.ps1
```

## 🎯 Your notebook is now ready to run!

All dependencies are installed and the kernel is registered. You should be able to:
- ✅ Load audio files with librosa
- ✅ Process spectrograms
- ✅ Train CNN models with TensorFlow
- ✅ Visualize results with matplotlib
- ✅ Work with the IRMAS dataset

Happy coding! 🎵🤖
