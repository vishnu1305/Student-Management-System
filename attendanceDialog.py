from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *



class Ui_attendancedialog(object):
    def setupUi(self, resultdialog, att):
        if resultdialog.objectName():
            resultdialog.setObjectName(u"resultdialog")
        resultdialog.resize(1200, 700)
        app_icon = QIcon("Assests/sxcmt.png")
        resultdialog.setWindowIcon(app_icon)
        resultdialog.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.centralwidget = QWidget(resultdialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(370, 10, 600, 250))
        self.frame.setStyleSheet(u"background-color:rgb(255, 255, 255);\nborder-radius:'10px';\n")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_sem1_i = QLabel(self.frame)
        self.label_sem1_i.setObjectName(u"label_sem1_i")
        self.label_sem1_i.setGeometry(QRect(40, 100, 111, 16))
        self.label_sem1_i.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 150, 111, 16))
        self.label_4.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 200, 111, 21))
        self.label_5.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.label_sem4_i = QLabel(self.frame)
        self.label_sem4_i.setObjectName(u"label_sem4_i")
        self.label_sem4_i.setGeometry(QRect(300, 100, 111, 16))
        self.label_sem4_i.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 150, 111, 16))
        self.label_7.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 200, 111, 16))
        self.label_8.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 491, 65))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(15)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"background-color:#626D78\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.labelSem1AttendanceEdit = QLabel(self.frame)
        self.labelSem1AttendanceEdit.setObjectName(u"labelSem1AttendanceEdit")
        self.labelSem1AttendanceEdit.setGeometry(QRect(160, 100, 50, 16))
        self.labelSem1AttendanceEdit.setStyleSheet(u"font: 10pt ; \n"
"")
        self.labelSem2AttendanceEdit = QLabel(self.frame)
        self.labelSem2AttendanceEdit.setObjectName(u"labelSem2AttendanceEdit")
        self.labelSem2AttendanceEdit.setGeometry(QRect(160, 150, 50, 16))
        self.labelSem2AttendanceEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem3AttendanceEdit = QLabel(self.frame)
        self.labelSem3AttendanceEdit.setObjectName(u"labelSem3AttendanceEdit")
        self.labelSem3AttendanceEdit.setGeometry(QRect(160, 200, 50, 16))
        self.labelSem3AttendanceEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem4AttendanceEdit = QLabel(self.frame)
        self.labelSem4AttendanceEdit.setObjectName(u"labelSem4AttendanceEdit")
        self.labelSem4AttendanceEdit.setGeometry(QRect(420, 200, 50, 16))
        self.labelSem4AttendanceEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem5AttendanceEdit = QLabel(self.frame)
        self.labelSem5AttendanceEdit.setObjectName(u"labelSem5AttendanceEdit")
        self.labelSem5AttendanceEdit.setGeometry(QRect(420, 100, 50, 16))
        self.labelSem5AttendanceEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem6AttendanceEdit = QLabel(self.frame)
        self.labelSem6AttendanceEdit.setObjectName(u"labelSem6AttendanceEdit")
        self.labelSem6AttendanceEdit.setGeometry(QRect(420, 150, 50, 16))
        self.labelSem6AttendanceEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.label.raise_()
        self.label_sem1_i.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_sem4_i.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        # self.label_15.raise_()
        self.labelSem1AttendanceEdit.raise_()
        self.labelSem2AttendanceEdit.raise_()
        self.labelSem3AttendanceEdit.raise_()
        self.labelSem4AttendanceEdit.raise_()
        self.labelSem5AttendanceEdit.raise_()
        self.labelSem6AttendanceEdit.raise_()
      
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 250, 1051, 500))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        # resultdialog.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(resultdialog)
        self.statusbar.setObjectName(u"statusbar")
        # resultdialog.setStatusBar(self.statusbar)
        
        self.frame_3_layout=QVBoxLayout()
        self.frame_3.setLayout(self.frame_3_layout)
        # Start of Barchart value
        # self.values=[5,10,8,6,7,7.5]
        self.values1=[0,0,0,0,0,0]
        try:
                if(att[0]!=""):
                        self.values1[0]=float(att[0])
                if(att[1]!=""):
                        self.values1[1]=float(att[1])
                if(att[2]!=""):
                        self.values1[2]=float(att[2])
                if(att[3]!=""):
                        self.values1[3]=float(att[3])
                if(att[4]!=""):
                        self.values1[4]=float(att[4])
                if(att[5]!=""):
                        self.values1[5]=float(att[5])

        except:
                if(att[0]==""):
                        self.values1[0]="Na"
                if(att[1]==""):
                        self.values1[1]="Na"
                if(att[2]==""):
                        self.values1[2]="Na"
                if(att[3]==""):
                        self.values1[3]="Na"
                if(att[4]==""):
                        self.values1[4]="Na"
                if(att[5]==""):
                        self.values1[5]="Na"

        print(self.values1)
        # self.barset=QtCharts.QBarSet("Attendance")
        self.barset1=QtCharts.QBarSet("Attendance")
        # for self.value in self.values:
        #     self.barset.append(self.value)
        for self.value1 in self.values1:
            self.barset1.append(self.value1)
            
        self.series=QtCharts.QBarSeries()
        # self.series.append(self.barset)
        self.series.append(self.barset1)
        self.chart=QtCharts.QChart()
        self.chart.addSeries(self.series)
        # abc
        self.categories=['SemesterI','SemesterII','SemesterIII','SemesterIV','SemesterV','SemesterVI']
        self.x_axis=QtCharts.QBarCategoryAxis()
        self.x_axis.append(self.categories)
        self.chart.setAxisX(self.x_axis,self.series)
        
        self.y_axis=QtCharts.QValueAxis()
        self.chart.setAxisY(self.y_axis,self.series)
        self.y_axis.setRange(0,100)
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.axisX().setTitleText('Semester')        
        self.chart.axisY().setTitleText('Percentage (%)')
        # self.chart.setTitle("Bar Chart")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart_view=QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.frame_3_layout.addWidget(self.chart_view)

        ##
        

        ##

        self.retranslateUi(resultdialog, att)

        QMetaObject.connectSlotsByName(resultdialog)
    # setupUi

    def retranslateUi(self, resultdialog, att):
        resultdialog.setWindowTitle(QCoreApplication.translate("resultdialog", u"Attendance", None))
        self.label_sem1_i.setText(QCoreApplication.translate("resultdialog", u"Semester1:", None))
        self.label_4.setText(QCoreApplication.translate("resultdialog", u"Semester2:", None))
        self.label_5.setText(QCoreApplication.translate("resultdialog", u"Semester3:", None))
        self.label_sem4_i.setText(QCoreApplication.translate("resultdialog", u"Semester4:", None))
        self.label_7.setText(QCoreApplication.translate("resultdialog", u"Semester5:", None))
        self.label_8.setText(QCoreApplication.translate("resultdialog", u"Semester6:", None))


        #1,2,3,4,5,6
        self.labelSem1AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[0]+"%", None))
        self.labelSem2AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[1]+"%", None))
        self.labelSem3AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[2]+"%", None))
        self.labelSem4AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[3]+"%", None))
        self.labelSem5AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[4]+"%", None))
        self.labelSem6AttendanceEdit.setText(QCoreApplication.translate("resultdialog", u""+att[5]+"%", None))
        
        self.label.setText(QCoreApplication.translate("resultdialog", u"<html><head/><body><p><span style=\" font-size:11pt;color:#ffffff\">  Attendance Information</span></p></body></html>", None))