
# video Background removal script

![Description of GIF](https://static.wixstatic.com/media/cef1ec_54a56e778ebe48ceb892641ec060f808~mv2.gif)

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

## Note

This script uses the 'u2net_human_seg' model from rembg for background removal. This model is designed for human segmentation and may not work as well for other types of objects.
