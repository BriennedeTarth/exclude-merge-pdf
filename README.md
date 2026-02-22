# PDF Merger Utility
Automatically combine multiple PDF files into a single document. It features a smart exclusion filter and dynamic naming based on the current date.

## Features

* **Batch Processing**: Automatically finds all `.pdf` files in the current directory.
* **Smart Filter**: Skips any files prefixed with `EXCLUIR-` (useful for keeping source files or templates out of the final merge).
* **Dynamic Naming**: Generates the output file using the format `mergedPDF-DDMMYYYY.pdf`.

---

## 🛠️ Prerequisites

Before running the script, ensure you have Python installed and the `PyPDF2` library:

```bash
pip install PyPDF2

```

---

## 📂 Project Structure

```text
.
├── script.py           # The merger script
├── document1.pdf       # Included in merge
├── document2.pdf       # Included in merge
└── EXCLUIR-notes.pdf   # Automatically skipped

```

---

##  Usage

1. Place the script in the same folder as the PDFs you want to merge.
2. (Optional) Prefix any PDFs you want to skip with **"EXCLUIR-"**.
3. Run the script:
```bash
python script.py

```


## Extra: How to Create an Executable

We will use PyInstaller, which bundles your script and all its dependencies (like PyPDF2) into a single file.
1. Install PyInstaller

Open your terminal or command prompt and run:
Bash

pip install pyinstaller

2. Generate the Executable

Navigate to the folder where your script (e.g., merger.py) is located and run the following command:
Bash

pyinstaller --onefile --clean merger.py

What these flags do:

    --onefile: Bundles everything into a single .exe file instead of a folder full of files.

    --clean: Clears the PyInstaller cache before building (prevents old errors).

    --noconsole (Optional): If you don't want a black command prompt window to pop up when you run the program, add this flag.

📂 Where is my file?

After the process finishes, you will see a few new folders in your directory:

    dist/: This is where your finished merger.exe lives.

    build/: Temporary files used during the conversion (you can delete this).

    merger.spec: A configuration file (you can delete this).

⚠️ Important Considerations

    Antivirus Software: Sometimes Windows Defender or Antivirus programs flag fresh PyInstaller executables as "unknown threats." You may need to click "Run anyway" or whitelist the file.

    Permissions: Since your script deletes and writes files, ensure the .exe is run in a folder where it has write permissions (avoiding C:\Windows or protected System folders).

    Operating Systems: You must build the executable on the OS you plan to use it on. If you want a Windows .exe, you must run the command on Windows. If you want a Mac app, run it on macOS.
