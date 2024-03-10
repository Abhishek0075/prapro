import pyarrow.parquet as pq
import requests
from io import BytesIO
from PIL import Image
from pathlib import Path
# import time
# import psutil

# def monitor_system(interval=1):
#     while True:
#         # Monitor CPU usage
#         cpu_percent = psutil.cpu_percent(interval=interval)
#         print(f"CPU Usage: {cpu_percent}%")

#         # Monitor network usage
#         network_io = psutil.net_io_counters()
#         print(
#             f"Network Usage: Sent={network_io.bytes_sent} bytes, Received={network_io.bytes_recv} bytes"
#         )

#         time.sleep(interval)
rootFilePath = Path(__file__).parent.parent.resolve()

def download_and_save_images(links, max_images=1000):
    count = 0
    for link in links:
        count += 1
        try:
            response = requests.get(link)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image.save(f"{rootFilePath}/images/image_{count}.jpg")
                if count >= max_images:
                    break
            else:
                continue
                # print(f"Failed to download image from {link}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image from {link}: {e}")


if __name__ == "__main__":

    table = pq.read_table(f"{rootFilePath}/testerFile.parquet")
    links = table["URL"]

    # monitor_thread = threading.Thread(target=monitor_system)
    # monitor_thread.start()

    download_and_save_images(links[0:2])
