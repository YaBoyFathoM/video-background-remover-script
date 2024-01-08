import cv2
import argparse
from moviepy.editor import AudioFileClip, VideoFileClip
from rembg import remove, new_session

def parse_args():
    """
    Parse command-line arguments.
    Returns:
        Namespace: The parsed arguments as a namespace.
    """
    parser = argparse.ArgumentParser(description='Remove background from video.')
    parser.add_argument('-i', '--input', help='Input video file path', required=True)
    parser.add_argument('-o', '--output_video_path', help='Output video file path', required=True)
    return parser.parse_args()

def process_video(input_video, output_video_path):
    video = cv2.VideoCapture(input_video)
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_completed = 0
    audio = AudioFileClip(input_video)
    audio.write_audiofile('audio.mp3', codec='mp3')
    audio.close()
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    session = new_session('u2net_human_seg')
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        result = remove(frame, session=session)
        result = cv2.cvtColor(result, cv2.COLOR_RGBA2RGB)
        out.write(result)
        frames_completed += 1
        progress = frames_completed / total_frames * 100
        print(f'Processing frames: {progress:.2f}%', end='\r')
    out.release()
    video.release()
    video = VideoFileClip(output_video_path)
    video = video.set_audio(AudioFileClip('taylor.mp3'))
    video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

def main():
    """
    Main function.
    """
    args = parse_args()
    process_video(args.input, args.output)

if __name__ == "__main__":
    main()
