# Ai-Assiatant
# Speech Recognition and Voice Assistant

This project is a Python-based voice assistant that uses libraries like `speech_recognition`, `pyttsx3`, `pywhatkit`, and `wikipedia` to perform various tasks based on voice commands. It includes functionalities like playing YouTube videos, retrieving information from Wikipedia, and providing contact details like phone numbers and email addresses.

## Features

- **Play YouTube Videos:** Say "play [video name]" to play a video on YouTube.
- **Tell the Date:** Ask "date" to get the current date.
- **Tell the Time:** Ask "time" to get the current time.
- **Search Wikipedia:** Ask "who is [person's name]" to retrieve a brief summary from Wikipedia.
- **Retrieve Phone Numbers:** Ask "phone number of [name]" to get the phone number from the predefined dictionary.
- **Retrieve Gmail Addresses:** Ask "gmail of [name]" to get the email address from the predefined dictionary.

## Prerequisites

Make sure you have Python installed on your system. You also need to install the required Python libraries. Use the following commands to install them:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
```

## Usage

1. Clone this repository or copy the script into a Python file (e.g., `voice_assistant.py`).
2. Make sure your microphone is connected and accessible.
3. Run the script:

```bash
python voice_assistant.py
```

4. Speak your command clearly when prompted. The assistant will listen and respond accordingly.

## Example Commands

- "Play Shape of You"
- "What is the date?"
- "What time is it?"
- "Who is Albert Einstein?"
- "Phone number of Ravi"
- "Gmail of Raj"

## Code Overview

### Key Dictionaries

- `phone_numbers`: Stores predefined phone numbers for specific names.
- `gmails`: Stores predefined Gmail addresses for specific names.

### Functions

- `speak(command)`: Converts text to speech.
- `commands()`: Listens for voice input, processes commands, and performs the corresponding action.

### Libraries Used

- **`speech_recognition`**: For capturing and processing voice input.
- **`pyttsx3`**: For text-to-speech conversion.
- **`pywhatkit`**: For playing YouTube videos.
- **`wikipedia`**: For retrieving summaries about people or topics.
- **`datetime`**: For fetching the current date and time.

## Error Handling

The script includes error handling for issues like microphone capture errors. If an error occurs, it will print a message to the console.

## Note

- Ensure you have a stable internet connection for functionalities like playing YouTube videos or retrieving Wikipedia data.
- You can expand the `phone_numbers` and `gmails` dictionaries to include more contacts.

## License

This project is open-source and available under the MIT License.
