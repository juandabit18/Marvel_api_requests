#!/usr/bin/python3

import hashlib, requests, webbrowser, shutil, json

puk = "1e7ba5ed30011bea00c1e83d13065a24"
prk = "04bfdce07ec3dad0b8a17210138e9c43ea03330c"
ts = "2"
suma = ts+prk+puk
hash = hashlib.md5(suma.encode("utf-8")).hexdigest()

parameter = {"apikey": puk, "ts": ts, "hash": hash}

r = requests.get("http://gateway.marvel.com/v1/public/characters", parameter)

packages_json = r.json()

packages_cute = json.dumps(packages_json, indent=2)
#print(packages_cute)

#data = input("Enter the name of the character: ")
data = "spider-man"

package_url = "http://gateway.marvel.com/v1/public/characters?nameStartsWith={}".format(data)
print("The url to search for the character is:", package_url)
r = requests.get(package_url, parameter)
package_json = r.json()
package_str_cute = json.dumps(package_json, indent=2)

package_dr = package_json["data"]["results"][0]
package_dr_str_cute = json.dumps(package_dr, indent=2)

character_name = package_dr["name"]
character_description = package_dr["description"]

print("The information of the character is:\nName: {}\nDescription: {}".format(character_name, character_description))

image_url = package_dr["thumbnail"]["path"]+".jpg"

webbrowser.open_new_tab(image_url)
