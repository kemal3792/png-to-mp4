import os
import numpy as np
from glob import glob
from moviepy.editor import ImageSequenceClip
from PIL import Image

def create_video_from_images(directory, output_path, resolution=(1280, 720), duration=0.5, bg_color=(255, 255, 255)):
    # PNG dosyalarını bul
    png_files = glob(os.path.join(directory, '**', '*.png'), recursive=True)

    # Görüntüleri işle
    images = []
    for file in png_files:
        img = Image.open(file).convert("RGBA")
        
        # Yeni arka plan ile canvas oluştur
        canvas = Image.new("RGBA", resolution, bg_color + (255,))
        img.thumbnail(resolution, Image.Resampling.LANCZOS)
        img_position = ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2)
        canvas.paste(img, img_position, img)

        # RGB formatına dönüştür (RGBA -> RGB)
        canvas = canvas.convert("RGB")
        images.append(np.array(canvas))  # NumPy dizisine dönüştür

    # Video oluşturma
    clip = ImageSequenceClip(images, fps=1/duration)
    clip.write_videofile(output_path, codec="libx264", fps=30)

# Kullanım örneği
directory_path = r'C:\Users\BARAN\Desktop\etsy-products\animals\cat\test2'
output_video_path = r'C:\Users\BARAN\Desktop\etsy-products\animals\cat\output_video.mp4'
resolution = (1280, 720)  # video resolution
duration_per_image = 0.8  # Duration for each image (seconds)
background_color = (255, 255, 255)  # White background

create_video_from_images(directory_path, output_video_path, resolution, duration_per_image, background_color)
