# Discord School Bot

Open source discord bot that reminds you of your online classes

## Installation and hosting

This guide will cover how to install and host the bot on a raspberry pi. You can use any modell you want, although i suggest using the model 3 B+ onwards.

### Steps
1. Headless installation of raspberry pi os
![Raspberry pi imager](/img/img1.PNG)

a) Using the official [Raspberry Pi Imager](https://www.raspberrypi.org/software/), burn the version of your liking into a bootable Micro SD Card to run on the raspberry pi. (I recommend using the Lite version since it doesn't inlcude a desktop environment, there for making the pi run faster)

b) After burning the Raspberry pi os image, load it on the raspberry and let it boot. After a couple of minutes, take out the micro SD card and plug again into your computer. Then, in the file manager, create a file called "ssh" ***whith out an extension***. And then pop the card into the raspberry pi.
![SSH File](/img/img2.png)

c) To configure your pi, you need the IP address. You con find this in your router's DCHP lease allocation table

d) SSH into your pi

        ssh pi@ip-address
        Default password: raspberry
2. Starting the bot and leaving it running
    a) Creating a separate screen environment to leave the bot running

            screen -S "Scheduler"
            screen -ls (To confirm the screen was created correctly)
    ![Bot start](/img/img4.PNG)
    b) Connect to that Screen environment

            screen -r "Scheduler"

    c) Once you are in your raspberry pi, you need to make sure python is installed

                sudo apt-get update && apt-get upgrade
                sudo apt-get install python3.6
    d) Using python's packet manager install Discord.py dependencies and Screen (this will later be used to leave the process running)

            pip3 install discord
            sudo apt-get install Screen
    e) Clone this repository and navigate to it 

            git clone https://github.com/tenapato/discord-school-bot
            cd discord-school-bot/
    f) Start the bot and wait for it to initialize correctly

            python3 main.py
    ![Bot start](/img/img3.PNG)

    g) To detach from the screen use Ctrl+A+D, after that you can close the terminal normally
## How to customize the Discord bot code  

a) At the beginning of the code the is a template that shows you how classes should be added

![Class template](/img/img5.PNG)

You can add more classes by copying everything in between the keys "{}" and separating the by a comma. e.g:

    {
        "Class_name": "Coding 101",
        "Days" : ["Monday", "Tuesday"],
        "Schedule" : ["14:00", "16:00"],
        "Remind": ["13:55"],
        "zoom_link": "https://itesm.zoom.us/my/testzoomlink",
        "People": ["<@1000000000000>",],

    },
    {
    "Class_name": "Coding 102",
    "Days" : ["Monday", "Tuesday"],
    "Schedule" : ["14:00", "16:00"],
    "Remind": ["13:55"],
    "zoom_link": "https://itesm.zoom.us/my/testzoomlink",
    "People": ["<@1000000000000>",],

    }   

Notes:
- Days should be in quotation marks and separated by commas (As of now only up to 2 days are supported)
- Same applies to the schedule
- The remind data is when you will get remminded to join the class
- To tag people you should add the in the folling format, and should be separated by commas
> "<@user_id>"

b) You should create a channel to which the bot will send the reminders

        channel = client.get_channel('channel_id')

You can get the Channel_id by right a channel and clicking on Copy Id:

![Class template](/img/img6.PNG)

After getting the code, paste it in between the single quotes

c) Get your client id by follwing this [tutorial](https://discord.com/developers/docs/topics/oauth2)