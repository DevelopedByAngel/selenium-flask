from flask import Flask,render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
# from bs4  import BeautifulSoup
import os
import re
import time
app=Flask(__name__)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
try:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
except:
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=r'C:\\Users\CLEMENT\Downloads\chromedriver_win32\chromedriver.exe')

# driverig=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver.get("https://www.google.com")
# html = driver.page_source
@app.route("/")
def main():
    # return ("<h1>"+html[:30]+"</h1>")
    # url = "PLLADcgxbx5IUdyln2GsoEViWCw6kHp0Ey"
    url = "https://www.youtube.com/channel/UCzh5hQc_O3r3xjh9sXrM7-A/playlists"
    # try:
    driver.get(url)
    driver.execute_script('window.scrollTo(0,document.querySelector("ytd-browse").scrollHeight)')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,document.querySelector("ytd-browse").scrollHeight)')
    time.sleep(2)
    html = driver.page_source
    try:
        soup = bs4.BeautifulSoup(html,features="lxml")
        ret = soup.find_all("ytd-grid-playlist-renderer")
        a = soup.find_all("a")
        li = []
        t = []
        # return ret
        for i in ret:
            pal = i.find("h3")
            if str(pal.text).strip() != "":
                # print(pal.text)
                t.append(str(pal.text).strip())
        for i in a:
            if re.search("/play", str(i.attrs.get("href"))) and str(i.text).strip() == "View full playlist":
                video = i.attrs.get('href')
                # print(video + " v")
                if video in li:
                    continue
                else:
                    li.append(video[15:])
        print(len(li), len(t))
        if len(li) == 0 or len(t) == 0:
            print("again")
            return main()
        else:
            # no_of_play1, play1, tr1, script1 = next("https://www.youtube.com/c/Unakkennapaa/playlists")
            # print(len(li) + no_of_play1, li + play1, t + tr1, '' + script1)
            # return (len(li) + no_of_play1, li + play1, t + tr1, '' + script1)
            return render_template("inner.html", no_of_play=len(li), play=li, tr=t,script="")
        # return ("ok")

    except Exception as e:
        return str(e)
@app.route("/show/<url>")
def show(url):
    print("https://www.youtube.com/playlist?list=" + url)
    l, t, imag = link("https://www.youtube.com/playlist?list=" + url)
    if (len(l) == 0):
        print("again link")
        return video(url)
    elif (len(imag) == 0):
        print("again image")
        return video(url)
    else:
        return render_template('2.html', video=l, no_of_video=len(l), title=t, img=imag, script="")
def link(url):
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url)
    while (True):
        try:
            driver.execute_script(
                'window.scrollTo(0,((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)-((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)/1.5)))')
            time.sleep(0.5)
            driver.execute_script(
                'window.scrollTo(0,((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)-((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)/2)))')
            time.sleep(0.5)
            driver.execute_script(
                'window.scrollTo(0,((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)-((document.querySelector("ytd-playlist-video-list-renderer").scrollHeight)/3)))')
            time.sleep(0.5)
            driver.execute_script(
                'window.scrollTo(0,(document.querySelector("ytd-playlist-video-list-renderer").scrollHeight))')
            time.sleep(0.5)
            break
        except Exception as e:
            continue
    html = driver.page_source
    # driver.close()
    soup =bs4.BeautifulSoup(html,features="lxml")
    a = soup.find_all("a")
    clicklink = []
    for i in a:
        if (str(i.attrs.get("id")) == "thumbnail" and i.attrs.get("href") != None):
            if("https://www.youtube.com/"+i.attrs.get("href") not in clicklink):
                clicklink.append("https://www.youtube.com/"+i.attrs.get("href"))
    title = []
    span = soup.find_all("span")
    for i in span:
        if (str(i.attrs.get("id")) == "video-title" and str(i.text).strip() != ''):
            if(str(i.text).strip() not in title):
                title.append(str(i.text).strip())
    # soup = BeautifulSoup(html, features="lxml")
    div = soup.find_all("ytd-thumbnail")
    image = []
    print(div)
    for d in div:
        im = d.find("a").find("yt-img-shadow").find("img")
        print(im.attrs.get("src"))
        if(im.attrs.get("src") not in image):
            image.append(im.attrs.get("src"))
    print("ok",len(clicklink))
    return clicklink,title,image
if __name__=='__main__':
    app.run()