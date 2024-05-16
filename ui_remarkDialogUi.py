from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QMovie,
    QRadialGradient)
from PySide2.QtWidgets import *
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json



# json_data = '''
# {
#   "type": "service_account",
#   "project_id": "readwrite-382017",
#   "private_key_id": "0360781022506ddc6c0455c63288bca1bf97dbb2",
#   "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCguPAOjF7+YRfT\\n00z2R8YYaBVVmQnqAUcghvF6hUXA/Tt0XGhGUxRMQ62IQIskuBAJNEkteDFT1Tka\\nWJm55ZFqHmSJeI6Q/bUaU47lVfeBy/jT/k61o9qQvnLyuta+dhMX51shntfbqcrn\\nK+HXO9fzkgyGXgzsP35uSGxt3DOkRfls8TCgeqkHxHzhGw+HcXB78TqakdWpPTj2\\nla4K5vPceNXbXi87Taty8HgzyF+YEotWkxGwiGouG2JydFN9NT5ID5G1LFQR1rQU\\nFlYfftTZZ0/YxQpmF0NC+R6GYL/v+68zrR+sCQalP/+DhFt1kK5prnYOLe7VrKHW\\npLzMxeiJAgMBAAECggEAAqf6ETsywqGUQlHYowiwBVQPdTOQ3eWKZwuyKRAl946N\\niW9RmFk4iaNWVmZH9UQ7ilOv1NfGHevwmNAZyiTLfd+1muTwGzwAuhXQ5gShI2cP\\nzDz29Up99lfjIEJIr7kVpoR2yiZKsMkljtEX5POGJYmx7AuiHW8M1w1IUr9Cwt5Z\\nHTQ06EWjsKOUwiFq/ubvfD0BKWRoArAoj08VDEgkZ4go4xNc5IiPjxgBt7ddNFKc\\nJP+DBDiJke8ZA2xCaZXjs0j9X7Qna7wWgLE+mI3+bzhwAQyhcbWFVUaXwM+KCkAV\\nRcIj7eVCtIOjTiM/A2RGqzvoiINsc4RquC8vegisYQKBgQDSKMzpac4pnFEkTaYp\\ndJeuvMG0jJpMoAhUjjGP/cpJWWjzWdo5s111xZqw3DnCziHu+iFkKvQK87DthaAh\\nfZ0s6dQ6hc1LxRlaw/xH85XeKHR8U62Uci4EVrYT4Xp5gpJR1WBSY8lBvpXeqDSc\\n2SjseYaQlEmcfABPGlEsifZ7oQKBgQDDx5nLhp7MOvZI4TYj7+17SX0dqqDtg3Mf\\nh/MeuqhBqWAW437cCGLbTeOJ3F06QQERFLwgyR6hFjiucuUgJt5JwgyjeswsFHMt\\nPcapWy6czE3GvzEh/VtghpobwbZ+ZLRkKckA0TryRbKZjhs9sbKy/6HEEyx3cGys\\naSQyyqyD6QKBgQCqou4d5wa5ym4np9RufHhcLG6rBi6SYK3i2cFsRIhmne4VCLOj\\nffs4kMVVLLrJbU0oGHfcOPQFoG/bq0+lYbSorwLesZ1LFDHN/KtuUF0zEG3kNJ0P\\nltW+OBmGcuFan6XmQ/X9b4ANnY1aSADQCZKszs9vvLc4E4a8s4WNQEedgQKBgHFi\\n9IuPWADoVSM4a+a8WkoA8dlwrOtiKhak4gV2DWSZ9/DJqPs+UCK7JYD+g2/tnfSK\\nkbpbQMYC3KkMGe9ZE3ycSj2ULROKdHpLQPdsu75MBO+KY6ZP2dA5pJ9WvZ7OLDum\\nh6dVhlIyU5HjX5uHgvtwWfv5LtOt5QKlkjVodCmhAoGBAMu1moG4uANvjZUVs/6Z\\nCiCwecRlP9M0TofPn4ycLMumV091rZwqvL8/sMH1noKJ6N7yu6gxPZ/HZA5qW+VR\\nk9nbb4fi27wl4JkguVbhoWD6P8OvXAybh3VzDL+Oh929xo8DuryFerh72gAgYKWF\\nMtiZp3Ejwgw0scsgJDHswkyK\\n-----END PRIVATE KEY-----\\n",
#   "client_email": "sxcmt-879@readwrite-382017.iam.gserviceaccount.com",
#   "client_id": "104746371805781563913",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sxcmt-879%40readwrite-382017.iam.gserviceaccount.com"
# }
# '''

file_path = 'Assests/json/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
with open(file_path) as f:
    credentials_info = json.load(f)
# credentials_info = json.loads('Assests/json/keys.json')
creds = service_account.Credentials.from_service_account_info(credentials_info, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1cVvWPTNWRRmxcPkA872LdXikqQoMm5-93lq3MiqYygw'
service = build('sheets', 'v4', credentials=creds, static_discovery=False)
sheet = service.spreadsheets()


class Ui_remarkDialog(object):
    def setupUi(self, MainWindow,roll):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        app_icon = QIcon("Assests/sxcmt.png")
        MainWindow.setWindowIcon(app_icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:#ffffff\n"
"}\n"
"\n"
"#addRemarkMainFrame{\n"
"	background-color:#ffffff;\n"
"}\n"
"\n"
"#remarkUpdateBtn{\n"
"	background-color:#626D78;\n"
"	color:#ffffff;\n"
"	border-radius:14px;\n"
"}\n"
"\n"
"#remarkEdit , #remarkRollEdit{\n"
"	border:none;\n"
"	border-bottom: 1px solid #626D78;\n"
"	background-color:#ffffff;\n"
"}\n"
"#remarkEdit {\n"
"	border: 0.5px solid #666;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.addRemarkMainFrame = QFrame(self.centralwidget)
        self.addRemarkMainFrame.setObjectName(u"addRemarkMainFrame")
        self.addRemarkMainFrame.setGeometry(QRect(0, 0, 601, 391))
        self.addRemarkMainFrame.setFrameShape(QFrame.StyledPanel)
        self.addRemarkMainFrame.setFrameShadow(QFrame.Raised)
        self.remarkRollEdit = QLineEdit(self.addRemarkMainFrame)
        self.remarkRollEdit.setObjectName(u"remarkRollEdit")
        self.remarkRollEdit.setGeometry(QRect(50, 50, 501, 41))
        self.remarkRollEdit.setText(roll)
        font = QFont()
        font.setPointSize(10)
        self.remarkRollEdit.setFont(font)
        self.remarkEdit = QLineEdit(self.addRemarkMainFrame)
        self.remarkEdit.setObjectName(u"remarkEdit")
        self.remarkEdit.setGeometry(QRect(50, 120, 501, 151))
        self.remarkEdit.setFont(font)
        self.remarkUpdateBtn = QPushButton(self.addRemarkMainFrame)
        self.remarkUpdateBtn.setObjectName(u"remarkUpdateBtn")
        self.remarkUpdateBtn.setGeometry(QRect(190, 310, 231, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.remarkUpdateBtn.setFont(font1)
        self.remarkUpdateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.remarkUpdateBtn.clicked.connect(lambda:update_remark(self))

        self.loadgif = QLabel(self.addRemarkMainFrame)
        self.loadgif.setObjectName(u"resultBtn")
        self.loadgif.setGeometry(QRect(700, 30, 40, 40))
        self.loadgif.setMinimumSize(QSize(40, 40))
        self.loadgif.setFont(font)
        self.loadgif.setScaledContents(True)
        # self.loadgif.setText("load")

        self.loading_movie = QMovie("Assests/loading.gif")
        self.loadgif.setMovie(self.loading_movie)

        self.loadgif.hide()

        self.retranslateUi(MainWindow)

        # def update_remark(self):
        #     self.loadgif.show()
        #     self.loading_movie.start()
        #     sheet = service.spreadsheets()
        #     roll = self.remarkRollEdit.text().upper()
        #     # roll = "BCA2022001"
        #     print(roll)
        #     # if(roll[0:7]=="BCA2022"):
        #     #     sheettoaccess = "BCAI"
        #     # if(roll[0:7]=="BCA2021"):
        #     #     sheettoaccess = "BCAII"
        #     # if(roll[0:7]=="BCA2020"):
        #     #     sheettoaccess = "BCAIII"

        #     # if(roll[0:7]=="BBA2022"):
        #     #     sheettoaccess = "BBAI"
        #     # if(roll[0:7]=="BBA2021"):
        #     #     sheettoaccess = "BBAII"
        #     # if(roll[0:7]=="BBA2020"):
        #     #     sheettoaccess = "BBAIII"

        #     # if(roll[0:7]=="BCP2022"):
        #     #     sheettoaccess = "BCPI"
        #     # if(roll[0:7]=="BCP2021"):
        #     #     sheettoaccess = "BCPII"
        #     # if(roll[0:7]=="BCP2020"):
        #     #     sheettoaccess = "BCPIII"

        #     # if(roll[0:7]=="BBE2022"):
        #     #     sheettoaccess = "BBA(IB)I"
        #     # if(roll[0:7]=="BBE2021"):
        #     #     sheettoaccess = "BBA(IB)II"
        #     # if(roll[0:7]=="BBE2020"):
        #     #     sheettoaccess = "BBA(IB)III"

        #     # if(roll[0:7]=="BMC2022"):
        #     #     sheettoaccess = "BA(JMC)I"
        #     # if(roll[0:7]=="BMC2021"):
        #     #     sheettoaccess = "BA(JMC)II"
        #     # if(roll[0:7]=="BMC2020"):
        #     #     sheettoaccess = "BA(JMC)III"
            
        #     if(roll[0:3]=="BCA"):
        #         sheettoaccess = ["BCAI","BCAII","BCAIII"]
        #     if(roll[0:3]=="BBA"):
        #         sheettoaccess = ["BBAI","BBAII","BBAIII"]
        #     if(roll[0:3]=="BCP"):
        #         sheettoaccess = ["BCPI","BCPII","BCPIII"]

        #     if(roll[0:3]=="BMC"):
        #         sheettoaccess = ["BMCI","BMCII","BMCIII"]
        #     if(roll[0:3]=="BBE"):
        #         sheettoaccess = ["BBEI","BBEII","BBEIII"]
        #     for n in range(0,3):
        #         result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheettoaccess[n]+"!A1:A200").execute()
        #         values = result.get('values')
        #         values_length = len(values)
        #         for i in range(0,len(values)):
        #             if roll==values[i][0]:
        #                 break
        #         result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheettoaccess+"!AI"+str(i+1)+":AK"+str(i+1)).execute()
        #         values = result.get('values')
        #         print(values)
        #         if(values==None):
        #             range_to_update = sheettoaccess+"!AI"+str(i+1)  #need change
        #         elif(values[0][0]==""):
        #             range_to_update = sheettoaccess+"!AJ"+str(i+1)  #need change
        #         elif(len(values[0])==1):
        #             range_to_update = sheettoaccess+"!AJ"+str(i+1)  #need change
        #         else:
        #             range_to_update = sheettoaccess+"!AK"+str(i+1)  #need change
        #         request = sheet.values().update(
        #             spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #             range=range_to_update,  
        #             valueInputOption="USER_ENTERED",
        #             body={"values": [[self.remarkEdit.text().upper()]]}
        #             ).execute()
            
        #     self.loading_movie.stop()
        #     self.loadgif.hide()
        
        def update_remark(self):
            self.loadgif.show()
            self.loading_movie.start()
            sheet = service.spreadsheets()
            roll = self.remarkRollEdit.text().upper()
            
            if roll.startswith("BCA"):
                sheettoaccess = ["BCAI", "BCAII", "BCAIII"]
            elif roll.startswith("BBA"):
                sheettoaccess = ["BBAI", "BBAII", "BBAIII"]
            elif roll.startswith("BCP"):
                sheettoaccess = ["BCPI", "BCPII", "BCPIII"]
            elif roll.startswith("BMC"):
                sheettoaccess = ["BMCI", "BMCII", "BMCIII"]
            elif roll.startswith("BBE"):
                sheettoaccess = ["BBEI", "BBEII", "BBEIII"]
            
            
            for sheetname in sheettoaccess:
                result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{sheetname}!A1:A200").execute()
                values = result.get('values')
                
                if values:
                    for i, row in enumerate(values, start=1):
                        if roll == row[0]:
                            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{sheetname}!AI{i}:AK{i}").execute()
                            values = result.get('values')
                            
                            if values is None or values[0][0] == "":
                                field_to_update = "AI"
                            elif len(values[0]) == 1:
                                field_to_update = "AJ"
                            else:
                                field_to_update = "AK"
                            
                            range_to_update = f"{sheetname}!{field_to_update}{i}"
                            request = sheet.values().update(
                                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_to_update,
                                valueInputOption="USER_ENTERED",
                                body={"values": [[self.remarkEdit.text().upper()]]}
                            ).execute()
                            
                            break  # Exit the loop once the roll number is found and updated
            QMessageBox.warning(None, "Student's Remark Update", "Student's Remarks Update Successfully")       
            self.loading_movie.stop()
            self.loadgif.hide()

            


        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Remark", None))
        self.remarkRollEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Roll No.", None))
        self.remarkUpdateBtn.setText(QCoreApplication.translate("MainWindow", u"Add Remarks", None))

