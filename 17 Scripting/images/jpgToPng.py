# JPG to PNG converter
# za sajtove je bolji png
import sys
import os
from PIL import Image


# path = sys.argv[1] ovo ne radi pa sam promenila u abs path
# output = sys.argv[2]
# mora / na kraju da bi usao u folder
path = '/images/pokemoni/'
output = '/images/new/'
print(path, output)

if not os.path.exists(output):
    os.mkdir(output)

for filename in os.listdir(path):  # listdir lista fajlove u folderu
    img = Image.open(f'{path}{filename}')
    clean_name = os.path.splitext(filename)[0]  # da izbrise jpg
    img.save(f'{output}{clean_name}.png', 'png')
