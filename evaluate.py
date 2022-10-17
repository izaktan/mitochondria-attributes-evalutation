import os
import utils
import kimimaro
import h5py
import numpy as np
import pandas as pd
from skimage.io import imread

from utils import *

output_filename = "out.csv"

def evaluate(file_dir, out_dir=[os.getcwd() + "/out/"], data_resolution=[30,8,8]):
    if not os.path.isdir(file_dir):
        raise FileNotFoundError("{} directory does not exist".format(file_dir))
    else:
        input_file = check_files(file_dir)

    os.makedirs(out_dir, exist_ok=True)


    output_path = os.path.join(out_dir, output_filename)
    print("\tCalculating GT statistics . . .")


    """Calculate instances statistics such as volume, skeleton size and cable length."""
    if not os.path.exists(output_path):
        print("\tReading file {} . . .".format(input_file))
        if str(input_file).endswith('.h5'):
            h5f = h5py.File(input_file, 'r')
            k = list(h5f.keys())
            img = np.array(h5f[k[0]])
        else:
            img = imread(input_file)

        # evaluate volume
        values, volumes = evaluate_volume(img)

        print("\tSkeletonizing . . .")
        skels = kimimaro.skeletonize(img, parallel=0, parallel_chunk_size=100, dust_threshold=0)
        keys = list(skels.keys())
        print("\tCalculating cable length . . .")
        del img
        c_length = []
        skel_size = []
        vol = []
        for label in keys:
            ind_skel = skels[label]
            l = evaluate_cable_length(ind_skel.vertices, ind_skel.edges, res = data_resolution)
            c_length.append(l)
            skel_size.append(ind_skel.vertices.shape[0])
            vol.append(volumes[values.index(label)])

        # Kimimaro drops very tiny instances (e.g. 1 pixel instances). To be coherent later on we need those also
        # so we check which instances where not processed
        for v in values:
            if not v in keys:
                keys.append(v)
                vol.append(volumes[values.index(v)])
                c_length.append(1)
                skel_size.append(1)

        data_tuples = list(zip(keys,vol,skel_size,c_length))
        dataframe = pd.DataFrame(data_tuples, columns=['label','volume','skel_size','cable_length'])
    else:
        print("\tOutput directory already exist: {} )".format(output_path))
        dataframe = pd.read_csv(output_path, index_col=False)

    print("\tSaving statistics in {}".format(output_path))
    dataframe.to_csv(output_path, index=False)