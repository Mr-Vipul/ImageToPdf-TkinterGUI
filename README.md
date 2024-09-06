# Image to PDF Converter

Image to PDF Converter is a Python application that allows you to convert multiple images into a single PDF file using a simple graphical interface built with Tkinter.


![Screenshot 2024-09-06 234652](https://github.com/user-attachments/assets/5356c9f9-fd9a-493b-8fe7-b52c063a336d)



## Installation

To install the required dependencies, use the package manager pip to install the required libraries.

```bash
pip install pillow
```

## Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory and run the script app.py to launch the Image to PDF Converter.

```python
python app.py
```

Once the app is running:

1. Click "Select Images" to browse and add images.
2. Enter the desired name for the output PDF file.
3. Click "Convert to PDF" to create the PDF from the selected images

.
```python
from app import ImageToPdf

# Initialize the Tkinter window
root = tk.Tk()

# Create an instance of ImageToPdf class
converter = ImageToPdf(root)

# Start the GUI application
root.mainloop()
```
# Features
1. Select multiple images for conversion.
2. Convert images to PDF in a specified order.
3. Simple and user-friendly interface.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to update documentation and tests as appropriate.
