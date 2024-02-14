from downloader import Downloader
import time

if __name__ == "__main__":
    try:
        d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\links.parquet")
        start = time.time()
        print(d[0:50])
        end = time.time()
        print("Time taken to read the parquet file: ", end - start)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting gracefully...")
