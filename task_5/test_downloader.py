from downloader import Downloader
import os


def test_downloader_index():
    d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\testerFile.parquet")
    paths = d[0]
    assert len(paths) > 0 # Just to make sure there is some checking as we can't predict the exact number of files
    assert os.path.exists(paths[0])
    os.remove(paths[0])


def test_downloader_slice():
    d = Downloader(r"C:\Users\itsab\Documents\Github\prapro\testerFile.parquet")
    paths = d[0:5]
    assert len(paths) > 0 # Checking done
    for path in paths:
        assert os.path.exists(path)

    for path in paths:
        os.remove(path)
