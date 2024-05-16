from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QMovie)
from PySide2.QtWidgets import *
from threading import Thread
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# importing Dialogs
from resultDialog import *
from attendanceDialog import *
from ui_remarkDialogUi import *
from ui_updateUi import *
# importing Getinfo
from getinfo import *

from settings import *
import json

class Ui_Main(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1998)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        
        app_icon = QIcon("Assests/sxcmt.png")
        MainWindow.setWindowIcon(app_icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:\"#626D78\";\n"
"}\n"
"#centralwidget{\n"
"		background-color:\"#626D78\";\n"
"}\n"
"#menuFrame{\n"
"	background-color:\"#626D78\";\n"
"}\n"
"#dashboardFrame{\n"
"	background-color:\"#ffffff\";\n"
"	border-top-left-radius:70px ;\n"
"	border-bottom-left-radius:70px ;\n"
"}\n"
"#dashboardMenuBtn , #addremarkMenuBtn , #logoutMenuBtn , #settingMenuBtn , #updateMenuBtn ,#exitMenuBtn{\n"
"	border-radius: 20px;\n"
"}\n"
"#dashboardMenuBtn {\n"
"	background-color:\"#ffffff\";\n"
"}\n"
"#addremarkMenuBtn , #logoutMenuBtn , #settingMenuBtn , #updateMenuBtn , #exitMenuBtn {\n"
"	color:\"#ffffff\"\n"
"}\n"
"#dashboardTopFrame{\n"
"	background-color:\"#F6F6F6\";\n"
"	border-top-left-radius:70px ;\n"
"}\n"
"\n"
"#dashboardDashBtn , #resultBtn , #attendanceBtn{\n"
"	border-top-left-radius:25px ;\n"
"	border-top-right-radius:25px ;\n"
"}\n"
"#dashboardDashBtn {\n"
"	background-color:\"#626D78\";\n"
"	color:\"#ffffff\"\n"
"}\n"
"#rollSearchTextEdit{\n"
"	background-color:\"transparent\";\n"
""
                        "	border: none;\n"
"}\n"
"#personalDetailHead, #feeDetailHead , #remarkDetailHead{\n"
"	background-color:\"#626D78\";\n"
"	border-top-right-radius:50px ;\n"
"	border-bottom-left-radius:50px ;\n"
"}\n"
"\n"
"#personalDetailHeadLabel , #feeDetailHeadLabel , #remarksDetailHeadLabel{\n"
"		color:\"#ffffff\";\n"
"}"
"#label{\n"
"		border-radius:\"100%\";\n"
"}")
        # MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 1980))
        self.leftmainFrame = QFrame(self.centralwidget)
        self.leftmainFrame.setObjectName(u"leftmainFrame")
        self.leftmainFrame.setGeometry(QRect(-10, -20, 350, 2001))
        self.leftmainFrame.setMaximumSize(QSize(350, 16777215))
        self.leftmainFrame.setStyleSheet(u"")
        self.leftmainFrame.setFrameShape(QFrame.StyledPanel)
        self.leftmainFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.leftmainFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 70, 160, 140))
        # self.label.setPixmap(QPixmap(u"Assests/Images/BCA2022001.jpeg"))
        self.label.setPixmap(QPixmap(u"Assests\\logo.png"))
        self.label.setScaledContents(True)
        self.line = QFrame(self.leftmainFrame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(70, 250, 231, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.menuFrame = QFrame(self.leftmainFrame)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setGeometry(QRect(50, 300, 261, 501))
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menuFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboardMenuBtn = QPushButton(self.menuFrame)
        self.dashboardMenuBtn.setObjectName(u"dashboardMenuBtn")
        self.dashboardMenuBtn.setMaximumSize(QSize(16777215, 65))
        font = QFont()
        font.setFamily(u"Catamaran")
        font.setPointSize(10)
        self.dashboardMenuBtn.setFont(font)
        self.dashboardMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.dashboardMenuBtn)

        self.updateMenuBtn = QPushButton(self.menuFrame)
        self.updateMenuBtn.setObjectName(u"updateMenuBtn")
        self.updateMenuBtn.setMinimumSize(QSize(80, 80))
        self.updateMenuBtn.setFont(font)
        self.updateMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"Assests/updatebtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateMenuBtn.setIcon(icon)
        self.updateMenuBtn.setIconSize(QSize(70, 70))

        self.verticalLayout.addWidget(self.updateMenuBtn)
        self.updateMenuBtn.clicked.connect(lambda:openUpdateDialog(self))

        self.settingMenuBtn = QPushButton(self.menuFrame)
        self.settingMenuBtn.setObjectName(u"settingMenuBtn")
        self.settingMenuBtn.setMaximumSize(QSize(300, 80))
        self.settingMenuBtn.setFont(font)
        self.settingMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"Assests/settingBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingMenuBtn.setIcon(icon1)
        self.settingMenuBtn.setIconSize(QSize(70, 70))
        self.settingMenuBtn.clicked.connect(lambda:showUpdateDialog(self))
        def showUpdateDialog(self):
            class LoginDialog(QDialog):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    self.setWindowTitle("Session Update")
                    app_icon = QIcon("Assests/sxcmt.png")
                    self.setWindowIcon(app_icon)

                    # Widgets
                    self.username_label = QLabel("Username:")
                    self.username_input = QLineEdit()

                    self.password_label = QLabel("Password:")
                    self.password_input = QLineEdit()
                    self.password_input.setEchoMode(QLineEdit.Password)

                    self.login_button = QPushButton("Update")
                    self.login_button.clicked.connect(lambda:login_clicked(self))

                    # Layout
                    layout = QVBoxLayout()
                    layout.addWidget(self.username_label)
                    layout.addWidget(self.username_input)
                    layout.addWidget(self.password_label)
                    layout.addWidget(self.password_input)
                    layout.addWidget(self.login_button)

                    self.setLayout(layout)

                    def login_clicked(self):
                        username = self.username_input.text()
                        password = self.password_input.text()
                        
                        uri = "mongodb+srv://sxcmt:sxcmt@sxcmt.uvrp8pj.mongodb.net/?retryWrites=true&w=majority&appName=SXCMT"

                        # Create a new client and connect to the server
                        client = MongoClient(uri, server_api=ServerApi('1'))

                        db = client["userdb"]

                        collection = db["update"]
                        user = collection.find_one({"username": username, "password": password})

                        # Add your login logic here, for example:
                        if user:
                            departmentChange(self)
                            QMessageBox.warning(None, "Authorized", "Update Successfull")
                        else:
                            QMessageBox.warning(None, "Unauthorized", "You are not Authorized for any Updation")

            login_dialog = LoginDialog()
            if login_dialog.exec_() == QDialog.Accepted:
                print("Dialog Accepted")
            else:
                print("Dialog Rejected")

        self.verticalLayout.addWidget(self.settingMenuBtn)

        self.addremarkMenuBtn = QPushButton(self.menuFrame)
        self.addremarkMenuBtn.setObjectName(u"addremarkMenuBtn")
        self.addremarkMenuBtn.setMinimumSize(QSize(80, 80))
        self.addremarkMenuBtn.setFont(font)
        self.addremarkMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Assests/addremarkBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addremarkMenuBtn.setIcon(icon2)
        self.addremarkMenuBtn.setIconSize(QSize(70, 70))
        self.addremarkMenuBtn.clicked.connect(lambda:openRemarkDialog(self))

        self.verticalLayout.addWidget(self.addremarkMenuBtn)

        # self.logoutMenuBtn = QPushButton(self.menuFrame)
        # self.logoutMenuBtn.setObjectName(u"logoutMenuBtn")
        # self.logoutMenuBtn.setMinimumSize(QSize(0, 65))
        # self.logoutMenuBtn.setFont(font)
        # self.logoutMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        # icon3 = QIcon()
        # icon3.addFile(u"Assests/logoutBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        # self.logoutMenuBtn.setIcon(icon3)
        # self.logoutMenuBtn.setIconSize(QSize(40, 16))

        # self.verticalLayout.addWidget(self.logoutMenuBtn)

        # self.exitMenuBtn = QPushButton(self.leftmainFrame)
        # self.exitMenuBtn.setObjectName(u"exitMenuBtn")
        # self.exitMenuBtn.setGeometry(QRect(140, 1000, 75, 23))
        # self.exitMenuBtn.setMaximumSize(QSize(16777215, 50))
        # font1 = QFont()
        # font1.setFamily(u"Catamaran")
        # font1.setPointSize(10)
        # self.exitMenuBtn.setFont(font1)
        self.dashboardFrame = QFrame(self.centralwidget)
        self.dashboardFrame.setObjectName(u"dashboardFrame")
        self.dashboardFrame.setGeometry(QRect(339, 0, 1931, 1051))
        self.dashboardFrame.setMinimumSize(QSize(0, 800))
        self.dashboardFrame.setMaximumSize(QSize(16777215, 1920))
        self.dashboardFrame.setFrameShape(QFrame.StyledPanel)
        self.dashboardFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dashboardFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dashboardTopFrame = QFrame(self.dashboardFrame)
        self.dashboardTopFrame.setObjectName(u"dashboardTopFrame")
        self.dashboardTopFrame.setMaximumSize(QSize(16777215, 80))
        self.dashboardTopFrame.setFrameShape(QFrame.StyledPanel)
        self.dashboardTopFrame.setFrameShadow(QFrame.Raised)
        self.dashboardDashBtn = QPushButton(self.dashboardTopFrame)
        self.dashboardDashBtn.setObjectName(u"dashboardDashBtn")
        self.dashboardDashBtn.setGeometry(QRect(130, 30, 175, 50))
        self.dashboardDashBtn.setMinimumSize(QSize(175, 50))
        self.dashboardDashBtn.setMaximumSize(QSize(156, 40))
        self.dashboardDashBtn.setFont(font)
        self.dashboardDashBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.resultBtn = QPushButton(self.dashboardTopFrame)
        self.resultBtn.setObjectName(u"resultBtn")
        self.resultBtn.setGeometry(QRect(310, 30, 156, 50))
        self.resultBtn.setMinimumSize(QSize(156, 45))
        self.resultBtn.setFont(font)
        self.resultBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.resultBtn.clicked.connect(lambda:resultsection(self))



        self.loadgif = QLabel(self.dashboardTopFrame)
        self.loadgif.setObjectName(u"resultBtn")
        self.loadgif.setGeometry(QRect(700, 30, 40, 40))
        self.loadgif.setMinimumSize(QSize(40, 40))
        self.loadgif.setFont(font)
        self.loadgif.setScaledContents(True)
        # self.loadgif.setText("load")

        self.loading_movie = QMovie("Assests/loading.gif")
        self.loadgif.setMovie(self.loading_movie)

        self.loadgif.hide()
        



        self.pushButton = QPushButton(self.dashboardTopFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1260, -20, 100, 120))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"Assests/searchBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(140, 140))
        self.pushButton.clicked.connect(lambda:processing(self))
        self.rollSearchTextEdit = QLineEdit(self.dashboardTopFrame)
        self.rollSearchTextEdit.setObjectName(u"rollSearchTextEdit")
        self.rollSearchTextEdit.setGeometry(QRect(990, 23, 181, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.rollSearchTextEdit.setFont(font2)
        # self.rollSearchTextEdit.setTabChangesFocus(True)
        self.attendanceBtn = QPushButton(self.dashboardTopFrame)
        self.attendanceBtn.setObjectName(u"attendanceBtn")
        self.attendanceBtn.setGeometry(QRect(460, 30, 156, 50))
        self.attendanceBtn.setMinimumSize(QSize(156, 45))
        self.attendanceBtn.setFont(font)
        self.attendanceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.attendanceBtn.clicked.connect(lambda:openAttendanceDialog(self))

        self.verticalLayout_2.addWidget(self.dashboardTopFrame)

        self.dashboardFram = QFrame(self.dashboardFrame)
        self.dashboardFram.setObjectName(u"dashboardFram")
        self.dashboardFram.setFrameShape(QFrame.StyledPanel)
        self.dashboardFram.setFrameShadow(QFrame.Raised)
        self.personalDetailFrame = QFrame(self.dashboardFram)
        self.personalDetailFrame.setObjectName(u"personalDetailFrame")
        self.personalDetailFrame.setGeometry(QRect(140, 120, 700, 600))
        self.personalDetailFrame.setMinimumSize(QSize(700, 400))
        self.personalDetailFrame.setMaximumSize(QSize(16777215, 600))
        self.personalDetailFrame.setFrameShape(QFrame.StyledPanel)
        self.personalDetailFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.personalDetailFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.personalDetailHead = QFrame(self.personalDetailFrame)
        self.personalDetailHead.setObjectName(u"personalDetailHead")
        self.personalDetailHead.setMinimumSize(QSize(400, 60))
        self.personalDetailHead.setMaximumSize(QSize(16777215, 60))
        self.personalDetailHead.setFrameShape(QFrame.StyledPanel)
        self.personalDetailHead.setFrameShadow(QFrame.Raised)
        self.personalDetailHeadLabel = QLabel(self.personalDetailHead)
        self.personalDetailHeadLabel.setObjectName(u"personalDetailHeadLabel")
        self.personalDetailHeadLabel.setGeometry(QRect(50, 20, 211, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.personalDetailHeadLabel.setFont(font3)

        self.verticalLayout_3.addWidget(self.personalDetailHead, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.personalDetailFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.nameLabelS1 = QLabel(self.frame_3)
        self.nameLabelS1.setObjectName(u"nameLabelS1")
        self.nameLabelS1.setGeometry(QRect(80, 30, 71, 16))
        font4 = QFont()
        font4.setFamily(u"Catamaran")
        font4.setPointSize(10)
        self.nameLabelS1.setFont(font4)
        self.fnameLabelS1 = QLabel(self.frame_3)
        self.fnameLabelS1.setObjectName(u"fnameLabelS1")
        self.fnameLabelS1.setGeometry(QRect(80, 130, 151, 21))
        self.fnameLabelS1.setFont(font4)
        self.mnameLabelS1 = QLabel(self.frame_3)
        self.mnameLabelS1.setObjectName(u"mnameLabelS1")
        self.mnameLabelS1.setGeometry(QRect(80, 180, 141, 21))
        self.mnameLabelS1.setFont(font4)
        self.contactLabelS1 = QLabel(self.frame_3)
        self.contactLabelS1.setObjectName(u"contactLabelS1")
        self.contactLabelS1.setGeometry(QRect(80, 230, 101, 21))
        self.contactLabelS1.setFont(font4)
        self.pcontactLabelS1 = QLabel(self.frame_3)
        self.pcontactLabelS1.setObjectName(u"pcontactLabelS1")
        self.pcontactLabelS1.setGeometry(QRect(80, 280, 181, 21))
        self.pcontactLabelS1.setFont(font4)
        self.rollLabelS1 = QLabel(self.frame_3)
        self.rollLabelS1.setObjectName(u"rollLabelS1")
        self.rollLabelS1.setGeometry(QRect(80, 80, 101, 21))
        self.rollLabelS1.setFont(font4)
        self.something1LabelS1 = QLabel(self.frame_3)
        self.something1LabelS1.setObjectName(u"something1LabelS1")
        self.something1LabelS1.setGeometry(QRect(80, 330, 121, 21))
        self.something1LabelS1.setFont(font4)
        self.colonLabelName = QLabel(self.frame_3)
        self.colonLabelName.setObjectName(u"colonLabelName")
        self.colonLabelName.setGeometry(QRect(290, 30, 71, 16))
        self.colonLabelName.setFont(font4)
        self.colonLabelRoll = QLabel(self.frame_3)
        self.colonLabelRoll.setObjectName(u"colonLabelRoll")
        self.colonLabelRoll.setGeometry(QRect(290, 80, 71, 16))
        self.colonLabelRoll.setFont(font4)
        self.colonLabelFname = QLabel(self.frame_3)
        self.colonLabelFname.setObjectName(u"colonLabelFname")
        self.colonLabelFname.setGeometry(QRect(290, 130, 71, 16))
        self.colonLabelFname.setFont(font4)
        self.colonLabelMname = QLabel(self.frame_3)
        self.colonLabelMname.setObjectName(u"colonLabelMname")
        self.colonLabelMname.setGeometry(QRect(290, 180, 71, 16))
        self.colonLabelMname.setFont(font4)
        self.colonLabelContact = QLabel(self.frame_3)
        self.colonLabelContact.setObjectName(u"colonLabelContact")
        self.colonLabelContact.setGeometry(QRect(290, 230, 71, 16))
        self.colonLabelContact.setFont(font4)
        self.colonLabelPcontact = QLabel(self.frame_3)
        self.colonLabelPcontact.setObjectName(u"colonLabelPcontact")
        self.colonLabelPcontact.setGeometry(QRect(290, 280, 71, 16))
        self.colonLabelPcontact.setFont(font4)
        self.colonLabelSomething1 = QLabel(self.frame_3)
        self.colonLabelSomething1.setObjectName(u"colonLabelSomething1")
        self.colonLabelSomething1.setGeometry(QRect(290, 330, 71, 16))
        self.colonLabelSomething1.setFont(font4)
        self.nameLabelEdit1 = QLabel(self.frame_3)
        self.nameLabelEdit1.setObjectName(u"nameLabelEdit1")
        self.nameLabelEdit1.setGeometry(QRect(350, 30, 321, 20))
        self.nameLabelEdit1.setFont(font4)
        self.rollLabelEdit1 = QLabel(self.frame_3)
        self.rollLabelEdit1.setObjectName(u"rollLabelEdit1")
        self.rollLabelEdit1.setGeometry(QRect(350, 80, 321, 16))
        self.rollLabelEdit1.setFont(font4)
        self.fnameLabelEdit1 = QLabel(self.frame_3)
        self.fnameLabelEdit1.setObjectName(u"fnameLabelEdit1")
        self.fnameLabelEdit1.setGeometry(QRect(350, 130, 321, 20))
        self.fnameLabelEdit1.setFont(font4)
        self.mnameLabelEdit1 = QLabel(self.frame_3)
        self.mnameLabelEdit1.setObjectName(u"mnameLabelEdit1")
        self.mnameLabelEdit1.setGeometry(QRect(350, 180, 331, 20))
        self.mnameLabelEdit1.setFont(font4)
        self.contactLabelEdit1 = QLabel(self.frame_3)
        self.contactLabelEdit1.setObjectName(u"contactLabelEdit1")
        self.contactLabelEdit1.setGeometry(QRect(350, 230, 321, 16))
        self.contactLabelEdit1.setFont(font4)
        self.pcontactLabelEdit1 = QLabel(self.frame_3)
        self.pcontactLabelEdit1.setObjectName(u"pcontactLabelEdit1")
        self.pcontactLabelEdit1.setGeometry(QRect(350, 280, 321, 16))
        self.pcontactLabelEdit1.setFont(font4)
        self.somethingLabelEdit1 = QLabel(self.frame_3)
        self.somethingLabelEdit1.setObjectName(u"somethingLabelEdit1")
        self.somethingLabelEdit1.setGeometry(QRect(350, 330, 321, 20))
        self.somethingLabelEdit1.setFont(font4)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame = QFrame(self.dashboardFram)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(960, 120, 500, 600))
        self.frame.setMinimumSize(QSize(500, 600))
        self.frame.setMaximumSize(QSize(16777215, 400))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.feeDetailHead = QFrame(self.frame)
        self.feeDetailHead.setObjectName(u"feeDetailHead")
        self.feeDetailHead.setMinimumSize(QSize(0, 60))
        self.feeDetailHead.setFrameShape(QFrame.StyledPanel)
        self.feeDetailHead.setFrameShadow(QFrame.Raised)
        self.feeDetailHeadLabel = QLabel(self.feeDetailHead)
        self.feeDetailHeadLabel.setObjectName(u"feeDetailHeadLabel")
        self.feeDetailHeadLabel.setGeometry(QRect(50, 20, 211, 21))
        self.feeDetailHeadLabel.setFont(font3)

        self.verticalLayout_5.addWidget(self.feeDetailHead, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 500))
        self.frame_4.setMaximumSize(QSize(16777215, 600))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.fee1stYearLabels1 = QLabel(self.frame_4)
        self.fee1stYearLabels1.setObjectName(u"fee1stYearLabels1")
        self.fee1stYearLabels1.setGeometry(QRect(80, 50, 81, 16))
        self.fee1stYearLabels1.setFont(font4)
        self.fee2ndYearLabels1_2 = QLabel(self.frame_4)
        self.fee2ndYearLabels1_2.setObjectName(u"fee2ndYearLabels1_2")
        self.fee2ndYearLabels1_2.setGeometry(QRect(90, 140, 81, 16))
        self.fee2ndYearLabels1_2.setFont(font4)
        self.fee3rdYearLabels1 = QLabel(self.frame_4)
        self.fee3rdYearLabels1.setObjectName(u"fee3rdYearLabels1")
        self.fee3rdYearLabels1.setGeometry(QRect(90, 240, 81, 16))
        self.fee3rdYearLabels1.setFont(font4)
        self.feeOtp1yrCbx = QCheckBox(self.frame_4)
        self.feeOtp1yrCbx.setObjectName(u"feeOtp1yrCbx")
        self.feeOtp1yrCbx.setGeometry(QRect(140, 80, 67, 18))
        font5 = QFont()
        font5.setFamily(u"Catamaran")
        font5.setPointSize(8)
        self.feeOtp1yrCbx.setFont(font5)
        self.fee1st1yrCbx = QCheckBox(self.frame_4)
        self.fee1st1yrCbx.setObjectName(u"fee1st1yrCbx")
        self.fee1st1yrCbx.setGeometry(QRect(230, 80, 67, 18))
        self.fee1st1yrCbx.setFont(font5)
        self.fee2nd1yrCbx = QCheckBox(self.frame_4)
        self.fee2nd1yrCbx.setObjectName(u"fee2nd1yrCbx")
        self.fee2nd1yrCbx.setGeometry(QRect(320, 80, 67, 18))
        self.fee2nd1yrCbx.setFont(font5)
        self.feeOtp2yrCbx = QCheckBox(self.frame_4)
        self.feeOtp2yrCbx.setObjectName(u"feeOtp2yrCbx")
        self.feeOtp2yrCbx.setGeometry(QRect(140, 180, 67, 18))
        self.feeOtp2yrCbx.setFont(font5)
        self.fee1st2yrCbx = QCheckBox(self.frame_4)
        self.fee1st2yrCbx.setObjectName(u"fee1st2yrCbx")
        self.fee1st2yrCbx.setGeometry(QRect(230, 180, 67, 18))
        self.fee1st2yrCbx.setFont(font5)
        self.fee2nd2yrCbx = QCheckBox(self.frame_4)
        self.fee2nd2yrCbx.setObjectName(u"fee2nd2yrCbx")
        self.fee2nd2yrCbx.setGeometry(QRect(320, 180, 67, 18))
        self.fee2nd2yrCbx.setFont(font5)
        self.feeOtp3yrCbx = QCheckBox(self.frame_4)
        self.feeOtp3yrCbx.setObjectName(u"feeOtp3yrCbx")
        self.feeOtp3yrCbx.setGeometry(QRect(140, 290, 67, 18))
        self.feeOtp3yrCbx.setFont(font5)
        self.fee1st3yrCbx = QCheckBox(self.frame_4)
        self.fee1st3yrCbx.setObjectName(u"fee1st3yrCbx")
        self.fee1st3yrCbx.setGeometry(QRect(230, 290, 67, 18))
        self.fee1st3yrCbx.setFont(font5)
        self.fee2nd3yrCbx = QCheckBox(self.frame_4)
        self.fee2nd3yrCbx.setObjectName(u"fee2nd3yrCbx")
        self.fee2nd3yrCbx.setGeometry(QRect(320, 290, 67, 18))
        self.fee2nd3yrCbx.setFont(font5)

        self.verticalLayout_5.addWidget(self.frame_4)

        self.label_2 = QLabel(self.dashboardFram)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 620, 300, 300))
        self.label_2.setMinimumSize(QSize(300, 300))
        self.label_2.setPixmap(QPixmap(u"Assests/extraAsset1.png"))
        self.label_2.setScaledContents(True)
        self.frame_2 = QFrame(self.dashboardFram)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(960, 570, 500, 300))
        self.frame_2.setMinimumSize(QSize(0, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.remarkDetailHead = QFrame(self.frame_2)
        self.remarkDetailHead.setObjectName(u"remarkDetailHead")
        self.remarkDetailHead.setMinimumSize(QSize(0, 60))
        self.remarkDetailHead.setFrameShape(QFrame.StyledPanel)
        self.remarkDetailHead.setFrameShadow(QFrame.Raised)
        self.remarksDetailHeadLabel = QLabel(self.remarkDetailHead)
        self.remarksDetailHeadLabel.setObjectName(u"remarksDetailHeadLabel")
        self.remarksDetailHeadLabel.setGeometry(QRect(60, 20, 211, 21))
        self.remarksDetailHeadLabel.setFont(font3)

        self.verticalLayout_6.addWidget(self.remarkDetailHead, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        font6 = QFont()
        font6.setFamily(u"Montserrat Medium")
        self.frame_5.setFont(font6)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.remarkLabels1_1 = QLabel(self.frame_5)
        self.remarkLabels1_1.setObjectName(u"remarkLabels1_1")
        self.remarkLabels1_1.setGeometry(QRect(50, 30, 121, 21))
        self.remarkLabels1_1.setFont(font4)
        self.remarkLabels1_2 = QLabel(self.frame_5)
        self.remarkLabels1_2.setObjectName(u"remarkLabels1_2")
        self.remarkLabels1_2.setGeometry(QRect(50, 70, 121, 21))
        self.remarkLabels1_2.setFont(font4)
        self.remarkLabels1_3 = QLabel(self.frame_5)
        self.remarkLabels1_3.setObjectName(u"remarkLabels1_3")
        self.remarkLabels1_3.setGeometry(QRect(50, 110, 121, 21))
        self.remarkLabels1_3.setFont(font4)
        self.colonLabelRemark1 = QLabel(self.frame_5)
        self.colonLabelRemark1.setObjectName(u"colonLabelRemark1")
        self.colonLabelRemark1.setGeometry(QRect(160, 30, 71, 16))
        self.colonLabelRemark1.setFont(font4)
        self.colonLabelRemark2 = QLabel(self.frame_5)
        self.colonLabelRemark2.setObjectName(u"colonLabelRemark2")
        self.colonLabelRemark2.setGeometry(QRect(160, 70, 71, 16))
        self.colonLabelRemark2.setFont(font4)
        self.colonLabelRemark3 = QLabel(self.frame_5)
        self.colonLabelRemark3.setObjectName(u"colonLabelRemark3")
        self.colonLabelRemark3.setGeometry(QRect(160, 110, 71, 16))
        self.colonLabelRemark3.setFont(font4)
        self.remarkLabelEdit_1 = QLabel(self.frame_5)
        self.remarkLabelEdit_1.setObjectName(u"remarkLabelEdit_1")
        self.remarkLabelEdit_1.setGeometry(QRect(200, 30, 321, 16))
        self.remarkLabelEdit_1.setFont(font4)
        self.remarkLabelEdit_2 = QLabel(self.frame_5)
        self.remarkLabelEdit_2.setObjectName(u"remarkLabelEdit_2")
        self.remarkLabelEdit_2.setGeometry(QRect(200, 70, 321, 16))
        self.remarkLabelEdit_2.setFont(font4)
        self.remarkLabelEdit_3 = QLabel(self.frame_5)
        self.remarkLabelEdit_3.setObjectName(u"remarkLabelEdit_3")
        self.remarkLabelEdit_3.setGeometry(QRect(200, 110, 321, 16))
        self.remarkLabelEdit_3.setFont(font4)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.verticalLayout_2.addWidget(self.dashboardFram)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # QMetaObject.connectSlotsByName(MainWindow)


        #OPENING DIALOGS
        global marks, mark,att
        mark=["","","","","",""]
        marks=["","","","","",""]
        att=["","","","","",""]
        def resultsection(self):
            self.result_dialog = QDialog()
            self.ui2 =Ui_resultdialog()
            self.ui2.setupUi(self.result_dialog, marks ,mark )
            self.result_dialog.exec_()

        def openAttendanceDialog(self):
            self.result_dialog = QDialog()
            self.ui2 =Ui_attendancedialog()
            self.ui2.setupUi(self.result_dialog, att )
            self.result_dialog.exec_()

        def openRemarkDialog(self):
            self.result_dialog = QDialog()
            self.ui2 =Ui_remarkDialog()
            self.ui2.setupUi(self.result_dialog,self.rollSearchTextEdit.text())
            self.result_dialog.exec_()

        def openUpdateDialog(self):
            self.result_dialog = QDialog()
            self.ui2 =Ui_Update()
            self.ui2.setupUi(self.result_dialog)
            self.result_dialog.exec_()
    

        def departmentChange1():
            # with open('Assests/json/getInfoYear.json', 'r') as file:
            #     data = json.load(file)

            # for year_data in data['YearData']:
            #     for key in year_data:
            #         year_prefix = key[:-4] 
            #         year_data[key] = year_prefix + str(int(year_data[key][-4:]) + 1)

            # with open('Assests/json/getInfoYear.json', 'w') as file:
            #     json.dump(data, file, indent=4)


            source_spreadsheet_id = SAMPLE_SPREADSHEET_ID
            destination_spreadsheet_id = SAMPLE_SPREADSHEET_ID
            source_sheet_name = ["BCAII",'BCAI',"BBAII","BBAI","BCPII","BCPI","BBA(IB)II","BBA(IB)I","BA(JMC)II","BA(JMC)I"]
            destination_sheet_name =  ["BCAIII",'BCAII',"BBAIII","BBAII","BCPIII","BCPII","BBA(IB)III","BBA(IB)II","BA(JMC)III","BA(JMC)II"]
            for i in range(0,len(destination_sheet_name)):
                copy_sheet(source_spreadsheet_id, destination_spreadsheet_id, source_sheet_name[i], destination_sheet_name[i])
                if(i in [1,3,5,7,9,11]):
                    print("sdcs",source_sheet_name[i])
                    clear_request = sheet.values().clear(spreadsheetId=destination_spreadsheet_id, range=source_sheet_name[i]).execute()
                    range_to_update = source_sheet_name[i]+"!A1"
                    request_body = {
                        "values": [["Roll No","Name","Father's Name","Mother's Name","Contact No.","Parent's Contact No.","Address","Attendance_Sem1","Attendance_Sem2","Attendance_Sem3","Attendance_Sem4","Attendance_Sem5","Attendance_Sem6","feeYear1_Otp","feeYear1_1st_inst","feeYear1_2nd_inst","feeYear2_Otp","feeYear2_1st_inst","feeYear2_2nd_inst","feeYear3_Otp","feeYear3_1st_inst","feeYear3_2nd_inst","In_Result_Sem1","In_Result_Sem2","In_Result_Sem3","In_Result_Sem4","In_Result_Sem5","In_Result_Sem6","Ex_Result_Sem1","Ex_Result_Sem2","Ex_Result_Sem3","Ex_Result_Sem4","Ex_Result_Sem5","Ex_Result_Sem6","Remarks","Remarks","Remarks"]]
                    }
                    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                    range=range_to_update,
                                                    valueInputOption="USER_ENTERED",
                                                    body=request_body)
                    response = request.execute()
        def departmentChange(self):
            thread1 = Thread(target=departmentChange1)
            thread1.start()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SXCMT Student Mgmt. System", None))
        self.label.setText("")
        self.dashboardMenuBtn.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.updateMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Update Information", None))
        self.settingMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Session Update", None))
        self.addremarkMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Add Remarks", None))
        # self.logoutMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        # self.exitMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.dashboardDashBtn.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.resultBtn.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton.setText("")
        self.rollSearchTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Roll Search", None))
        self.attendanceBtn.setText(QCoreApplication.translate("MainWindow", u"Attendance", None))
        self.personalDetailHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Personal Information :", None))
        self.nameLabelS1.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.fnameLabelS1.setText(QCoreApplication.translate("MainWindow", u"Father's Name", None))
        self.mnameLabelS1.setText(QCoreApplication.translate("MainWindow", u"Mother's Name", None))
        self.contactLabelS1.setText(QCoreApplication.translate("MainWindow", u"Contact No.", None))
        self.pcontactLabelS1.setText(QCoreApplication.translate("MainWindow", u"Parent's Contact No.", None))
        self.rollLabelS1.setText(QCoreApplication.translate("MainWindow", u"Roll No.", None))
        self.something1LabelS1.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.colonLabelName.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelRoll.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelFname.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelMname.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelContact.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelPcontact.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelSomething1.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.nameLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.rollLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.fnameLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.mnameLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.contactLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.pcontactLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.somethingLabelEdit1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.feeDetailHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Fee Details :", None))
        self.fee1stYearLabels1.setText(QCoreApplication.translate("MainWindow", u"1st Year", None))
        self.fee2ndYearLabels1_2.setText(QCoreApplication.translate("MainWindow", u"2nd Year", None))
        self.fee3rdYearLabels1.setText(QCoreApplication.translate("MainWindow", u"3rd Year", None))
        self.feeOtp1yrCbx.setText(QCoreApplication.translate("MainWindow", u"OTP", None))
        self.fee1st1yrCbx.setText(QCoreApplication.translate("MainWindow", u"1st", None))
        self.fee2nd1yrCbx.setText(QCoreApplication.translate("MainWindow", u"2nd", None))
        self.feeOtp2yrCbx.setText(QCoreApplication.translate("MainWindow", u"OTP", None))
        self.fee1st2yrCbx.setText(QCoreApplication.translate("MainWindow", u"1st", None))
        self.fee2nd2yrCbx.setText(QCoreApplication.translate("MainWindow", u"2nd", None))
        self.feeOtp3yrCbx.setText(QCoreApplication.translate("MainWindow", u"OTP", None))
        self.fee1st3yrCbx.setText(QCoreApplication.translate("MainWindow", u"1st", None))
        self.fee2nd3yrCbx.setText(QCoreApplication.translate("MainWindow", u"2nd", None))
        self.label_2.setText("")
        self.remarksDetailHeadLabel.setText(QCoreApplication.translate("MainWindow", u"Remarks :", None))
        self.remarkLabels1_1.setText(QCoreApplication.translate("MainWindow", u"Remark 1 ", None))
        self.remarkLabels1_2.setText(QCoreApplication.translate("MainWindow", u"Remark 2", None))
        self.remarkLabels1_3.setText(QCoreApplication.translate("MainWindow", u"Remark 3", None))
        self.colonLabelRemark1.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelRemark2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.colonLabelRemark3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.remarkLabelEdit_1.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.remarkLabelEdit_2.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        self.remarkLabelEdit_3.setText(QCoreApplication.translate("MainWindow", u"..................................", None))
        
    
def refresh_gui(self):
    # Clear all UI elements or set them to default values
    self.remarkLabelEdit_1.clear()
    self.remarkLabelEdit_2.clear()
    self.remarkLabelEdit_3.clear()
    # Clear other UI elements similarly   
    
def processing(self):
    print("bye")
    self.loadgif.show()
    self.loading_movie.start()
    def read():
        print(self.rollSearchTextEdit.text().upper())
        print("hello")
        global dataList
        dataList=readdata(self.rollSearchTextEdit.text().upper())
        print(type(dataList))
        print(dataList)
        try:
            self.rollLabelEdit1.setText(dataList[0])
            self.nameLabelEdit1.setText(dataList[1])
            self.fnameLabelEdit1.setText(dataList[2])
            self.mnameLabelEdit1.setText(dataList[3])
            self.contactLabelEdit1.setText(dataList[4])
            self.pcontactLabelEdit1.setText(dataList[5])
            self.somethingLabelEdit1.setText(dataList[6])
            att[0]=dataList[7]
            att[1]=dataList[8]
            att[2]=dataList[9]
            att[3]=dataList[10]
            att[4]=dataList[11]
            att[5]=dataList[12]
            if(dataList[13]=="Paid"):
                self.feeOtp1yrCbx.setChecked(True)
            else:
                self.feeOtp1yrCbx.setChecked(False)
            if(dataList[14]=="Paid"):
                self.fee1st1yrCbx.setChecked(True)
            else:
                self.fee1st1yrCbx.setChecked(False)
            if(dataList[15]=="Paid"):
                self.fee2nd1yrCbx.setChecked(True)
            else:
                self.fee2nd1yrCbx.setChecked(False)
            if(dataList[16]=="Paid"):
                self.feeOtp2yrCbx.setChecked(True)
            else:
                self.feeOtp2yrCbx.setChecked(False)
            if(dataList[17]=="Paid"):
                self.fee1st2yrCbx.setChecked(True)
            else:
                self.fee1st2yrCbx.setChecked(False)
            if(dataList[18]=="Paid"):
                self.fee2nd2yrCbx.setChecked(True)
            else:
                self.fee2nd2yrCbx.setChecked(False)
            if(dataList[19]=="Paid"):
                self.feeOtp3yrCbx.setChecked(True)
            else:
                self.feeOtp3yrCbx.setChecked(False)
            if(dataList[20]=="Paid"):
                self.fee1st3yrCbx.setChecked(True)
            else:
                self.fee1st3yrCbx.setChecked(False)
            if(dataList[21]=="Paid"):
                self.fee2nd3yrCbx.setChecked(True)
            else:
                self.fee2nd3yrCbx.setChecked(False)
            marks[0]=dataList[22]
            marks[1]=dataList[23]
            marks[2]=dataList[24]
            marks[3]=dataList[25]   
            marks[4]=dataList[26]
            marks[5]=dataList[27]
            print(marks)
            mark[0]=dataList[28]
            mark[1]=dataList[29]
            mark[2]=dataList[30]
            mark[3]=dataList[31]
            mark[4]=dataList[32]
            mark[5]=dataList[33]
            print(mark)
            
            # if(dataList[36]==""):
            #     self.remarkLabelEdit_3.setText(".............")
            print("remark : " , dataList[36])
            self.remarkLabelEdit_1.setText(dataList[34])
            self.remarkLabelEdit_2.setText(dataList[35])
            self.remarkLabelEdit_3.setText(dataList[36])
            print("Kuch der")
        except:
            self.label.setPixmap(QPixmap(u"Assests\\logo.png"))
            print("pjotologo12")
            
            
            
        # print(mark)
        try:
            print("hello",retrieve_photo(dataList[0]+".jpeg"))
            if(retrieve_photo(dataList[0]+".jpeg")):
                print("Hello1"+"Assests/Images/"+dataList[0]+".jpeg")
                self.label.setPixmap(QPixmap("Assests/Images/"+dataList[0]+".jpeg"))
            else:
                print("No Photo")
                self.label.setPixmap(QPixmap(u"Assests\\logo.png"))
        except:
            self.label.setPixmap(QPixmap(u"Assests\\logo.png"))
            print("pjotologo")

        self.loading_movie.stop()
        self.loadgif.hide()
        # Execute the read function
    refresh_gui(self)
    read()

    # If dataList is empty, show a message box
    if not dataList:
        QMessageBox.warning(None, "No Data Found", "No data found for the Provided Roll Number")
    
    thread1 = Thread(target=read)
    thread1.start()
    print("after")
    