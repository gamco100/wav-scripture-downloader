import datetime
import os
import shutil
from download_function import *
from flask import Flask, render_template, request


# ------------------------ SERVER ---------------------------------
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", year=datetime.datetime.now().year)


@app.route("/downloaded", methods=["POST"])
def clicked_on_download():

    folder_path = os.path.join(os.getcwd(), 'static', 'output')

    try:
        shutil.rmtree(folder_path)
        print(f"Folder {folder_path} deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")

    os.mkdir(folder_path)

    query_data = request.form.to_dict()
    list_query = query_data["query_to_download"].splitlines()
    list_query = [item.strip() for item in list_query]

    files_downloaded = download_query(list_query)

    return render_template("download_page.html", has_downloaded=True,
                           what_was_downloaded=files_downloaded, year=datetime.datetime.now().year)


if __name__ == "__main__":
    app.run(debug=True)
