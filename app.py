import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from pytube import YouTube, Stream

# Create flask instance
app = Flask(__name__)
app.secret_key = "123456789"
# formats = []
vid = None

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/down', methods=["GET", "POST"])
def down():
    if request.method == "POST":
        url = request.form.get("url")
        fmt = request.form.get("format")
        vid = YouTube(url)
        session['data'] = url
        formats = []
        if fmt == "audio":
            formats = vid.streams.filter(only_audio=True)
        else:
            formats = vid.streams.filter(progressive=True)
        itags = {}
        for f in formats:
            stream_str = str(f)
            match = re.search(r'itag="(\d+)"', stream_str)
            if match:
                itag_val = match.group(1)
            else:
                print("No match found.")
            itags[itag_val] = stream_str
    return render_template('down.html', formats=formats, itags=itags, keys=itags.keys())

@app.route('/dd', methods=["GET", "POST"])
def dd():
    url = session.get('data')
    if request.method == "POST":
        vid = YouTube(url)
        itag = request.form.get("itag")
        str = vid.streams.get_by_itag(itag)
        str.download()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)