import matplotlib.pyplot as plt
from string import ascii_lowercase, ascii_uppercase
from PIL import Image
import subprocess

def clean():
    subprocess.run("rm data/*.png", shell=True)

clean()

font = {'family' : 'monospace'}

for letter in list(ascii_lowercase+ascii_uppercase):
    fig = plt.figure()
    plt.subplots(figsize=(0.5, 0.5))
    plt.text(0.5, 0.5, letter, font)
    plt.savefig(f"data/{letter}.png")
    plt.close('all')

    img = Image.open(f"data/{letter}.png")
    img_res = img.crop((25, 13, 35, 26))
    img_res.save(f"data/{letter}_result.png")
