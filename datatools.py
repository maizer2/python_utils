import os
from tqdm import tqdm
from PIL import Image

def img_resize(dir_path: str, resize_shape: tuple, out_path = None):
    dir_list = os.listdir(dir_path)

    if out_path is None:
        out_path = os.path.join(dir_path, "resize")
    
    os.makedirs(out_path, exist_ok=True)

    print(f"Resize images \"{dir_path}\" to \"{out_path}\"")
    for image in tqdm(dir_list):
        img = Image.open(os.path.join(dir_path, image))
        img.resize(resize_shape)
        img.save(os.path.join(out_path, image))
        
    print("Done")
