import pyarrow.parquet as pq
import requests
from io import BytesIO
from PIL import Image
import time 
import threading
import psutil

# Monitor system usage

# def monitor_system(interval=1):
#     while True:
#         # Monitor CPU usage
#         cpu_percent = psutil.cpu_percent(interval=interval)
#         print(f"CPU Usage: {cpu_percent}%")

#         # Monitor network usage
#         network_io = psutil.net_io_counters()
#         print(f"Network Usage: Sent={network_io.bytes_sent} bytes, Received={network_io.bytes_recv} bytes")

#         time.sleep(interval)



def threaded_downloadSave(links):
    lock = threading.Lock()
    global counter # Initialize count variable outside the loop
    counter = 0

    for link in links:
        try:
            response = requests.get(link)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                lock.acquire()  # Acquire the lock
                try:
                    image.save(f'C:\\Users\\itsab\\Documents\\Github\\prapro\\images\\image_{counter}.jpg')
                    print(f"Image saved successfully as image_{counter}.jpg")
                    counter += 1  # Increment counter within the critical section
                finally:
                    lock.release()  # Release the lock
            else:
                print(f"Failed to download image from {link}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image from {link}: {e}")

global counter

if(__name__ == "__main__"):
    
    table = pq.read_table(r'C:\Users\itsab\Documents\Github\prapro\links.parquet')
    df = table.to_pandas()

    # Start a thread to monitor system usage
    
    # monitor_thread = threading.Thread(target=monitor_system)
    # monitor_thread.start()
    
    threads = []

    # Create and start multiple threads to download and save images
    
    total_links = len(df['URL'][0:20]) # Just taking a small subset of the df
    num_partitions = 5
    
    partition_size = total_links // num_partitions
    print("Total links:", total_links, "Partition size:", partition_size)
    
    for i in range(num_partitions+1):
        print(partition_size)
        start_index = i * partition_size
        end_index = (i + 1) * partition_size
        
        if (i == num_partitions):  # Last partition
            end_index = total_links
            
        print("Partition:", i, "Start:", start_index, "End:", end_index)
        
        # Need to add lock at the threaded_downloadSave function for the count variable
        
        thread = threading.Thread(target=threaded_downloadSave, args=(df['URL'][start_index:end_index],))
        thread.start()
        threads.append(thread)



    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    print("All threads finished")
    # monitor_thread.join()