import multiprocessing
import time
import concurrent.futures as conF
from main import InstaBot
from secrets import pw
import list_creation

if __name__ == "__main__":
    with conF.ProcessPoolExecutor() as executor:
        followerProcess = executor.submit(InstaBot, 'lifeof_alejandro', pw, 1)
        followingProcess = executor.submit(InstaBot,'lifeof_alejandro', pw, 0)
        d1 = followerProcess.result()
        d2 = followingProcess.result()

        print(d1)

