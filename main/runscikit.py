__author__ = 'David McInnis'

import skimage.io as skio

image = skio.imread('1.jpg', True) #http://images.metmuseum.org/CRDImages/as/original/DP118649_CRD.jpg


skio.imshow(image)
skio.show()
