from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel, QGridLayout, QWidget, QProgressBar
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import sys
import pytube
import os
res=[]
audio_res=[]
class Load_Window(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.setGeometry(0,0,500,200)
        self.setWindowTitle("Load Window")
        #self.setWindowFlag(Qt.FramelessWindowHint)
        title = QLabel("I am the Load window", self)
        self.pbar = QProgressBar(self)
        
        self.pbar.setGeometry(30, 40, 200, 25)

        self.label_1 = QLabel('no title bar', self)
  
        # moving position
        self.label_1.move(100, 100)
  
        # setting up border and background color
        self.label_1.setStyleSheet("background-color: lightgreen;border: 3px solid green")
        
        title.setAlignment(QtCore.Qt.AlignCenter)
        title.move(200,200)
        

    def progressUpdate(self):
        self.show()
        self.pbar.setValue(100)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowIcon(QtGui.QIcon('image.png'))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")

        

        
        self.gridLayout.addWidget(self.comboBox, 7, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)


        #Select Combination
        
        self.radioButton.toggled.connect(self.video)
        self.radioButton_2.toggled.connect(self.audio)
        
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap('image.png') #Adding image to label
        self.label.setPixmap(self.pixmap) #Set Image
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.pushButton.setText(_translate("MainWindow", "Download Content"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Youtube Video URL"))
        self.radioButton_2.setText(_translate("MainWindow", "MP3"))
        self.radioButton.setText(_translate("MainWindow", "Video"))
        #self.label.setText(_translate("MainWindow", "Link"))
        self.pushButton.clicked.connect(self.download)

    def download(self):
        if self.radioButton.isChecked():
                text=self.lineEdit.text()
                if text=="":
                    print("Enter Link")
                else:
                    #print(self.comboBox.currentText())
                    video=pytube.YouTube(text)
                    video.streams.filter(res=f"{self.comboBox.currentText()}").first().download(filename="video.mp4")
                    audio = video.streams.filter(only_audio=True)
                    audio[0].download(filename="audio.mp4")
                    # combine the video clip with the audio clip
                    video_clip = VideoFileClip("video.mp4")
                    audio_clip = AudioFileClip("audio.mp4")
                    final_clip = video_clip.set_audio(audio_clip)
                    final_clip.write_videofile(f"{video.title}" + ".mp4")
                    os.remove("video.mp4")
                    os.remove("audio.mp4")
        elif self.radioButton_2.isChecked():
            text=self.lineEdit.text()
            if text=="":
                print("Enter Link")
            else:
                print(self.comboBox.currentText())
                audio=pytube.YouTube(text)
                video=pytube.YouTube(text)
                audio = audio.streams.filter(only_audio=True,abr=f"{self.comboBox.currentText()}")
                audio[0].download(filename=f"{video.title}" + ".mp3")
                

    def video(self,selected):
        if selected:
            text=self.lineEdit.text()
            if text=="":
                pass
                res.clear()
                self.comboBox.clear()
            else:
                LoadWin = Load_Window()
                #LoadWin.show()
                LoadWin.progressUpdate()
                video=pytube.YouTube(text)
                for stream in video.streams:
                    if(stream.resolution in res):
                        pass
                    elif(stream.resolution == None):
                        pass
                    else:
                        res.append(stream.resolution)
                self.comboBox.clear()
                self.comboBox.addItems(res)  
                LoadWin.close()

    def audio(self,selected):
        if selected:
            text=self.lineEdit.text()
            if text=="":
                pass
                res.clear()
                self.comboBox.clear()
            else:
                yt = pytube.YouTube(text)
                best_audio_stream = yt.streams.filter(only_audio=True).all()
                
                for stream in best_audio_stream:
                    if(stream.abr in audio_res):
                        pass
                    elif(stream.abr== None):
                        pass
                    else:
                        audio_res.append(stream.abr)
                print(audio_res)    
                self.comboBox.clear()
                self.comboBox.addItems(audio_res)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
