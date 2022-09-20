from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from PIL import Image

#Get info from the user about the searchable stuff
search_item = 'tony stark' #String
directory = r'C:\Users\Eli Brignac\OneDrive\Pictures\TonyStark' #Make it a raw string or use \\ instead of \
file_name = 'Ironman' #String
driver = None

def open_google():
    global driver
    driver = webdriver.Chrome('C:\chromedriver.exe')  # Dont change


#Opens google images and searches the image
def search_google_images():
    driver.get('https://images.google.com/')
    box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    box.send_keys(search_item)
    box.send_keys(Keys.ENTER)

#Will scroll down the whole website until it can no longer scroll
def scroll_down():
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

#screenshot the images and put them in the directory
#Can increase the amount of images saved by increasing the for loop range
#Note that google normally won't show more then 999 images of a single topic
def save_all_images():
    counter = 0
    #1000 is more then enough to get all of the photos google images has to offer
    for i in range(1, 1000):
        try:
            image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
            counter += 1
            image.screenshot(directory + '\\' + file_name + str(counter) + '.jpg')
        except:
            pass
    print('All Images have successfully been saved to "' + directory + '"')

def close_browser():
    driver.quit()

def remove_all_images():
    for i in range(1, 1000):
        try:
            os.remove(directory + '\\' + file_name + str(i) + '.jpg')
        except:
            pass
    print('All images have successfully been removed from "'+ directory + '"')


def convert_1080x1080():
    counter = 1
    for pic in os.listdir(directory):
        im = Image.open(directory + '\\' + pic)
        im1 = im.resize((1080, 1080))
        rgb_im = im1.convert('RGB')
        rgb_im.save(directory + '\\' + file_name + str(counter) + '.jpg')
        #os.remove(directory + '\\' + file_name + str(i) + '.jpg')
        counter += 1
        print(pic, rgb_im.size)


# open_google()
# search_google_images()
# scroll_down()
# save_all_images()
# close_browser()
convert_1080x1080()
# remove_all_images()
