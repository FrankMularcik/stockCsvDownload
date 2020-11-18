import wget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

os.chdir(r'C:\Users\mular')

#open chrome but don't show the window
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options = chrome_options)
url = "https://www.youtube.com/c/FrankMularcik/videos"

browser.get(url)

#find the first video title
video = browser.find_element_by_xpath("//a[@id='video-title']")
title = str(video.text)

#click the video and capture the url
video.click()
vidurl = str(browser.current_url)

#get thumbnail url and download it
thumb_url = vidurl.split('=')
thumbnail = wget.download('https://i.ytimg.com/vi/' + thumb_url[1] + '/maxresdefault.jpg')

#close browser
browser.quit()


