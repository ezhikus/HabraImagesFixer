#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

import requests

def get_topic_images(topic_id):
    req = requests.get('http://habrahabr.ru/post/' + str(topic_id) + '/')
    if req.status_code != 200:
        return
    print(req.text)

def main():
    get_topic_images(250997)

if __name__ == '__main__':
    main()
