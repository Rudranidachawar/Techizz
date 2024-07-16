import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(output_folder, f"frame_{count}.jpg"), frame)
        count += 1
    cap.release()
    print(f"Extracted {count} frames from {video_path}")

if __name__ == "__main__":
    video_path = 'data/raw/sample_video.mp4'
    output_folder = 'data/processed/frames'
    extract_frames(video_path, output_folder)
