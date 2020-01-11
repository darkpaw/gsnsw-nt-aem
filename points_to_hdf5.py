import numpy as np
import h5py

from read_aem_points import load_aem_points


data_points, lines = load_aem_points()

dp = np.array(data_points)

with h5py.File('data/data.h5', 'w') as hf:
    hf.create_dataset('nt_aem_pts', data=dp, compression="gzip", compression_opts=9)


hf = h5py.File('data/data.h5', 'r')
print(hf.keys())

pts = hf.get('nt_aem_pts')
print(pts)

pts_arr = np.array(pts)
print(pts_arr.shape)

hf.close()
