# LabaBot: Telegram study bot.

#### <a href="https://www.youtube.com/watch?v=KIISj27Uc4A">See the presentation video here.</a>

## About

This repository is the source code of my CS50x' final project. The project is a telegram bot that helps you study. The idea came from my girlfriend, which is currently studying for university entrance exams and all of the functionalities came to solve her problems. In the end, i built this bot because i wanted to help her and other students to study better, and also learn about some new technologies.

## Main tools

The main tool used for this project was the python library _python-telegram-bot_, which is a convenint wrapper for the telegram library that helps with the development of bots. To explain the structure of the project, i need to contextualize some elements of this library:
1. _CommandsHandler_: is a class that defines a function to be triggered when some command is used by the user.
2. _MessageHandler_: is a class that defines a function to be triggered when some textual element or phrase is used by the user.
3. _ConversationHandler_: is a class that defines a set of command and message handlers to construct a conversation, or a process that requires multiple messages with the user.
4. _JobQueue_: is a class that allow a bot to schedule events in the future. 
I also used some other various python libraries for API integration, XML and HTML parsing, date and time conversion and validation.

## Main problems faced

### Non-relational database

Instead of using a conventional relational database, i opted for using _mongodb_, a document-oriented non-relation database. The main problem i faced was learning the architecture and how to use it's python driver commands to perform CRUD operations.

### Parsing data

Some API's sent their response data in different patterns for each request, which required me to perform some creative parsing with HTML and XML.

### Documentation and resources

The _python-telegram-bot_ is a famous python library, but very few resources on its features are available, which made the documentation essential for making this project, because dealing with elements such as the JobQueue could only be found in it.

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
1. The _/start_ and _/help_ command give you a list of the commands.
2. The _/hello_ command gives you more information about the author and the bot itself.
The bot also includes some hidden commands, not explicitly available for the user because it can lead to some unfortunate mistakes:
1. The _/cleartasks_ and _cleartests_ commands clear all of your tasks and tests, respectively. I made them only so that i could test the task and tests functiionalities better.
And last, a feature that is not a command:
1. The bot sends you a warning message on the day of your test, so that you can prepare yourself.

## Future improvements.

I plan on deploying this bot in the near future, which is why i plan on analyzing performance, database usage and overall improving integration with other applications. Some actual problems are:
1. Making data such as the test reminders in the jobqueue persist when the server is turned off.
2. Add validators for API dependencies.
3. Improve the test warning feature, adding multiple warnings and custom warning time.
3. Add more features for helping students.
