import time
import numpy as np
import multiprocessing.shared_memory as shm
from concurrent import futures

def random_filler(arr_shared, size, partition_number):
    # Open the shared memory block
    memory = shm.SharedMemory(name=arr_shared)
    arr = np.ndarray(shape=(size,), dtype=np.float64, buffer=memory.buf)
    np.random.seed()  # Use a random seed
    start = partition_number * size//10
    
    if partition_number != 9 :
        end = start + (size//10)-1
        arr[start:end] = np.random.randint(-50,50,(size//10)-1)
    else :
        end = start + size//10
        arr[start:end] = np.random.randint(-50,50,size//10)
        
    memory.close()
        
def create_filled_array(n) :
    start = time.time()
    # Create a large NumPy array and store it in shared memory
    memory = shm.SharedMemory(create=True, size=n * np.float64().itemsize)

    with futures.ProcessPoolExecutor() as executor:
        processes = [executor.submit(random_filler, memory.name, n, i) for i in range(10)]
        futures.wait(processes)
    
    arr = np.ndarray(shape=(n,), dtype=np.float64, buffer=memory.buf)
    
    print(f"Time taken : {time.time() - start}")
    arr = np.array(arr)
    memory.close()
    memory.unlink()
    # Close the shared memory block
    return arr
