from numpyArray import converter
import numpy as np


def test_converter():
    random_array = np.array(
        [
            [71, 66, 31, 15, 20],
            [31, 35, 53, 30, 31],
            [30, 93, 98, 46, 53],
            [46, 53, 26, 28, 50],
            [34, 0, 86, 68, 83],
        ],
        dtype=np.int64,
    )
    converted_array = converter(random_array)
    assert np.array_equal(random_array, converted_array)
