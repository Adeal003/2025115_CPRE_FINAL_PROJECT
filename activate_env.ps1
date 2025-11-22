# CPRE 587 Audio Classification Environment Activation Script
# Run this script to activate your virtual environment

Write-Host "🎵 CPRE 587 Audio Classification Project" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
$projectDir = "U:\cpre_587\2025115_CPRE_FINAL_PROJECT"
Set-Location $projectDir
Write-Host "📁 Changed to project directory: $projectDir" -ForegroundColor Green

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& ".\cpre587_env\Scripts\Activate.ps1"

Write-Host ""
Write-Host "✅ Environment activated! You can now:" -ForegroundColor Green
Write-Host "   • jupyter lab          (start Jupyter Lab)" -ForegroundColor White
Write-Host "   • python script.py     (run Python scripts)" -ForegroundColor White
Write-Host "   • pip install package  (install new packages)" -ForegroundColor White
Write-Host ""
Write-Host "📓 Don't forget to select 'CPRE587 Audio Classification' kernel in VS Code!" -ForegroundColor Magenta
