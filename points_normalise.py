import numpy as np
import h5py


hf = h5py.File('data/data.h5', 'r')
print(hf.keys())

pts = hf.get('nt_aem_pts')
print(pts)

pts_arr = np.array(pts)

hf.close()

print(pts_arr.shape)


rows_max = []

for row in pts_arr:
    row_max = max(row[3:])
    rows_max.append(row_max)

max_value = max(rows_max)
print(max_value)

# print(pts_arr[:20, 3:] / max_value)

normalised_values = pts_arr[:, 3:] / max_value

with h5py.File('data/data.h5', 'a') as hf:
    hf.create_dataset('nt_aem_pts_normalised', data=normalised_values, compression="gzip", compression_opts=9)




