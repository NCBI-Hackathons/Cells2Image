import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import filters
from skimage import measure

import image_data
import image_processing as ip


# moviegen=image_data.all_movies()
# for em,movie in enumerate(moviegen):
    # print em

for em in range(5):
    # em=0
    movie=image_data.load_movie(em)
    start=max(image_data.images[em]['rounded']-30,0)
    stop=image_data.images[em]['egress']+10
    framegen=image_data.some_frames(movie,start,stop)
    x=image_data.synced_times(em)
    x=x[start:stop]

    features=[]
    for ef,frame in enumerate(framegen):
        centroid,lab,nlab=ip.find_food_vacuole_centroid(frame[0,:,:])
        props,M=ip.get_cell_mask(frame,centroid,ptile=75,blur_sigma=15)
        
        # circ=4*np.pi*props[0].area/(props[0].perimeter**2)
        # features.append(circ)

        intens=props[1].mean_intensity
        features.append(intens)

        # entrop=measure.shannon_entropy(props[1].intensity_image)
        # features.append(entrop)
        
        # polar,(r,a) = ip.topolar(props[1].intensity_image)
        # radscore=np.var(polar.sum(axis=0))
        # # radscore=ip.feature_radial_std(frame,centroid,radius=50)
        # features.append(radscore)


        # fig=plt.figure(1,figsize=(8,4));fig.clf()
        # ax1=plt.subplot(1,2,1)
        # plt.cla()
        # plt.imshow(frame[0,:,:],cmap='gray')
        # plt.plot(centroid[1],centroid[0],'ro')
        # ax1.get_xaxis().set_ticks([])
        # ax1.get_yaxis().set_ticks([])
        
        # ax2=plt.subplot(1,2,2)
        # plt.cla()
        # plt.imshow(M*frame[0,:,:],cmap='gray')
        # ax2.get_xaxis().set_ticks([])
        # ax2.get_yaxis().set_ticks([])

        # # plt.imshow(props[0].intensity_image,cmap='gray')
        # # plt.imshow(polar,cmap='gray')
        # plt.draw()
        # plt.pause(0.01)

        # filename="../scratchImage/image%i.jpg" % ef
        # fig.savefig(filename,format='jpg')

        # plt.close()

    features = np.array(features)
    maxfeat = features.max(axis=0)
    minfeat = features.min(axis=0)
    features = (features.astype(np.float)-minfeat) / (maxfeat-minfeat)

    plt.plot(x,features)
    plt.xlabel("frame")
    # plt.ylabel("circularity")
    plt.ylabel("mean intensity")
    # plt.ylabel("radial variance")
    plt.draw()
    plt.pause(0.01)

# filename="images/circularity.png"
filename="images/mean_intensity.png"
# filename="images/radvar.png"
plt.savefig(filename,format='png')


# ix=1
# movie = skimage.io.imread(''.join([load_images.prefix,load_images.images[ix]['filename']]))
# # print images[ix]['rounded']
# stop=load_images.images[ix]['egress']

# # circ=np.array(movie.shape[0])
# circ=[]
# intens=[]
# feature=[]
# # for frame in range(stop):
# for frame in range(movie.shape[0]):
#     A=movie[frame,1,:,:]
#     Afluo=movie[frame,0,:,:]

#     B,RP=ip.get_cell_mask(A,(250,250),ptile=75,blur_sigma=15)
    
#     circ.append(4*np.pi*RP.area/(RP.perimeter**2))
#     # intens.append(np.sum(B*Afluo))
#     intens.append(np.sum(B*Afluo)/np.sum(B))

#     L=measure.label(B)
#     props=measure.regionprops(L,A)

#     feature.append(props[0].mean_intensity)


#     # plt.subplot(1,2,1)
#     # plt.imshow(A,cmap='gray')
#     # plt.subplot(1,2,2)
#     # plt.imshow(A*B,cmap='gray')
#     # # plt.imshow(Afluo*B,cmap='gray')
#     # # plt.show()
#     # plt.draw()
#     # plt.pause(0.001)
#     # plt.imshow(B,cmap='gray')
#     #plt.imshow(L,cmap='gray')


# # plt.plot(circ)
# plt.subplot(3,1,1)
# plt.plot(range(stop),circ[:stop])
# plt.subplot(3,1,2)
# plt.plot(range(stop),feature[:stop])
# plt.subplot(3,1,3)
# plt.plot(range(stop),intens[:stop])
# plt.show()