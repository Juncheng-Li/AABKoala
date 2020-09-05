from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('./images/background1.png')
rgb_im1 = im1.convert('RGB')
im2 = Image.open('./3DCRT.png')
rgb_im2 = im2.convert('RGB')

rgb_im1.paste(rgb_im2)
rgb_im1.save('./resultPaste.jpg', quality=95)
