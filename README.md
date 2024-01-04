# Remove Background from Video

This Python script uses OpenCV and the rembg library to remove the background from a video. It processes each frame of the video, removes the background, and then reassembles the video with the original audio.

## Dependencies

- OpenCV
- rembg
- moviepy
- argparse

You can install these dependencies using pip:

```bash
pip install opencv-python-headless rembg moviepy argparse
```

## Usage

The script is run from the command line and takes two arguments: the input video file path and the output video file path.

```bash
python removebackground.py -i input.mp4 -o output.mp4
```

## How it Works

The script first parses the command-line arguments to get the input and output video file paths. It then starts a new rembg session and opens the input video file with OpenCV. It gets the frames per second (fps) and total frame count of the video.

The script then enters a loop where it reads each frame of the video, removes the background using rembg, converts the result to BGRA color space, and appends the result to a list of frames. It also keeps track of the number of frames processed.

Once all frames have been processed, it creates a new video clip from the list of frames using moviepy, sets the audio of the clip to the original audio, and writes the clip to the output video file path.

## Note

This script uses the 'u2net_human_seg' model from rembg for background removal. This model is designed for human segmentation and may not work as well for other types of objects.
