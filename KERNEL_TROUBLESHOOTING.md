# 🔧 Kernel Selection Troubleshooting Guide

## 🎯 **Try These Solutions in Order:**

### **Solution 1: Restart VS Code Completely**
1. **Close VS Code entirely** (not just the notebook)
2. **Reopen VS Code**  
3. **Open your notebook again**
4. **Click "Select Kernel"** - You should now see:
   - `CPRE587 Audio Classification`
   - Or `cpre587_audio` 
   - Or `cpre587_env`

### **Solution 2: Use Command Palette Method**
1. Press **Ctrl+Shift+P** 
2. Type: **"Python: Select Interpreter"**
3. Look for: **`U:\cpre_587\2025115_CPRE_FINAL_PROJECT\cpre587_env\Scripts\python.exe`**
4. Select it
5. Then in your notebook, try "Select Kernel" again

### **Solution 3: Manual Kernel Selection**
1. Click **"Select Kernel"** in notebook
2. Choose **"Select Another Kernel..."**  
3. Select **"Jupyter Kernel..."**
4. Look for one of these names:
   - **`CPRE587 Audio Classification`**
   - **`cpre587_audio`** 
   - **`cpre587_env`**

### **Solution 4: Direct Python Interpreter**
1. Click **"Select Kernel"**
2. Choose **"Python Environments..."**
3. Select: **`U:\cpre_587\2025115_CPRE_FINAL_PROJECT\cpre587_env\Scripts\python.exe`**

### **Solution 5: Reload Window**
1. Press **Ctrl+Shift+P**
2. Type: **"Developer: Reload Window"**  
3. This refreshes VS Code's Python extension
4. Try kernel selection again

## 🔍 **Available Kernel Names to Look For:**
- `CPRE587 Audio Classification` 
- `cpre587_audio`
- `cpre587_env` 
- `python3` (from your virtual environment)

## ✅ **Quick Test After Selecting Kernel:**
Run this in your first notebook cell:
```python
import sys
print("Python executable:", sys.executable)
print("Should contain 'cpre587_env'")

import librosa, tensorflow as tf
print(f"✅ Libraries loaded! TF: {tf.__version__}, Librosa: {librosa.__version__}")
```

## 🚨 **If Nothing Works:**

### **Nuclear Option - Fresh Kernel Registration:**
```powershell
# In your terminal, run:
.\cpre587_env\Scripts\Activate.ps1
python -m ipykernel install --user --name=audio_kernel --display-name="Audio Classification Kernel"
```

Then restart VS Code and look for "Audio Classification Kernel"

## 💡 **Pro Tips:**
- **Kernel names** might appear differently than expected
- **Look for any kernel** that mentions your environment path
- **Python path** should contain `cpre587_env` 
- **If unsure**, select any kernel with `cpre587` in the name

## 🎯 **Most Common Solution:**
**Just restart VS Code completely!** This fixes 80% of kernel detection issues.

---
*After selecting the correct kernel, your notebook should run without import errors!*
