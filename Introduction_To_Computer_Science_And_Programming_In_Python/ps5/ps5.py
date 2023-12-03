# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Zakraia Jaddad
# Collaborators: None 
# Time: 

import feedparser
import requests
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """

    response = requests.get(url, verify=False)

    feed_content = response.content

    # editing 

    feed = feedparser.parse(feed_content)
    print(feed)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory : 

    def __init__(self, guid, title, description, link, pubdate): 
        self.__guid = guid
        self.__title = title
        self.__description = description
        self.__link = link
        self.__pubdate = pubdate


    # guid  
    def get_guid(self): 
        return self.__guid

    def set_guid(self, new_guid):
        self.__guid = new_guid         

    # title
    def get_title(self):
        return self.__title
    
    def set_title(self, new_title): 
        self.__title = new_title

    # description
    def get_description(self):
        return self.__description
    
    def set_description(self, new_description):
        self.__description = new_description

    # link
    def get_link(self):
        return self.__link
    
    def set_link(self, new_link):
        self.__link = new_link

    # pubdate
    def get_pubdate(self): 
        return self.__pubdate

    def set_pubdate(self, new_pubdate): 
        self.__pubdate = new_pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger): 

    def __init__(self, phrase : str) -> None:
        super().__init__()
        self.__phrase = phrase

    def is_phrase_in(self, text : str) -> bool:
        """ 
            takes a text: string
        """

        # case sensitive
        phrase = self.__phrase.lower().split(' ')
        text = text.lower()

        # removeing punctuations
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

        clean_text = clean_text.split(' ')

        # simple binary search 
        correct_word_counter = 0


        for word in clean_text: 

            if len(word) == 0: 
                continue

            if word == phrase[correct_word_counter]: 
                correct_word_counter += 1

            else : # means start again it's not the right words 
                correct_word_counter = 0


            if correct_word_counter == len(phrase): 
                return True

        return False

# Problem 3
class TitleTrigger(PhraseTrigger): 
    def __init__(self, phrase: str) -> None:
        super().__init__(phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase: str) -> None:
        super().__init__(phrase)

    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())
        
# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger): 
    def __init__(self, time: str) -> None:
        super().__init__()
        # convert time to datetime
        self.__time = datetime.strptime(time, "%d %b %Y %H:%M:%S")

    def get_time(self):
        return self.__time  

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, time: str) -> None:
        super().__init__(time)

    def evaluate(self, story) -> bool:
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) < self.get_time().replace(tzinfo=pytz.timezone("EST"))

class AfterTrigger(TimeTrigger):
    def __inti__(self, time: str) -> None:
        super().__init__(time)

    def evaluate(self, story) -> bool :
        return story.get_pubdate().replace(tzinfo=pytz.timezone("EST")) > self.get_time().replace(tzinfo=pytz.timezone("EST"))


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):

    def __init__(self, trigger) -> None:
        self.__trigger = trigger
        
    def evaluate(self, story):
        return not self.__trigger.evaluate(story)


# Problem 8
class AndTrigger(Trigger): 
    def __init__(self, trigger_1, trigger_2 ) -> None:
        self.__trigger_1 = trigger_1
        self.__trigger_2 = trigger_2

    def evaluate(self, story):
        return self.__trigger_1.evaluate(story) and self.__trigger_2.evaluate(story)

# Problem 9
class OrTrigger(Trigger): 
    def __init__(self, trigger_1, trigger_2) -> None:
        self.__trigger_1 = trigger_1
        self.__trigger_2 = trigger_2

    def evaluate(self, story):
            return self.__trigger_1.evaluate(story) or self.__trigger_2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("https://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            """ 
                This is no longer working 
            """
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            print(10, 'hello', stories)
            time.sleep(10)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

