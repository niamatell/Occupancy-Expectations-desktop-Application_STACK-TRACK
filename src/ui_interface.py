# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.Widgets import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(919, 661)
        MainWindow.setStyleSheet(u"*{\n"
"     background-color: transparent;\n"
"}\n"
"\n"
"#homeBtn{\n"
"background-color: #1461A3;\n"
"      border-left: 3px solid #EBF1F6;\n"
"       font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_16 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.LoginPage.setStyleSheet(u"#footer_3{\n"
"     background-color: #0D406D;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"#mainBody{\n"
"	background-color: #FFFFFF;\n"
"}\n"
"#LoginPage{\n"
"background-color: #0F497B;\n"
"}\n"
"#loginBtn, #signupBtn{\n"
"     text-align: left;\n"
"     text-align: center;\n"
"	background-color: #0F497B;\n"
"	color: #ffffff;\n"
"}\n"
"QPushButton{\n"
"     padding: 5px 10px;\n"
"     border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"	     background-color: #1b1b27;\n"
"	     color:#FFFFFF;\n"
"        padding: 10px 10px;\n"
"         border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.LoginPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.LoginPage)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.logo = QWidget(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_24 = QVBoxLayout(self.logo)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.label_22 = QLabel(self.logo)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(273, 70))
        self.label_22.setMaximumSize(QSize(273, 70))
        self.label_22.setPixmap(QPixmap(u"../../Users/surfac/Downloads/stacktrack.png"))
        self.label_22.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.label_22)


        self.verticalLayout_5.addWidget(self.logo, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.body = QWidget(self.widget)
        self.body.setObjectName(u"body")
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBody = QWidget(self.body)
        self.mainBody.setObjectName(u"mainBody")
        self.mainBody.setMinimumSize(QSize(400, 550))
        self.mainBody.setMaximumSize(QSize(400, 500))
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.mainBody)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(400, 50))
        self.label_3.setMaximumSize(QSize(400, 150))
        self.label_3.setPixmap(QPixmap(u"../../Users/surfac/Downloads/pixlr-image-generator-279762b6-9f18-416c-974c-39e91337df78.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.loginForm = QWidget(self.mainBody)
        self.loginForm.setObjectName(u"loginForm")
        self.horizontalLayout_3 = QHBoxLayout(self.loginForm)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.loginForm)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.widget_4 = QWidget(self.loginPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 391, 351))
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.loginLabel = QLabel(self.widget_4)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(30, 0, 111, 50))
        self.loginLabel.setMinimumSize(QSize(0, 0))
        self.loginLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet(u"color: #265fa9;\n"
"padding-left: 15px;")
        self.loginLabel.setMargin(0)
        self.loginBtn = QPushButton(self.widget_4)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(120, 220, 140, 31))
        self.loginBtn.setMinimumSize(QSize(140, 0))
        self.loginBtn.setMaximumSize(QSize(140, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.loginBtn.setFont(font1)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"color:#FFFFFF;\n"
"")
        self.goToSigninBtn = QPushButton(self.widget_4)
        self.goToSigninBtn.setObjectName(u"goToSigninBtn")
        self.goToSigninBtn.setGeometry(QRect(140, 300, 100, 31))
        self.goToSigninBtn.setMinimumSize(QSize(100, 0))
        self.goToSigninBtn.setFont(font1)
        self.goToSigninBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToSigninBtn.setStyleSheet(u"*{\n"
"background-color: #EFBA2E;\n"
"border: 1px solid #265fa9;\n"
"}")
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(50, 260, 291, 20))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.label_14.setFont(font2)
        self.gridLayoutWidget = QWidget(self.widget_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 50, 381, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.passIcon = QLabel(self.gridLayoutWidget)
        self.passIcon.setObjectName(u"passIcon")
        self.passIcon.setMinimumSize(QSize(12, 12))
        self.passIcon.setMaximumSize(QSize(12, 12))
        self.passIcon.setPixmap(QPixmap(u"../../Eurogate/Qss/icons/Icons/font_awesome/solid/lock.png"))
        self.passIcon.setScaledContents(True)

        self.gridLayout.addWidget(self.passIcon, 2, 0, 1, 1)

        self.eyeBtn = QPushButton(self.gridLayoutWidget)
        self.eyeBtn.setObjectName(u"eyeBtn")
        self.eyeBtn.setMinimumSize(QSize(20, 20))
        self.eyeBtn.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eyeBtn.setIcon(icon)

        self.gridLayout.addWidget(self.eyeBtn, 2, 3, 1, 1)

        self.password = QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(12, 12))
        self.label_13.setMaximumSize(QSize(12, 12))
        self.label_13.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.username = QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.errorMessage = QLabel(self.widget_4)
        self.errorMessage.setObjectName(u"errorMessage")
        self.errorMessage.setGeometry(QRect(30, 190, 291, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Display"])
        font3.setPointSize(9)
        self.errorMessage.setFont(font3)
        self.errorMessage.setStyleSheet(u"color: #ff0000;")
        self.stackedWidget_2.addWidget(self.loginPage)
        self.signinPage = QWidget()
        self.signinPage.setObjectName(u"signinPage")
        self.widget_5 = QWidget(self.signinPage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(-1, -10, 401, 371))
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.loginLabel_2 = QLabel(self.widget_5)
        self.loginLabel_2.setObjectName(u"loginLabel_2")
        self.loginLabel_2.setGeometry(QRect(30, 10, 121, 50))
        self.loginLabel_2.setMinimumSize(QSize(0, 0))
        self.loginLabel_2.setMaximumSize(QSize(16777215, 50))
        self.loginLabel_2.setFont(font)
        self.loginLabel_2.setStyleSheet(u"color:#265fa9;\n"
"padding-left: 15px;")
        self.loginLabel_2.setMargin(0)
        self.goToLoginBtn = QPushButton(self.widget_5)
        self.goToLoginBtn.setObjectName(u"goToLoginBtn")
        self.goToLoginBtn.setGeometry(QRect(140, 340, 120, 31))
        self.goToLoginBtn.setMaximumSize(QSize(120, 16777215))
        self.goToLoginBtn.setFont(font1)
        self.goToLoginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToLoginBtn.setStyleSheet(u"*{\n"
"background-color: #EFBA2E;\n"
"border: 1px solid #265fa9;\n"
"}")
        self.signupBtn = QPushButton(self.widget_5)
        self.signupBtn.setObjectName(u"signupBtn")
        self.signupBtn.setGeometry(QRect(130, 300, 140, 31))
        self.signupBtn.setMinimumSize(QSize(140, 0))
        self.signupBtn.setMaximumSize(QSize(140, 16777215))
        self.signupBtn.setFont(font1)
        self.signupBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signupBtn.setStyleSheet(u"")
        self.gridLayoutWidget_4 = QWidget(self.widget_5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(20, 60, 371, 211))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.signPassword = QLineEdit(self.gridLayoutWidget_4)
        self.signPassword.setObjectName(u"signPassword")
        self.signPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.signPassword, 3, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(12, 12))
        self.label_5.setMaximumSize(QSize(12, 12))
        self.label_5.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/circle-user.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(12, 12))
        self.label_6.setMaximumSize(QSize(12, 12))
        self.label_6.setPixmap(QPixmap(u"../../Eurogate/Qss/icons/Icons/font_awesome/solid/lock.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.fullName = QLineEdit(self.gridLayoutWidget_4)
        self.fullName.setObjectName(u"fullName")

        self.gridLayout_4.addWidget(self.fullName, 0, 1, 1, 1)

        self.signUsername = QLineEdit(self.gridLayoutWidget_4)
        self.signUsername.setObjectName(u"signUsername")

        self.gridLayout_4.addWidget(self.signUsername, 1, 1, 1, 1)

        self.email = QLineEdit(self.gridLayoutWidget_4)
        self.email.setObjectName(u"email")

        self.gridLayout_4.addWidget(self.email, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(12, 12))
        self.label_7.setMaximumSize(QSize(12, 12))
        self.label_7.setPixmap(QPixmap(u"../../Eurogate/Qss/icons/Icons/font_awesome/solid/envelope.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.eyeBtn_5 = QPushButton(self.gridLayoutWidget_4)
        self.eyeBtn_5.setObjectName(u"eyeBtn_5")
        self.eyeBtn_5.setMinimumSize(QSize(20, 20))
        self.eyeBtn_5.setMaximumSize(QSize(20, 20))
        self.eyeBtn_5.setIcon(icon)

        self.gridLayout_4.addWidget(self.eyeBtn_5, 3, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(12, 12))
        self.label_11.setMaximumSize(QSize(12, 12))
        self.label_11.setPixmap(QPixmap(u"../../Eurogate/Qss/icons/Icons/font_awesome/solid/user.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)

        self.errorMessage_2 = QLabel(self.widget_5)
        self.errorMessage_2.setObjectName(u"errorMessage_2")
        self.errorMessage_2.setGeometry(QRect(40, 270, 311, 21))
        self.errorMessage_2.setFont(font3)
        self.errorMessage_2.setStyleSheet(u"color: #ff0000;")
        self.stackedWidget_2.addWidget(self.signinPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget_2)


        self.verticalLayout_2.addWidget(self.loginForm)


        self.horizontalLayout.addWidget(self.mainBody)


        self.verticalLayout_5.addWidget(self.body, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignVCenter)

        self.footer_3 = QWidget(self.LoginPage)
        self.footer_3.setObjectName(u"footer_3")
        self.horizontalLayout_11 = QHBoxLayout(self.footer_3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 3, 0, 3)
        self.label_25 = QLabel(self.footer_3)
        self.label_25.setObjectName(u"label_25")
        font4 = QFont()
        font4.setFamilies([u"Arial Rounded MT Bold"])
        font4.setPointSize(8)
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout_11.addWidget(self.label_25, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer_3, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.LoginPage)
        self.MainPage = QWidget()
        self.MainPage.setObjectName(u"MainPage")
        self.MainPage.setStyleSheet(u"*{\n"
"     border: none;\n"
"     background-color: transparent;\n"
"     background: transparent;\n"
"     padding: 0;\n"
"     margin: 0;\n"
"\n"
"}\n"
"\n"
"#header{\n"
"     background-color: #0F497B;\n"
"} \n"
"#footer_2{\n"
"background-color: #0D406D;\n"
"color: #ffffff;\n"
"}\n"
"#MainPage{\n"
" background-color: #ffffff;\n"
"}\n"
"\n"
"#userBtn, #importBtn, #exportBtn{\n"
"     text-align: center;\n"
"	\n"
" }\n"
" #leftMenu{\n"
"background-color: #0F497B;\n"
" text-align: left;\n"
"  padding: 5px 10px;\n"
"}\n"
" QPushButton{\n"
"\n"
"      padding: 5px 10px;\n"
"      background-color: transparent;\n"
"	 color: #ffffff;\n"
"\n"
"    \n"
"}\n"
"#homeBtn{\n"
"      border-left: 3px solid #EBF1F6;\n"
"       font-weight: bold;\n"
"       background-color: #1461A3;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #10205A;\n"
"        padding: 5px 10px;\n"
"         border-radius: 5px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.MainPage)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainBody2 = QWidget(self.MainPage)
        self.mainBody2.setObjectName(u"mainBody2")
        self.verticalLayout_14 = QVBoxLayout(self.mainBody2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBody2)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(170, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.menuBtn = QPushButton(self.frame_2)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMaximumSize(QSize(24, 24))
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn.setStyleSheet(u"color: #10205A;")
        icon1 = QIcon()
        icon1.addFile(u"../../Users/surfac/Downloads/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon1)
        self.menuBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_4.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(200, 40))
        self.label_21.setPixmap(QPixmap(u"../../Users/surfac/Downloads/stacktrack.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_21, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.userBtn = QPushButton(self.frame)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setMinimumSize(QSize(38, 38))
        self.userBtn.setMaximumSize(QSize(38, 38))
        font5 = QFont()
        font5.setStrikeOut(False)
        self.userBtn.setFont(font5)
        self.userBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../../Users/surfac/Downloads/se-deconnecter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon2)
        self.userBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.userBtn, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_14.addWidget(self.header)

        self.mainBody_2 = QWidget(self.mainBody2)
        self.mainBody_2.setObjectName(u"mainBody_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody_2.sizePolicy().hasHeightForWidth())
        self.mainBody_2.setSizePolicy(sizePolicy)
        self.mainBody_2.setMinimumSize(QSize(919, 593))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBody_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody_2)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(130, 500))
        self.leftMenu.setStyleSheet(u"QPushButton{\n"
"text-align: left;\n"
"border-radius: 0px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 0)
        self.widget_6 = QWidget(self.leftMenu)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(130, 0))
        self.widget_6.setStyleSheet(u"margin-bottom: 15px;\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 15, 0, -1)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_9 = QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.homeBtn = QPushButton(self.widget_7)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setFont(font1)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: #1461A3;")
        icon3 = QIcon()
        icon3.addFile(u"../../Users/surfac/Downloads/accueil (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon3)
        self.homeBtn.setFlat(False)

        self.verticalLayout_9.addWidget(self.homeBtn)

        self.reportsBtn = QPushButton(self.widget_7)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setFont(font1)
        self.reportsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"../../Users/surfac/Downloads/barre-graphique.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon4)
        self.reportsBtn.setIconSize(QSize(14, 14))

        self.verticalLayout_9.addWidget(self.reportsBtn)

        self.settingsBtn = QPushButton(self.widget_7)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font1)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"../../Users/surfac/Downloads/parametre.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)

        self.verticalLayout_9.addWidget(self.settingsBtn)


        self.verticalLayout_8.addWidget(self.widget_7)


        self.verticalLayout_7.addWidget(self.widget_6, 0, Qt.AlignVCenter)

        self.line = QFrame(self.leftMenu)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: #EBF1F6;")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.exportBtn = QPushButton(self.leftMenu)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setFont(font1)
        self.exportBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportBtn.setStyleSheet(u"margin-top: 20px;")
        icon6 = QIcon()
        icon6.addFile(u"../../Users/surfac/Downloads/fleche-vers-le-bas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportBtn.setIcon(icon6)

        self.verticalLayout_7.addWidget(self.exportBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody_2)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.mainBodyContent.setStyleSheet(u"background-color: #EBF1F6;")
        self.verticalLayout_11 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.mainPages = QCustomQStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_12 = QVBoxLayout(self.homePage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_8 = QFrame(self.homePage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: transparent;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: #ffffff;")
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setFamilies([u"Arial Rounded MT Bold"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"padding: 5px;\n"
"margin-left: 5px;")

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"#frame_10{\n"
"padding: 10px;\n"
"}\n"
"#densityChartWidget{\n"
"padding: 30px;}")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.pieChartWidget = QWidget(self.frame_10)
        self.pieChartWidget.setObjectName(u"pieChartWidget")
        self.pieChartWidget.setStyleSheet(u"background-color: #ffffff;")
        self.verticalLayout_13 = QVBoxLayout(self.pieChartWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, 30, -1)
        self.label_8 = QLabel(self.pieChartWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamilies([u"Arial Rounded MT Bold"])
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.label_8.setFont(font7)

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.pieChartWidget)

        self.line_2 = QFrame(self.frame_10)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: #EBF1F6;\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.densityChartWidget = QWidget(self.frame_10)
        self.densityChartWidget.setObjectName(u"densityChartWidget")
        self.densityChartWidget.setStyleSheet(u"background-color: #ffffff;\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.densityChartWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(6, -1, -1, -1)
        self.label_20 = QLabel(self.densityChartWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 20))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamilies([u"Arial Rounded MT Bold"])
        font8.setPointSize(9)
        self.label_20.setFont(font8)

        self.verticalLayout_10.addWidget(self.label_20, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.densityChartWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_27 = QVBoxLayout(self.widget_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 0, -1, 100)
        self.progressBarYardDensity = QProgressBar(self.widget_10)
        self.progressBarYardDensity.setObjectName(u"progressBarYardDensity")
        self.progressBarYardDensity.setMinimumSize(QSize(200, 30))
        self.progressBarYardDensity.setFont(font1)
        self.progressBarYardDensity.setStyleSheet(u"")
        self.progressBarYardDensity.setValue(24)
        self.progressBarYardDensity.setOrientation(Qt.Horizontal)
        self.progressBarYardDensity.setInvertedAppearance(False)

        self.verticalLayout_27.addWidget(self.progressBarYardDensity)


        self.verticalLayout_10.addWidget(self.widget_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.densityChartWidget)


        self.verticalLayout_6.addWidget(self.frame_10, 0, Qt.AlignTop)


        self.verticalLayout_21.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_4)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lineGraphWidget = QWidget(self.frame_4)
        self.lineGraphWidget.setObjectName(u"lineGraphWidget")
        self.lineGraphWidget.setStyleSheet(u"background-color: #ffffff;\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.lineGraphWidget)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 6, -1, 0)
        self.label_26 = QLabel(self.lineGraphWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"padding: 5px;\n"
"margin-left: 5px;")

        self.verticalLayout_25.addWidget(self.label_26, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.lineGraphWidget)


        self.verticalLayout_21.addWidget(self.frame_4)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.reportsPage.setStyleSheet(u"            QTableWidget {\n"
"                background-color: #FFFFFF;\n"
"                border: 1px solid #DDDDDD;\n"
"                font-size: 10px;\n"
"                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"            }\n"
"            QHeaderView::section {\n"
"                background-color: #E0EFF9;\n"
"                color: #333333;\n"
"                padding: 2px;\n"
"                border: none;\n"
"                font-size: 10px;\n"
"                font-weight: bold;\n"
"            }\n"
"                                       \n"
"            QTableWidget::item {\n"
"                padding: 4px;\n"
"            }\n"
"QTableWidget::item:selected {\n"
"    background-color: #E3F7EB;\n"
"\n"
"}\n"
"          ")
        self.verticalLayout_4 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.reportsPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 130))
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(3)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"padding: 6px;")

        self.verticalLayout_19.addWidget(self.label_2)

        self.tableWidget_2 = QTableWidget(self.frame_5)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMaximumSize(QSize(16777215, 70))
        self.tableWidget_2.setStyleSheet(u"")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Raised)
        self.tableWidget_2.setLineWidth(0)
        self.tableWidget_2.setMidLineWidth(2)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_19.addWidget(self.tableWidget_2, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_6 = QFrame(self.reportsPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(2)
        self.frame_6.setMidLineWidth(3)
        self.verticalLayout_20 = QVBoxLayout(self.frame_6)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 10, 15, 15)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font9 = QFont()
        font9.setFamilies([u"Arial Rounded MT Bold"])
        font9.setPointSize(10)
        self.label_4.setFont(font9)
        self.label_4.setStyleSheet(u"padding: 8px;")

        self.verticalLayout_20.addWidget(self.label_4)

        self.tableWidget = QTableWidget(self.frame_6)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(40)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        font10 = QFont()
        font10.setFamilies([u"Segoe UI,Tahoma,Geneva,Verdana,sans-serif"])
        self.tableWidget.setFont(font10)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(2)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(20)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_20.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.reportsPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.mainPages.addWidget(self.accountPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsPage.setStyleSheet(u"#changePassBtn, #changeEmailBtn {\n"
"	background-color:#1b1b27;\n"
"	color: #FFFFFF;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_9 = QWidget(self.settingsPage)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_3 = QFrame(self.widget_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: #ffffff;")
        self.frame_3.setFrameShape(QFrame.Panel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setMidLineWidth(2)
        self.verticalLayout_22 = QVBoxLayout(self.frame_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(20, -1, -1, -1)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        font11 = QFont()
        font11.setFamilies([u"Arial Rounded MT Bold"])
        font11.setPointSize(13)
        font11.setBold(True)
        self.label_17.setFont(font11)
        self.label_17.setStyleSheet(u"color:#265fa9;")

        self.verticalLayout_22.addWidget(self.label_17)

        self.widget_3 = QWidget(self.frame_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 100))
        self.layoutWidget = QWidget(self.widget_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(6, 6, 481, 70))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(8)
        self.gridLayout_3.setVerticalSpacing(12)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.newEmail = QLineEdit(self.layoutWidget)
        self.newEmail.setObjectName(u"newEmail")

        self.gridLayout_3.addWidget(self.newEmail, 1, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)

        self.eyeBtn_4 = QPushButton(self.layoutWidget)
        self.eyeBtn_4.setObjectName(u"eyeBtn_4")
        self.eyeBtn_4.setMinimumSize(QSize(20, 20))
        self.eyeBtn_4.setMaximumSize(QSize(20, 20))
        self.eyeBtn_4.setIcon(icon)

        self.gridLayout_3.addWidget(self.eyeBtn_4, 0, 2, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.passEmail = QLineEdit(self.layoutWidget)
        self.passEmail.setObjectName(u"passEmail")
        self.passEmail.setMinimumSize(QSize(250, 0))
        self.passEmail.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.passEmail, 0, 1, 1, 1)

        self.changeEmailBtn = QPushButton(self.widget_3)
        self.changeEmailBtn.setObjectName(u"changeEmailBtn")
        self.changeEmailBtn.setGeometry(QRect(540, 20, 101, 41))
        self.changeEmailBtn.setMaximumSize(QSize(180, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI Semibold"])
        font12.setPointSize(9)
        font12.setBold(True)
        self.changeEmailBtn.setFont(font12)
        self.changeEmailBtn.setStyleSheet(u"background-color: #1461A3;")

        self.verticalLayout_22.addWidget(self.widget_3)

        self.errorMessage_4 = QLabel(self.frame_3)
        self.errorMessage_4.setObjectName(u"errorMessage_4")
        self.errorMessage_4.setMinimumSize(QSize(0, 20))
        self.errorMessage_4.setMaximumSize(QSize(16777215, 15))
        self.errorMessage_4.setFont(font3)
        self.errorMessage_4.setStyleSheet(u"color: #ff0000;")

        self.verticalLayout_22.addWidget(self.errorMessage_4)

        self.successMessage_2 = QLabel(self.frame_3)
        self.successMessage_2.setObjectName(u"successMessage_2")
        self.successMessage_2.setMaximumSize(QSize(16777215, 20))
        self.successMessage_2.setFont(font3)
        self.successMessage_2.setStyleSheet(u"color: #00A36C;")

        self.verticalLayout_22.addWidget(self.successMessage_2)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.frame_81 = QFrame(self.widget_9)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setStyleSheet(u"background-color: #ffffff;")
        self.frame_81.setFrameShape(QFrame.Panel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.frame_81.setLineWidth(3)
        self.frame_81.setMidLineWidth(2)
        self.verticalLayout_23 = QVBoxLayout(self.frame_81)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(20, -1, -1, -1)
        self.label_16 = QLabel(self.frame_81)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font11)
        self.label_16.setStyleSheet(u"color:#265fa9;")
        self.label_16.setLineWidth(0)
        self.label_16.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_16)

        self.widget_8 = QWidget(self.frame_81)
        self.widget_8.setObjectName(u"widget_8")
        self.changePassBtn = QPushButton(self.widget_8)
        self.changePassBtn.setObjectName(u"changePassBtn")
        self.changePassBtn.setGeometry(QRect(550, 20, 121, 41))
        self.changePassBtn.setFont(font12)
        self.changePassBtn.setStyleSheet(u"background-color: #1461A3;")
        self.widget1 = QWidget(self.widget_8)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(6, 6, 501, 62))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.currentPassword = QLineEdit(self.widget1)
        self.currentPassword.setObjectName(u"currentPassword")
        self.currentPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.currentPassword, 0, 1, 1, 1)

        self.eyeBtn_3 = QPushButton(self.widget1)
        self.eyeBtn_3.setObjectName(u"eyeBtn_3")
        self.eyeBtn_3.setMinimumSize(QSize(20, 20))
        self.eyeBtn_3.setMaximumSize(QSize(20, 20))
        self.eyeBtn_3.setIcon(icon)

        self.gridLayout_2.addWidget(self.eyeBtn_3, 0, 2, 1, 1)

        self.newPassword = QLineEdit(self.widget1)
        self.newPassword.setObjectName(u"newPassword")
        self.newPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.newPassword, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)

        self.eyeBtn_2 = QPushButton(self.widget1)
        self.eyeBtn_2.setObjectName(u"eyeBtn_2")
        self.eyeBtn_2.setMinimumSize(QSize(20, 20))
        self.eyeBtn_2.setMaximumSize(QSize(20, 20))
        self.eyeBtn_2.setIcon(icon)

        self.gridLayout_2.addWidget(self.eyeBtn_2, 2, 2, 1, 1)


        self.verticalLayout_23.addWidget(self.widget_8)

        self.successMessage = QLabel(self.frame_81)
        self.successMessage.setObjectName(u"successMessage")
        self.successMessage.setMinimumSize(QSize(0, 20))
        self.successMessage.setMaximumSize(QSize(16777215, 15))
        self.successMessage.setFont(font3)
        self.successMessage.setStyleSheet(u"color: #00A36C;")

        self.verticalLayout_23.addWidget(self.successMessage)

        self.errorMessage_3 = QLabel(self.frame_81)
        self.errorMessage_3.setObjectName(u"errorMessage_3")
        self.errorMessage_3.setMinimumSize(QSize(0, 20))
        self.errorMessage_3.setMaximumSize(QSize(16777215, 15))
        self.errorMessage_3.setFont(font3)
        self.errorMessage_3.setStyleSheet(u"color: #ff0000;")

        self.verticalLayout_23.addWidget(self.errorMessage_3)


        self.verticalLayout_17.addWidget(self.frame_81)


        self.verticalLayout_18.addWidget(self.widget_9)

        self.mainPages.addWidget(self.settingsPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.label_12 = QLabel(self.helpPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(100, 140, 91, 81))
        self.mainPages.addWidget(self.helpPage)

        self.verticalLayout_11.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainBodyContent)


        self.verticalLayout_14.addWidget(self.mainBody_2)


        self.verticalLayout_15.addWidget(self.mainBody2)

        self.footer_2 = QWidget(self.MainPage)
        self.footer_2.setObjectName(u"footer_2")
        font13 = QFont()
        font13.setFamilies([u"Arial Rounded MT Bold"])
        font13.setPointSize(7)
        self.footer_2.setFont(font13)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 3, 0, 3)
        self.label_10 = QLabel(self.footer_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout_6.addWidget(self.label_10, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.footer_2)

        self.stackedWidget.addWidget(self.MainPage)

        self.verticalLayout_16.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_14.setBuddy(self.goToSigninBtn)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.username, self.password)
        QWidget.setTabOrder(self.password, self.eyeBtn)
        QWidget.setTabOrder(self.eyeBtn, self.loginBtn)
        QWidget.setTabOrder(self.loginBtn, self.goToSigninBtn)
        QWidget.setTabOrder(self.goToSigninBtn, self.fullName)
        QWidget.setTabOrder(self.fullName, self.signUsername)
        QWidget.setTabOrder(self.signUsername, self.email)
        QWidget.setTabOrder(self.email, self.signPassword)
        QWidget.setTabOrder(self.signPassword, self.eyeBtn_5)
        QWidget.setTabOrder(self.eyeBtn_5, self.signupBtn)
        QWidget.setTabOrder(self.signupBtn, self.goToLoginBtn)
        QWidget.setTabOrder(self.goToLoginBtn, self.menuBtn)
        QWidget.setTabOrder(self.menuBtn, self.homeBtn)
        QWidget.setTabOrder(self.homeBtn, self.reportsBtn)
        QWidget.setTabOrder(self.reportsBtn, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.settingsBtn)
        QWidget.setTabOrder(self.settingsBtn, self.passEmail)
        QWidget.setTabOrder(self.passEmail, self.newEmail)
        QWidget.setTabOrder(self.newEmail, self.eyeBtn_4)
        QWidget.setTabOrder(self.eyeBtn_4, self.changeEmailBtn)
        QWidget.setTabOrder(self.changeEmailBtn, self.currentPassword)
        QWidget.setTabOrder(self.currentPassword, self.newPassword)
        QWidget.setTabOrder(self.newPassword, self.eyeBtn_3)
        QWidget.setTabOrder(self.eyeBtn_3, self.eyeBtn_2)
        QWidget.setTabOrder(self.eyeBtn_2, self.changePassBtn)
        QWidget.setTabOrder(self.changePassBtn, self.exportBtn)
        QWidget.setTabOrder(self.exportBtn, self.userBtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.mainPages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_22.setText("")
        self.label_3.setText("")
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.goToSigninBtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"New user ?     Sign up to create your account !", None))
        self.passIcon.setText("")
        self.eyeBtn.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_13.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.errorMessage.setText("")
        self.loginLabel_2.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.goToLoginBtn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.signupBtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.signPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.fullName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.signUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_7.setText("")
        self.eyeBtn_5.setText("")
        self.label_11.setText("")
        self.errorMessage_2.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Eurogate Tanger   COPYRIGHT 2024", None))
        self.menuBtn.setText("")
        self.label_21.setText("")
        self.userBtn.setText("")
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"Export reports", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CURRENT STATE OF THE YARD", None))
#if QT_CONFIG(whatsthis)
        self.frame_10.setWhatsThis(QCoreApplication.translate("MainWindow", u"QFrame", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"The actual occupancy of the Yard", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Level of density in the Yard", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"EXPECTED OCCUPANCY VARIATION", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TODAY'S STATUS", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Actual occupancy", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Operational Capacity", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Yard density", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"OCCUPANCY FORECAST", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ETB", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Vessel name", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Load quantity", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Discharge quantity", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Expected occupancy in TEU", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Expected occupancy in %", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Change E-mail :", None))
        self.newEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your new email", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"New e-mail :", None))
        self.eyeBtn_4.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Password :", None))
        self.passEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your current password", None))
        self.changeEmailBtn.setText(QCoreApplication.translate("MainWindow", u"Change e-mail", None))
        self.errorMessage_4.setText("")
        self.successMessage_2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Change password :", None))
        self.changePassBtn.setText(QCoreApplication.translate("MainWindow", u"Change password", None))
        self.currentPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your current password", None))
        self.eyeBtn_3.setText("")
        self.newPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your new password", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Current password :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"New password :", None))
        self.eyeBtn_2.setText("")
        self.successMessage.setText("")
        self.errorMessage_3.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Eurogate Tanger  COPYRIGHT 2024", None))
    # retranslateUi

