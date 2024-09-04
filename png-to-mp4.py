import os
import numpy as np
from glob import glob
from moviepy.editor import ImageSequenceClip
from PIL import Image

def create_video_from_images(directory, output_path, resolution=(1280, 720), duration=0.5, bg_color=(255, 255, 255)):
    # Find PNG files
    png_files = glob(os.path.join(directory, '**', '*.png'), recursive=True)

    # Process images
    images = []
    for file in png_files:
        img = Image.open(file).convert("RGBA")
        
        # Create canvas with new background
        canvas = Image.new("RGBA", resolution, bg_color + (255,))
        img.thumbnail(resolution, Image.Resampling.LANCZOS)
        img_position = ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2)
        canvas.paste(img, img_position, img)

        # Convert to RGB format (RGBA -> RGB)
        canvas = canvas.convert("RGB")
        images.append(np.array(canvas))  # NumPy dizisine dönüştür

    # Creating videos
    clip = ImageSequenceClip(images, fps=1/duration)
    clip.write_videofile(output_path, codec="libx264", fps=30)

# Usage example
directory_path = r'C:\...\test2'
output_video_path = r'C:\...\output_video.mp4'
resolution = (1280, 720)  # video resolution
duration_per_image = 0.8  # Duration for each image (seconds)
background_color = (255, 255, 255)  # White background

create_video_from_images(directory_path, output_video_path, resolution, duration_per_image, background_color)
