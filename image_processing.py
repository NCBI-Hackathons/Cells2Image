import numpy as np
from scipy import ndimage

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

    polar = geometric_transform(img, transform, order=order)

    rads = max_radius * np.linspace(0,1,img.shape[0])
    angs = np.linspace(0, 2*np.pi, img.shape[1])

    return polar, (rads, angs)


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