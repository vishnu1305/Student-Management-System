from PySide2.QtCharts import QtCharts
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *



class Ui_resultdialog(object):
    def setupUi(self, resultdialog, marks, mark):
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
        self.frame.setGeometry(QRect(70, 10, 600, 250))
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
        # self.label_15 = QLabel(self.frame)
        # self.label_15.setObjectName(u"label_15")
        # self.label_15.setGeometry(QRect(90, 10, 35, 35))
        # self.label_15.setMinimumSize(QSize(35, 35))
        # self.label_15.setMaximumSize(QSize(35, 35))/

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 491, 65))
        font = QFont()
        # font.setFamily(u"Times New Roman")
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
        self.labelSem1InternalEdit = QLabel(self.frame)
        self.labelSem1InternalEdit.setObjectName(u"labelSem1InternalEdit")
        self.labelSem1InternalEdit.setGeometry(QRect(160, 100, 30, 16))
        self.labelSem1InternalEdit.setStyleSheet(u"font: 10pt ; \n"
"")
        self.labelSem2InternalEdit = QLabel(self.frame)
        self.labelSem2InternalEdit.setObjectName(u"labelSem2InternalEdit")
        self.labelSem2InternalEdit.setGeometry(QRect(160, 150, 30, 16))
        self.labelSem2InternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem3InternalEdit = QLabel(self.frame)
        self.labelSem3InternalEdit.setObjectName(u"labelSem3InternalEdit")
        self.labelSem3InternalEdit.setGeometry(QRect(160, 200, 30, 16))
        self.labelSem3InternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem4InternalEdit = QLabel(self.frame)
        self.labelSem4InternalEdit.setObjectName(u"labelSem4InternalEdit")
        self.labelSem4InternalEdit.setGeometry(QRect(420, 200, 30, 16))
        self.labelSem4InternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem5InternalEdit = QLabel(self.frame)
        self.labelSem5InternalEdit.setObjectName(u"labelSem5InternalEdit")
        self.labelSem5InternalEdit.setGeometry(QRect(420, 100, 30, 16))
        self.labelSem5InternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.labelSem6InternalEdit = QLabel(self.frame)
        self.labelSem6InternalEdit.setObjectName(u"labelSem6InternalEdit")
        self.labelSem6InternalEdit.setGeometry(QRect(420, 150, 30, 16))
        self.labelSem6InternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.label.raise_()
        self.label_sem1_i.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_sem4_i.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        # self.label_15.raise_()
        self.labelSem1InternalEdit.raise_()
        self.labelSem2InternalEdit.raise_()
        self.labelSem3InternalEdit.raise_()
        self.labelSem4InternalEdit.raise_()
        self.labelSem5InternalEdit.raise_()
        self.labelSem6InternalEdit.raise_()
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(640, 10, 600, 250))
        self.frame_2.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 491, 65))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"background-color:#626D78; border-radius:10px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        # self.label_16 = QLabel(self.frame_2)
        # self.label_16.setObjectName(u"label_16")
        # self.label_16.setGeometry(QRect(50, 14, 35, 35))
        # self.label_16.setMinimumSize(QSize(35, 35))
        # self.label_16.setMaximumSize(QSize(35, 35))
        self.labelSem6ExternalEdit = QLabel(self.frame_2)
        self.labelSem6ExternalEdit.setObjectName(u"labelSem6ExternalEdit")
        self.labelSem6ExternalEdit.setGeometry(QRect(420, 200, 30, 16))
        self.labelSem6ExternalEdit.setStyleSheet(u"font: 10pt ; \n"
"")
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(300, 200, 111, 16))
        self.label_18.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.labelSem5ExternalEdit = QLabel(self.frame_2)
        self.labelSem5ExternalEdit.setObjectName(u"labelSem5ExternalEdit")
        self.labelSem5ExternalEdit.setGeometry(QRect(420, 150, 30, 16))
        self.labelSem5ExternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 200, 111, 21))
        self.label_20.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.labelSem3ExternalEdit = QLabel(self.frame_2)
        self.labelSem3ExternalEdit.setObjectName(u"labelSem3ExternalEdit")
        self.labelSem3ExternalEdit.setGeometry(QRect(160, 200, 30, 16))
        self.labelSem3ExternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 150, 111, 16))
        self.label_22.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"\n"
"")
        self.labelSem1ExternalEdit = QLabel(self.frame_2)
        self.labelSem1ExternalEdit.setObjectName(u"labelSem1ExternalEdit")
        self.labelSem1ExternalEdit.setGeometry(QRect(160, 100, 30, 16))
        #/
        self.labelSem1ExternalEdit.setStyleSheet(u"font: 10pt ; \n"
"")
        self.label_sem1_e = QLabel(self.frame_2)
        self.label_sem1_e.setObjectName(u"label_sem1_e")
        self.label_sem1_e.setGeometry(QRect(40, 100, 111, 16))
        self.label_sem1_e.setStyleSheet(u"font: 10pt ;color:#0b5884\n"
"")
        self.labelSem2ExternalEdit = QLabel(self.frame_2)
        self.labelSem2ExternalEdit.setObjectName(u"labelSem2ExternalEdit")
        self.labelSem2ExternalEdit.setGeometry(QRect(160, 150, 30, 16))
        self.labelSem2ExternalEdit.setStyleSheet(u"font: 10pt ;\n"
"")
        self.label_sem4_e = QLabel(self.frame_2)
        self.label_sem4_e.setObjectName(u"label_sem4_e")
        self.label_sem4_e.setGeometry(QRect(300, 100, 111, 16))
        self.label_sem4_e.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
        self.labelSem4ExternalEdit = QLabel(self.frame_2)
        self.labelSem4ExternalEdit.setObjectName(u"labelSem4ExternalEdit")
        self.labelSem4ExternalEdit.setGeometry(QRect(420, 100, 30, 16))
        self.labelSem4ExternalEdit.setStyleSheet(u"font: 10pt ; \n"
"")
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(300, 150, 111, 16))
        self.label_28.setStyleSheet(u"font: 10pt ; color:#0b5884\n"
"")
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
        self.values=[0,0,0,0,0,0]
        self.values1=[0,0,0,0,0,0]
        try:
                if(marks[0]!=""):
                        self.values1[0]=float(marks[0])
                if(marks[1]!=""):
                        self.values1[1]=float(marks[1])
                if(marks[2]!=""):
                        self.values1[2]=float(marks[2])
                if(marks[3]!=""):
                        self.values1[3]=float(marks[3])
                if(marks[4]!=""):
                        self.values1[4]=float(marks[4])
                if(marks[5]!=""):
                        self.values1[5]=float(marks[5])

                if(mark[0]!=""):
                        self.values[0]=float(mark[0])
                if(mark[1]!=""):
                        self.values[1]=float(mark[1])
                if(mark[2]!=""):
                        self.values[2]=float(mark[2])
                if(mark[3]!=""):
                        self.values[3]=float(mark[3])
                if(mark[4]!=""):
                        self.values[4]=float(mark[4])
                if(mark[5]!=""):
                        self.values[5]=float(mark[5])
                print("hii")

        except:
                if(marks[0]==""):
                        self.values1[0]="0"
                if(marks[1]==""):
                        self.values1[1]="0"
                if(marks[2]==""):
                        self.values1[2]="0"
                if(marks[3]==""):
                        self.values1[3]="0"
                if(marks[4]==""):
                        self.values1[4]="0"
                if(marks[5]==""):
                        self.values1[5]="0"

                if(mark[0]==""):
                        self.values[0]="0"
                if(mark[1]==""):
                        self.values[1]="0"
                if(mark[2]==""):
                        self.values[2]="0"
                if(mark[3]==""):
                        self.values[3]="0"
                if(mark[4]==""):
                        self.values[4]="0"
                if(mark[5]==""):
                        self.values[5]="0"

                print("hii2")

        print(self.values1)
        print(marks)
        print(mark)
        self.barset=QtCharts.QBarSet("Internal")
        self.barset1=QtCharts.QBarSet("External")
        for self.value in self.values:
            self.barset.append(self.value)
        for self.value1 in self.values1:
            self.barset1.append(self.value1)
            
        self.series=QtCharts.QBarSeries()
        self.series.append(self.barset)
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
        self.y_axis.setRange(0,10)
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.axisX().setTitleText('Semester')        
        self.chart.axisY().setTitleText('SCGPA')
        # self.chart.setTitle("Bar Chart")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart_view=QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.frame_3_layout.addWidget(self.chart_view)

        ##
        

        ##

        self.retranslateUi(resultdialog, marks,mark)

        QMetaObject.connectSlotsByName(resultdialog)
    # setupUi

    def retranslateUi(self, resultdialog, marks,mark):
        resultdialog.setWindowTitle(QCoreApplication.translate("resultdialog", u"Result", None))
        self.label_sem1_i.setText(QCoreApplication.translate("resultdialog", u"Semester1:", None))
        self.label_4.setText(QCoreApplication.translate("resultdialog", u"Semester2:", None))
        self.label_5.setText(QCoreApplication.translate("resultdialog", u"Semester3:", None))
        self.label_sem4_i.setText(QCoreApplication.translate("resultdialog", u"Semester4:", None))
        self.label_7.setText(QCoreApplication.translate("resultdialog", u"Semester5:", None))
        self.label_8.setText(QCoreApplication.translate("resultdialog", u"Semester6:", None))



        #1,2,3,4,5,6
        self.labelSem1InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[0], None))
        self.labelSem2InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[1], None))
        self.labelSem3InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[2], None))
        self.labelSem4InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[3], None))
        self.labelSem5InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[4], None))
        self.labelSem6InternalEdit.setText(QCoreApplication.translate("resultdialog", u""+mark[5], None))
        
        # self.label_15.setText(QCoreApplication.translate("resultdialog", u"<html><head/><body><p><img src=\"prof.png\" width=\"35\" height=\"35\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("resultdialog", u"<html><head/><body><p><span style=\" font-size:11pt;color:#ffffff\">  Internal Marks</span></p></body></html>", None))
        
        
        self.label_2.setText(QCoreApplication.translate("resultdialog", u"<html><head/><body><p><span style=\" font-size:11pt;color:#ffffff\">External Marks</span></p></body></html>", None))
        # self.label_16.setText(QCoreApplication.translate("resultdialog", u"<html><head/><body><p><img src=\"prof.png\" width=\"35\" height=\"35\"/></p></body></html>", None))
        
        self.label_sem1_e.setText(QCoreApplication.translate("resultdialog", u"Semester1:", None))
        self.label_22.setText(QCoreApplication.translate("resultdialog", u"Semester2:", None))
        self.label_20.setText(QCoreApplication.translate("resultdialog", u"Semester3:", None))
        self.label_sem4_e.setText(QCoreApplication.translate("resultdialog", u"Semester4:", None))
        self.label_28.setText(QCoreApplication.translate("resultdialog", u"Semester5:", None))
        self.label_18.setText(QCoreApplication.translate("resultdialog", u"Semester6:", None))
        #1,2,3,4,5,6
        self.labelSem1ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[0], None))
        self.labelSem2ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[1], None))
        self.labelSem3ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[2], None))
        self.labelSem4ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[3], None))
        self.labelSem5ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[4], None))
        self.labelSem6ExternalEdit.setText(QCoreApplication.translate("resultdialog", u""+marks[5], None))
        
        
        
        
        
        
