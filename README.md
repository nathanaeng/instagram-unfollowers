# Instagram Unfollower Tracker
## NOTICE:
As of recently, this script does not seem to work consistently. I am currently investigating this, and may look into using another library.

Keep track of who unfollows you on Instagram!

## How It Works
This script uses a package called [igramscraper](https://pypi.org/project/igramscraper/) to scrape Instagram. In order to use this script, you must create a 'bot' or 'fake' account which will be used to access your actual Instagram account. This serves as a layer as safety - if Instagram detects unusual behavior and shuts down the account due to scraping, the 'bot' account will be affected, not your own.

The script will generate a list of your current followers and store that in `followers.txt`. Each subsequent execution of the script will compare `followers.txt` (which now stores your old followers or the list of followers at the time you last ran the script) with a list of your current followers, print the difference, and then re-write `followers.txt` with the current followers. In terminal talk, essentially `diff` is being ran against your old and current followers.

## Usage
1. Run `pip install -r requirements.txt` (Note: you may need to use `pip3`)
2. Enter your 'bot' account credentials in `unfollowers.py` (at the top of the file)
3. Enter your actual username in `unfollowers.py` (at the top of the file)
4. Run `unfollowers.py` once to generate a `.txt` file containing your followers
5. Run `unfollowers.py` an additional time to see Instagram unfollow statistics (it will take some time for your followers to change though)

Steps 1-4 only need to be ran once for initialization. After that, step 5 can be used at any time.

## Things to Note:
- Users that change their username will show up as 'unfollowers'
- Deleted accounts will show up as 'unfollowers'
- You should not run this script multiple times consecutively without any breaks in between. This could potentially cause a `429 Error`.

## More Specifics
- Account being fetched can have a maximum of 1 million followers. However, the script will take an extremely long time to run with an account of this size, so it is recommended to use this script on accounts with less followers (~0-5000).
