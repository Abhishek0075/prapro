import numpy as np
from filler import create_filled_array
 
def test_Nan():
    arr = create_filled_array(100000)
    assert not np.isnan(arr).any()