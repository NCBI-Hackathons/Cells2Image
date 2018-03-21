from scipy.stats import zscore
import numpy as np


def gradient_trigger(input_series, threshold=-2.5):
    # function takes a 1D input series and outputs the gradients, z scores of the gradients
    # and the frame when the z score threshold is first crossed

    gradients = np.gradient(input_series)
    # set gradient of first data point to zero
    gradients[0] = 0.

    # set first 2 z_scores to 0
    z_scores = [0., 0.]
    for i in range(2, len(gradients)):
        z_scores.append(zscore(gradients[:i])[-1])

    z_scores = np.array(z_scores)

    if threshold >= 0:
        trigger_index = np.where(z_scores >= threshold)[0][0]
    else:
        trigger_index = np.where(z_scores <= threshold)[0][0]

    return gradients, z_scores, trigger_index

