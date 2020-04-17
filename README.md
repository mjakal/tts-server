# Wine TTS Server App

What is it? This is a bridge between two operating systems, with this app you can enjoy your favorite high quality SAPI5 voices on your linux machine.

I'm trying to create a simple interface for interacting with Windows SAPI5 engine on Linux using Wine and some other tools: (Python, Flask, pyttsx...).

## How to run it

Configure your Wine PREFIX to work with SAPI5 engine. If you are not sure how to do that, click on the link below:

[How to install and use Windows sapi5 voices on Linux](https://github.com/mjakal/sapi5_on_linux)

If you were able to get SAPI5 engine working, download and install the latest version of Python 2.7 on your TTS WINEPREFIX.

I will assume that you followed my tutorial for setting up WINEPREFIX and that your folder structure is identical to mine. On the other hand, modify the commands below for your folder structure.

First we need to check if Python is installed correctly on wine. Open your terminal and run these commands:

```
WINEPREFIX=~/.PlayOnLinux/wineprefix/tts wine cmd
python --version
```

Console output should be similar to this

```
Python 2.7.x
```

Open a new terminal window and navigate to tts WINEPREFIX drive_c folder.

```
~/.PlayOnLinux/wineprefix/tts/drive_c
```

Clone the repo.

```
git clone https://github.com/mjakal/tts-server.git
```

After cloning, go back to the terminal running Wine cmd app. Navigate to c:\ and cd into tts-server folder that you just cloned and run these commands.

```
pip install -r requirements.txt
python app.py
```

And thats it. Now you can check if everything went well by opening your browser and visiting this url.

[http://localhost:4000](http://localhost:4000)

## How to use it

I also included couple of handy shell scripts to help you interact with tts server from your linux system. In order to use them, make sure you have xclip installed on your system.

```
sudo apt-get install xclip
```

Shell scripts are located in /scripts folder.

* start.sh - starts the tts server. (If you have a different path to WINEPREFIX, change the start.sh location variable.)
* say.sh - speak text, you can set voice name as a script param (e.g. ./say.sh "voice name")
* stop.sh - stop reading text

You can also configure scripts to run by pressing hotkey. 

Copy/paste say.sh, stop.sh scripts from the repo to your /home/scripts folder and run these commands:

```
chmod +x say.sh
chmod +x stop.sh
```

1. On Ubuntu, open start menu, type in Keyboard and open the app.
2. Select Shortcuts tab and on the left hand side chose Custom shortcuts
3. Click on Add custom shortcut button
4. Enter a name then under Command, enter the script location. See the example below.

```
sh /home/(your_user_name)/scripts/say.sh 'voice name'
sh /home/(your_user_name)/scripts/stop.sh
```

## TTS Server API

GET Request - list all SAPI voices

```
curl http://localhost:4000/api/v1/voices
```

POST Request - Speak text params: (data: { voice: "Voice Name", text: "Some Text" })

```
curl http://localhost:4000/api/v1/speak -d"voice=Microsoft Mary&text=Test this app"
```

GET Request - Stop reading

```
curl http://localhost:4000/api/v1/stop
```
