import glob
import shutil
from pref import prefecture

used = set()
for f in glob.glob("irasutoya_images/*.png"):
    for p in prefecture.keys():
        if p in f:
            used.add(p)
            shutil.copy(f, f"png/{prefecture[p]}.png")

print(set(prefecture.keys())-used)
