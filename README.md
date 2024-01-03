# Speech-to-Text Dictation using Python

This Python script utilizes the `speech_recognition` library to enable speech-to-text dictation. The code allows for continuous speech recognition, converting spoken words into text and typing them using the `pyautogui` library.

## Prerequisites

- Python 3
- Install required Python libraries:

    ```bash
    pip install pyautogui
    pip install SpeechRecognition
    ```

## How to Use

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Run the script:

    ```bash
    python your_script.py
    ```

## Features

- Start and stop dictation using voice commands.
- Continuously transcribe spoken words into text.
- Typing the transcribed text using `pyautogui`.
- Graceful handling of stop commands to end dictation.

## Code Overview

### `Dictation` Class

- `start`: Initiates the dictation process and continuously listens in the background.
- `stop`: Stops the dictation process.
- `callback`: Callback function for speech recognition, typing the recognized words using `pyautogui`.

### `test` Function

- Creates an instance of the `Dictation` class and starts the dictation process.

### `spell_word` Function

- Takes an input text and returns a string spelling out each letter.

## Example

To test the script, run the provided `test()` function. Speak into the microphone, and the recognized words will be typed using `pyautogui`. The dictation will stop when you say "stop," "dictate," or "jarvis."

```python
from your_script import test

test()
