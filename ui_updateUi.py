from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from update import *
from phototMongo import *


# class Ui_Update(object):
#     def setupUi(self, MainWindow):
#         if MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(543, 349)
#         MainWindow.setStyleSheet(u"#MainWindow{\n"
# "	background-color:#ffffff;\n"
# "}\n"
# "#updateComboBox{\n"
# "	border : none;\n"
# "	border-bottom:1px solid #555555;\n"
# "}\n"
# "#updateBtn{\n"
# "	background-color:#626D78;\n"
# "	color:#ffffff;\n"
# "	border-radius:15px;\n"
# "}\n"
# "#uploadExcelBtn,#uploadExcelBtn_Profile{\n"
# "		border-radius:15px;\n"
# "		background-color:#ffffff;\n"
# "	   border:1px solid #555555;\n"
# "}")
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.updateComboBox = QComboBox(self.centralwidget)
#         self.updateComboBox.addItem("")
#         self.updateComboBox.addItem("")
#         self.updateComboBox.addItem("")
#         self.updateComboBox.addItem("")
#         self.updateComboBox.addItem("")
#         self.updateComboBox.setObjectName(u"updateComboBox")
#         self.updateComboBox.setGeometry(QRect(50, 140, 441, 51))
#         font = QFont()
#         font.setPointSize(8)
#         self.updateComboBox.setFont(font)
#         self.uploadExcelBtn = QPushButton(self.centralwidget)
#         self.uploadExcelBtn.setObjectName(u"uploadExcelBtn")
#         self.uploadExcelBtn.setGeometry(QRect(50, 60, 211, 51))
#         self.uploadExcelBtn.setFont(font)
#         self.uploadExcelBtn.clicked.connect(lambda:dialog(self,1))
#         self.updateBtn = QPushButton(self.centralwidget)
#         self.updateBtn.setObjectName(u"updateBtn")
#         self.updateBtn.setGeometry(QRect(170, 230, 201, 61))
#         self.updateBtn.clicked.connect(lambda:update_btn(self))
#         self.updateBtn.setFont(font)
#         self.uploadExcelBtn_Profile = QPushButton(self.centralwidget)
#         self.uploadExcelBtn_Profile.setObjectName(u"uploadExcelBtn_Profile")
#         self.uploadExcelBtn_Profile.setGeometry(QRect(280, 60, 211, 51))
#         self.uploadExcelBtn_Profile.setFont(font)
#         self.uploadExcelBtn_Profile.clicked.connect(lambda:dialog(self,0))

#         self.retranslateUi(MainWindow)

#         QMetaObject.connectSlotsByName(MainWindow)

#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Update Detais", None))
#         self.updateComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Student Details", None))
#         self.updateComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Fee Details", None))
#         self.updateComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Attendance Details", None))
#         self.updateComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Internal Marks", None))
#         self.updateComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"External Marks", None))

#         self.uploadExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Upload Excel", None))
#         self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#         self.uploadExcelBtn_Profile.setText(QCoreApplication.translate("MainWindow", u"Update Image", None))
#     # retranslateUi


# def dialog(self, a):
#     global excelFileName1
#     global ab
#     ab=a
#     if(ab==1):
#         excelFileName1 = ""
#         excelFileName1 = QFileDialog.getOpenFileName(None, 'Open file', 'c:/',"All Files (*)")
#         print(excelFileName1)
#     else:
#         folder_path = QFileDialog.getExistingDirectory(None, "Select Folder", "/path/to/default/directory")
#         if folder_path:
#             print("Selected folder:", folder_path)
#             excelFileName1 = folder_path


# def update_btn(self):
#     if(ab==1):
#         if(self.updateComboBox.currentText()=="Student Details"):
#             get_student_details(excelFileName1[0])
#         elif(self.updateComboBox.currentText()=="Fee Details"):
#             get_fees(excelFileName1[0])
#         elif(self.updateComboBox.currentText()=="Attendance Details"):
#             get_attendance(excelFileName1[0])
#         elif(self.updateComboBox.currentText()=="Internal Marks"):
#             get_internal_marks(excelFileName1[0])
#         elif(self.updateComboBox.currentText()== "External Marks"):
#             get_external_marks(excelFileName1[0])

#     else:
#         # print(excelFileName1[0])
#         upload_photos(excelFileName1)
#         print("hi")
    







class Ui_Update(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 349)
        app_icon = QIcon("Assests/sxcmt.png")
        MainWindow.setWindowIcon(app_icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:#ffffff;\n"
"}\n"
"#updateComboBox{\n"
"	border : none;\n"
"	border-bottom:1px solid #555555;\n"
"}\n"
"#newComboBox{\n"
"	border : none;\n"
"	border-bottom:1px solid #555555;\n"
"}\n"
"#updateBtn{\n"
"	background-color:#626D78;\n"
"	color:#ffffff;\n"
"	border-radius:15px;\n"
"}\n"
"#uploadExcelBtn,#uploadExcelBtn_Profile{\n"
"		border-radius:15px;\n"
"		background-color:#ffffff;\n"
"	   border:1px solid #555555;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.updateComboBox = QComboBox(self.centralwidget)
        self.updateComboBox.addItem("")
        self.updateComboBox.addItem("")
        self.updateComboBox.addItem("")
        self.updateComboBox.addItem("")
        self.updateComboBox.addItem("")
        self.updateComboBox.addItem("")
        self.updateComboBox.setObjectName(u"updateComboBox")
        self.updateComboBox.setGeometry(QRect(50, 140, 441, 51))
        font = QFont()
        font.setPointSize(8)
        self.updateComboBox.setFont(font)
        self.uploadExcelBtn = QPushButton(self.centralwidget)
        self.uploadExcelBtn.setObjectName(u"uploadExcelBtn")
        self.uploadExcelBtn.setGeometry(QRect(50, 60, 211, 51))
        self.uploadExcelBtn.setFont(font)
        self.uploadExcelBtn.clicked.connect(lambda: dialog(self, 1))
        self.updateBtn = QPushButton(self.centralwidget)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(170, 260, 201, 61))
        self.updateBtn.clicked.connect(lambda: update_btn(self))
        self.updateBtn.setFont(font)
        self.uploadExcelBtn_Profile = QPushButton(self.centralwidget)
        self.uploadExcelBtn_Profile.setObjectName(u"uploadExcelBtn_Profile")
        self.uploadExcelBtn_Profile.setGeometry(QRect(280, 60, 211, 51))
        self.uploadExcelBtn_Profile.setFont(font)
        self.uploadExcelBtn_Profile.clicked.connect(lambda: dialog(self, 0))
        

        # Add a new ComboBox
        self.newComboBox = QComboBox(self.centralwidget)
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.addItem("")
        self.newComboBox.setObjectName(u"newComboBox")
        self.newComboBox.setGeometry(QRect(50, 200, 200, 51))
        self.newComboBox.setFont(font)


        self.newComboBoxsem = QComboBox(self.centralwidget)
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.addItem("")
        self.newComboBoxsem.setObjectName(u"newComboBox")
        self.newComboBoxsem.setGeometry(QRect(290, 200, 200, 51))
        self.newComboBoxsem.setFont(font)



        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Update Details", None))
        self.updateComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Type Of Excel", None))
        self.updateComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Student Details", None))
        self.updateComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fee Details", None))
        self.updateComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Attendance Details", None))
        self.updateComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Internal Marks", None))
        self.updateComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"External Marks", None))

        self.uploadExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Upload Excel", None))
        self.updateBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.uploadExcelBtn_Profile.setText(QCoreApplication.translate("MainWindow", u"Update Image", None))
        # Set text for the new ComboBox
        self.newComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Department", None))
        self.newComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"BCAI", None))
        self.newComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"BCAII", None))
        self.newComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"BCAIII", None))
        self.newComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"BBAI", None))
        self.newComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"BBAI", None))
        self.newComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"BBAII", None))
        self.newComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"BBAIII", None))
        self.newComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"BBA(IB)I", None))
        self.newComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"BBA(IB)II", None))
        self.newComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"BBA(IB)III", None))
        self.newComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"BCPI", None))
        self.newComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"BCPII", None))
        self.newComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"BCPIII", None))
        self.newComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"BA(JMC)I", None))
        self.newComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"BA(JMC)II", None))
        self.newComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"BA(JMC)III", None))

        self.newComboBoxsem.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Semester", None))
        self.newComboBoxsem.setItemText(1, QCoreApplication.translate("MainWindow", u"I", None))
        self.newComboBoxsem.setItemText(2, QCoreApplication.translate("MainWindow", u"II", None))
        self.newComboBoxsem.setItemText(3, QCoreApplication.translate("MainWindow", u"III", None))
        self.newComboBoxsem.setItemText(4, QCoreApplication.translate("MainWindow", u"IV", None))
        self.newComboBoxsem.setItemText(5, QCoreApplication.translate("MainWindow", u"V", None))
        self.newComboBoxsem.setItemText(6, QCoreApplication.translate("MainWindow", u"VI", None))

        self.newComboBox.currentTextChanged.connect(lambda:setCombotext(self))
        self.newComboBoxsem.currentTextChanged.connect(lambda:setCombotext1(self))
    # retranslateUi


def dialog(self, a):
    global excelFileName1
    global ab

    ab = a
    if(ab == 1):
        excelFileName1 = ""
        excelFileName1 = QFileDialog.getOpenFileName(None, 'Open file', 'c:/', "All Files (*)")
        print(excelFileName1)
    else:
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder", "/path/to/default/directory")
        if folder_path:
            print("Selected folder:", folder_path)
            excelFileName1 = folder_path


def setCombotext(self):
    global newcombo
    newcombo = self.newComboBox.currentText()
    # print(newcombo)

def setCombotext1(self):
    global newcombosem
    newcombosem = self.newComboBoxsem.currentText()
    # print(newcombo)

def update_btn(self):
    if(ab == 1):
        if(self.updateComboBox.currentText() == "Student Details"):
            get_student_details(excelFileName1[0],newcombo)
        elif(self.updateComboBox.currentText() == "Fee Details"):
            get_fees(excelFileName1[0],newcombo)
        elif(self.updateComboBox.currentText() == "Attendance Details"):
            # print(newcombo)
            get_attendance(excelFileName1[0],newcombo,newcombosem)
        elif(self.updateComboBox.currentText() == "Internal Marks"):
            get_internal_marks(excelFileName1[0],newcombo,newcombosem)
        elif(self.updateComboBox.currentText() == "External Marks"):
            get_external_marks(excelFileName1[0],newcombo,newcombosem)

    else:
        # print(excelFileName1[0])
        upload_photos(excelFileName1)
        print("hi")
