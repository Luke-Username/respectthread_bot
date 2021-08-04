#!/bin/bash
# The purpose of automatically stopping and rerunning the bot
# every few minutes is so the code can stay up to date with GitHub.

while :
do
git pull origin master
python3 main-bot/respectthread_bot.py
sleep 30
done
