import numpy as np
import h5py


d1 = np.random.random(size=(1000, 20))
d2 = np.random.random(size=(1000, 200))

with h5py.File('data/data.h5', 'w') as hf:
    hf.create_dataset('dataset_1', data=d1)
    hf.create_dataset('dataset_2', data=d2)






