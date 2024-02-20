import os
from downloader import Downloader

# when we set paths global in downloader.py, it will be shared across all instances of Downloader

def test_downloader_index():
    path = r"C:\Users\itsab\Documents\Github\prapro\links.parquet"
    downloader_instance = Downloader(path)
    paths = downloader_instance[0]
    print(paths)
    assert len(paths) > 0 # Checking done
    assert os.path.exists(paths[0])
    os.remove(paths[0])


def test_downloader_slice():
    path = r"C:\Users\itsab\Documents\Github\prapro\links.parquet"
    downloader_instance = Downloader(path)
    paths = downloader_instance[0:100]
    print(paths)
    assert len(paths) > 0 # Checking done 
    for path in paths:
        assert os.path.exists(path)

    for path in paths:
        os.remove(path)
