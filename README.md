# Voice to Hindi Translator

This Python script uses the SpeechRecognition library to recognize speech from your microphone and the Googletrans library to translate the recognized speech into Hindi or any other language of your choice.

## Prerequisites

Before running the program, you'll need to install the required Python libraries:

```bash
pip install SpeechRecognition googletrans==4.0.0-rc1
```

You will also need an active internet connection for the Google Translate API to work.

## Usage

1. Run the script by executing the Python file in your terminal or IDE.

   ```bash
   python voice_translator.py
   ```

2. The program will prompt you to speak something. Speak clearly into your microphone.

3. The program will recognize your speech and display what you said.

4. It will then translate the recognized text into Hindi by default or any other language you specify.

5. The translated text will be displayed in the terminal.

## Customization

You can customize the target language by changing the `target_language` parameter in the `translate_text` function. For example, you can set it to `'fr'` for French.

```python
translate_text(recognized_text, target_language='fr')  # Translate to French
```

