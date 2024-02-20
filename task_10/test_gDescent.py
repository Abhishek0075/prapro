from gradientDescent import gDescent
import numpy as np

def test_gDescent():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    (slope, intercept) = gDescent(x,y)
    assert slope is not None
    assert intercept is not None
