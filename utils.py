import os
import numpy as np

# from skimage.io import imread

def check_files(directory):
    files = sorted(next(os.walk(directory))[2])
    if len(files) == 0:
        raise ValueError("No files found in {}".format(directory))
    if len(files) != 1:
        raise ValueError("Only one file expected. Found {}".format(len(files)))

    f = files[0]
    if not f.endswith('.h5') and not f.endswith('.tif'):
        raise ValueError("Only a .h5 or .tif file is expected. Given {}".format(os.path.join(directory,f)))
    return os.path.join(directory, f)

def evaluate_volume(img):
    print("\tCalculating volumes . . .")
    values, volumes = np.unique(img, return_counts=True)
    values=values[1:].tolist()
    volumes=volumes[1:].tolist()
    return values, volumes

def evaluate_cable_length(vertices, edges, res = [1,1,1]):
    # make sure vertices and res have the same order of zyx
    """
    Returns cable length of connected skeleton vertices in the same
    metric that this volume uses (typically nanometers).
    """
    if len(edges) == 0:
        return 0
    v1 = vertices[edges[:,0]]
    v2 = vertices[edges[:,1]]

    delta = (v2 - v1) * res
    delta *= delta
    dist = np.sum(delta, axis=1)
    dist = np.sqrt(dist)
    return np.sum(dist)