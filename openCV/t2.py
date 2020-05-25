# -*- coding : utf-8 -*-

import numpy as np
# pillow를 임포팅 하고, 원본을 불러온다.
from PIL import Image, ImageFilter
original_image = Image.open("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg")
original_image.show()

# 원본을 회전변환 시키자. 회전변환 시키는것은 pillow의 내장함수(.rotate(각도))를 사용하면 된다.
rotated_image = original_image.rotate(45)
rotated_image.show()

blurred_image = original_image.filter(filter=ImageFilter.SHARPEN)
#BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, SHARPEN, SMOOTH, SMOOTH_MORE
blurred_image .show()
print(f'원본은 : {np.array(original_image)}, 원본의 shape : {np.array(rotated_image).shape}\n원본의 타입: {type(np.array(blurred_image))}\n')
print(f'원본은 : {np.array(rotated_image)}, 원본의 shape : {np.array(rotated_image).shape}\n원본의 타입: {type(np.array(rotated_image))}\n')
print(f'원본은 : {np.array(blurred_image)}, 원본의 shape : {np.array(blurred_image).shape}\n원본의 타입: {type(np.array(blurred_image))}\n')
#im_blur.save("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg")
