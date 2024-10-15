from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
import os
from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = 'secret_key'
RESULTS_DIR = 'static/results'

# Create results directory if it doesn't exist
os.makedirs(RESULTS_DIR, exist_ok=True)

# Function to check authenticity
def check_authenticity(marked_image, background_color):
    width, height = marked_image.size
    pixel_mark = marked_image.load()
    for x in range(width):
        for y in range(height):
            if pixel_mark[x, y] != background_color:
                return False
    return True

# Function to generate and save heatmap
def generate_heatmap(pixel_data, width, height):
    pixel_values = np.zeros((height, width))
    for x in range(width):
        for y in range(height):
            pixel_values[y][x] = sum(pixel_data[x, y])
    plt.imshow(pixel_values, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title('Heatmap')
    plt.savefig(os.path.join(RESULTS_DIR, 'Heatmap_Graph.png'))
    plt.close()

# ELA function
def error_level_analysis(original_image_path, scale_factor=20, difference_threshold=50):
    original_image = Image.open(original_image_path)
    temporary_image_path = os.path.join(RESULTS_DIR, 'Temporary_Image.jpg')
    original_image.save(temporary_image_path, quality=90)
    temporary_image = Image.open(temporary_image_path)

    # Calculate the difference image
    difference = ImageChops.difference(original_image, temporary_image)
    pixel_data = difference.load()
    width, height = difference.size

    # Create a new image for marking differences
    marked_image = Image.new('RGB', (width, height), (0, 0, 0))
    pixel_mark = marked_image.load()

    # Loop through each pixel to calculate the difference and mark if above threshold
    for x in range(width):
        for y in range(height):
            pixel_diff = sum(pixel_data[x, y])  # Calculate the sum of RGB values
            if pixel_diff > difference_threshold:
                intensity = min((pixel_diff - difference_threshold) * scale_factor, 255)  # Cap intensity
                pixel_mark[x, y] = (intensity, 0, 0)  # Mark in red channel

    # Save the marked image
    marked_image_path = os.path.join(RESULTS_DIR, 'Result_Image.jpg')
    marked_image.save(marked_image_path)
    
    generate_heatmap(pixel_data, width, height)
    
    is_authentic = check_authenticity(marked_image, (0, 0, 0))
    
    return is_authentic

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file_path = os.path.join(RESULTS_DIR, file.filename)
            file.save(file_path)

            is_authentic = error_level_analysis(file_path)
            result_text = "The Image is authentic" if is_authentic else "The Image is not authentic"
            flash(result_text)

            return redirect(url_for('results'))

    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/static/results/<path:filename>')
def send_results(filename):
    return send_from_directory(RESULTS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
