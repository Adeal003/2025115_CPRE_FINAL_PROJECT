# Git Configuration Setup Guide

## 🔧 Set Your Git Username and Email

You need to configure your Git identity for proper commit attribution. Here are the commands:

### **Global Configuration (Recommended)**
This sets your identity for all Git repositories on this machine:

```powershell
# Set your name (replace with your actual name)
git config --global user.name "Your Full Name"

# Set your email (replace with your actual email)
git config --global user.email "your.email@example.com"
```

### **Local Configuration (Project-specific)**  
This sets your identity only for this specific project:

```powershell
# Set your name for this project only
git config user.name "Your Full Name"

# Set your email for this project only  
git config user.email "your.email@example.com"
```

## 📝 **Example with Common Formats:**

### For Iowa State Students:
```powershell
git config --global user.name "John Doe"
git config --global user.email "jdoe@iastate.edu"
```

### For GitHub Users:
```powershell
git config --global user.name "John Doe" 
git config --global user.email "john.doe@gmail.com"
# Or use GitHub's noreply email:
git config --global user.email "username@users.noreply.github.com"
```

## ✅ **Verify Your Configuration:**
```powershell
# Check what's configured
git config --list

# Check specific values
git config user.name
git config user.email
```

## 🔐 **GitHub Authentication (if needed):**
If you're pushing to GitHub, you may also need:
```powershell
# For HTTPS (recommended)
git config --global credential.helper manager

# Check remote URL
git remote -v
```

## 💡 **Pro Tips:**

1. **Use your real name** - this appears in commit history
2. **Use a consistent email** - preferably the same one associated with your GitHub account
3. **Global vs Local**: 
   - Use `--global` for personal projects
   - Use local config for work/school projects with different identities

## 🚀 **Quick Setup Commands:**

Replace the placeholders below with your actual information:

```powershell
# Navigate to your project (if not already there)
Set-Location "U:\cpre_587\2025115_CPRE_FINAL_PROJECT"

# Set your identity (CUSTOMIZE THESE!)
git config --global user.name "Your Name Here"
git config --global user.email "your.email@domain.com"

# Verify it worked
git config --list | findstr user
```

---

**🎯 Your Next Steps:**
1. Choose your name and email
2. Run the configuration commands above
3. Verify with `git config --list`
4. Make a test commit to verify everything works!
