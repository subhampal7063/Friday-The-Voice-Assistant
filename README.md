
# Friday AI Assistant

## Overview

Friday is a voice-controlled AI assistant that performs a variety of tasks based on user commands. From fetching information from Wikipedia to playing songs on YouTube and even sending emails, Friday is designed to assist with everyday activities.

## Features

- **Greeting the User**: Friday greets the user based on the time of the day.
- **Voice Commands**: Listens to user commands using speech recognition.
- **Wikipedia Integration**: Searches and provides a summary from Wikipedia.
- **Open Websites**: Opens commonly used websites like YouTube, Google, GeeksforGeeks, HackerRank, and Stack Overflow.
- **Play Songs**: Plays songs on YouTube based on user requests.
- **Tell Jokes**: Provides random jokes for a quick laugh.
- **Time Query**: Tells the current time.
- **Email Sending**: Sends emails to specified addresses.
- **Custom Greetings**: Responds to specific questions or commands like "how are you" or "who is your owner."

## Technologies Used

- **Python Libraries**:
  - `pyttsx3`: For text-to-speech functionality.
  - `datetime`: For fetching the current date and time.
  - `speech_recognition`: For converting speech to text.
  - `wikipedia`: For retrieving information from Wikipedia.
  - `webbrowser`: For opening web pages.
  - `pywhatkit`: For playing YouTube videos.
  - `smtplib`: For sending emails.
  - `os`: For opening files or applications.
  - `pyjokes`: For fetching jokes.

## Prerequisites

1. **Python 3.7 or higher**: Ensure Python is installed on your system.
2. **Libraries**: Install the required libraries using the following command:

   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyjokes
   ```

3. **Email Configuration**: Update the email and password in the `sendemail` function to match your own. Ensure "Less secure app access" is enabled for the email account you're using.

## How to Run the Project

1. Clone the repository or copy the script file to your local system.
2. Open a terminal or command prompt in the directory containing the script.
3. Run the script:

   ```bash
   python friday_ai.py
   ```

4. Speak your commands into the microphone when prompted.

## Commands

Here are some example commands you can give to Friday:

- **Wikipedia**: "Tell me about Python programming language on Wikipedia."
- **Open Websites**: "Open YouTube", "Open Google", "Open GeeksForGeeks".
- **Play Songs**: "Play [song name]".
- **Jokes**: "Tell me a joke."
- **Time**: "What is the time?"
- **Email**: "Send an email to me."
- **Custom Questions**: "How are you?", "Who is your owner?", "I love you".

## File Structure

- **`friday_ai.py`**: Main script containing the implementation of Friday AI Assistant.

## Important Notes

- **Microphone Access**: Ensure your microphone is properly configured and accessible by Python.
- **Email Functionality**: Use your credentials cautiously. For secure use, consider implementing OAuth2 for Gmail or using environment variables to store sensitive data.
- **Error Handling**: The assistant will prompt you to repeat a command if it does not understand your input.

## Future Enhancements

- Add functionality to fetch live news updates.
- Integrate advanced natural language processing for better understanding of user commands.
- Include a graphical user interface (GUI) for better user interaction.
