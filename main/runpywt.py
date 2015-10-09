__author__ = 'David McInnis'

import matplotlib.pyplot as plt
from scipy import ndimage

import pywt


# Load image
original = ndimage.imread('1.jpg', mode='L')

waveList = pywt.wavelist()
fileCount = 0
for a in waveList:
    wavelet = pywt.Wavelet(a)
    LL, (LH, HL, HH) = pywt.dwt2(original, a, mode='sym')
    fig = plt.figure()
    for i in range(1,7):
        ax = fig.add_subplot(2, 3, i)
        ax.imshow(LL, origin='image', interpolation="nearest", cmap=plt.cm.gray)
        LL, (LH, HL, HH) = pywt.dwt2(LL, a, mode='sym')
    saveStr = 'w' + str(fileCount) + '.png'
    plt.savefig(saveStr)
    plt.close()
    fileCount += 1




# Wavelet transform of image, and plot approximation and details
#titles = ['Approximation', ' Horizontal detail',
#          'Vertical detail', 'Diagonal detail']
#coeffs2 = pywt.dwt2(original, 'bior1.3')
#LL, (LH, HL, HH) = coeffs2
#fig = plt.figure()
#for i, a in enumerate([LL, LH, HL, HH]):
#    ax = fig.add_subplot(2, 2, i + 1)
#    ax.imshow(a, origin='image', interpolation="nearest", cmap=plt.cm.gray)
#    ax.set_title(titles[i], fontsize=12)

#fig.suptitle("dwt2 coefficients", fontsize=14)

#plt.show()


