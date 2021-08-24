# THIS CONTAINS THE CLASS IMPLEMENTATION FOR OUR INTERNET SPEED POLICE BOT THAT COMPLAINTS ON TWITTER.
from selenium import webdriver
import time


PROMISED_DOWN = 300
PROMISED_UP = 300
CHROME_DRIVER_PATH = "C:/Users/nikyadav/Downloads/100 days/Development/chromedriver.exe"
USERNAME = ''  # YOUR USERNAME
PASSWORD = ''  # YOUR PASSWORD


class SpeedComplaintBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.download_speed = None
        self.upload_speed = None

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start_test = self.driver.find_element_by_css_selector('.start-text')
        start_test.click()
        time.sleep(10)
        speed_found = False

        while not speed_found:
            try:
                self.download_speed = float(self.driver.find_element_by_css_selector('.download-speed').text)
                self.upload_speed = float(self.driver.find_element_by_css_selector('.upload-speed').text)
                speed_found = True

            except ValueError:
                time.sleep(5)

    def raise_complaint(self):
        if self.download_speed >= PROMISED_DOWN and self.upload_speed >= PROMISED_UP:
            print("Speed is Good!! No need to complain")
        else:
            self.driver.get('https://twitter.com/login')
            email = self.driver.find_element_by_name('session[username_or_email]')
            password = self.driver.find_element_by_name('session[password]')

            email.send_keys(USERNAME)
            password.send_keys(PASSWORD)

            login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                             'div/div[2]/form/div/div[3]/div/div/span/span')
            login_button.click()
            tweet_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                          'div/div/div/div/div[2]/div/div[2]/div[1]/div/'
                                                          'div/div/div[2]/div[1]/div/div/div/div/div/div/'
                                                          'div/div/label/div[1]/div/div/div/div/div[2]/'
                                                          'div/div/div/div')
            tweet_box.send_keys(f'hey @airtelindia why am I getting down/up speed of'
                                f'{self.download_speed}/{self.upload_speed} Mbps when i paid for'
                                f' {PROMISED_DOWN}/{PROMISED_UP} Mbps')
            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/'
                                                             'main/div/div/div/div/div/div[2]/div/div[2]/div[1]'
                                                             '/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet_button.click()

    def power_down_bot(self):
        self.driver.quit()
