# -*- coding:utf-8 -*-

test_mode = 'pillow'

"""pillow로 했는데 여기서 암튼 뭐때문에 하이패스 필터 -> 이미지가 날카로워짐."""

if(test_mode=='pillow'):
    from PIL import Image, ImageFilter
    image=Image.open("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg")
    #image.show()
    #image.rotate(45).show()
    im_blur = image.filter(filter=ImageFilter.EDGE_ENHANCE)
        #BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, SHARPEN, SMOOTH, SMOOTH_MORE
    im_blur.show()
    im_blur.save("pillow_sangwa.jpg")

"""근데 pillow로 실행한 이미지 파일은 ndarray가 아니라서 아까처럼 우리가 직접만든 필터로 할 수 없음!!"""

"""pillow에서 ndarray로 캐스트하는 방법을 찾아야함!"""