#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

def get_topic_images(topic_id):
    req = requests.get('http://habrahabr.ru/post/' + str(topic_id) + '/')
    if req.status_code != 200:
        return
    all_images = re.findall(r'<img\s+src="([^"]+)"', req.text)
    result = set()
    for image in all_images:
        if image.find('//habrastorage.org/') != -1 or image.find('mc.yandex.ru/watch') != -1 or image.find('ad.adriver.ru') != -1:
            continue
        if image.find('"/images/') != -1 or image.find('http://habrahabr.ru/i/') != -1:
            continue
        result.add(image)
    return result

def get_images_for_topics_range(start_topic_id, end_topic_id):
    images = set()
    for i in range(start_topic_id, end_topic_id):
        images.update(get_topic_images(i))
    print(images)

def main():
    get_images_for_topics_range(61884, 61885)

if __name__ == '__main__':
    main()
