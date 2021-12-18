try: from PIL import Image
except ImportError: import Image
from argparse import ArgumentParser
from os import path
def filecheck(file):
    if path.isfile(file): return file
    else: exit("File {} does not exist".format(file))
parser = ArgumentParser()
parser.add_argument('--file', type = filecheck, required = True)
args = parser.parse_args()
source = Image.open(args.file).convert("RGBA")
img = Image.new("RGB", source.size)
pix = img.load()
for i in range(source.size[0]):
    for j in range(source.size[1]):
        scale = max(1, max(source.size) // (1 << 8))
        if (i // scale + j // scale) % 2: # resolution of no more than 1<<8
            pix[i, j] = (0xFF,) * 3
Image.blend(source, img.convert("RGBA"), .95).save(path.join(path.dirname(args.file), "hidden_" + path.basename(args.file)), "PNG")
