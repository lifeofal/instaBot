from selenium.common.exceptions import NoSuchElementException
from time import sleep


def following(driver):
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a") \
        .click()

    following_names = _get_names(driver,"Following")

    driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
        .click()
    return following_names


def followers(driver):
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") \
        .click()

    follower_names = _get_names(driver,"Followers")

    driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button") \
        .click()
    return follower_names

def _get_names(driver, methodName):
    print("the {} method has called the _get_names method".format(methodName))
    try:

        sugs = driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]")

        driver.execute_script('arguments[0].scrollIntoView()', sugs)
    except NoSuchElementException:
        print("No suggestions tab found. Continuing..")
        pass
    sleep(1)

    last_ht, ht = 0, 1
    scroll_box = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    while last_ht != ht:
        last_ht = ht
        sleep(1)
        ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)

    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    return names




