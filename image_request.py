import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")

import requests
from pathlib import Path

out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

image_url = "https://www.ymori.com/bookspython2nen/sample1.png"
imgdata = requests.get(image_url)

filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

with open(out_path, mode="wb") as f:
    f.write(imgdata.content)