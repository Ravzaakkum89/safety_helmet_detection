import cv2
from playsound import playsound
import srcScripts as srcScripts
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from detector import Detector
from projeUI import Ui_MainWindow
class YoloUIWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(YoloUIWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.videoStart_Button.clicked.connect(self.startVideo_Button)
        self.ui.detectionStart_Button.clicked.connect(self.startDetection_Button)
        self.ui.audibleAlert_Button.clicked.connect(self.audibleWarning_Status)

        self.cap_mainCamera = cv2.VideoCapture("video1.mp4")
        self.specialDetector = Detector(weightsFilename="best.pt")
        self.IsVideoStart = False
        self.IsDetectionStart = False
        self.IsAudibleWarning = True

    def audibleWarning_Status(self):
        if self.IsAudibleWarning:
            self.IsAudibleWarning = False
            self.ui.audibleAlert_Button.setText("Sesli Uyarıları Aç")

        else:
            self.IsAudibleWarning = True
            self.ui.audibleAlert_Button.setText("Sesli Uyarıları Kapat")

    """
        alert_Status = 0: No Alert
        alert_Status = 1: Alert
    """

    def alert_Changer(self, alert_Status):
        if alert_Status == False:
            self.ui.Alert_Text_Correct.setVisible(True)
            self.ui.Alert_Text_Danger.setVisible(False)
        else:
            if self.IsAudibleWarning:
                playsound("uyari.mp3")
            self.ui.Alert_Text_Correct.setVisible(False)
            self.ui.Alert_Text_Danger.setVisible(True)

    def startDetection_Button(self):
        if self.IsDetectionStart == False:
            self.IsDetectionStart = True
            self.ui.detectionStart_Button.setText("Tespit Etmeyi Durdur")

        else:
            self.IsDetectionStart = False
            self.ui.detectionStart_Button.setText("Tespit Etmeyi Başlat")

    def startVideo_Button(self):
        if self.IsVideoStart == False:
            self.IsVideoStart = True
            self.ui.videoStart_Button.setText("Videoyu Durdur")
            Thread(target=self.showStart, args=()).start()

        else:
            self.IsVideoStart = False
            self.ui.videoStart_Button.setText("Videoyu Başlat")

    def showStart(self):
        while True:
            ret, frame = self.cap_mainCamera.read()

            if self.IsDetectionStart:
                results = self.specialDetector.detect(frame)
                print(results)
                srcScripts.drawArea(frame, results)
                self.alert_Changer(srcScripts.alertController(results))
            else:
                self.alert_Changer(False)

            img = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.ui.CameraPlayer.setPixmap(QtGui.QPixmap.fromImage(img))
            cv2.waitKey(1)

            if self.IsVideoStart == False:
                break

        self.alert_Changer(False)


app = QApplication([])
window = YoloUIWindow()
window.show()
app.exec_()
