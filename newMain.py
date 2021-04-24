
from time import sleep
import multiprocessing
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import concurrent.futures as conF
from secrets import pw
from selenium import webdriver


class InstaBot:
    def __init__(self, user, pw):
        self.user = user
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("window-size=1920,1080")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--proxy-server='direct://'")
        self.chrome_options.add_argument("--proxy-bypass-list=*")
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
        self.chrome_options.headless = True

        print("Would you like to run this in headless? (y/n)")
        answer = input()
        #
        # Initiate the headless or webbrowser run
        #
        if answer == 'n' or answer == 'n':
            try:
                self.driver = webdriver.Chrome()
            except Exception:
                print("Default webdriver not found. Switching to path")
                self.driver = webdriver.Chrome('C:\\bin\chromedriver.exe')
        else:
            try:
                self.driver = webdriver.Chrome(options=self.chrome_options)
            except Exception:
                print("Default webdriver not found. Switching to path")
                self.driver = webdriver.Chrome('C:\\bin\chromedriver.exe', options=self.chrome_options)

        #
        # Try catch for if Log in or Verification code pop up fails
        #
        try:
            self.driver.get("https://instagram.com")
            self.agent = self.driver.execute_script("return navigator.userAgent")
            # print(self.agent)
            # self.driver.get_screenshot_as_file("errorcapture1.png")
            self.driver.implicitly_wait(5)

            try:
                self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
                    .send_keys(user)
            except Exception:
                print("xpath Element not found with \"//input[@name=\"username\"]\"")
                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            # self.driver.find_element_by_xpath("//input[@name=\"username\"]")

            self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
                .send_keys(pw)

            self.driver.find_element_by_xpath("//button[@type=\"submit\"]") \
                .click()

            try:
                self.driver.find_element_by_xpath("//input[@name=\"verificationCode\"]").send_keys()

                self.driver.find_element_by_xpath("//button[contains(text(),'Confirm')]").click()

                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()



            except NoSuchElementException:
                print("Verification pop up did not appear. Continuing..")

                pass
        except Exception:
            print("Error occured in \'Log in\' phase. Capturing screenshot of page")
            self.driver.get_screenshot_as_file("LogInError.png")

            exit()
        print("Log In complete.. Running after_Log")
        self.after_Log()



    def after_Log(self):
        try:

            try:
                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

            except Exception:
                print("\'Save info\' page not found. Continuing.. ")
                pass
            try:
                self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

            except Exception:
                print("\'Notification pop up\' not found. Continuing.. ")
                pass

            try:
                self.driver.find_element_by_xpath("//a[contains(@href, '/{}/')]".format(self.user)) \
                    .click()

            except NoSuchElementException:
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img') \
                    .click()

                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div') \
                    .click()
        except Exception:
            print("Error occured in \'After Log\' phase. Capturing screenshot of page")
            self.driver.get_screenshot_as_file("AfterLogError.png")
            exit()

    def following(self):

        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a") \
            .click()

        self.following_names = self._get_names("Following")

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        return self.following_names

    def followers(self):

        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") \
            .click()

        self.follower_names = self._get_names("Followers")

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
            .click()
        return self.followers_names

    def _get_names(self, methodName):
        print("the {} method has called the _get_names method".format(methodName))
        try:

            sugs = self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]")

            self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        except NoSuchElementException:
            print("No suggestions tab found. Continuing..")
            pass
        sleep(1)

        last_ht, ht = 0, 1
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        return names

    def list_creation(self,trigger):

        if trigger != 1:
            print("Running Following method")
            return self.following()
        else:
            print("Running Follower method")
            return self.followers()

    def windowSelection(self, windowNum):
        if windowNum == 1:
            print("windowNum is 1")
            window = self.driver.window_handles[1]
            self.driver.switch_to.window(window)
            self.list_creation(windowNum)

        else:
            print("windowNum is 0")
            self.list_creation(windowNum)

    def processCreation(self):

        p1 = multiprocessing.Process(target=self.windowSelection, args=[1])
        p2 = multiprocessing.Process(target=self.windowSelection, args=[0])

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        self.driver.execute_script("window.open('http://www.instagram.com/{}')".format(self.user))


        # with conF.ProcessPoolExecutor() as executor:
        #     print("running p1")
        #     followerProcess = executor.submit(self.windowSelection,1)
        #     print("running p2")
        #     followingProcess = executor.submit(self.windowSelection,0)
        #     follower_names = followerProcess.result()
        #     following_names = followingProcess.result()
        #
        #     not_following_back = [user for user in following_names if user not in follower_names]
        #     print(not_following_back)




if __name__ == "__main__":
    my_bot = InstaBot('hunterwilson21', 'Jeeplife21!')
    print("Running List_Creation")
    my_bot.processCreation()




