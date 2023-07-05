from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("C:/Users/ASUSKIM/Desktop/AR/New folder/image/Lin Yi/300px-Lin_Yi.jpg")
img2 = Image.open("C:/Users/ASUSKIM/Desktop/AR/New folder/image/Lin Yi/Lin Yi Pic10.jpg")

# img.show()    #show the default os image viewer

# plt.imshow(img)     #show the image with matplotlib
# plt.imshow(img2)

# print(img.size)   #wdith height
# print(img.mode)   #color description
# print(img.format) #file format

# img.save("newImg.jpg")  #save as a newfile

# #crop the image
# left = 80
# top = 15
# right = 230
# bottom = 210
# crop_img = img.crop((left, top, right, bottom))
# plt.imshow(crop_img)

# # copy image
# copied_img = img.copy()
# plt.imshow(copied_img)

# # transposing: rotate
# tran_img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
# plt.imshow(tran_img1)
# plt.title("Flip left to right")
# tran_img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
# plt.imshow(tran_img2)
# plt.title("Flip top to bottom")

# # rotate using degree
# angle = 45
# ro_img = img.rotate(angle)
# plt.imshow(ro_img)


# # resizing technique: hamming,bilinear,nearest,box,bicubic,lanczos
# newResize = (200,300)
# resize_img = img.resize(newResize, Image.BILINEAR)
# plt.imshow(resize_img)

# # watermark on picture
# from PIL import ImageFont
# from PIL import ImageDraw
# watermark_img = img.copy()
# draw = ImageDraw.Draw(watermark_img)
# font = ImageFont.truetype("C:/Users/ASUSKIM/Desktop/AR/New folder/Pil image processing/arial.ttf",20)  #choose font
# # (position, text-watermark, fill_color, font-object)
# draw.text((0,0),"Lin-Yi",(0,0,0),font=font)
# plt.imshow(watermark_img)

# # image watermark
# size = (200,300)
# crop_img = img.copy()
# crop_img.thumbnail(size) #preserve aspect ratio

# copied_img = img.copy()
# copied_img.paste(crop_img,(100,200))
# plt.imshow(copied_img)

# # convert to black and white
# bw_img = img.convert('L')
# plt.imshow(bw_img, cmap="gray") #use cmap = gray for matplotlib to correctly show black and white

# # convert different formats
# new_format_img = img.convert('HSV')
# plt.imshow(new_format_img)

# # convert numpy formats
# numpy_arr = np.array(img)
# print(numpy_arr.shape)

# numpy_img = Image.fromarray(numpy_arr)
# plt.imshow(numpy_img)

# # image enhance
# from PIL import ImageEnhance
# img_color_enhan = img.copy()
# # img1 = ImageEnhance.Color(img_color_enhan).enhance(2.5)
# # plt.imshow(img1)
# # img1 = ImageEnhance.Contrast(img_color_enhan).enhance(2.5)
# # plt.imshow(img1)
# # img1 = ImageEnhance.Brightness(img_color_enhan).enhance(1.5)
# # plt.imshow(img1)
# # img1 = ImageEnhance.Sharpness(img_color_enhan).enhance(2.5)
# # plt.imshow(img1)

# # blend image or image over image
# copied_img = img.copy()
# copied_img2 = img2.copy()
# copied_img2 = copied_img2.resize(copied_img.size)   #make both img same size
# # blending
# img_blend = Image.blend(copied_img,copied_img2,-1)
# plt.imshow(img_blend)

# flipping channel
img_channel = img.copy()
r,g,b = img_channel.split()
im = Image.merge("RGB",(b,g,r))
plt.imshow(im)