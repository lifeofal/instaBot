from time import sleep

from selenium.common.exceptions import NoSuchElementException

from secrets import pw
from selenium import webdriver

class InstaBot:
    def __init__(self, user, pw, sc):
        self.user = user


        self.driver = webdriver.Chrome('C:\\bin\chromedriver.exe');
        self.driver.get("https://instagram.com")
        sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(user)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
            .click()

        sleep(2)
        try:
            self.driver.find_element_by_xpath("//input[@name=\"verificationCode\"]").send_keys(sc)

            self.driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()

            sleep(2)

            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()



        except NoSuchElementException:
            sleep(1)
            pass

        self.after_Log()

    def after_Log(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(3)

        try:
            self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.user)) \
            .click()

        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img') \
                .click()
            sleep(1)

            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div')\
            .click()

        sleep(2)



    def following(self):


        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a") \
            .click()
        sleep(1)

        self.following_names = self._get_names()

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
        .click()


    def followers(self):

        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") \
            .click()
        sleep(1)

        self.follower_names = self._get_names()

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()


    def _get_names(self):
        try:

            sugs = self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]")

            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        except NoSuchElementException:
            pass
        sleep(1)

        last_ht, ht =0,1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        while last_ht !=ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        return names

    def list_creation(self):
        self.following()
        self.followers()
        not_following_back = [user for user in self.following_names if user not in self.follower_names]
        print(not_following_back)



my_bot = InstaBot('lifeof_alejandro', pw, 28901647)
my_bot.list_creation()