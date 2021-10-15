docker run --rm -v "$(pwd):/src/" cdrx/pyinstaller-windows -c \
  "pyinstaller main.py --onedir --onefile --clean && \
  mv dist/main.exe main.exe && \
  rm -rf __pycache__/ build/ dist/ main.spec"
