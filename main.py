import sys
import uuid

import cv2
import numpy as np
import os
import time

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class Detect_fruits(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.appleLabel = QtWidgets.QLabel("Detect apples")
        self.appleButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.appleLabel.setFont(self.font)
        self.appleButton.setFont(self.font2)
        self.appleButton.setFixedSize(100, 50)
        self.peachLabel = QtWidgets.QLabel("Detect peachs")
        self.peachButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.peachLabel.setFont(self.font)
        self.peachButton.setFont(self.font2)
        self.peachButton.setFixedSize(100, 50)
        self.strawberryLabel = QtWidgets.QLabel("Detect strawberries")
        self.strawberryButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.strawberryLabel.setFont(self.font)
        self.strawberryButton.setFont(self.font2)
        self.strawberryButton.setFixedSize(100, 50)
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.orangeLabel = QtWidgets.QLabel("Detect oranges")
        self.orangeButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.orangeLabel.setFont(self.font)
        self.orangeButton.setFont(self.font2)
        self.orangeButton.setFixedSize(100, 50)
        self.bananaLabel = QtWidgets.QLabel("Detect banana")
        self.bananaButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.bananaLabel.setFont(self.font)
        self.bananaButton.setFont(self.font2)
        self.bananaButton.setFixedSize(100, 50)
        self.pearLabel = QtWidgets.QLabel("Detect pear")
        self.pearButton = QtWidgets.QPushButton("Detect")
        self.font = QtGui.QFont("Arial", 24)
        self.font2 = QtGui.QFont("Arial", 12)
        self.pearLabel.setFont(self.font)
        self.pearButton.setFont(self.font2)
        self.pearButton.setFixedSize(100, 50)
        self.writingArea = QtWidgets.QLabel()
        self.writingArea.setText("3 seconds after clicking the button, the camera will turn on and take a photo.")
        self.writingArea.setStyleSheet("font-size: 26px; color: red; font-weight: bold;")
        self.writingArea.setAlignment(QtCore.Qt.AlignCenter)

        self.h_box1 = QtWidgets.QHBoxLayout()
        self.h_box1.addWidget(self.appleLabel)
        self.h_box1.addWidget(self.appleButton)
        self.h_box2 = QtWidgets.QHBoxLayout()
        self.h_box2.addWidget(self.peachLabel)
        self.h_box2.addWidget(self.peachButton)
        self.h_box3 = QtWidgets.QHBoxLayout()
        self.h_box3.addWidget(self.strawberryLabel)
        self.h_box3.addWidget(self.strawberryButton)
        self.h_box4 = QtWidgets.QHBoxLayout()
        self.h_box4.addWidget(self.orangeLabel)
        self.h_box4.addWidget(self.orangeButton)
        self.h_box5 = QtWidgets.QHBoxLayout()
        self.h_box5.addWidget(self.bananaLabel)
        self.h_box5.addWidget(self.bananaButton)
        self.h_box6 = QtWidgets.QHBoxLayout()
        self.h_box6.addWidget(self.pearLabel)
        self.h_box6.addWidget(self.pearButton)

        apple_color = QtGui.QColor(255, 0, 0)
        peach_color = QtGui.QColor(255, 165, 0)
        strawberry_color = QtGui.QColor(255, 0, 255)
        orange_color = QtGui.QColor(255, 140, 0)
        banana_color = QtGui.QColor(255, 255, 0)
        pear_color = QtGui.QColor(0, 128, 0)


        self.appleLabel.setStyleSheet(f"background-color: {apple_color.name()};")
        self.appleButton.setStyleSheet(f"color: {apple_color.name()};")
        self.peachLabel.setStyleSheet(f"background-color: {peach_color.name()};")
        self.peachButton.setStyleSheet(f"color: {peach_color.name()};")
        self.strawberryLabel.setStyleSheet(f"background-color: {strawberry_color.name()};")
        self.strawberryButton.setStyleSheet(f"color: {strawberry_color.name()};")
        self.orangeLabel.setStyleSheet(f"background-color: {orange_color.name()};")
        self.orangeButton.setStyleSheet(f"color: {orange_color.name()};")
        self.bananaLabel.setStyleSheet(f"background-color: {banana_color.name()};")
        self.bananaButton.setStyleSheet(f"color: {banana_color.name()};")
        self.pearLabel.setStyleSheet(f"background-color: {pear_color.name()};")
        self.pearButton.setStyleSheet(f"color: {pear_color.name()};")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(self.h_box1)
        v_box.addStretch()
        v_box.addLayout(self.h_box2)
        v_box.addStretch()
        v_box.addLayout(self.h_box3)
        v_box.addStretch()
        v_box.addLayout(self.h_box4)
        v_box.addStretch()
        v_box.addLayout(self.h_box5)
        v_box.addStretch()
        v_box.addLayout(self.h_box6)
        v_box.addStretch()
        v_box.addWidget(self.writingArea)
        v_box.addStretch()

        self.setLayout(v_box)

        self.appleButton.clicked.connect(lambda: self.Tespit_et("apple"))
        self.peachButton.clicked.connect(lambda: self.Tespit_et("peach"))
        self.strawberryButton.clicked.connect(lambda: self.Tespit_et("strawberry"))
        self.orangeButton.clicked.connect(lambda: self.Tespit_et("orange"))
        self.bananaButton.clicked.connect(lambda: self.Tespit_et("banana"))
        self.pearButton.clicked.connect(lambda: self.Tespit_et("pear"))


        width = 960
        height = 540
        appWidth = 700
        appHeight = 475
        self.setGeometry(width - appWidth, height - appHeight, appWidth * 2, appHeight * 2)

        self.setWindowTitle("Fruits Detection")

        self.show()


    def Tespit_et(self, fruit):

        self.writingArea.setStyleSheet("font-size: 26px; color: blue; font-weight: bold;")

        # Loading Photos
        cap = cv2.VideoCapture(0)

        time.sleep(3)

        ret, frame = cap.read()
        os.chdir("C:\\Users\\MAHMUT\\PycharmProjects\\MeyveDetection")
        imgname = os.path.join("images\\", "image_" + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)


        cap.release()
        cv2.destroyAllWindows()


        # Fotoğraflardaki istenen meyveyi tespi etme
        weight_file = ''

        file_list = os.listdir("C:\\Users\\MAHMUT\\PycharmProjects\\MeyveDetection\\weight_files")

        for file in file_list:
            name = file.split("_")[2]
            if fruit == name:
                weight_file = file

        os.chdir("C:\\Users\\MAHMUT\\PycharmProjects\\MeyveDetection")


        config_file = 'yolov3_custom.cfg'
        class_labels = 'coco.names'

        with open(class_labels, 'r') as f:
            classes = f.read().splitlines()


        net = cv2.dnn.readNetFromDarknet(config_file, os.path.join("C:\\Users\\MAHMUT\\PycharmProjects\\MeyveDetection\\weight_files", weight_file))


        os.chdir("C:\\Users\\MAHMUT\\PycharmProjects\\MeyveDetection\\images")
        files = os.listdir()
        for file in files:
            image = cv2.imread(file)
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

            # Object detection with the YOLOv3 model
            net.setInput(blob)
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
            outputs = net.forward(output_layers)
            i = 0

            # Drawing detected objects
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    if confidence > 0.5:
                        i += 1

            self.writingArea.setText("{} {}s detected.".format(i, fruit))

            os.remove(file)


app = QtWidgets.QApplication(sys.argv)
DetectFruits = Detect_fruits()
sys.exit(app.exec_())


