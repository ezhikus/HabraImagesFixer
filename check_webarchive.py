#!/usr/bin/env python3

import requests
import json
from time import sleep

def write_to_unfixable(line):
    print(' FAIL')
    with open('img_info/unfixable_images.txt', "a") as out_file:
        out_file.write(line)

def write_to_fixable(line, new_url):
    print(' OK - ' + new_url)
    with open('img_info/fixable_images.txt', "a") as out_file:
        out_file.write(line.strip() + ' ' + new_url + '\n')

def check_webarchive():
    line_number = 0
    with open('img_info/bad_images.txt', "r") as in_file:
        for line in in_file:
            line_number += 1
            if len(line.split()) < 2:
                continue
            url = line.split()[1]
            try:
                print(line.strip())
                req = requests.get('http://archive.org/wayback/available?url=' + url,  timeout = 8)
                if req.status_code != 200:
                    raise

                data = json.loads(req.text)
                if data['archived_snapshots']['closest']['available'] != True or len(data['archived_snapshots']['closest']['url']) == 0:
                    raise

                req_img = requests.head(data['archived_snapshots']['closest']['url'], verify=False, timeout = 8)
                if req_img.status_code != 200 or 'Content-Type' not in req_img.headers or 'image/' not in req_img.headers['Content-Type']:
                    raise

                write_to_fixable(line, data['archived_snapshots']['closest']['url'])

                if line_number % 100 == 0:
                    print('Processed lines:' + str(line_number))
                sleep(0.5)
            except:
                write_to_unfixable(line)

check_webarchive()