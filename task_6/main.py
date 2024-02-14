from downloader import Downloader

if __name__ == "__main__":
    d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\links.parquet")
    paths = d[0:30]
    print(paths)
