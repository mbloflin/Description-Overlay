# CLI Description-Image-Overlay

A command line script that overlays descriptive text on each supplied PNG image and then creates an MP4 movie for easy viewing, displaying each image for 3 seconds.

## Features

- Command line script that processes a supplied folder full of PNGs.
- VENV based workflow.
- Minimal required files to install (Python, Git, and FFmpeg are prerequisites).
- Descriptive overlay placed on each PNG based on supplied descriptions.
- MP4 creation of all processed images, showing each for 3 seconds.

## Running on Windows 10/11

Ensure the required dependencies are met:

- Python - 3.10.6 or later.
- FFmpeg binaries with the System Path set to the Bin folder - 6.1.1 recommended.
- Git and pip installed.

To run:

1. Place images in the `Input-images` folder.
2. Replace or edit the `descriptions.txt` file and save.
3. Ensure the number of images matches the number of descriptions.
4. Verify that your PNGs are in numerical or alphabetical order to match the order in the `descriptions.txt` file.
5. Open a command prompt at the main folder location.
6. Activate the venv: `.\venv\Scripts\activate`.
7. Run `overlay_text.py`: `python overlay_text.py`.
8. Overlayed PNGs will be in `Outputs\Output_images`.
9. MP4 will be in `Outputs\Output_MP4`.
10. Planned feature: One-click BAT file execution for simpler workflow.

### Installation on Windows 10/11

1. Install [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) or newer, ensuring you check "Add Python to PATH".
2. Install [Git](https://git-scm.com/download/win) on your system if it's not already installed.
3. Install pip if it's not already installed.
4. Clone the project repository: `git clone https://github.com/mbloflin/Description-Image-overlay.git`.
5. Navigate to the project directory in your terminal.
6. Set up a Python virtual environment in the project directory (if not already done during initial setup): `python -m venv .venv`.
7. Activate the virtual environment: `.\venv\Scripts\activate`.
8. Install the project's dependencies: `pip install -r requirements.txt`.

## Documentation

This README is currently the only documentation provided.

## Credits

- Original idea and pseudocode by Brad Loflin.
- Python code finalized and debugged in Visual Studio Code, version 1.87.0 by Microsoft Inc.
- Python code co-pilot was ChatGPT
