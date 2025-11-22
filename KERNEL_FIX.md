# Fix Jupyter Notebook Kernel Issue - "No module named 'numpy'"

## Problem
Your notebook is using a Python kernel that doesn't have the required packages (numpy, tensorflow, librosa, etc.) installed.

## Solution: Select the Correct Python Kernel

### Method 1: Using VS Code Kernel Selector (Recommended)

1. **Open your notebook** (`week1_audio_classifier.ipynb`) in VS Code

2. **Click on the kernel selector** in the top-right corner of the notebook
   - It might show something like "Python 3.x.x" or a different Python version

3. **Select "Select Another Kernel..."** from the dropdown

4. **Choose "Python Environments..."**

5. **Select the Python 3.13.5 interpreter**:
   ```
   Python 3.13.5 ('C:\Program Files\Python313\python.exe')
   ```
   Or look for:
   ```
   C:\Program Files\Python313\python.exe
   ```

6. **Wait for the kernel to connect** (you'll see a checkmark when ready)

7. **Run the first cell again** to verify numpy imports successfully

### Method 2: Using Command Palette

1. Press `Ctrl+Shift+P` to open Command Palette

2. Type: **"Notebook: Select Notebook Kernel"**

3. Select **"Python Environments..."**

4. Choose **Python 3.13.5** from `C:\Program Files\Python313\python.exe`

5. Run your notebook cells again

### Method 3: Restart VS Code

Sometimes VS Code needs a restart to detect the correct Python environment:

1. Close VS Code completely
2. Reopen VS Code
3. Open the notebook
4. Select the kernel using Method 1 above

## Verify the Fix

After selecting the correct kernel, run this in a notebook cell:

```python
import sys
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

import numpy as np
print(f"NumPy version: {np.__version__}")

import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")

import librosa
print(f"Librosa version: {librosa.__version__}")
```

**Expected Output:**
```
Python executable: C:\Program Files\Python313\python.exe
Python version: 3.13.5 ...
NumPy version: 2.3.5
TensorFlow version: 2.20.0
Librosa version: 0.11.0
```

## Still Not Working?

If the kernel selector doesn't show Python 3.13.5, you may need to install ipykernel:

```powershell
& "C:/Program Files/Python313/python.exe" -m pip install ipykernel
& "C:/Program Files/Python313/python.exe" -m ipykernel install --user --name python313 --display-name "Python 3.13.5"
```

Then restart VS Code and select the "Python 3.13.5" kernel.

## All Installed Packages

Your Python 3.13.5 environment has ALL required packages:

✅ TensorFlow 2.20.0
✅ librosa 0.11.0  
✅ numpy 2.3.5
✅ pandas 2.3.3
✅ matplotlib 3.10.7
✅ scikit-learn 1.7.2
✅ scipy 1.16.3
✅ soundfile 0.13.1
✅ h5py 3.15.1
✅ seaborn 0.13.2
✅ jupyter, jupyterlab, ipykernel

**You just need to make sure your notebook is using this Python environment!**
