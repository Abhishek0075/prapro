from downloader import Downloader
import time
from pathlib import Path
if __name__ == "__main__":
    rootFilePath = Path(__file__).resolve().parent.parent
    try:
        d = Downloader(f"{rootFilePath}/testerFile.parquet")
        start = time.time()
        print(d[0:20])
        end = time.time()
        print("Time taken to read the parquet file: ", end - start)
    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting gracefully...")
