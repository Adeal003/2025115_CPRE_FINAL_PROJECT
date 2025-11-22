# QUICK FIX: Select the Correct Kernel in VS Code

## The Problem
Your notebook shows: `ModuleNotFoundError: No module named 'numpy'`

**This means your notebook is using the WRONG Python kernel.**

## ✅ The Solution (Takes 30 seconds)

### Step-by-Step Instructions:

1. **Look at the TOP-RIGHT corner of your notebook** in VS Code
   - You'll see a button showing the current kernel (e.g., "Python 3.x.x")

2. **CLICK on that kernel button**

3. **In the dropdown that appears:**
   - Click "Select Another Kernel..."
   - Then click "Python Environments..."

4. **Select this exact kernel:**
   ```
   Python 3.13.5 (All Packages)
   ```
   OR if you see:
   ```
   Python 3.13.5
   C:\Program Files\Python313\python.exe
   ```

5. **Wait 2-3 seconds** for the kernel to start

6. **Run your first notebook cell again** - numpy should now import successfully!

## Visual Guide

```
┌─────────────────────────────────────────────────────┐
│  week1_audio_classifier.ipynb                       │
│                                    [Python 3.x.x ▼] │ ← CLICK HERE
│─────────────────────────────────────────────────────│
│  Cell 1:                                            │
│  import numpy as np                                 │
└─────────────────────────────────────────────────────┘
```

After clicking, you'll see a menu:
```
Select Notebook Kernel
  ▶ Select Another Kernel...        ← Select this
  ▶ Python 3.11.x
  ▶ Python 3.13.5 (All Packages)   ← Or this if visible
```

Then:
```
Select Kernel Source
  ▶ Jupyter Kernel...
  ▶ Python Environments...          ← Select this
```

Finally select:
```
  ▶ Python 3.13.5 (All Packages)
    C:\Program Files\Python313\python.exe
```

## Verify It Worked

After selecting the kernel, add a new cell and run:

```python
import sys
print("✅ Python:", sys.executable)

import numpy as np
print("✅ NumPy:", np.__version__)

import tensorflow as tf
print("✅ TensorFlow:", tf.__version__)

import librosa
print("✅ Librosa:", librosa.__version__)

print("\n🎉 All packages working!")
```

**Expected output:**
```
✅ Python: C:\Program Files\Python313\python.exe
✅ NumPy: 2.3.5
✅ TensorFlow: 2.20.0
✅ Librosa: 0.11.0

🎉 All packages working!
```

## Alternative Method (If Above Doesn't Work)

1. Press **Ctrl+Shift+P** (Command Palette)
2. Type: **"Notebook: Select Notebook Kernel"**
3. Press Enter
4. Select **"Python Environments..."**
5. Choose **"Python 3.13.5 (All Packages)"**

## Still Having Issues?

1. **Restart VS Code completely** (File → Exit, then reopen)
2. Open your notebook
3. Follow the steps above again
4. The kernel should now appear

## Why This Happened

VS Code has multiple Python interpreters installed on your system. Your notebook was using one that doesn't have numpy, tensorflow, and librosa installed. The correct interpreter is:

**`C:\Program Files\Python313\python.exe`**

This one has ALL packages installed:
- ✅ TensorFlow 2.20.0
- ✅ NumPy 2.3.5  
- ✅ Librosa 0.11.0
- ✅ Pandas, Matplotlib, SciPy, Scikit-learn, etc.

---

**Once you select the correct kernel, everything will work!** 🚀
