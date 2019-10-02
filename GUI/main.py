import sys
import GUI_test_2
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt, QObject, QEvent
from PyQt5.QtGui import QPixmap, QImage, QFont
import cv2
import time
import detect
import Dialog

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    def setCapture(self, cap):
        self.cap = cap

    def run(self):

        while True:
            ret, frame = self.cap.read()
            detections = detect.getDetections(frame)

            for detection in detections:
                cv2.rectangle(frame, (detection[0], detection[1]), (detection[2], detection[3]), (0, 0, 255), 3)

            time.sleep(0.025)
            if ret:

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgbImage = cv2.resize(rgbImage, (640, 480 ), interpolation= cv2.INTER_AREA)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


def clickable(widget):
    class Filter(QObject):

        clicked = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True

            return False


    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def clicked():
    ui.person_colorbar_0.setStyleSheet('background-color: #55fc02')
    th.setCapture(cv2.VideoCapture('7.mp4'))

    w = QDialog()
    wi = Dialog.Ui_Form()
    wi.setupUi(w)
    w.setModal(False)
    w.show()


ui = GUI_test_2.Ui_MainWindow()
th = Thread()


if __name__ == '__main__':

    thumbnails =list()

    app = QApplication(sys.argv)
    main = QMainWindow()
    ui.setupUi(main)
    clickable(ui.mainCamera).connect(clicked)


    thumbnail_Layout = ui.gridLayout_3

    for idx in range(thumbnail_Layout.count()):
        
        thumbnail = thumbnail_Layout.itemAt(idx) # this returns a QFrame which  holds VBox--> [image Lable, color Lable]
        thumbnails.append(thumbnail)

    th.changePixmap.connect(ui.setImage)
    th.setCapture(cv2.VideoCapture(0))
    th.start()

    main.show()
    sys.exit(app.exec_())




