import numpy as np
import h5py


hf = h5py.File('data/data.h5', 'r')
print(hf.keys())

pts = hf.get('nt_aem_pts')
print(pts)

pts_arr = np.array(pts)

hf.close()

print(pts_arr.shape)




