from time import sleep
from os import path
from sys import exit
import random
import ast

try:
    from igramscraper.instagram import Instagram
except ImportError:
    print("Please run 'pip install -r requirements.txt' before running this script")
    exit()

# bot account username
bot_username = 'FILL THIS OUT'

# bot account password
bot_password = 'FILL THIS OUT'

# username of account to track
username = 'FILL THIS OUT'

def get_unfollowers(current, old):
    ''' returns a list of unfollowers '''
    return list(set(old) - set(current))

def check():
    ''' runs unfollower statistic check '''
    try:
        print("Running check...")

        # instantiation
        instagram = Instagram()
        instagram.with_credentials(bot_username, bot_password)
        instagram.login(force=False, two_step_verificator=True)
        sleep(random.randint(1,2))

        # get current followers
        followers = []
        account = instagram.get_account(username)
        sleep(random.randint(1,2))
        followers = instagram.get_followers(account.identifier, 10**6, 100, delayed=True) # get 100 followers per request at delayed intervals

        curr = []

        for follower in followers['accounts']:
            curr.append(follower.username)

        # update followers list
        if path.exists("followers.txt"):
            with open("followers.txt", "r+") as f:
                old = f.read()
                f.seek(0)
                f.write(str(curr))
                f.truncate()

            old = ast.literal_eval(str(old))

            # calculate followers
            unfollowers = get_unfollowers(curr, old)

            print('-----------------------')
            print(f'Follower Count: {len(curr)}')
            print(f'Unfollow Count: {len(unfollowers)}\nUnfollowers: {str(unfollowers)[1:-1]}')
            print('-----------------------')
        
        else:
            print("This is your first time running. 'followers.txt' generated.")
            with open("followers.txt", "w") as f:
                f.write(str(curr))

    except KeyboardInterrupt:   # hides error messages on keyboard interrupt
        exit(0)


if __name__ == "__main__":
	check()







