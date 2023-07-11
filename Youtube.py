from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import subprocess
import sys
import pytube


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        text=self.lineEdit.text()
        if text=="":
            print("Enter Link")
        else:
            print(self.comboBox.currentText())
            video=pytube.YouTube(text)
            video.streams.first().download() #This controls the video quality of the stream
            video.streams.filter(progressive=True,file_extension='mp4')#Use this to further filter out the video
            video.streams.get_by_resolution(f"{self.comboBox.currentText()}").download()

    def video(self,selected):
        if selected:
            self.comboBox.clear()
            resolution=["Select Resolution","Highest","1080p","720p","480p","360p","240p","144p"]
            self.comboBox.addItems(resolution)

    def audio(self,selected):
        if selected:
            self.comboBox.clear()
            resolution=["Select Audio Quality","Highest","320Kpbs","240Kpbs","192Kpbs"]
            self.comboBox.addItems(resolution)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
