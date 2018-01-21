#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ficapy
# Create: '21/01/2018'

import os
from apscheduler.schedulers.blocking import BlockingScheduler
from telegram import Bot, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from hackernews import HackerNews

token = os.getenv("TOKEN")
assert token

hn = HackerNews()
bot = Bot(token)

scheduler = BlockingScheduler(timezone="Asia/Shanghai")


@scheduler.scheduled_job('cron', id='telegram', hour=9)
def message():
    print("Send Message")
    for story_id in hn.top_stories(limit=10):
        item = hn.get_item(story_id)

        score = InlineKeyboardButton(text="Score: {}".format(item.score), url=item.url)
        url = InlineKeyboardButton(text="Comments: {}".format(item.descendants),
                                   url="https://news.ycombinator.com/item?id={}".format(item.item_id))
        reply_markup = InlineKeyboardMarkup([[score, url]])
        bot.sendMessage(chat_id="@MyHN_Bot",
                        text="*{text}* [{url}]({url})".format(text=item.title, url=item.url),
                        parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

bot.sendMessage(chat_id="@MyHN_Bot",text="Everything is OK👌")
scheduler.start()
