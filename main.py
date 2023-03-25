from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Create a Tkinter window
root = Tk()
root.title("Image Watermarking App")
root.geometry("400x400")

# Define a function to open an image file
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        watermark_image(image)

# Define a function to add a watermark to an image
def watermark_image(image):
    # Define the text and font for the watermark
    text = simpledialog.askstring("Watermark Text", "Enter watermark text:")
    font = ImageFont.truetype("arial.ttf", 750)

    # Create a copy of the input image
    watermark = image.copy()

    # Create a drawing context for the watermark image
    draw = ImageDraw.Draw(watermark)

    # Get the bounding box of the text
    text_box = draw.textbbox((0, 0), text, font=font)

    # Calculate the position of the text
    x = (watermark.width - text_box[2]) / 2
    y = (watermark.height - text_box[3]) / 2

    # Draw the text on the watermark image
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    # Add an alpha channel to the watermark image and set the alpha value to 128
    watermark.putalpha(128)

    # Combine the input image and the watermark image
    if watermark.mode == 'RGBA':
        output = Image.alpha_composite(image.convert("RGBA"), watermark)
    else:
        output = Image.composite(image, watermark.convert("RGB"), watermark)

    # Save the output image file
    output_file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if output_file_path:
        output.save(output_file_path)


# Create a button to open an image file
open_button = Button(root, text="Open Image", command=open_file)
open_button.pack()

# Run the Tkinter event loop
root.mainloop()
