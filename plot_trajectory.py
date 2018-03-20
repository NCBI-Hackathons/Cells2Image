import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import time
import skimage.draw

import image_data
import image_processing as ip


if __name__ == "__main__":

    movgen = image_data.all_movies()

    for em,movie in enumerate(movgen):
        framegen = image_data.all_frames(movie)
        x = image_data.synced_times(em)
        features = []
        for ef,frame in enumerate(framegen):
            feat = []
            #imgplot = plt.imshow(frame[1,:,:])
            #imgplot.set_cmap('gray')

            com_out = np.zeros([frame.shape[1],frame.shape[2]])
            com, labels, numlabels = ip.find_food_vacuole_centroid(frame[1,:,:])
            #com_out[labels==1] = 1
            rr,cc = skimage.draw.circle(com[0],com[1],10)
            com_out[rr,cc] = 1

            feat.append(np.sum(frame[0,int(com[0])-50:int(com[0])+50,int(com[1])-50:int(com[1])+50]))

            feat.append(np.sum(frame[1,int(com[0])-50:int(com[0])+50,int(com[1])-50:int(com[1])+50]))
            #patch,stuff = ip.topolar(frame[0,int(com[0])-50:int(com[0])+50,int(com[1])-50:int(com[1])+50])
            #plt.imshow(com_out, alpha=0.25, cmap=plt.get_cmap('Oranges'))

            #print ef
            #plt.imshow(patch)
            features.append(feat)
        features = np.array(features)
        plt.plot(x, features)
        plt.draw()
        plt.pause(10)
