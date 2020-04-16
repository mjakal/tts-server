#!/bin/bash
# Read selected text

# Parse sapi5 voice name when calling this script
# Ex: sh say.sh 'yome voice name'
voice_name=$1

# Get text from clipboard
selected_text=$(xclip -out -selection primary)

# Make API call
curl http://localhost:4000/api/v1/speak -d"voice=$voice_name&text=$selected_text"
