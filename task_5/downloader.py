import requests
import pyarrow.parquet as pq
import PIL.Image as Image
from io import BytesIO
from pathlib import Path

rootFilePath = Path(__file__).resolve().parent.parent
class Downloader:

    def __init__(self, path: str):
        table = pq.read_table(path)
        self.data = table[0:1500]["URL"]

    def __getitem__(self, index):

        if isinstance(index, int):
            if index < 0 or index >= len(self.data):
                raise IndexError("Index out of range")
            links = [self.data[index]]

        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self.data))
            links = self.data[start:stop]

        count = 0
        paths = []
        for link in links:
            try:
                response = requests.get(link)
                count += 1
                # print(response.content)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    path = f"{rootFilePath}\\images\\image_{count}.jpg"
                    image.save(path)
                    paths.append(path)
                else:
                    print(
                        f"Failed to download image from {link}. Status code: {response.status_code}"
                    )
            except Exception as e:
                print(f"Error downloading image from {link}: {e}")

        return paths
