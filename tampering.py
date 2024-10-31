#Code to tamper any image 
from PIL import Image, ImageDraw
import os

def create_unauthentic_image(original_image_path, output_path):
   
    original_image = Image.open(original_image_path).convert("RGB")
    draw = ImageDraw.Draw(original_image)
    width, height = original_image.size
    draw.rectangle([width//4, height//4, width//2, height//2], fill=(255, 0, 0, 128)) 
    original_image.save(output_path)
    print(f"Unauthentic image saved as: {output_path}")
project_directory = 'C:\\Users\\USER\\Desktop\\PixelTrace\\sample'  # Adjust this path as needed
original_image_path = os.path.join(project_directory, 'notmycat.jpg')
output_image_path = os.path.join(project_directory, 'notmycat_unauthentic.jpg')

create_unauthentic_image(original_image_path, output_image_path)
