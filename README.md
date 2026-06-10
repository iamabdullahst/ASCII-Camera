# macOS Terminal ASCII Camera

A fun, lightweight Python application that captures the video feed from your MacBook's built-in webcam and renders it in real-time as ASCII art directly in your terminal.

## Features

- Real-time video capture using OpenCV.
- Dynamically resizes the output to fit your current terminal window dimensions.
- Automatically adjusts aspect ratios to account for the shape of terminal characters.
- Simple, customizable ASCII character mappings.

## Prerequisites

- **macOS**: Designed specifically for the macOS Terminal (though it may work on other Unix-like systems).
- **Python 3.6+**: You'll need Python installed on your system.

## Installation

1. **Clone the repository** (or download the source files):
   ```bash
   cd ascii_cam
   ```

2. **Create a virtual environment**:
   It's highly recommended to use a virtual environment to manage dependencies.
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: This installs `opencv-python` and pins `numpy<2.0.0` for compatibility).*

## Usage

1. Ensure your virtual environment is active:
   ```bash
   source .venv/bin/activate
   ```

2. Run the application:
   ```bash
   python ascii_cam.py
   ```

> **Important macOS Permissions Note**: The first time you run this script, macOS will prompt you to grant the Terminal application permission to access your Camera. You must click **OK** for the application to work. If you accidentally deny it, you can fix it by going to **System Settings > Privacy & Security > Camera**.

### Tips for Best Results
- **Font Size**: For a higher "resolution" ASCII image, decrease your terminal's font size (usually `Cmd + -`) and maximize your terminal window.
- **Exiting**: Press `Ctrl + C` at any time to gracefully exit the application and release the camera.

## How it Works

The script leverages `cv2.VideoCapture(0)` to grab frames from the webcam. Each frame is horizontally flipped (for a mirror effect) and converted to grayscale. 

The terminal dimensions are queried using Python's `shutil.get_terminal_size()`. The script resizes the grayscale frame to match these dimensions, applying an aspect ratio correction factor so the image doesn't appear squished (since terminal characters are taller than they are wide). 

Finally, the grayscale pixel intensities (ranging from 0 to 255) are mapped to a string of ASCII characters (from darkest `@` to lightest `.`) and printed rapidly to the screen using ANSI escape sequences (`\033[2J\033[H`) to clear the terminal without flickering.
