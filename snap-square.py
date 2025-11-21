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

    # Horizontal offset to center
    x = (size - img.width) // 2
    
    # Vertical offset to center
    y = (size - img.height) // 2
    
    # Paste with transparency mask
    square_img.paste(img, (x, y), img)

    # Prepare output file name
    if not output_file:
        base, _ = os.path.splitext(input_file)
        output_file = f"{base}_square.png"

    # Save
    square_img.save(output_file)
    print(f"Saved: {output_file}")

# Run when executed directly
if __name__ == '__main__':
    # Check if input provided
    if len(sys.argv) < 2:
        print("Usage: python square_image.py input_image [output_image]")
    else:
        # Get input filename
        input_image = sys.argv[1]
        # Get output filename if provided
        output_image = sys.argv[2] if len(sys.argv) > 2 else None
        square_image(input_image, output_image)
