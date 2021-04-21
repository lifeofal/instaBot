import multiprocessing
import time
import concurrent.futures as conF
from main import InstaBot
from secrets import pw
import list_creation

if __name__ == "__main__":
    with conF.ProcessPoolExecutor() as executor:
        followerProcess = executor.submit(InstaBot, 'lifeof_alejandro', pw)
        #followingProcess = executor.submit(InstaBot,'lifeof_alejandro', pw)

        #d1 = followingProcess.result()
        d2 = followerProcess.result()

        following_names = list_creation(d2.driver, 0)
        follower_names = list_creation(d2.driver, 1)

        not_following_back = [user for user in following_names if user not in follower_names]
        print(not_following_back)