import numpy as np;
import matplotlib.pyplot as plt
import matplotlib.image as img

pix = img.imread("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg")
pix = 128 + pix * 0.5
pix = pix.astype('uint8')
plt.imshow(pix)
plt.show()
plt.imsave("matplotlib_sangwa.jpg", pix)
