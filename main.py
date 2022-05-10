import json
import os

import requests

kext_data = requests.get("https://raw.githubusercontent.com/dortania/build-repo/builds/config.json").json()

required_kexts = json.load(open("kexts.json"))

kext_links = {i: kext_data[i]["versions"][0]["links"]["release"] for i in kext_data if i in required_kexts}

try:
    os.mkdir("kexts")
except:
    pass

for name, url in kext_links.items():
    kext_file = requests.get(url).content
    with open(os.path.join("kexts", name + ".zip"), "wb") as f:
        f.write(kext_file)
    print("Downloaded {}".format(name))

print("Done! Kexts in the `kexts` folder")
