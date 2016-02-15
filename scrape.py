#!/usr/bin/python
import praw
import urllib
import time

score = raw_input(“Popularity: ")
amount = raw_input("Number of Pictures: ")


user_agent = (“PicFinder”)

r = praw.Reddit(user_agent = user_agent)

multireddit = "pepethefrog+memes+vertical+dogfort+wojak+rarepepes+firstworldproblems+inglip+advice animals"

submissions = r.get_subreddit(multireddit).get_top(limit = int(amount) + 1)

num = 1


for submission in submissions:


    if submission.score >= int(score):

        if "imgur" in submission.url:
            new_url = submission.url[0:7]  + submission.url[7:len(submission.url)] + ".jpg"
            print new_url
            urllib.urlretrieve(new_url, str(num)+ ".jpg")
            num = num + 1


        elif "imgflip" in submission.url:
            new_url = submission.url[0:8] + "i." + submission.url[8:19] + submission.url[21:27]+".jpg"
            print new_url
            urllib.urlretrieve(new_url, str(num)  + ".jpg")
            num = num + 1

        elif "reddit" in submission.url :
            pass


        else:

            print submission.url
            urllib.urlretrieve(submission.url, str(num)  + ".webloc")
            num = num + 1

    else:
        pass










