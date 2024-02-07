import requests
import pyarrow.parquet as pq
import PIL as Image
from io import BytesIO

class Downloader :

    def __init__(self, pq_file : str) :
        table = pq.read_table(pq_file)
        df = table.to_pandas()
        self.data = df[0:1500]

    def __getitem__(self, index):
        
        if isinstance(index, int):
            if index < 0 or index >= len(self.data):
                raise IndexError("Index out of range")
            links = [self.data.iloc[index]["URL"]]

        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self.data))
            links = self.data.iloc[start:stop]["URL"]

        count = 0
        paths = []
        for link in links:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    path = f'C:\\Users\\itsab\\Documents\\Github\\prapro\\images\\image_{count}.jpg'
                    image.save(path)
                    paths.append(path)
                    count += 1
                else:
                    print(f"Failed to download image from {link}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading image from {link}: {e}")
        
d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\links.parquet")
print(d[10])
