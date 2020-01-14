import numpy as np
import h5py
from colour import Color


hf = h5py.File('data/data.h5', 'r')
print(hf.keys())

pts = hf.get('nt_aem_pts_normalised')
print(pts)

pts_arr = np.array(pts)

hf.close()

print(pts_arr.shape)


c1 = Color("green")
c2 = Color("yellow")
colour_range = list(c1.range_to(c2, 100))

print(colour_range)


def value_to_colour(value: float) -> str:
    col_idx = int(value * 100) - 1
    try:
        col = colour_range[col_idx]
    except IndexError as e:
        print(col_idx, value)
        raise e
    assert isinstance(col, Color)
    return col.get_hex()

pts_coloured = []

for rw in pts_arr:
    rw_col = list(map(value_to_colour, rw))
    pts_coloured.append(rw_col)

cols_arr = np.array(pts_coloured)

print(cols_arr)
