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
Python 2.7.15
0105:fixme:msvcrt:__clean_type_info_names_internal (0x1e2719e0) stub
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

[http://localhost:3000](http://localhost:3000)

## TTS Server API

GET Request - list all SAPI voices

```
curl http://localhost:3000/api/v1/voices
```

POST Request - Speak text params: (data: { voice: "Voice Name", text: "Some Text" })

```
curl http://localhost:3000/api/v1/speak -d"voice=Microsoft Mary&text=Test this app"
```

GET Request - Stop reading

```
curl http://localhost:3000/api/v1/stop
```
