from pathlib import Path
import imageio

def create_animation(image_folder, output_file, fps=5):
    images = []
    for f in sorted(Path(image_folder).glob("*.png")):
        images.append(imageio.imread(f))
    imageio.mimsave(output_file, images, fps=fps)
