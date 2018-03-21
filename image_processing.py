import numpy as np
from scipy import ndimage
from skimage.morphology import binary_dilation
from skimage import measure
from skimage import filters


def topolar(img, order=1):
    """
    Transform img to its polar coordinate representation.

    order: int, default 1
        Specify the spline interpolation order.
        High orders may be slow for large images.
    """
    '''From Stackreg'''
    # max_radius is the length of the diagonal
    # from a corner to the mid-point of img.
    max_radius = 0.5*np.linalg.norm( img.shape )

    def transform(coords):
        # Put coord[1] in the interval, [-pi, pi]
        theta = 2*np.pi*coords[1] / (img.shape[1] - 1.)

        # Then map it to the interval [0, max_radius].
        radius = max_radius * coords[0] / img.shape[0]

        i = 0.5*img.shape[0] - radius*np.sin(theta)
        j = radius*np.cos(theta) + 0.5*img.shape[1]
        return i,j

    polar = ndimage.interpolation.geometric_transform(img, transform, order=order)

    rads = max_radius * np.linspace(0,1,img.shape[0])
    angs = np.linspace(0, 2*np.pi, img.shape[1])

    return polar, (rads, angs)

def feature_radial_std(frame,centroid,radius=50):
    polar,(r,a) = topolar(frame[1,int(centroid[0])-radius:int(centroid[0])+radius,int(centroid[1])-radius:int(centroid[1])+radius])
    score = np.std(polar.sum(axis=0))
    return score

def find_food_vacuole_centroid(frame):
    dark_thresh = np.percentile(frame,0.25)
    mask = frame < dark_thresh
    labels, numlabel = ndimage.label(mask)
    for l in range(numlabel+1):
        if np.sum(labels == l) < 300:
            labels[labels==l] = 0
    labels, numlabel = ndimage.label(labels)
    com = ndimage.measurements.center_of_mass(np.ones(labels.shape),labels,numlabel)
    return com, labels, numlabel

def get_cell_mask(frame,centroid,ptile=75,blur_sigma=15):
    props=[]

    #first get the mask from gray image
    img=frame[0,:,:]
    M=np.abs(img-np.percentile(img.flatten(),ptile))
    M=ndimage.gaussian_filter(M,blur_sigma)
    thr = filters.threshold_otsu(M)
    M=M>thr
    L=measure.label(M)
    RP=measure.regionprops(L,intensity_image=img)
    d2=[]
    for obj in RP:
        d2.append((obj.centroid[0]-centroid[0])**2+(obj.centroid[1]-centroid[1])**2)

    keep=np.argmin(d2)
    M[L!=keep+1]=0
    props.append(RP[keep])
    
    #now get the region properties using the fluoresence channels
    L=measure.label(M)
    RP=measure.regionprops(L,intensity_image=frame[1,:,:])
    props.append(RP[0])
    RP=measure.regionprops(L,intensity_image=frame[2,:,:])
    props.append(RP[0])

    return props, M

def get_donut(center_mask):
    # takes a mask and returns the donut mask around it

    #generate circular mask for dilation
    r = 50
    y,x = np.ogrid[-r:r, -r:r]
    circle = x*x + y*y <= r*r

    # dilate and subtract
    total_mask = binary_dilation(center_mask,circle)
    donut_mask = total_mask - center_mask

    return donut_mask
