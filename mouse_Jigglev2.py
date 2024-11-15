# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:20:23 2024
@author: EI10098
"""
import pyautogui
import time
import random
import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot, QThread

class JigglerThread(QThread):
    def __init__(self):
        super().__init__()
        self.running = False  # Flag to control the running state

    def run(self):
        self.running = True  # Set running flag to True when starting
        while self.running:
            x_offset = random.randint(-1, 1)
            y_offset = random.randint(-1, 1)
            pyautogui.move(x_offset, y_offset, duration=0.1)
            time.sleep(10)  # Wait for 10 seconds before moving again

    def stop(self):
        self.running = False  # Set running flag to False to stop the thread

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(100, 100)
        self.setWindowTitle('Mouse Jiggler version: 1.0')
        self.setWindowIcon(QIcon('cutemouse.jpg'))  
        
        label = QLabel(self)
        pixmap = QPixmap('cutemouse.jpg')  
        self.setCentralWidget(label)
        frame_pixmap = pixmap.scaled(500, 500, aspectRatioMode=1)
        label.setPixmap(frame_pixmap)

        # Set "turn on" button as an instance variable
        self.button_1 = QPushButton('On', self)
        self.button_1.setToolTip('Turn on mouse jiggler')
        self.button_1.move(135, 400)
        self.button_1.clicked.connect(self.start_mouse_jiggler)

        # Set "turn off" button as an instance variable
        self.button_2 = QPushButton('Off', self)
        self.button_2.setToolTip('Turn off mouse jiggler')
        self.button_2.move(266, 400)
        self.button_2.clicked.connect(self.stop_mouse_jiggler)

        # Initialize the jiggler thread
        self.jiggler_thread = JigglerThread()

    @pyqtSlot()
    def start_mouse_jiggler(self):
        if not self.jiggler_thread.isRunning():  # Start thread only if it's not already running
            print("Mouse jiggler started.")
            self.jiggler_thread.start()

    @pyqtSlot()
    def stop_mouse_jiggler(self):
        print("Mouse jiggler stopped.")
        self.jiggler_thread.stop()  # Stop the jiggler thread
        if self.jiggler_thread.isRunning():
            self.jiggler_thread.quit()  # Quit the thread after stopping

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    