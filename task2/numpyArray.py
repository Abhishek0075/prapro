import numpy as np
import time

size = (1000, 1000)  

time1 = time.perf_counter()
# Generate a random array of shape (m, n) with values between 5 and 25
random_array = np.random.randint(0,100, size=size)
time2 = time.perf_counter()

print("Random Array:")
print(random_array)

print("Time taken to generate random array using numpy: ", time2-time1, " s")

inBytes = random_array.tobytes()

generated_array = np.frombuffer(inBytes, dtype=random_array.dtype).reshape(random_array.shape)
print(generated_array)
