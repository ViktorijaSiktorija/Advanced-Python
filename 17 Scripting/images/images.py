from PIL import Image, ImageFilter

img = Image.open(
    '/images/new/pikachu.png')
print(img)

# izadje PIL objekat
# format - kaze koji je format jpeg itd
print(img.format)

# size
print(img.size)

# mode boje, RGB
print(img.mode)

# dir, koje metode imamo
print(dir(print))

# ImageFilter, sharpen, smooth
filtered = img.filter(ImageFilter.BLUR)

# save da sacuva
# png suportuje filtere
#filtered.save("blur.png", "png")

# convert - menja sliku u druge formate
filtered = img.convert('L')
#filtered.save("crnobelo.png", "png")

# show
# filtered.show()

# rotate
rotiran = filtered.rotate(90)
# rotiran.save("rotiran.png", "png")

# resize prihvata tapl
resized = filtered.resize((16, 16))
resized.save("resized.ico", "ico")

# crop
(left, upper, right, lower) = (100, 100, 400, 400)
im_crop = filtered.crop((left, upper, right, lower))
# im_crop.save("crop.png", "png")

img2 = Image.open(
    '/images/astro.jpg')
resized2 = img2.resize((400, 400))
# nije dobro jer unisti aspect ratio
# img2.save('mali_astro.jpg')
# thumbnail zadrzava aspect ratio
# maks je 400 400
img2.thumbnail((400, 200))
# img2.save('tambnejl.jpg')
