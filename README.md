# Simple File Explorer

Simple File Explorer is a lightweight, cross-platform graphical application built with Python's Tkinter library. It provides a minimalistic interface for browsing and selecting files from your local system.

## Features
- **File Browsing**: Open and navigate through your file system
- **File Type Filtering**: Filter by all files or text documents only
- **Clean Interface**: Simple, intuitive GUI with clear file path display
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with standard Python installations)

### Setup
1. Ensure Python is installed on your system
2. Save the code to a file (e.g., `file_explorer.py`)
3. No additional dependencies required - Tkinter comes with standard Python

## Usage

### Running the Application
```bash
python file_explorer.py
```

### Interface Components
1. **Browse Files Button**: Click to open the file dialog
2. **File Path Display**: Shows the full path of the selected file

### How to Use
1. Launch the application
2. Click the "Browse Files" button
3. Navigate through your file system in the dialog window
4. Select a file (optionally filter by file type using the dropdown)
5. The selected file path will appear below the button

### File Type Filters
The dialog offers two filtering options:
- **All files (*.*)**: Shows all files in the directory
- **Text documents (*.txt)**: Shows only text files with .txt extension

## Code Structure

### Main Components
- `root`: Main application window (400×200 pixels)
- `browse_file()`: Function that handles file selection
- `browse_button`: Button that triggers file browsing
- `file_path_label`: Label that displays the selected file path

### Key Functions
- `browse_file()`: Opens file dialog, captures selection, and updates the display
- `filedialog.askopenfilename()`: Tkinter's built-in file dialog function

## Technical Details

### Dependencies
- `tkinter`: Standard Python GUI toolkit
- `os`: Used for file system operations (implicitly through filedialog)

### Application Properties
- **Window Title**: "Simple File explorer"
- **Window Size**: 400×200 pixels
- **Text Wrapping**: File paths wrap at 380 pixels for readability

## Customization Options

### Modify Window Size
Change the geometry in the code:
```python
root.geometry("600x300")  # Wider and taller window
```

### Add More File Filters
Extend the filetypes list:
```python
filetypes=[
    ("All files", "*.*"),
    ("Text documents", "*.txt"),
    ("Python files", "*.py"),
    ("Images", "*.png *.jpg *.jpeg")
]
```

### Change Button Text
```python
browse_button = tk.Button(root, text="Select File", command=browse_file)
```

## Limitations
- Only single file selection (no multi-select)
- No file preview functionality
- No directory browsing beyond file selection
- Basic interface without advanced file operations

## Troubleshooting

### Common Issues
1. **Tkinter not found**: Install tkinter using your system's package manager
   - Ubuntu/Debian: `sudo apt-get install python3-tk`
   - macOS: Usually pre-installed with Python
   - Windows: Included with standard Python installation

2. **Window doesn't appear**: Ensure you're running the script with Python 3

3. **File dialog doesn't open**: Check if your system has a graphical interface

## Extending the Application

### Potential Enhancements
1. Add multi-file selection capability
2. Implement directory browsing
3. Add file preview functionality
4. Include file properties display
5. Add search functionality within directories
6. Implement dark/light theme toggle

### Example Enhancement: Multiple File Selection
```python
def browse_files():
    file_paths = filedialog.askopenfilenames(
        title="Select Files",
        filetypes=[("All files", "*.*"), ("Text documents", "*.txt")]
    )
    if file_paths:
        file_path_label.config(text=f"Selected {len(file_paths)} files")
```

## License
This code is provided as-is for educational and personal use. Feel free to modify and distribute with proper attribution.

## Support
For issues or questions, please ensure:
- You're using a supported Python version (3.6+)
- Tkinter is properly installed on your system
- You have necessary file system permissions

## Screenshot
```
+------------------------------------------+
|         Simple File explorer             |
|                                          |
|            [Browse Files]                |
|                                          |
| Selected File: /path/to/your/file.txt    |
+------------------------------------------+
```

## Version
Current Version: 1.0.0  
Initial Release: Basic file selection functionality
