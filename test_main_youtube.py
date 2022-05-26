from collections import Counter
from unittest import TestCase

import requests
from bs4 import BeautifulSoup


def get_videotags(vid_url):
    if vid_url.__contains__(".com"):
        request = requests.get(vid_url)
        soup = BeautifulSoup(request.content, 'html5lib')
        tags = ', '.join(
            [meta_tag.attrs.get("content") for meta_tag in soup.find_all("meta", {"property": "og:video:tag"})])
        return tags

    else:
        print("no tags found")


class Test(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.target_video = "https://www.youtube.com/watch?v=W_HDjqL-Z3M"

    def video_existing_tags(self):

        if not get_videotags(self.target_video):
            return True
        else:
            return False

    def do_youtube_stuff(self):


        self.fail()

    def get_keywords_dictionary(self):
        return self.vid_tag_trends

    def set_keywords_dictionary(self, tube_urls: list):
        vid_diction = {}

        for url in tube_urls:
            vid_diction[url] = get_videotags(url)
        self.vid_tag_trends = vid_diction

    def get_average_kexwords(self):

        print("vid total = {}".format(self.vid_count()))

        print("total number of tags: {}".format(self.tag_total()))

        print("average number of tags {}".format(self.tag_total() / self.vid_count()))

    def most_frequent_tags(self):
        return Counter(self.all_tags().lstrip(' ').split(',')).most_common(
            int(self.tag_total() / self.vid_count()))

    def vid_count(self):
        return len(self.vid_tag_trends.keys())

    def all_tags(self):
        words = ""
        for tag in self.vid_tag_trends.values():
            words += (tag.strip() + ',')
        print(words)
        return words

    def tag_total(self):
        sum_of_tags = 0
        for vid in self.vid_tag_trends.keys():
            sum_of_tags += len(self.vid_tag_trends[vid].lstrip().split(','))
        return sum_of_tags

    def update_video(self, keywords_to_use):

        # TODO

        pass

    def save_existing_tags(self, video_to_update_url=None):
        self.backup_tags = get_videotags(video_to_update_url)

    def test_upper(self):
        self.set_keywords_dictionary(
            ["https://www.youtube.com/watch?v=gim2kprjL50", "https://www.youtube.com/watch?v=nY3O_gIjCP8"])

        self.get_average_keywords()
        common_keys = self.most_frequent_tags()
        print(common_keys)
        print("keyword bot")

