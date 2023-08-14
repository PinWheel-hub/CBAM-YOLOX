from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget

from GUI import Ui_MainWindow
from myVideoWidget import myVideoWidget
from predict import video_predict, set_if_stop
import runtrs
import sys, cv2, os


class myMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('识别视频')

        self.sld_video_pressed=False  #判断当前进度条识别否被鼠标点击
        self.videoFullScreen = False   # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()   # 创建一个全屏的widget
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的
        self.btn_open.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playVideo)       # play
        self.btn_stop.clicked.connect(self.pauseVideo)       # pause
        self.btn_return.clicked.connect(self.return2)
        self.btn_recognize.clicked.connect(self.recognize)
        self.btn_result.clicked.connect(self.play_result)

        #self.btn_cast.clicked.connect(self.castVideo)        # 视频截图
        self.player.positionChanged.connect(self.changeSlide)      # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  #双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)   #双击响应
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)   # 进度条拖拽跳转
        self.sld_video.ClickedValue.connect(self.clickedSlider)  # 进度条点击跳转
        self.sld_audio.valueChanged.connect(self.volumeChange)  # 控制声音播放
        self.player.setVolume(0)
        self.videopath = ""
        set_if_stop(False)
        #self.btn_cast.hide()

    def castVideo(self):
        screen = QGuiApplication.primaryScreen()
        cast_jpg = './'+QDateTime.currentDateTime().toString("yyyy-MM-dd hh-mm-ss-zzz")+'.jpg'
        screen.grabWindow(self.wgt_video.winId()).save(cast_jpg)

    def volumeChange(self, position):
        volume= round(position/self.sld_audio.maximum()*100)
        print("vlume %f" %volume)
        self.player.setVolume(volume)
        self.lab_audio.setText("音量:"+str(volume)+"%")

    def clickedSlider(self, position):
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            seconds = int((1 - position / self.vidoeLength) * self.player.duration() / 1000)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            self.lab_video.setText(str(h).rjust(2, '0') + ":" + str(m).rjust(2, '0') + ":" + str(s).rjust(2, '0'))
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            seconds = int((1 - position / self.vidoeLength) * self.player.duration() / 1000)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            self.lab_video.setText(str(h).rjust(2, '0') + ":" + str(m).rjust(2, '0') + ":" + str(s).rjust(2, '0'))

    def pressSlider(self):
        self.sld_video_pressed = True
        print("pressed")

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            #print(self.player.duration())
            self.vidoeLength = self.player.duration()+0.1
            self.sld_video.setValue(round((position/self.vidoeLength)*100))
            seconds = int((1-position/self.vidoeLength) * self.player.duration() / 1000)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            self.lab_video.setText(str(h).rjust(2, '0') + ":" + str(m).rjust(2, '0') + ":" + str(s).rjust(2, '0'))

    def openVideoFile(self):
        videofile = QFileDialog.getOpenFileUrl()[0]
        capture = cv2.VideoCapture(videofile.path()[1:])
        ref, frame = capture.read()
        if not ref:
            QMessageBox.critical(self, "错误", "视频格式错误")
        else:
            self.player.setMedia(QMediaContent())
            if (os.path.exists(self.videopath + ".mp4")):
                try:
                    os.remove(self.videopath + ".mp4")
                except:
                    pass
            self.videopath = videofile.path()[1:]
            print(self.videopath)
            self.player.setMedia(QMediaContent(videofile))  # 选取视频文件
            self.player.play()  # 播放视频
            self.player.pause()
            #print(self.player.availableMetaData())

    def playVideo(self):
        self.player.play()


    def pauseVideo(self):
        self.player.pause()

    def return2(self):
        set_if_stop(True)
        self.player.setMedia(QMediaContent())
        if (os.path.exists(self.videopath + ".mp4")):
            try:
                os.remove(self.videopath + ".mp4")
            except:
                pass
        self.close()
        self.window = runtrs.home_page()
        self.videoFullScreenWidget.hide()
        self.window.show()

    def videoDoubleClicked(self, text):

        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.setVideoOutput(self.wgt_video)
                self.videoFullScreenWidget.hide()
                self.videoFullScreen = False
            else:
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.videoFullScreenWidget.setFullScreen(1)
                self.videoFullScreen = True

    def recognize(self):
        capture = cv2.VideoCapture(self.videopath)
        ref, frame = capture.read()
        if not ref:
            QMessageBox.critical(self, "错误", "视频格式错误")
        else:
            video_predict(self.videopath)
            QMessageBox.information(self, "通知", "识别完成")

    def play_result(self):
        capture = cv2.VideoCapture(self.videopath + ".mp4")
        ref, frame = capture.read()
        if not ref:
            QMessageBox.critical(self, "错误", "请先完成识别")
        else:
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.videopath + ".mp4")))  # 选取视频文件
            self.player.play()  # 播放视频
            self.player.pause()
            QMessageBox.information(self, "通知", "识别结果加载成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())