# LabaBot: Telegram study bot.

#### <a href="https://www.youtube.com/watch?v=KIISj27Uc4A">See the presentation video here.</a>

## About

This repository is the source code of my CS50x' final project. The project is a telegram bot that helps you study. The idea came from my girlfriend, which is currently studying for university entrance exams, and i wanted to help her and other students to study better.

## Project structure

1. In them main file _main.py_, we have the entry point of the application.
2. The _env.py_ stores all of the enviroment variables and sensitive information.
3. The _utils_ folder contains the code for all the handlers divided in its categories. Which are: command handlers, message handlers, conversation handlers and function that deal with the jobqueue functionality.
4. The _connections_ folder is where all of the code for connecting with API's and the mongodb database are.

## Bot features

Here are some of the main commands of the bot:
1. The _/def_ command lets you get the definition for a word in the portuguese dictionary.
2. The _/wiki_ commands lets you get the definition for a concept in the portuguese wikipedia.
3. The _/addtask_, _/removetask_ and _/seetasks_ lets you add, remove and see all of your tasks.
4. The _/addtest_, _/removetest_ and _/seetest_ lets you add, remove and see all of your test.
5. The _/startpomodoro_ and _/cancelpomodoro_ allow you to start and stop pomodoro session.
The bot also include some helper commands for better usage.

## Future improvements.

I plan on deploying this bot in the near future, which is why i plan on analyzing performance, database usage and overall improving integration with other applications. Some actual problems are:
1. Making data such as the test reminders in the jobqueue persist when the server is turned off.
2. Add validators for API dependencies.
3. Add more features for helping students.
