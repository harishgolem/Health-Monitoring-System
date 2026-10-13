@echo off
setlocal
python -m pip install --upgrade pip
python -m pip install pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name NeuroPulse main.py
echo.
echo If build succeeded, your EXE is in the dist folder.
pause
