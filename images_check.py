#!/usr/bin/env python3

import requests
from time import sleep

def check_images():
    line_number = 0
    start_line_number = 0
    end_line_number = 999999
    out_file_suffix = '1'
    with open('img_info/all_images.txt', "r") as in_file:
        for line in in_file:
            line_number += 1
            if line_number < start_line_number:
                continue
            if line_number > end_line_number:
                break
            if len(line.split()) < 2:
                continue
            url = line.split()[1]
            try:
                req = requests.head(url, verify=False, timeout = 8)
                print(line.strip())
                if req.status_code == 200 and 'Content-Type' in req.headers and 'image/' in req.headers['Content-Type']:
                    print(' OK')
                    with open('img_info/good_images' + out_file_suffix + '.txt', "a") as out_file:
                        out_file.write(line)
                else:
                    print(' FAIL')
                    with open('img_info/bad_images' + out_file_suffix + '.txt', "a") as out_file:
                        out_file.write(line)
                if line_number % 100 == 0:
                    print('Processed lines:' + str(line_number))
                sleep(0.05)
            except:
                with open('img_info/bad_images' + out_file_suffix + '.txt', "a") as out_file:
                    out_file.write(line)

check_images()