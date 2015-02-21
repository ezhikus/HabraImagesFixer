#!/usr/bin/env python3

import requests

def check_images():
    with open('img_info/all_images.txt', "r") as f:
        f.write(ulr_info + '\n')

    req = requests.get('http://habrahabr.ru/post/' + str(topic_id) + '/')
    if req.status_code != 200:
        return result