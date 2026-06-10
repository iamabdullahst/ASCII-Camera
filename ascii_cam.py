import cv2
import os
import shutil
import sys
import time

# ASCII characters from darkest to lightest
# You can experiment with different character sets!
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def get_terminal_size():
    # Return (width, height)
    size = shutil.get_terminal_size((80, 24))
    return size.columns, size.lines

def map_pixels_to_ascii(image):
    # Flatten the image array and map values to ASCII
    pixels = image.flatten()
    interval = 256 / len(ASCII_CHARS)
    # Ensure index doesn't go out of bounds (which might happen if pixel is exactly 256, though it shouldn't be)
    ascii_str = "".join([ASCII_CHARS[min(int(pixel // interval), len(ASCII_CHARS) - 1)] for pixel in pixels])
    return ascii_str

def main():
    # 0 is usually the built-in webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera. Please ensure you have granted Terminal permission to access the camera.")
        sys.exit(1)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
            
            # Flip the frame horizontally (mirror effect makes it more intuitive for a front-facing camera)
            frame = cv2.flip(frame, 1)
            
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Get terminal size
            term_width, term_height = get_terminal_size()
            
            # Calculate new dimensions
            height, width = gray.shape
            aspect_ratio = height / width
            
            # Terminal characters are typically roughly twice as tall as they are wide.
            # We multiply by 0.5 to account for this.
            char_aspect_ratio = 0.5 
            
            new_width = term_width
            new_height = int(new_width * aspect_ratio * char_aspect_ratio)
            
            # If the image is taller than the terminal, scale down to fit height instead
            if new_height > (term_height - 1): # -1 to leave room for the prompt at the bottom
                new_height = term_height - 1
                new_width = int(new_height / (aspect_ratio * char_aspect_ratio))
                
            if new_width <= 0 or new_height <= 0:
                 continue
            
            # Resize image
            resized_image = cv2.resize(gray, (new_width, new_height))
            
            # Convert to ASCII
            ascii_str = map_pixels_to_ascii(resized_image)
            
            # Split the string into lines of the correct width
            img_width = resized_image.shape[1]
            ascii_str_len = len(ascii_str)
            ascii_img = "\n".join([ascii_str[index: index + img_width] for index in range(0, ascii_str_len, img_width)])
            
            # Clear screen and move cursor to top-left
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.write(ascii_img)
            sys.stdout.flush()
            
            # Small delay to keep CPU usage reasonable (~30 FPS max)
            time.sleep(0.03)
            
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass
    finally:
        sys.stdout.write("\033[2J\033[H")
        print("\nExiting ASCII Camera.")
        cap.release()

if __name__ == "__main__":
    main()
