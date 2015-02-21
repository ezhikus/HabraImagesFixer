#!/usr/bin/env python3

import requests

def check_images():
    with open('img_info/all_images.txt', "r") as in_file:
        with open('img_info/bad_images.txt', "w") as out_file:
            for line in in_file:
                print(line)
                url = line.split()[1]
                req = requests.get(url)
                if req.status_code == 200:
                    print('OK')
                else:
                    print('FAIL')
                    out_file.write(line)