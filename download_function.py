import dict_bible_books
from scripture_classes import Scripture, DownloadManager

# ------------------------ CONSTANTS ---------------------------------
ENDPOINT = "https://b.jw-cdn.org/apis/pub-media/GETPUBMEDIALINKS"
BIBLE_BOOKS_NUMBER = dict_bible_books.BIBLE_BOOKS_NUMBER_T

# ------------------------ MAIN ---------------------------------


def download_query(lines):

    scriptures = [line.strip().lower() for line in lines]

    print("All scriptures entered. Please wait while we process the downloads.")

    downloaded_files = []

    # Process each input line
    for address in scriptures:

        texto = Scripture(address=address)

        # Getting the json from the API
        try:
            params = {
                "booknum": BIBLE_BOOKS_NUMBER[f"{texto.bible_book}"],
                "output": "json",
                "pub": "nwt",
                "fileformat": "MP3",
                "alllangs": 0,
                "track": texto.chapter,
                "langwritten": "T",
                "txtCMSLang": "T",
            }

        except KeyError:
            continue

        downloader = DownloadManager(endpoint=ENDPOINT, parameters=params, scripture_object=texto)

        if downloader.json == 1:
            print("Couldn't connect to server. Please check to see if your computer is connected to the internet.")
            exit()
        elif downloader.json == 2:
            print(f"Error [{texto.address}]: Invalid scripture.")
            continue

        result = downloader.download_audio()

        if result == 0:
            print(f"{texto.address} (status): in")
            file_name = (f"{downloader.scripture_object.bible_book}_{downloader.scripture_object.chapter}."
                         f"{downloader.scripture_object.verses_string}.wav")
            downloaded_files.append(file_name)

        elif result == 1:
            print("Could open the buffer file on folder 'input'. Make sure the folder and the file within it exist.")
            exit()

        elif result == 2:
            print(f"{texto.address} (status): error; the audio for that scripture doesn't exist.")
            continue

    return downloaded_files
