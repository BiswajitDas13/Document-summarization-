import os
import io
import pandas as pd
from dotenv import load_dotenv
from flask import Flask, render_template, Response, redirect, url_for
from drive_service import get_files_from_folder, download_file
from parser import extract_text
from summarizer import summarize_text

load_dotenv()

app = Flask(__name__)

FOLDER_ID = os.getenv("GOOGLE_FOLDER_ID", "").strip()

# simple in-memory cache for one run (optional)
CACHE = []


def build_results():
    if not FOLDER_ID:
        raise ValueError("GOOGLE_FOLDER_ID is missing in .env")

    files = get_files_from_folder(FOLDER_ID)

    results = []
    for f in files:
        name = f["name"]
        file_id = f["id"]

        file_stream = download_file(file_id)
        text = extract_text(file_stream, name)

        if text.strip():
            summary = summarize_text(text)
            results.append({"file_name": name, "summary": summary})

    return results


@app.route("/")
def home():
    global CACHE
    try:
        if not CACHE:
            CACHE = build_results()
        return render_template("index.html", results=CACHE, error=None)
    except Exception as e:
        return render_template("index.html", results=[], error=str(e))


@app.route("/refresh")
def refresh():
    global CACHE
    CACHE = []
    return redirect(url_for("home"))


@app.route("/download")
def download_csv():
    global CACHE
    if not CACHE:
        CACHE = build_results()

    df = pd.DataFrame([{"File Name": x["file_name"], "Summary": x["summary"]} for x in CACHE])
    stream = io.StringIO()
    df.to_csv(stream, index=False)

    return Response(
        stream.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=summaries.csv"}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)