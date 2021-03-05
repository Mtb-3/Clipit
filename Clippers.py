from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5 import QtGui, QtWidgets
from moviepy.editor import *
import os
import sys

# QMainWindow to customize your app
class DialogApp(QWidget):
    clips = []
    def __init__(self):
        super().__init__()

        #Window size
        self.resize(300,300)

        #Set title/icon
        self.setWindowIcon(QtGui.QIcon('film_reel.png'))
        title = "Clippers"
        self.setWindowTitle(title)

        #Folder select button
        self.button1 = QPushButton('Folder')
        self.button1.clicked.connect(self.get_folder)

        self.preview = QPushButton('Preview')
        self.preview.clicked.connect(self.handlePreview)
        
        #Export video button
        self.export_video = QPushButton('Export Video')
        self.export_video.clicked.connect(self.handleExport)
        
        #Window layout instance
        layout = QVBoxLayout()

        #Add widgets to layout
        layout.addWidget(self.button1)       
        layout.addWidget(self.preview)
        layout.addWidget(self.export_video)
        
        #Set layout on application window
        self.setLayout(layout)

    #Directory Dialog + append video files
    def get_folder(self):
        cliparray = []
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        
        for filename in os.listdir(dir_path):
            cliparray.append(VideoFileClip(dir_path + "/" + filename))
        self.clips = cliparray
        
    #Preview video 
    def handlePreview(self):
        final_clip = concatenate_videoclips(self.clips)
        final_clip.audio = final_clip.audio.set_fps(44100)
        final_clip.preview()
    
    #Export file     
    def handleExport(self):
        final_clip = concatenate_videoclips(self.clips)
        final_clip.audio = final_clip.audio.set_fps(44100)
        final_clip.write_videofile('clipout.mp4',threads=8, logger = None)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    demo = DialogApp()
    demo.show()
    sys.exit(app.exec_())
        

