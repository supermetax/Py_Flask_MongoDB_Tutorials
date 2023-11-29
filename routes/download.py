# routes/download.py
from flask import render_template, request, jsonify
from pytube import YouTube

def configure_download(app):
    @app.route('/download', methods=['GET', 'POST'])
    def download():
        video_info = None

        if request.method == 'POST':
            video_url = request.form['video_url']

            try:
                yt = YouTube(video_url)
                stream = yt.streams.get_highest_resolution()
                stream.download('downloads')

                # Store video information for displaying on the same page
                video_info = {'title': yt.title, 'author': yt.author, 'thumbnail': yt.thumbnail_url}
            except Exception as e:
                return f"Error downloading the video: {str(e)}"

        return render_template('download.html', video_info=video_info)
