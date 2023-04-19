import os
from gtts import gTTS

# ICAO dictionary
icao_dict = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

def stringToICAO(string, icao_dict):
    # Convert string to ICAO equivalent
    icao_string = ""
    for char in string.upper():
        if char in icao_dict:
            icao_string += icao_dict[char] + " "
        else:
            icao_string += char + " "
    return icao_string

# Read text file
with open('input.txt', 'r') as file:
    text = file.read()

# Convert text to ICAO
icao_text = stringToICAO(text, icao_dict)

# Use gTTS to create speech
tts = gTTS(text=icao_text, lang='en')

# Save speech as mp3 file
tts.save('output.mp3')




