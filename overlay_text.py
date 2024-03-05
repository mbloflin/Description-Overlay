import subprocess
import os

def overlay_text_on_images(image_folder, descriptions_file, output_folder, video_output=None, display_duration=3):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read descriptions from file
    with open(descriptions_file, 'r') as file:
        descriptions = [line.strip() for line in file.readlines()]
    
    # List and sort PNG files in the input directory
    png_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    png_files.sort()  # Sort files alphanumerically

    # Check if the number of descriptions matches the number of images
    if len(descriptions) != len(png_files):
        print("Warning: The number of descriptions does not match the number of PNG files.")
        return

    # Process each image and assign new sequential names
    for i, filename in enumerate(png_files):
        input_image = os.path.join(image_folder, filename)
        # New naming convention: Simple numeric sequence
        output_image = os.path.join(output_folder, f'overlay_{i+1:05d}.png')
        
        description = descriptions[i] if i < len(descriptions) else "No description"
        
        subprocess.run([
            'ffmpeg',
            '-i', input_image,
            '-vf', f"drawtext=text='{description}':fontfile='C\:/Windows/Fonts/Arial.ttf':x=10:y=H-th-10:fontcolor=white:fontsize=34:box=1:boxcolor=black@0.5",
            '-loglevel', 'error',  # Only show error messages
            '-y',
            output_image
        ], check=True)

    # Create a video from the processed images
    if video_output:
        frame_rate = str(1/display_duration)  # Frame rate, based on display duration of each image
        # Adjusted pattern to match new file names
        input_pattern = os.path.join(output_folder, 'overlay_%05d.png')
        
        subprocess.run([
            'ffmpeg',
            '-framerate', frame_rate,
            '-i', input_pattern,
            '-c:v', 'libx264',
            '-r', '30',
            '-pix_fmt', 'yuv420p',
            '-loglevel', 'error',  # Only show error messages
            video_output
        ], check=True)

# Example usage - Update these paths to match your project structure
image_folder = 'Input_images'
descriptions_file = 'descriptions.txt'
output_folder = 'Outputs/Output_images'
video_output = 'Outputs/Output_MP4/output_video.mp4'

overlay_text_on_images(image_folder, descriptions_file, output_folder, video_output, display_duration=3)
