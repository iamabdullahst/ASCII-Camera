# Terminal ASCII Camera

A fun, lightweight cross-platform Python application that captures the video feed from your webcam and renders it in real-time as ASCII art directly in your terminal.

## Features

- Real-time video capture using OpenCV.
- Dynamically resizes the output to fit your current terminal window dimensions.
- Automatically adjusts aspect ratios to account for the shape of terminal characters.
- Simple, customizable ASCII character mappings.

## Prerequisites

- **Cross-Platform**: Works on macOS, Windows, and Linux terminals.
- **Python 3.6+**: You'll need Python installed on your system.

## Installation & Usage

I have provided automated scripts that will check for a virtual environment, set it up, install the required dependencies (like `opencv-python`), and run the application.

1. **Clone the repository** (or download the source files):
   ```bash
   cd ascii_cam
   ```

2. **Run the application**:
   - **On macOS/Linux**: 
     ```bash
     ./run.sh
     ```
   - **On Windows**: 
     Double-click `run.bat` or run it from the command prompt:
     ```cmd
     run.bat
     ```

> **Important macOS Permissions Note**: The first time you run this script, macOS will prompt you to grant the Terminal application permission to access your Camera. You must click **OK** for the application to work. If you accidentally deny it, you can fix it by going to **System Settings > Privacy & Security > Camera**.

### Tips for Best Results
- **Font Size**: For a higher "resolution" ASCII image, decrease your terminal's font size (usually `Cmd + -`) and maximize your terminal window.
- **Exiting**: Press `Ctrl + C` at any time to gracefully exit the application and release the camera.

## How it Works

The script leverages `cv2.VideoCapture(0)` to grab frames from the webcam. Each frame is horizontally flipped (for a mirror effect) and converted to grayscale. 

The terminal dimensions are queried using Python's `shutil.get_terminal_size()`. The script resizes the grayscale frame to match these dimensions, applying an aspect ratio correction factor so the image doesn't appear squished (since terminal characters are taller than they are wide). 

Finally, the grayscale pixel intensities (ranging from 0 to 255) are mapped to a string of ASCII characters (from darkest `@` to lightest `.`) and printed rapidly to the screen using ANSI escape sequences (`\033[2J\033[H`) to clear the terminal without flickering.
