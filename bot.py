import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests
import datetime
import json
import pytz
from time import strftime,localtime

moment_now = strftime("%A, %d %b %Y, %H-%M", localtime())

#telegram secret
updater = Updater(token='XXXXX_your_bot_token_XXXXX', use_context=True)

def start(update, context):
    #time scheduler
    while True:
        time.sleep(10)
        x = strftime("%H-%M", localtime())
        #here, change your daily alert accordingly
        if (x == '17-35'):
            print('working') 
            #### REDDIT ####
            subreddit = 'hiphopheads'
            limit = 100
            t = 'week'
            url = str('https://www.reddit.com/r/%s/top.json?t=%s&limit=%s'%(subreddit,t,limit))
            #below, pass your user agent to let the reddit API who you are
            r = requests.get(url,headers={'User-Agent': 'specify your user agent to reddit'})
            data = r.json()
            top_songs = []
            for i in range(0,100):
                title = data['data']['children'][i]['data']['title']
                if "FRESH" in title and "ALBUM" not in title \
                                    and "VIDEO" not in title:
                    print(title)
                    url = data['data']['children'][i]['data']['url']
                    top_songs.append(str(url))
    
            for song in top_songs[0:3]:
                context.bot.send_message(chat_id=update.effective_chat.id, text=song)
                time.sleep(3)
            time.sleep(100)
                    ####

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
