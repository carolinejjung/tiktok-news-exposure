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
        self.all_videos = []

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

        output_dic['id'] = [video_url.split('/')[-2] for video_url in self.video_list]
        video_stats_list = self.video_stats()
        output_dic['likes'] = video_stats_list[0]
        output_dic['comment_count'] = video_stats_list[1]
        output_dic['saves'] = video_stats_list[2]
        output_dic['shares'] = video_stats_list[3]
        output_dic['hashtags'] = self.get_hashtag()
        output_dic['music'] = self.get_music()
        output_dic['author'] = self.get_author()
        output_dic['description'] = self.get_description()
        self.scroll_to_bottom()
        output_dic['comments'] = self.get_comments()
        
        #where the comments are
        #comment_cont = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-13revos-DivCommentListContainer ekjxngi3"]')

        return output_dic
    
    def video_stats(self):
        try:
            video_stats = self.chromebrowser.find_elements(By.XPATH, '//*[@class="css-n6wn07-StrongText edu4zum2"]')
            likes = self.get_stats(video_stats[0].text)
            comment_count = self.get_stats(video_stats[1].text)
            saves = self.get_stats(video_stats[2].text)
            shares = self.get_stats(video_stats[3].text)

            return [likes, comment_count, saves, shares]
        except NoSuchElementException:
            print("Video stats elements not found.")
            return []

    def get_stats(self, num_as_string):
        try:
            # Extract numerical value using regex
            match = re.search(r'(\d+\.\d+|\d+)([KM])?', num_as_string)
            if match:
                # Check if suffix (K or M) is present
                if match.group(2) == 'K':
                    converted = float(match.group(1)) * 1000  # Convert K to actual number
                elif match.group(2) == 'M':
                    converted = float(match.group(1)) * 1000000  # Convert M to actual number
                else:
                    converted = float(match.group(1))
                return int(converted)
            else:
                return 0
        except (NoSuchElementException, ValueError):
            print(f"Unable to retrieve the number of target:{num_as_string}")
            return -1
        
    def get_hashtag(self):
        try:
            hashtag_list = self.chromebrowser.find_elements(By.XPATH, './/*[@class="css-1p6dp51-StrongText ejg0rhn2"]')
            if hashtag_list == None:
                return []
            else:
                return [hashtag.text.strip('#') for hashtag in hashtag_list]
        except NoSuchElementException:
            print("Hashtag element not found.")
            return []
    
    def get_music(self):
        try:
            music_info = self.chromebrowser.find_element(By.XPATH, ".//*[@class='css-pvx3oa-DivMusicText epjbyn3']")
            music = music_info.text if music_info else None
            if music:
                return music
            else:
                return None
        except (NoSuchElementException, ValueError):
            print("Unable to retrieve the number of music")
            return -1
        
    def get_author(self):
        try:
            author_element = self.chromebrowser.find_element(By.XPATH, ".//*[@class='css-1c7urt-SpanUniqueId evv7pft1']")
            return author_element.text if author_element else None
        except NoSuchElementException:
            print("Author element not found.")
            return None
        
    def get_description(self):
        try:
            description_element = self.chromebrowser.find_element(By.XPATH, ".//*[@class='css-j2a19r-SpanText efbd9f0']")
            return description_element.text if description_element else None
        except NoSuchElementException:
            print("Description element not found.")
            return None

    def scroll_to_bottom(self):
        try:
            old_comment_elements = self.chromebrowser.find_element(By.XPATH, ".//*[@class='css-1i7ohvi-DivCommentItemContainer eo72wou0']")
            new_comment_elements = None
            while new_comment_elements != None and new_comment_elements != old_comment_elements:
                self.actions.move_to_element(old_comment_elements[-1]).perform()
                new_comment_elements = self.chromebrowser.find_element(By.XPATH, ".//*[@class='css-1i7ohvi-DivCommentItemContainer eo72wou0']")
                time.sleep(1)
        except NoSuchElementException:
            print("Not able to get to the bottom.")
            return None
        
    def get_comments(self):
        all_comments = []
        try:
            comments = self.chromebrowser.find_elements(By.XPATH, ".//*[@class='css-xm2h10-PCommentText e1g2efjf6']//span[@dir]")
            for comment in comments:
                comment_text = comment.text
                all_comments.append(comment_text)
            return all_comments
        except NoSuchElementException:
            print("Error scraping comments down.")
            return None



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

#scraper.all_videos.append()


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