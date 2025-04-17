
# Speech detection searching

This project is a simple Python script that listens to your voice, performs a Google search (focused on Wikipedia), fetches content from the top result, and reads it aloud using text-to-speech.


## Features

🎤 Speech-to-text voice input

🔍 Google Custom Search integration

📖 Scrapes top search result (typically Wikipedia)

🗣️ Reads the content aloud using pyttsx3



## Working

- You speak a query (e.g., “Albert Einstein”).

- The script appends “wikipedia” to the query to focus on informative results.

- It uses Google’s Custom Search API to fetch the top link.

- Scrapes the first few paragraphs from that page.

- Reads the content aloud.
## Requirements
- Python 3.x

- Libraries:

  - speechrecognition

  - pyttsx3

  - httpx

  - beautifulsoup4

  - pyaudio (may require extra steps on macOS)


##  Deploment


```bash
 pip install speechrecognition pyttsx3 httpx beautifulsoup4 pyaudio
```
- If pyaudio fails on macOS, install portaudio via Homebrew:

```bash
brew install portaudio
```

- Then

```bash
pip install pyaudio
```

## Acknowledgements

- [Google search api](https://developers.google.com/custom-search/v1/overview)

- [Google search engine](https://programmablesearchengine.google.com/controlpanel/all)

 
 
