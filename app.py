from flask import Flask, render_template, request, redirect, url_for, flash
from downloader import download_media
from pytube import YouTube

# Create flask instance
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/down', methods=["GET", "POST"])
def down():
    if request.method == "POST":
        url = request.form.get("url")
        fmt = request.form.get("format")
        vid = YouTube(url)
        formats = []
        print(fmt)
        if fmt == "audio":
            formats = vid.streams.filter(only_audio=True)
        elif fmt == "video":
            formats = vid.streams.filter(progressive=True)
    return render_template('down.html', formats=formats)

if __name__ == "__main__":
    app.run(debug=True)