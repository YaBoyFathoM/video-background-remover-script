import cv2
import argparse
from moviepy.editor import AudioFileClip, ImageSequenceClip
from rembg import remove, new_session

def parse_args():
    """
    Parse command-line arguments.
    Returns:
        Namespace: The parsed arguments as a namespace.
    """
    parser = argparse.ArgumentParser(description='Remove background from video.')
    parser.add_argument('-i', '--input', help='Input video file path', required=True)
    parser.add_argument('-o', '--output', help='Output video file path', required=True)
    return parser.parse_args()

def process_video(input_video, output_video):
    """
    Process the video to remove the background.
    Args:
        input_video (str): The path to the input video.
        output_video (str): The path to the output video.
    """
    session = new_session('u2net_human_seg')
    video = cv2.VideoCapture(input_video)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_completed = 0
    audio = AudioFileClip(input_video)
    clip_frames = []
    while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
            result = remove(frame, session=session)
            result = cv2.cvtColor(result, cv2.COLOR_RGBA2BGRA)
            clip_frames.append(result)
            frames_completed += 1
            print(f"Total Frames: {total_frames}, Frames Completed: {frames_completed}", end='\r')
    clip = ImageSequenceClip(clip_frames, fps=fps)
    clip = clip.set_audio(audio)
    clip.write_videofile(output_video, fps=fps, codec='png', audio_codec='aac')
    video.release()

def main():
    """
    Main function.
    """
    args = parse_args()
    process_video(args.input, args.output)

if __name__ == "__main__":
    main()