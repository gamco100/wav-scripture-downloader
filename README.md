# Welcome to Wav Scripture Downloader

### Greetings
This is a simple flask app that downloads specific wav files for bible verses reading found on jw.org in **Portuguese**.

### Setup
It uses the modele **PyDub** for audio manipulation. **PyDub**, in turn, uses the **FFMPEG** library behind the curtains. **So in order for the __"Wav Scripture Downloader"__ to work you need to have the FFMPEG library installed.** If you are using **Windows,** simply downloading the code above will do the trick (that's because if you notice the 3 .exe files needed are already on the repository). However, if you are running this on a **macOS or Linux** environment, please follow the instructions on the link bellow: https://ffmpeg.org/download.html

### Instructions
- Type in each line a scripture address you wish to download
(ps: this only downloads audios from nwt-T)
- Use the following scripture address structure:
- [bible book] [chapter as a integer]:[verse blocks] (notice the space between the bible book and the chapter)
  - The verses should be divided using "," (comma) or "-" (hifen). If the verse block if formed by consecutive verses and only 2 verses in length, preferably use ","; if it's bigger than 2, use "-". You can divide multiple verse blocks using ",". 
  - Example:
    - ✗ Mateus capítulo seis versículo 9 e 8 e depois dos versículos 25-33. 
    - ✓ Mateus 6:9,8,25-33
- Each scripture must have verses inside only one chapter. Examples:
  - ✓ Mateus 6:28-33 
  - ✗ Mateus 6:28-33; 7:1-2 (for that, type in separate lines)
- You can separate verses with a comma, but they need to be in chronological order.
(and please, try not to write way too complex verses)
- The audio files will be downloaded automatically, if this doesn't happen, a link will be provided for you for each line of the query made.
