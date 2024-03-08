import requests
import pyarrow.parquet as pq
import PIL.Image as Image
from io import BytesIO
import threading
import sys

global counter
counter = 0

class Downloader:

    def __init__(self, path: str):
        table = pq.read_table(path)
        self.data = table[0:1500]["URL"]

    def downloadSave(self, links, paths):
        global counter
        lock = threading.Lock()

        for link in links:
            try:
                response = requests.get(link)
                counter += 1
                if response.status_code == 200:
                    lock.acquire()
                    try:
                        image = Image.open(BytesIO(response.content))
                        path = f"C:\\Users\\itsab\\Documents\\Github\\prapro\\images\\image_{counter}.jpg"
                        # print(f"Image saved successfully as image_{counter}.jpg")
                        print(f"Successful at {counter}")
                        image.save(path)
                        paths.append(path)
                    finally:
                        lock.release()
                else:
                    # print(
                    #     f"Failed to download image from {link}. Status code: {response.status_code}"
                    # )
                    print(f"Failed at {counter}")

            except KeyboardInterrupt:
                print("Ctrl+C detected. Stopping downloads.")
                sys.exit()
                
            except Exception as e:
                print(f"Error at {counter}")

    def __getitem__(self, index):
        global counter
        counter = 0
        paths = []

        if isinstance(index, int):
            if index < 0 or index >= len(self.data):
                raise IndexError("Index out of range")
            links = [self.data[index]]

        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self.data))
            links = self.data[start:stop]

        threads = []

        if len(links) < 10:
            num_threads = len(links)
            partition_size = 1
        else:
            num_threads = 10
            partition_size = len(links) // num_threads
            
        for i in range(num_threads):
            start_index = i * partition_size
            end_index = (i + 1) * partition_size

            if i == num_threads-1:  # Last partition
                end_index = len(links)

            # print("Partition:", i, "Start:", start_index, "End:", end_index)

            # Need to add lock at the threaded_downloadSave function for the count variable

            thread = threading.Thread(
                target=self.downloadSave, args=(links[start_index:end_index],paths, )
            )
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        return paths
