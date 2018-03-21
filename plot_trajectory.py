import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
import time
import skimage.draw


import image_data
import image_processing as ip


if __name__ == "__main__":

    movgen = image_data.all_movies()

    all_x=[]
    all_feat=[]

    for em,movie in enumerate(movgen):
        framegen = image_data.all_frames(movie)
        x = image_data.synced_times(em)
        features = []
        for ef,frame in enumerate(framegen):
            feat = []

            com_out = np.zeros([frame.shape[1],frame.shape[2]])
            com, labels, numlabels = ip.find_food_vacuole_centroid(frame[0,:,:])
            #com_out[labels==1] = 1
            rr,cc = skimage.draw.circle(com[0],com[1],10)
            com_out[rr,cc] = 1

            feat.append(np.sum(frame[1,int(com[0])-50:int(com[0])+50,int(com[1])-50:int(com[1])+50]))

            #if ef == 0:
            #    centroid = com
            #mask, RP = ip.get_cell_mask(frame,centroid)



            #feat.append(np.sum(frame[1,int(com[0])-50:int(com[0])+50,int(com[1])-50:int(com[1])+50]))

            features.append(feat)
        features = np.array(features)
        maxfeat = features.max(axis=0)
        features = features.astype(np.float) / maxfeat

        #maxfeat = features.max(axis=1)

        #plt.plot(x, norm)
        #plt.show()
        #plt.pause(10)

        all_x.append(x)
        all_feat.append(features)

        plt.plot(x,features)
        plt.draw()
        plt.pause(2)
