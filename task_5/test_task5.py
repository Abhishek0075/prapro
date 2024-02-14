from downloader import Downloader
import os


def test_downloader_index():
    d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\links.parquet")
    paths = d[0]
    assert os.path.exists(paths[0])
    os.remove(paths[0])


def test_downloader_slice():
    d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\links.parquet")
    paths = d[0:5]
    for path in paths:
        assert os.path.exists(path)

    for path in paths:
        os.remove(path)
