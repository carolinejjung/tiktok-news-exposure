from seleniumbase import Driver
#from selenium import webdriver
from selenium.webdriver.common.by import By # contains operators for the type of search we want to do
import time
from seleniumbase import BaseCase
from random import randint
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import html
import re
import numpy as np
import csv
from datetime import datetime
import os.path
import requests


class VideoScraper():

    chromebrowser = Driver(uc=True)
    actions = ActionChains(chromebrowser)

    def __init__(self, video_list, output_file):
        self.video_list = video_list
        self.output_file = output_file
        self.current_video = {}

    def fetch_all_video_tiktok(self):
        """
        Open tiktok, access webpage
        """
        for i, video_url in enumerate(self.video_list):
            self.chromebrowser.uc_open_with_reconnect(video_url,reconnect_time=5)
            if i == 0:
                time.sleep(40) #log in time!
            else:
                time.sleep(5) #no log in time

            try:
                #stats_bar = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-79f36w-DivActionBarWrapper eqrezik8"]')
                video_info = self.info_video()
                print(video_info) #printout
            except StaleElementReferenceException:
                print("Was not able to find sth.")

    def info_video(self):
        output_dic = {}
        like_text = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-n6wn07-StrongText edu4zum2"]')[0]
        like_stats = like_text.text
        print(like_stats)
        output_dic['like'] = like_stats
        return output_dic





        # self.chromebrowser.uc_open_with_reconnect(self.url,reconnect_time=5)
        # time.sleep(40)
        # new_url = "https://www.tiktokv.com/share/video/6998935379097193734/"
        # self.chromebrowser.uc_open_with_reconnect(new_url,reconnect_time=5)
        # time.sleep(100)


###testing###
test_url_list = ['https://www.tiktokv.com/share/video/7131051793299033390/', 'https://www.tiktokv.com/share/video/6995476685563104538/']

#response = requests.get(test_url)
#print(response.text)
scraper = VideoScraper(test_url_list, 'output.json')
scraper.fetch_all_video_tiktok()


    # def __init__(self, url):
    #     self.id = url.split('/')[-2]
    #     self.url = url
    #     self.likes = None
    #     self.saves = None
    #     self.shares = None
    #     self.comments = []
    #     self.comments_count = None
    #     self.creator = None
    #     self.sound = None
    #     self.description = None
    #     self.hashtags = []