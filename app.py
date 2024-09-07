import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os  # Import the os module

class ImageToPdf:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_list_box = tk.Listbox(root, height=10, width=50)  # Listbox to show selected files

        self.initialize_ui()

    def initialize_ui(self):
        # Title label
        title_label = tk.Label(self.root, text="Image to PDF", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)

        # Button to select images
        select_images_btn = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_btn.pack(pady=10)

        # Listbox to display selected images
        self.selected_images_list_box.pack(pady=10)

        # Label and Entry for output PDF name
        pdf_label = tk.Label(self.root, text="Output PDF Name:")
        pdf_label.pack(pady=5)
        pdf_entry = tk.Entry(self.root, textvariable=self.output_pdf_name)
        pdf_entry.pack(pady=5)

        # Button to convert images to PDF
        convert_btn = tk.Button(self.root, text="Convert to PDF", command=self.convert_to_pdf)
        convert_btn.pack(pady=10)

    def select_images(self):
        # Open file dialog to select image files
        file_paths = filedialog.askopenfilenames(
            title="Select Images", 
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        self.image_paths = list(file_paths)
        
        # Update the listbox with the selected image paths
        self.selected_images_list_box.delete(0, tk.END)  # Clear the listbox before inserting new items
        for path in self.image_paths:
            filename = os.path.basename(path)  # Get the filename from the path
            self.selected_images_list_box.insert(tk.END, filename)  # Insert filename into listbox

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("No Images", "Please select at least one image.")
            return

        if not self.output_pdf_name.get():
            messagebox.showwarning("No PDF Name", "Please enter a name for the output PDF.")
            return

        images = []
        for path in self.image_paths:
            img = Image.open(path).convert("RGB")
            images.append(img)

        # Save the images as a PDF
        output_pdf = self.output_pdf_name.get() + ".pdf"
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        
        messagebox.showinfo("Success", f"PDF '{output_pdf}' created successfully!")

def main():
    root = tk.Tk()
    root.title("Image to PDF")
    root.geometry("600x600")
    converter = ImageToPdf(root)
    root.mainloop()

if __name__ == "__main__":
    main()
