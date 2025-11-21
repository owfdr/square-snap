import sys
from PIL import Image
import os

def square_image(input_file, output_file=None):
    # Open the image
    img = Image.open(input_file).convert('RGBA')

    # Calculate max size
    size = max(img.width, img.height)

    # Create square transparent background
    square_img = Image.new('RGBA', (size, size), (255, 255, 255, 0))

    # Center the original image
    x = (size - img.width) // 2
    y = (size - img.height) // 2
    square_img.paste(img, (x, y), img)

    # Prepare output file name
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}_square.png"

    # Save
    square_img.save(output_file)
    print(f"Saved: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python square_image.py input_image [output_image]")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2] if len(sys.argv) > 2 else None
        square_image(input_image, output_image)
