import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filters
from skimage import measure

import load_images

import image_processing as ip

ix=1
movie = skimage.io.imread(''.join([load_images.prefix,load_images.images[ix]['filename']]))
# print images[ix]['rounded']
stop=load_images.images[ix]['egress']

# circ=np.array(movie.shape[0])
circ=[]
intens=[]
feature=[]
# for frame in range(stop):
for frame in range(movie.shape[0]):
    A=movie[frame,1,:,:]
    Afluo=movie[frame,0,:,:]

    B,RP=ip.get_cell_mask(A,(250,250),ptile=75,blur_sigma=15)
    
    circ.append(4*np.pi*RP.area/(RP.perimeter**2))
    # intens.append(np.sum(B*Afluo))
    intens.append(np.sum(B*Afluo)/np.sum(B))

    L=measure.label(B)
    props=measure.regionprops(L,A)

    feature.append(props[0].mean_intensity)


    # plt.subplot(1,2,1)
    # plt.imshow(A,cmap='gray')
    # plt.subplot(1,2,2)
    # plt.imshow(A*B,cmap='gray')
    # # plt.imshow(Afluo*B,cmap='gray')
    # # plt.show()
    # plt.draw()
    # plt.pause(0.001)
    # plt.imshow(B,cmap='gray')
    #plt.imshow(L,cmap='gray')


# plt.plot(circ)
plt.subplot(3,1,1)
plt.plot(range(stop),circ[:stop])
plt.subplot(3,1,2)
plt.plot(range(stop),feature[:stop])
plt.subplot(3,1,3)
plt.plot(range(stop),intens[:stop])
plt.show()