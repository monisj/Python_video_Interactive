import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from pytube import YouTube

class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'YouTube Downloader'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        url_label = QLabel('Enter the URL of the YouTube video:', self)
        url_label.move(20, 20)

        self.url_input = QLineEdit(self)
        self.url_input.move(20, 40)
        self.url_input.resize(360, 20)

        download_button = QPushButton('Download', self)
        download_button.move(20, 70)
        download_button.clicked.connect(self.download_video)

        self.download_message = QLabel('', self)
        self.download_message.move(20, 100)

        self.show()

    def download_video(self):
        # Get the URL of the YouTube video from the input field
        url = self.url_input.text()

        # Create a YouTube object and extract video streams
        video = YouTube(url)
        streams = video.streams

        # Select the highest resolution stream
        high_resolution_stream = streams.get_highest_resolution()

        # Download the video to the current working directory
        high_resolution_stream.download()

        # Display a message to confirm that the video has been downloaded
        self.download_message.setText('Video downloaded successfully!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    youtube_downloader = YouTubeDownloader()
    sys.exit(app.exec_())
