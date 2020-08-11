import os
from PIL import Image
import numpy as np

old_R, old_G, old_B = 21, 21, 21
new_R, new_G, new_B = 51, 50, 61
count = 0

def PrintFilesInDir(rootDir, prefix):
    files = os.listdir(rootDir)

    for file in files:
        path = os.path.join(rootDir, file)
        if os.path.isdir(path):
            print(prefix + path)
            PrintFilesInDir(path, prefix + "        ")
        else:
            global count
            count = count + 1
            print(prefix + file)
            ext = os.path.splitext(file)[1]
            if ext == ".png":
                ReplaceColor(path)

def ReplaceColor(path):
    image = Image.open(path)
    image = image.convert("RGBA")
    data = np.array(image)
    red, green, blue =  data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == old_R) & (green == old_G) & (blue == old_B)
    data[:, :, :3][mask] = [new_R, new_G, new_B]
    newImage = Image.fromarray(data)
    newImage.save(path)

rootDir = "./Resources"
PrintFilesInDir(rootDir, "")
print(count)