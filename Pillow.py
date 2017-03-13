# it's called PIL instead of pillow is totally a historical thing from Python 2 to Python 3
from PIL import Image
from PIL import ImageFilter # lots of other class

img = Image.open('flower.jpg')
img2 = Image.open('bridge.jpg')

"""
# print image info, and show image
print(img.size)
print(img.format)
img.show()

# crop an image
area = [100,100,200,200]
cropped_img = img.crop(area)
cropped_img.show()

# paste area need to be same as the picture
img2.paste(cropped_img,area)
img2.show()

# split image into 3 channels (r,g,b) or 4 (c,m,y,k) depending on the mode
print(img2.mode)
r,g,b=img2.split()
r.show()
g.show()
b.show()

# merge 3 channels back
new_img = Image.merge("RGB",(r,g,b))
#new_img = Image.merge("RGB",(g,b,g))
#new_img = Image.merge("RGB",(b,g,r))
new_img.show()

# resize
square = img2.resize((200,200))
square.show()

# transpose
flip = img2.transpose(Image.FLIP_LEFT_RIGHT)
flip.show()
spin = img2.transpose(Image.ROTATE_90)
spin.show()
"""
# Convert into other formats, e.g. from RBG to CMYK, L(black and white)
black_white = img2.convert("L")
black_white.show()

# using filter and modes from ImageFilter
blur = img2.filter(ImageFilter.BLUR)
detail = img2.filter(ImageFilter.DETAIL)
edges = img2.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()