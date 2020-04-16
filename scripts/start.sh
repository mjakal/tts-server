#!/bin/bash
# Start TTS Server App

# Set your wine prefix location if necessary
location=~/.PlayOnLinux/wineprefix/tts

# Start the server
WINEPREFIX=$location wine python c:/tts-server/app.py
