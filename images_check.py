#!/usr/bin/env python3

import requests
from time import sleep

def check_images():
    line_number = 0
    with open('img_info/all_images.txt', "r") as in_file:
        for line in in_file:
            url = line.split()[1]
            try:
                req = requests.head(url, verify=False, timeout = 10)
                print(line.strip())
                if req.status_code == 200 and 'Content-Type' in req.headers and 'image/' in req.headers['Content-Type']:
                    print(' OK')
                    with open('img_info/good_images.txt', "a") as out_file:
                        out_file.write(line)
                else:
                    print(' FAIL')
                    with open('img_info/bad_images.txt', "a") as out_file:
                        out_file.write(line)
                line_number += 1
                if line_number % 100 == 0:
                    print('Processed lines:' + str(line_number))
                sleep(0.1)
            except:
                with open('img_info/bad_images.txt', "a") as out_file:
                    out_file.write(line)

check_images()