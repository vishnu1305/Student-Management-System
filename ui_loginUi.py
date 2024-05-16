from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ui_mainUi import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        app_icon = QIcon("Assests/sxcmt.png")
        MainWindow.setWindowIcon(app_icon)
        MainWindow.setStyleSheet(u"#login_topFrame{\n"
"	background-color : \"#626D78\";\n"
"}\n"
"\n"
"#loginMainFrame{\n"
"		background-color : \"#ffffff\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginMainFrame = QFrame(self.centralwidget)
        self.loginMainFrame.setObjectName(u"loginMainFrame")
        self.loginMainFrame.setGeometry(QRect(0, 0, 501, 601))
        self.loginMainFrame.setStyleSheet(u"#passwordEdit , #loginEdit{\n"
"	border-radius : 10px;\n"
"	border-bottom:1px solid #555;\n"
"}\n"
"\n"
"#login_topFrame{\n"
"	border-radius : 50%;\n"
"}")
        self.loginMainFrame.setFrameShape(QFrame.StyledPanel)
        self.loginMainFrame.setFrameShadow(QFrame.Raised)
        self.login_topFrame = QFrame(self.loginMainFrame)
        self.login_topFrame.setObjectName(u"login_topFrame")
        self.login_topFrame.setGeometry(QRect(0, -40, 501, 191))
        self.login_topFrame.setFrameShape(QFrame.StyledPanel)
        self.login_topFrame.setFrameShadow(QFrame.Raised)
        self.logoLabel = QLabel(self.loginMainFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(180, 70, 150, 140))
        self.logoLabel.setPixmap(QPixmap(u"Assests/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.loginEdit = QTextEdit(self.loginMainFrame)
        self.loginEdit.setObjectName(u"loginEdit")
        self.loginEdit.setGeometry(QRect(100, 260, 311, 51))
        font = QFont()
        font.setPointSize(10)
        self.loginEdit.setFont(font)
        self.passwordEdit = QTextEdit(self.loginMainFrame)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setGeometry(QRect(100, 350, 311, 51))
        self.passwordEdit.setFont(font)
        self.loginBtn = QPushButton(self.loginMainFrame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(180, 462, 151, 61))
        font1 = QFont()
        font1.setFamily(u"Catamaran")
        font1.setPointSize(10)
        self.loginBtn.setFont(font1)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"#loginBtn{\n"
"	background-color:#626D78;\n"
"color:#ffffff;\n"
"border-radius:20px\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect login button to the login function
        self.loginBtn.clicked.connect(self.login)
        self.forgotPasswordBtn = QPushButton(self.loginMainFrame)
        self.forgotPasswordBtn.setObjectName(u"forgotPasswordBtn")
        self.forgotPasswordBtn.setGeometry(QRect(180, 540, 151, 31))
        font2 = QFont()
        font2.setFamily(u"Catamaran")
        font2.setPointSize(8)
        self.forgotPasswordBtn.setFont(font2)
        self.forgotPasswordBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotPasswordBtn.setStyleSheet(u"#forgotPasswordBtn{\n"
                                               "	color:#626D78;\n"
                                               "	text-decoration: underline;\n"
                                               "}")
        self.forgotPasswordBtn.setText(QCoreApplication.translate("MainWindow", u"Forgot Password?", None))

        # Connect "Forgot Password" button to the function
        self.forgotPasswordBtn.clicked.connect(self.forgot_password_dialog)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SXCMT Login", None))
        self.logoLabel.setText("")
        self.loginEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login Id", None))
        self.passwordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))

    def login(self):
        # Get the entered username and password
        username = self.loginEdit.toPlainText().strip()
        password = self.passwordEdit.toPlainText().strip()

        uri = "mongodb+srv://sxcmt:sxcmt@sxcmt.uvrp8pj.mongodb.net/?retryWrites=true&w=majority&appName=SXCMT"

        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))

        db = client["userdb"]

        collection = db["login"]
        user = collection.find_one({"username": username, "password": password})

        if user:
            self.result_dialog = QDialog()
            self.result_dialog.setWindowFlags(self.result_dialog.windowFlags() | Qt.WindowMinMaxButtonsHint)
            self.ui2 = Ui_Main()
            self.ui2.setupUi(self.result_dialog)
            self.result_dialog.show()  # Show the main window
            # app.exec_()  # Start the event loop
            self.MainWindow.close()  # Close the login window
        else:
            QMessageBox.warning(None, "Login Failed", "Invalid username or password")

                    
                
    def forgot_password_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Forgot Password")
        dialog.setFixedSize(300, 200)
        app_icon = QIcon("Assests/sxcmt.png")
        dialog.setWindowIcon(app_icon)

        layout = QVBoxLayout()

        label = QLabel("Enter your username:")
        layout.addWidget(label)

        username_edit = QLineEdit()
        layout.addWidget(username_edit)

        label_new_password = QLabel("Enter your new password:")
        layout.addWidget(label_new_password)

        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_edit)

        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: self.save_new_password(username_edit.text(), password_edit.text(), dialog))
        layout.addWidget(save_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def save_new_password(self, username, new_password, dialog):
        # Connect to MongoDB
        uri = "mongodb+srv://sxcmt:sxcmt@sxcmt.uvrp8pj.mongodb.net/?retryWrites=true&w=majority&appName=SXCMT"
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["userdb"]
        collection = db["login"]

        # Search for the user based on the username
        user = collection.find_one({"username": username})

        if user:
            # Update the password for the found user
            result = collection.update_one({"username": username}, {"$set": {"password": new_password}})

            if result.modified_count > 0:
                QMessageBox.information(None, "Password Changed", "Your password has been changed successfully.")
            else:
                QMessageBox.warning(None, "Password Change Failed", "Failed to change password. Please try again.")
        else:
            QMessageBox.warning(None, "User Not Found", "Username not found. Please enter a valid username.")

        dialog.accept()
        
        