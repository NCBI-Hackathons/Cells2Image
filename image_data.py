import skimage.io
import gc
import random
import numpy as np

prefix = '../Curated Images/'

images = [
            { 'filename':'recording1.czi - recording1.czi #03.tif', 'rounded':69, 'egress':76, 'length':124, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #07.tif', 'rounded':95, 'egress':102, 'length':124, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #09.tif', 'rounded':109, 'egress':114, 'length':124, 'notes':'egress fail' },
            { 'filename':'recording1.czi - recording1.czi #12.tif', 'rounded':23, 'egress':28, 'length':124, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #13.tif', 'rounded':90, 'egress':100, 'length':124, 'notes':'egress fail' },
            { 'filename':'recording1.czi - recording1.czi #14.tif', 'rounded':8, 'egress':12, 'length':124, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #17.tif', 'rounded':73, 'egress':81, 'length':124, 'notes':'' },
            { 'filename':'recording1.czi - recording1.czi #18.tif', 'rounded':9, 'egress':13, 'length':124, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #03.tif', 'rounded':61, 'egress':69, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #04.tif', 'rounded':38, 'egress':42, 'length':133, 'notes':'egress fail' },
            { 'filename':'recording2.czi - recording2.czi #05.tif', 'rounded':28, 'egress':40, 'length':133, 'notes':''},
            { 'filename':'recording2.czi - recording2.czi #06.tif', 'rounded':104, 'egress':110, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #09.tif', 'rounded':63, 'egress':69, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #11.tif', 'rounded':26, 'egress':31, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #14.tif', 'rounded':26, 'egress':33, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #15.tif', 'rounded':75, 'egress':82, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #17.tif', 'rounded':73, 'egress':78, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #18.tif', 'rounded':0, 'egress':6, 'length':133, 'notes':'' },
            { 'filename':'recording2.czi - recording2.czi #20.tif', 'rounded':90, 'egress':96, 'length':133, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #10.tif', 'rounded':455, 'egress':463, 'length':600, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #12.tif', 'rounded':194, 'egress':198, 'length':600, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #13.tif', 'rounded':134, 'egress':139, 'length':600, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #16.tif', 'rounded':250, 'egress':254, 'length':600, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #19.tif', 'rounded':145, 'egress':151, 'length':600, 'notes':'' },
            { 'filename':'timelapse.czi - timelapse.czi #20.tif', 'rounded':254, 'egress':259, 'length':600, 'notes':'' }
        ]


def synced_times(index, event='rounded'):
    if event == 'rounded':
        return np.array(range(0,images[index]['length']))-images[index]['rounded']
    elif event == 'egress':
        return np.array(range(0,images[index]['length']))-images[index]['egress']
    else:
        return np.array(range(0,images[index]['length']))

def all_movies():
    for image in images:
        print 'Loading movie',image['filename'],'...',
        img = skimage.io.imread(''.join([prefix,image['filename']]))
        print 'loaded'
        yield img
        gc.collect()

def load_movie(filename):
    movie = skimage.io.imread(''.join([prefix,filename]))
    return movie

def all_frames(movie):
    for ef,frame in enumerate(range(movie.shape[0])):
        timepoint = movie[frame,:,:,:].squeeze()
        yield timepoint

def fetch_random_frame():
    imgnum = random.randint(0,len(images))
    img = skimage.io.imread(''.join([prefix,images[imgnum]['filename']]))
    framenum = random.randint(0,img.shape[0])
    return img[framenum,:,:,:].squeeze()

if __name__ == "__main__":
    print synced_times(5)
