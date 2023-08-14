import sys, os

from PIL.ImageQt import ImageQt

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import trs, home
import py_player_demo

from predict import picture_predict, open_camera, set_if_stop
from PIL import Image

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

type45 = "i2,i4,i5,il100,il60,il80,io,ip,p10,p11,p12,p19,p23,p26,p27,p3,p5,p6,pg,ph4,ph4.5,ph5,pl100,pl120,pl20,pl30,pl40,pl5,pl50,pl60,pl70,pl80,pm20,pm30,pm55,pn,pne,po,pr40,w13,w32,w55,w57,w59,wo"
type45 = type45.split(',')

type45_chinese = "非机动车行驶,机动车行驶,靠右侧道路行驶,最低限速100km/h,最低限速60km/h,最低限速80km/h,其他指示标志,人行横道,禁止机动车驶入,禁止鸣喇叭,禁止摩托车驶入,禁止右转弯,禁止左转弯,禁止载货汽车驶入,禁止运输危险物品车辆驶入,禁止大型客车驶入,禁止掉头,禁止非机动车进入,减速让行,限高4m,限高4.5m,限高5m,限速100km/h,限速120km/h,限速20km/h,限速30km/h,限速40km/h,限速5km/h,限速50km/h,限速60km/h,限速70km/h,限速80km/h,限重20t,限重30t,限重55t,禁止停车,禁止驶入,其他禁令标志,解除限速40km/h,十字交叉路口,施工,注意儿童,注意行人,注意右方合流,其他警告标志"
type45_chinese = type45_chinese.split(',')

dict_chinese = dict(zip(type45, type45_chinese))

class home_page(QMainWindow):
    def __init__(self):
        super(home_page, self).__init__()
        ui = home.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(self)
        self.setWindowTitle('主界面')

        self.picture_btn = ui.pushButton
        self.picture_btn.clicked.connect(self.turn_to_picture)

        self.video_btn = ui.pushButton_2
        self.video_btn.clicked.connect(self.turn_to_video)

        self.exit_btn = ui.pushButton_4
        self.exit_btn.clicked.connect(self.exit_program)

        self.camera_btn = ui.pushButton_5
        self.camera_btn.clicked.connect(self.camera)

        self.camera_flag = False

    def turn_to_picture(self):
        self.close()
        self.window = traffic_sign()
        self.window.show()

    def turn_to_video(self):
        self.close()
        self.window = py_player_demo.myMainWindow()
        self.window.show()

    def camera(self):
        if(self.camera_flag):
            set_if_stop(True)
            self.camera_flag = False
        else:
            set_if_stop(False)
            self.camera_flag = True
            open_camera()

    def exit_program(self):
        set_if_stop(True)
        self.close()

class traffic_sign(QMainWindow):
    def __init__(self):
        super(traffic_sign, self).__init__()
        ui = trs.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(self)
        self.setWindowTitle('识别图片')

        self.path = ui.lineEdit

        self.choose_picture_btn = ui.pushButton
        self.choose_picture_btn.clicked.connect(self.choose_picture)

        self.open_picture_btn = ui.pushButton_2
        self.open_picture_btn.clicked.connect(self.open_picture)

        self.recognize_picture_btn = ui.pushButton_3
        self.recognize_picture_btn.clicked.connect(self.recognize_picture)

        self.return1_btn = ui.pushButton_4
        self.return1_btn.clicked.connect(self.return1)

        self.label1 = ui.label_2
        self.label1.mouseDoubleClickEvent = self.picture1_clicked
        self.picture1 = Image

        self.label2 = ui.label_3
        self.label2.mouseDoubleClickEvent = self.picture2_clicked
        self.picture2 = Image

        self.table = ui.tableWidget
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setHidden(True)
    def choose_picture(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "选择图片", "", "*.jpg;*.png;;All Files(*)")
        self.path.setText(imgName)

    def open_picture(self):
        imgName = self.path.text()
        try:
            image = Image.open(imgName)
        except:
            QMessageBox.critical(self, "错误", "图片格式错误")
        else:
            self.label2.clear()
            #jpg = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
            if(image.size[0] <= self.label1.width() and image.size[1] <= self.label1.height()):
                im = image.convert("RGB")
            elif(image.size[0] >= image.size[1]):
                im = image.resize(size=(self.label1.width(), int(image.size[1] * self.label1.height() / image.size[0]))).convert("RGB")
            else:
                im = image.resize(size=(int(image.size[0] * self.label1.width() / image.size[1]), self.label1.height())).convert("RGB")
            data = im.tobytes("raw", "RGB")
            qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(qim)
            self.label1.setPixmap(pix)
            self.table.clearContents()
            self.table.setRowCount(0)
            self.picture1 = image
            self.picture2 = Image

    def recognize_picture(self):
        imgName = self.path.text()
        try:
            image = Image.open(imgName)
        except:
            QMessageBox.critical(self, "错误", "图片格式错误")
        else:
            #jpg = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
            if (image.size[0] <= self.label1.width() and image.size[1] <= self.label1.height()):
                im = image.convert("RGB")
            elif (image.size[0] >= image.size[1]):
                im = image.resize(
                    size=(self.label1.width(), int(image.size[1] * self.label1.height() / image.size[0]))).convert(
                    "RGB")
            else:
                im = image.resize(
                    size=(int(image.size[0] * self.label1.width() / image.size[1]), self.label1.height())).convert(
                    "RGB")
            data = im.tobytes("raw", "RGB")
            qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
            pix1 = QtGui.QPixmap.fromImage(qim)
            self.label1.setPixmap(pix1)
            r_image, sign_list = picture_predict(imgName)
            for sign in sign_list:
                sign[2] = '(' + str(((int(sign[2]) + int(sign[4])) // 2)) + ',' + str(((int(sign[1]) + int(sign[3])) // 2)) + ')'
                sign[1] = dict_chinese[sign[0]]
                sign[3] = sign[5]
                del sign[-2: -1]
            #img.save(imgName + ".jpg")
            #jpg2 = QtGui.QPixmap(imgName + ".jpg").scaled(self.label2.width(), self.label2.height())
            if (r_image.size[0] <= self.label1.width() and r_image.size[1] <= self.label1.height()):
                im = r_image.convert("RGB")
            elif (r_image.size[0] >= r_image.size[1]):
                im = r_image.resize(
                    size=(self.label1.width(), int(r_image.size[1] * self.label1.height() / r_image.size[0]))).convert(
                    "RGB")
            else:
                im = r_image.resize(
                    size=(int(r_image.size[0] * self.label1.width() / r_image.size[1]), self.label1.height())).convert(
                    "RGB")
            data = im.tobytes("raw", "RGB")
            qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
            pix2 = QtGui.QPixmap.fromImage(qim)
            self.label2.setPixmap(pix2)
            #os.remove(imgName + ".jpg")
            self.table.clearContents()
            self.table.setRowCount(0)
            i = 0
            for sign in sign_list:
                self.table.insertRow(i)
                j = 0
                item = QTableWidgetItem(str(i+1))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.table.setItem(i, j, item)
                for s in sign:
                    j += 1
                    item = QTableWidgetItem(str(s))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.table.setItem(i, j, item)
                i += 1
            self.picture1 = image
            self.picture2 = r_image

    def picture1_clicked(self, test):
        if(self.picture1 != Image):
            self.picture1.show()

    def picture2_clicked(self, test):
        if (self.picture2 != Image):
            self.picture2.show()

    def return1(self):
        self.close()
        self.window = home_page()
        self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('img.ico'))
    my = home_page()
    my.show()
    sys.exit(app.exec_())