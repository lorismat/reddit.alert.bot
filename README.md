# What do I do?

It's fairly simple, every day, I send the top 3 most upvoted songs from reddit.com/r/hiphopheads of the past week.   
Now I work for personal users, and feel free to recreate this bot for your personal use!  
On my side, I deployed it on a raspberry to have it up and running 24/7.  

If you are interested in the process to have it up and running, [here is a quick guide](https://github.com/git1984/some.guides/blob/master/telegram_reddit_pi.md) to combine Telegram, Reddit and a raspberry.  

# How do I work

Once you have recreated your own bot and replaced the required variables, get your bot running and make it `/start`. You will get fresh update on Hip Hop music.  

Technologies used:

- Python3
- RaspberryPi 0, to deploy the service and get the bot up and running 24/7

# Repository structure

- `bot.py` is the core code
- `reddit.alert.env` is the virtual environment to set up
- `requirements.txt` is gathering the required packages

