import os, urllib.request

base = r"D:\做的小玩意\个人主页\demo\assets"
os.makedirs(base, exist_ok=True)

jobs = [
    ("https://aka.doubaocdn.com/s/tinSwKCSFb", os.path.join(base, "hero.png")),
    ("https://aka.doubaocdn.com/s/aZX8CUjdpr", os.path.join(base, "avatar.png")),
]

for url, path in jobs:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
        f.write(r.read())
    print("saved:", path, os.path.getsize(path), "bytes")
