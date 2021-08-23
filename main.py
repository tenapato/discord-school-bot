'''
School bot with schdule reminder
Dev: Patricio Tena

Version: 1.0

'''

import time
import discord
from discord.ext import commands, tasks
import datetime
from random import randint

classes_list = [
{
    "Class_name": "Coding 101",
    "Days" : ["Monday", "Tuesday"],
    "Schedule" : ["14:00", "16:00"],
    "Remind": ["13:55"],
    "zoom_link": "https://itesm.zoom.us/my/testzoomlink",
    "People": ["<@1000000000000>",],

}

]

weekdays = {0: "Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday"}  # Week day list for matching system day with human readable days

client = commands.Bot(command_prefix="!")  #Bot command prefix


@client.event
async def on_ready():
    check_schedule.start()
    print('Bot is ready')
    

@tasks.loop(seconds=59) # Check every 59 seconds to ensure one reminder is not repeated
async def check_schedule():
    channel = client.get_channel('channel_id')
    todays_day = weekdays[datetime.datetime.today().weekday()]
    current_time = time.strftime('%H:%M')

    for i in range(len(classes_list)):
        if todays_day in classes_list[i]["Days"]: # Check if the is a class
            if current_time in classes_list[i]["Remind"]: # If there is a class then remind at the given time
                print(classes_list[i]["Class_name"])
                if len(classes_list[i]["Days"]) > 1:
                    await channel.send(str(classes_list[i]["Name"] + ": " +str(classes_list[i]["zoom_link"]))+"\n"
                    + "Schedule: "+ str(classes_list[i]["Days"][0])+ " y "+ str(classes_list[i]["Days"][1]) + " | "+  str(classes_list[i]["Schedule"][0])+ " a "+ str(classes_list[i]["Schedule"][1]) +
                    "\n" + str(classes_list[i]["People"])[1:-1])    
                else:
                    await channel.send(str(classes_list[i]["Name"] + ": " +str(classes_list[i]["zoom_link"]))+"\n"
                        + "Schedule: "+ str(classes_list[i]["Days"][0]) + " | "+  str(classes_list[i]["Schedule"][0])+ " a "+ str(classes_list[i]["Schedule"][1]) +
                        "\n" + str(classes_list[i]["People"])[1:-1]) 




@client.command(name = "ping")   # Basic ping-pong command
async def on_message(message):
    await message.channel.send("pong")




client.run("client_id")