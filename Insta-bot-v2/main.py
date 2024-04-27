import config
from instagrapi import Client
from pytube import YouTube
from pytube.innertube import _default_clients
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

def no_session():
    cl = Client()
    if(int(input("Is there 2fa? yes = 1/ no = 0: "))):
        code = input("2FA Code: ")
    else:
        code = ""
    cl.login(config.username, config.password,verification_code=code)
    cl.dump_settings("session.json")

def session_upload():
    cl = Client()
    cl.load_settings("session.json")
    cl.delay_range = [1, 3]
    cl.login(config.username, config.password,verification_code="")
    cl.clip_upload("video.mp4",config.upload_text)

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename='video.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")

try:
    cl = Client()
    cl.load_settings("session.json")
    cl.login(config.username, config.password,verification_code="")
except:
    print("Session is not avaiable")
    print("Creating session.json")
    no_session()
    print("Sucessfull Created!")

link = input("Youtube Link:")
print("Downloading...")
Download(link)
print("Downloading Complete!!")
print("Staring Uploading on insta....")
session_upload()
print("Uploading on insta done!")