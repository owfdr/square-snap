import sys
from PIL import Image
import os
import glob

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
    
    # Delete original image file
    os.remove(input_file)
    print(f"Deleted: {input_file}")

def process_folder(folder_path):
    # Supported image extensions
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.tiff', '*.webp']
    
    # Find all image files in the folder
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))
        image_files.extend(glob.glob(os.path.join(folder_path, ext.upper())))
    
    if not image_files:
        print(f"No image files found in {folder_path}")
        return
    
    print(f"Found {len(image_files)} image(s) to process")
    
    # Process each image
    for image_file in image_files:
        print(f"\nProcessing: {image_file}")
        square_image(image_file)

# Run when executed directly
if __name__ == '__main__':
    # Check if input provided
    if len(sys.argv) < 2:
        print("Usage: python snap-square.py input_image_or_folder [output_image]")
        print("       If input is a folder, all images in the folder will be processed")
    else:
        # Get input path
        input_path = sys.argv[1]
        
        # Check if input is a directory
        if os.path.isdir(input_path):
            # Process all images in the folder
            process_folder(input_path)
        else:
            # Process single image file
            output_image = sys.argv[2] if len(sys.argv) > 2 else None
            square_image(input_path, output_image)
