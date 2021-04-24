from time import sleep

from selenium.common.exceptions import NoSuchElementException
from secrets import pw
from driver_methods import following,followers


def list_creation(driver, trigger):

    if not trigger:
        print("Running Following method")
        following_names = following(driver)
        return following_names

    else:
        print("Running Follower method")
        follower_names = followers(driver)
        return follower_names





