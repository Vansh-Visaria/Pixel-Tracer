# Error Level Analysis Tool

This project is a web application built with Flask that allows users to upload images and perform Error Level Analysis (ELA) to check for authenticity. The application provides a visual representation of the analysis results through marked images and heatmaps.

## Features

- Upload an image for analysis.
- Perform Error Level Analysis to detect image authenticity.
- Visualize results with marked images highlighting discrepancies.
- Generate and display heatmaps for a better understanding of analysis results.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Pillow (PIL)**: For image processing.
- **NumPy**: For numerical operations.
- **Matplotlib**: For generating heatmaps.
- **Bootstrap**: For responsive front-end design.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Hawk-of-Darkness/Pixel-Tracer.git
   cd error-level-analysis
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000.

## Usage
On the home page, upload an image file.
Click on the "Analyze" button.
The application will process the image and display the results on a new page, including:
The marked image indicating areas of potential tampering.
A heatmap visualizing the analysis results.
