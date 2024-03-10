from filler import create_filled_array 
import numpy as np

if __name__ == "__main__" :
    arr = create_filled_array(100000)
    if np.isnan(arr).any() :
        print("Nan is present in the array")
    else :
        print(np.isnan(arr))
        print("No Nan is present in the array")