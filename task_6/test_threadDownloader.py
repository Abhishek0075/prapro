import os
from downloader import Downloader
from pathlib import Path

# when we set paths global in downloader.py, it will be shared across all instances of Downloader
rootFilePath = Path(__file__).resolve().parent.parent
def test_downloader_index():
    path = f"{rootFilePath}\\testerFile.parquet"
    downloader_instance = Downloader(path)
    paths = downloader_instance[0]
    print(paths)
    assert len(paths) > 0 # Checking done
    assert os.path.exists(paths[0])
    os.remove(paths[0])


def test_downloader_slice():
    path = f"{rootFilePath}\\testerFile.parquet"
    downloader_instance = Downloader(path)
    paths = downloader_instance[0:30]
    print(paths)
    assert len(paths) > 0 # Checking done 
    for path in paths:
        assert os.path.exists(path)

    for path in paths:
        os.remove(path)
