import matplotlib.pyplot as plt
from string import ascii_lowercase, ascii_uppercase
from PIL import Image
import subprocess

def clean():
    subprocess.run("rm model_data/*.png", shell=True)
    subprocess.run("rm png_data/*.png", shell=True)

clean()

font = {'family' : 'monospace'}
fig = plt.figure()
for letter in list(ascii_lowercase+ascii_uppercase):

    # Generating plots with ascii letters and saving to png_data folder
    plt.subplots(figsize=(0.5, 0.5))
    plt.text(0.5, 0.5, letter, font)
    plt.savefig(f"png_data/{letter}.png")
    #plt.close(fig)

    img = Image.open(f"png_data/{letter}.png")          # Reading data
    for rot in range(-10, 11):

        img_res = img.rotate(rot)                       # Rotating
        img_res = img_res.crop((25, 13, 36, 30))        # Cutting smaller area
        img_res.save(f"model_data/{letter}_{rot}.png")  # Saving results
