#!/usr/bin/env python3

import requests
import re
import os
from time import sleep

def get_topic_images(topic_id):
    req = requests.get('http://habrahabr.ru/post/' + str(topic_id) + '/')
    result = set()
    if req.status_code != 200:
        return result
    all_images = re.findall(r'<img\s+src="([^"]+)"', req.text)
    
    for image in all_images:
        if image.find('//habrastorage.org/') != -1 or image.find('mc.yandex.ru/watch') != -1 or image.find('ad.adriver.ru') != -1:
            continue
        if image.find('/images/') == 0 or image.find('habrahabr.ru/i/') != -1 or image.find('geektimes.ru/i/') != -1 or image.find('megamozg.ru/i/') != -1:
            continue
        result.add(image)
    return result

def get_images_for_topics_range(start_topic_id, end_topic_id):
    for i in range(start_topic_id, end_topic_id):
        current_topic_images = get_topic_images(i)
        for j in current_topic_images:
            ulr_info = str(i) + " " + j
            print(ulr_info);
            with open('img_info/all_images.txt', "a") as f:
                f.write(ulr_info + '\n')
        sleep(0.5)

if not os.path.exists('img_info'):
    os.makedirs('img_info')
get_images_for_topics_range(1, 188436) #188436 - info about movement of all new images to habrastorage.org
#get_images_for_topics_range(21, 30)
