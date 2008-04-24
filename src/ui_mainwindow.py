# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Thu Apr 24 12:51:20 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,637,521).size()).expandedTo(MainWindow.minimumSizeHint()))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(0,76,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,76,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0,27,637,494))
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setWindowModality(QtCore.Qt.NonModal)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QtCore.QSize(16,16))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(205,205,205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(205,205,205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Window,brush)

        brush = QtGui.QBrush(QtGui.QColor(205,205,205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(205,205,205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Window,brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setFrameShape(QtGui.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")

        self.start = QtGui.QWidget()
        self.start.setGeometry(QtCore.QRect(2,2,615,403))
        self.start.setObjectName("start")

        self.label_4 = QtGui.QLabel(self.start)
        self.label_4.setGeometry(QtCore.QRect(210,100,350,117))
        self.label_4.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/sidux-logo.png"))
        self.label_4.setObjectName("label_4")

        self.label_12 = QtGui.QLabel(self.start)
        self.label_12.setGeometry(QtCore.QRect(350,220,80,71))
        self.label_12.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/pyfll-install.png"))
        self.label_12.setObjectName("label_12")

        self.label_2 = QtGui.QLabel(self.start)
        self.label_2.setGeometry(QtCore.QRect(10,30,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_2.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")

        self.label_19 = QtGui.QLabel(self.start)
        self.label_19.setGeometry(QtCore.QRect(10,70,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_19.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_19.setFont(font)
        self.label_19.setAutoFillBackground(False)
        self.label_19.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setOpenExternalLinks(True)
        self.label_19.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_19.setObjectName("label_19")

        self.label_20 = QtGui.QLabel(self.start)
        self.label_20.setGeometry(QtCore.QRect(10,110,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_20.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_20.setOpenExternalLinks(True)
        self.label_20.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_20.setObjectName("label_20")

        self.line_8 = QtGui.QFrame(self.start)
        self.line_8.setGeometry(QtCore.QRect(150,10,20,371))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.label_21 = QtGui.QLabel(self.start)
        self.label_21.setGeometry(QtCore.QRect(10,150,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_21.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_21.setFont(font)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_21.setObjectName("label_21")

        self.label_22 = QtGui.QLabel(self.start)
        self.label_22.setGeometry(QtCore.QRect(10,210,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_22.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_22.setFont(font)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_22.setOpenExternalLinks(True)
        self.label_22.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_22.setObjectName("label_22")

        self.label_23 = QtGui.QLabel(self.start)
        self.label_23.setGeometry(QtCore.QRect(10,250,141,26))

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Link,brush)

        brush = QtGui.QBrush(QtGui.QColor(223,223,223))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Highlight,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Link,brush)
        self.label_23.setPalette(palette)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label_23.setFont(font)
        self.label_23.setAutoFillBackground(False)
        self.label_23.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setOpenExternalLinks(True)
        self.label_23.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_23.setObjectName("label_23")
        self.stackedWidget.addWidget(self.start)

        self.disclaimer = QtGui.QWidget()
        self.disclaimer.setGeometry(QtCore.QRect(2,2,615,403))
        self.disclaimer.setObjectName("disclaimer")

        self.gridlayout1 = QtGui.QGridLayout(self.disclaimer)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label = QtGui.QLabel(self.disclaimer)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/install-gui-title.png"))
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label,0,0,1,1)

        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")

        spacerItem = QtGui.QSpacerItem(20,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout2.addItem(spacerItem,0,0,1,1)

        self.textBrowser_disclaimer = QtGui.QTextBrowser(self.disclaimer)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_disclaimer.sizePolicy().hasHeightForWidth())
        self.textBrowser_disclaimer.setSizePolicy(sizePolicy)
        self.textBrowser_disclaimer.setMinimumSize(QtCore.QSize(10,10))
        self.textBrowser_disclaimer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_disclaimer.setAutoFillBackground(False)
        self.textBrowser_disclaimer.setObjectName("textBrowser_disclaimer")
        self.gridlayout2.addWidget(self.textBrowser_disclaimer,1,0,1,1)
        self.gridlayout1.addLayout(self.gridlayout2,1,0,1,1)
        self.stackedWidget.addWidget(self.disclaimer)

        self.partition = QtGui.QWidget()
        self.partition.setGeometry(QtCore.QRect(2,2,615,403))
        self.partition.setObjectName("partition")

        self.gridlayout3 = QtGui.QGridLayout(self.partition)
        self.gridlayout3.setObjectName("gridlayout3")

        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setObjectName("gridlayout4")

        self.label_8 = QtGui.QLabel(self.partition)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/install-gui-title.png"))
        self.label_8.setObjectName("label_8")
        self.gridlayout4.addWidget(self.label_8,0,0,1,1)

        self.textBrowser_partition = QtGui.QTextBrowser(self.partition)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_partition.sizePolicy().hasHeightForWidth())
        self.textBrowser_partition.setSizePolicy(sizePolicy)
        self.textBrowser_partition.setOpenExternalLinks(True)
        self.textBrowser_partition.setObjectName("textBrowser_partition")
        self.gridlayout4.addWidget(self.textBrowser_partition,2,0,1,1)

        spacerItem1 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout4.addItem(spacerItem1,1,0,1,1)
        self.gridlayout3.addLayout(self.gridlayout4,0,0,1,1)

        self.line_5 = QtGui.QFrame(self.partition)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridlayout3.addWidget(self.line_5,0,1,1,1)

        spacerItem2 = QtGui.QSpacerItem(20,96,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem2,0,2,1,1)

        self.gridlayout5 = QtGui.QGridLayout()
        self.gridlayout5.setObjectName("gridlayout5")

        spacerItem3 = QtGui.QSpacerItem(110,80,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout5.addItem(spacerItem3,0,0,1,1)

        self.groupBox = QtGui.QGroupBox(self.partition)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout6 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout6.setObjectName("gridlayout6")

        self.gridlayout7 = QtGui.QGridLayout()
        self.gridlayout7.setObjectName("gridlayout7")

        self.comboBox_partition = QtGui.QComboBox(self.groupBox)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_partition.setFont(font)
        self.comboBox_partition.setObjectName("comboBox_partition")
        self.gridlayout7.addWidget(self.comboBox_partition,0,0,1,1)

        self.radioButton_gparted = QtGui.QRadioButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_gparted.sizePolicy().hasHeightForWidth())
        self.radioButton_gparted.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_gparted.setFont(font)
        self.radioButton_gparted.setChecked(True)
        self.radioButton_gparted.setObjectName("radioButton_gparted")
        self.gridlayout7.addWidget(self.radioButton_gparted,1,0,1,1)

        self.radioButton_cfdisk = QtGui.QRadioButton(self.groupBox)
        self.radioButton_cfdisk.setEnabled(True)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_cfdisk.sizePolicy().hasHeightForWidth())
        self.radioButton_cfdisk.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_cfdisk.setFont(font)
        self.radioButton_cfdisk.setObjectName("radioButton_cfdisk")
        self.gridlayout7.addWidget(self.radioButton_cfdisk,2,0,1,1)

        self.radioButton_fdisk = QtGui.QRadioButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_fdisk.sizePolicy().hasHeightForWidth())
        self.radioButton_fdisk.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_fdisk.setFont(font)
        self.radioButton_fdisk.setObjectName("radioButton_fdisk")
        self.gridlayout7.addWidget(self.radioButton_fdisk,3,0,1,1)

        self.pushButton_patition = QtGui.QPushButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_patition.sizePolicy().hasHeightForWidth())
        self.pushButton_patition.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_patition.setFont(font)
        self.pushButton_patition.setObjectName("pushButton_patition")
        self.gridlayout7.addWidget(self.pushButton_patition,4,0,1,1)
        self.gridlayout6.addLayout(self.gridlayout7,0,0,1,1)
        self.gridlayout5.addWidget(self.groupBox,1,0,1,1)

        self.checkBox_bootdisk = QtGui.QCheckBox(self.partition)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_bootdisk.setFont(font)
        self.checkBox_bootdisk.setObjectName("checkBox_bootdisk")
        self.gridlayout5.addWidget(self.checkBox_bootdisk,3,0,1,1)

        spacerItem4 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout5.addItem(spacerItem4,4,0,1,1)
        self.gridlayout3.addLayout(self.gridlayout5,0,3,1,1)

        spacerItem5 = QtGui.QSpacerItem(20,96,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout3.addItem(spacerItem5,0,4,1,1)
        self.stackedWidget.addWidget(self.partition)

        self.mountpoints = QtGui.QWidget()
        self.mountpoints.setGeometry(QtCore.QRect(2,2,615,403))
        self.mountpoints.setObjectName("mountpoints")

        self.gridlayout8 = QtGui.QGridLayout(self.mountpoints)
        self.gridlayout8.setObjectName("gridlayout8")

        self.label_5 = QtGui.QLabel(self.mountpoints)
        self.label_5.setWindowModality(QtCore.Qt.NonModal)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/install-gui-title.png"))
        self.label_5.setObjectName("label_5")
        self.gridlayout8.addWidget(self.label_5,0,0,1,1)

        self.gridlayout9 = QtGui.QGridLayout()
        self.gridlayout9.setObjectName("gridlayout9")

        spacerItem6 = QtGui.QSpacerItem(16,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem6,0,0,2,1)

        self.label_11 = QtGui.QLabel(self.mountpoints)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(False)
        self.label_11.setOpenExternalLinks(True)
        self.label_11.setObjectName("label_11")
        self.gridlayout9.addWidget(self.label_11,0,1,1,1)

        spacerItem7 = QtGui.QSpacerItem(16,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem7,0,2,2,1)

        self.comboBox_installtarget = QtGui.QComboBox(self.mountpoints)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_installtarget.setFont(font)
        self.comboBox_installtarget.setObjectName("comboBox_installtarget")
        self.gridlayout9.addWidget(self.comboBox_installtarget,1,1,1,1)
        self.gridlayout8.addLayout(self.gridlayout9,0,1,1,1)

        self.gridlayout10 = QtGui.QGridLayout()
        self.gridlayout10.setObjectName("gridlayout10")

        self.label_9 = QtGui.QLabel(self.mountpoints)
        self.label_9.setSizeIncrement(QtCore.QSize(10,10))
        self.label_9.setBaseSize(QtCore.QSize(15,13))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridlayout10.addWidget(self.label_9,0,0,1,1)

        self.tableWidget_mountpoints = QtGui.QTableWidget(self.mountpoints)
        self.tableWidget_mountpoints.setObjectName("tableWidget_mountpoints")
        self.gridlayout10.addWidget(self.tableWidget_mountpoints,1,0,1,1)
        self.gridlayout8.addLayout(self.gridlayout10,1,0,1,2)
        self.stackedWidget.addWidget(self.mountpoints)

        self.password = QtGui.QWidget()
        self.password.setGeometry(QtCore.QRect(2,2,615,394))
        self.password.setObjectName("password")

        self.gridlayout11 = QtGui.QGridLayout(self.password)
        self.gridlayout11.setObjectName("gridlayout11")

        self.gridlayout12 = QtGui.QGridLayout()
        self.gridlayout12.setObjectName("gridlayout12")

        self.label_7 = QtGui.QLabel(self.password)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/install-gui-title.png"))
        self.label_7.setObjectName("label_7")
        self.gridlayout12.addWidget(self.label_7,0,0,1,1)

        spacerItem8 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout12.addItem(spacerItem8,1,0,1,1)

        self.textBrowser_password = QtGui.QTextBrowser(self.password)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_password.sizePolicy().hasHeightForWidth())
        self.textBrowser_password.setSizePolicy(sizePolicy)
        self.textBrowser_password.setObjectName("textBrowser_password")
        self.gridlayout12.addWidget(self.textBrowser_password,2,0,1,1)
        self.gridlayout11.addLayout(self.gridlayout12,0,0,13,1)

        self.line_6 = QtGui.QFrame(self.password)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridlayout11.addWidget(self.line_6,0,1,13,1)

        self.label_13 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.gridlayout11.addWidget(self.label_13,0,2,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.lineEdit_rootpw = QtGui.QLineEdit(self.password)
        self.lineEdit_rootpw.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_rootpw.setObjectName("lineEdit_rootpw")
        self.hboxlayout.addWidget(self.lineEdit_rootpw)

        self.label_rootpw_icon = QtGui.QLabel(self.password)
        self.label_rootpw_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_rootpw_icon.setObjectName("label_rootpw_icon")
        self.hboxlayout.addWidget(self.label_rootpw_icon)
        self.gridlayout11.addLayout(self.hboxlayout,1,2,1,1)

        self.label_14 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName("label_14")
        self.gridlayout11.addWidget(self.label_14,2,2,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.lineEdit_rootpw_again = QtGui.QLineEdit(self.password)
        self.lineEdit_rootpw_again.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_rootpw_again.setObjectName("lineEdit_rootpw_again")
        self.hboxlayout1.addWidget(self.lineEdit_rootpw_again)

        self.label_rootpw_again_icon = QtGui.QLabel(self.password)
        self.label_rootpw_again_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_rootpw_again_icon.setObjectName("label_rootpw_again_icon")
        self.hboxlayout1.addWidget(self.label_rootpw_again_icon)
        self.gridlayout11.addLayout(self.hboxlayout1,3,2,1,1)

        self.line_2 = QtGui.QFrame(self.password)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridlayout11.addWidget(self.line_2,4,2,1,1)

        self.label_15 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.gridlayout11.addWidget(self.label_15,5,2,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.lineEdit_realname = QtGui.QLineEdit(self.password)
        self.lineEdit_realname.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_realname.setObjectName("lineEdit_realname")
        self.hboxlayout2.addWidget(self.lineEdit_realname)

        self.label_realname_icon = QtGui.QLabel(self.password)
        self.label_realname_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_realname_icon.setObjectName("label_realname_icon")
        self.hboxlayout2.addWidget(self.label_realname_icon)
        self.gridlayout11.addLayout(self.hboxlayout2,6,2,1,1)

        self.label_16 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName("label_16")
        self.gridlayout11.addWidget(self.label_16,7,2,1,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.lineEdit_username = QtGui.QLineEdit(self.password)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.hboxlayout3.addWidget(self.lineEdit_username)

        self.label_username_icon = QtGui.QLabel(self.password)
        self.label_username_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_username_icon.setObjectName("label_username_icon")
        self.hboxlayout3.addWidget(self.label_username_icon)
        self.gridlayout11.addLayout(self.hboxlayout3,8,2,1,1)

        self.label_17 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_17.setObjectName("label_17")
        self.gridlayout11.addWidget(self.label_17,9,2,1,1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.lineEdit_pw = QtGui.QLineEdit(self.password)
        self.lineEdit_pw.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.hboxlayout4.addWidget(self.lineEdit_pw)

        self.label_pw_icon = QtGui.QLabel(self.password)
        self.label_pw_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_pw_icon.setObjectName("label_pw_icon")
        self.hboxlayout4.addWidget(self.label_pw_icon)
        self.gridlayout11.addLayout(self.hboxlayout4,10,2,1,1)

        self.label_18 = QtGui.QLabel(self.password)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_18.setObjectName("label_18")
        self.gridlayout11.addWidget(self.label_18,11,2,1,1)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.lineEdit_pw_again = QtGui.QLineEdit(self.password)
        self.lineEdit_pw_again.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_pw_again.setObjectName("lineEdit_pw_again")
        self.hboxlayout5.addWidget(self.lineEdit_pw_again)

        self.label_pw_again_icon = QtGui.QLabel(self.password)
        self.label_pw_again_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_pw_again_icon.setObjectName("label_pw_again_icon")
        self.hboxlayout5.addWidget(self.label_pw_again_icon)
        self.gridlayout11.addLayout(self.hboxlayout5,12,2,1,1)
        self.stackedWidget.addWidget(self.password)

        self.hostname = QtGui.QWidget()
        self.hostname.setGeometry(QtCore.QRect(2,2,615,394))
        self.hostname.setObjectName("hostname")

        self.gridlayout13 = QtGui.QGridLayout(self.hostname)
        self.gridlayout13.setObjectName("gridlayout13")

        self.gridlayout14 = QtGui.QGridLayout()
        self.gridlayout14.setObjectName("gridlayout14")

        self.label_10 = QtGui.QLabel(self.hostname)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/install-gui-title.png"))
        self.label_10.setObjectName("label_10")
        self.gridlayout14.addWidget(self.label_10,0,0,1,1)

        spacerItem9 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout14.addItem(spacerItem9,1,0,1,1)

        self.textBrowser_hostname = QtGui.QTextBrowser(self.hostname)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_hostname.sizePolicy().hasHeightForWidth())
        self.textBrowser_hostname.setSizePolicy(sizePolicy)
        self.textBrowser_hostname.setObjectName("textBrowser_hostname")
        self.gridlayout14.addWidget(self.textBrowser_hostname,3,0,1,1)

        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout14.addItem(spacerItem10,2,0,1,1)
        self.gridlayout13.addLayout(self.gridlayout14,0,0,1,1)

        self.line_7 = QtGui.QFrame(self.hostname)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridlayout13.addWidget(self.line_7,0,1,1,1)

        self.gridlayout15 = QtGui.QGridLayout()
        self.gridlayout15.setObjectName("gridlayout15")

        spacerItem11 = QtGui.QSpacerItem(20,21,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout15.addItem(spacerItem11,0,0,1,1)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_25 = QtGui.QLabel(self.hostname)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_25.setObjectName("label_25")
        self.vboxlayout.addWidget(self.label_25)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.lineEdit_hostname = QtGui.QLineEdit(self.hostname)
        self.lineEdit_hostname.setMinimumSize(QtCore.QSize(160,0))
        self.lineEdit_hostname.setObjectName("lineEdit_hostname")
        self.hboxlayout6.addWidget(self.lineEdit_hostname)

        self.label_hostname_icon = QtGui.QLabel(self.hostname)
        self.label_hostname_icon.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/no.png"))
        self.label_hostname_icon.setObjectName("label_hostname_icon")
        self.hboxlayout6.addWidget(self.label_hostname_icon)
        self.vboxlayout.addLayout(self.hboxlayout6)

        self.line_3 = QtGui.QFrame(self.hostname)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.vboxlayout.addWidget(self.line_3)
        self.gridlayout15.addLayout(self.vboxlayout,1,0,1,1)

        spacerItem12 = QtGui.QSpacerItem(20,21,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout15.addItem(spacerItem12,2,0,1,1)

        self.groupBox_services = QtGui.QGroupBox(self.hostname)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_services.sizePolicy().hasHeightForWidth())
        self.groupBox_services.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_services.setFont(font)
        self.groupBox_services.setObjectName("groupBox_services")

        self.gridlayout16 = QtGui.QGridLayout(self.groupBox_services)
        self.gridlayout16.setObjectName("gridlayout16")

        self.checkBox_cupsys = QtGui.QCheckBox(self.groupBox_services)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cupsys.setFont(font)
        self.checkBox_cupsys.setChecked(True)
        self.checkBox_cupsys.setObjectName("checkBox_cupsys")
        self.gridlayout16.addWidget(self.checkBox_cupsys,0,0,1,1)

        self.checkBox_ssh = QtGui.QCheckBox(self.groupBox_services)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_ssh.setFont(font)
        self.checkBox_ssh.setObjectName("checkBox_ssh")
        self.gridlayout16.addWidget(self.checkBox_ssh,1,0,1,1)
        self.gridlayout15.addWidget(self.groupBox_services,3,0,1,1)

        spacerItem13 = QtGui.QSpacerItem(20,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout15.addItem(spacerItem13,4,0,1,1)

        spacerItem14 = QtGui.QSpacerItem(20,21,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout15.addItem(spacerItem14,6,0,1,1)

        self.groupBox_2 = QtGui.QGroupBox(self.hostname)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout17 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout17.setObjectName("gridlayout17")

        self.label_timezone = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_timezone.sizePolicy().hasHeightForWidth())
        self.label_timezone.setSizePolicy(sizePolicy)
        self.label_timezone.setMinimumSize(QtCore.QSize(0,30))
        self.label_timezone.setMaximumSize(QtCore.QSize(16777215,30))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_timezone.setFont(font)
        self.label_timezone.setFrameShadow(QtGui.QFrame.Plain)
        self.label_timezone.setScaledContents(False)
        self.label_timezone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timezone.setObjectName("label_timezone")
        self.gridlayout17.addWidget(self.label_timezone,0,1,1,1)

        self.pushButton_timezone = QtGui.QPushButton(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_timezone.sizePolicy().hasHeightForWidth())
        self.pushButton_timezone.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_timezone.setFont(font)
        self.pushButton_timezone.setObjectName("pushButton_timezone")
        self.gridlayout17.addWidget(self.pushButton_timezone,1,1,1,1)

        spacerItem15 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout17.addItem(spacerItem15,1,0,1,1)

        spacerItem16 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout17.addItem(spacerItem16,1,2,1,1)
        self.gridlayout15.addWidget(self.groupBox_2,5,0,1,1)
        self.gridlayout13.addLayout(self.gridlayout15,0,2,1,1)
        self.stackedWidget.addWidget(self.hostname)

        self.progress = QtGui.QWidget()
        self.progress.setGeometry(QtCore.QRect(2,2,615,394))
        self.progress.setObjectName("progress")

        self.gridlayout18 = QtGui.QGridLayout(self.progress)
        self.gridlayout18.setObjectName("gridlayout18")

        spacerItem17 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout18.addItem(spacerItem17,0,0,1,1)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        spacerItem18 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem18)

        self.label_6 = QtGui.QLabel(self.progress)
        self.label_6.setPixmap(QtGui.QPixmap(":/pixmaps/pixmaps/sidux-logo.png"))
        self.label_6.setObjectName("label_6")
        self.hboxlayout7.addWidget(self.label_6)

        spacerItem19 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem19)
        self.gridlayout18.addLayout(self.hboxlayout7,1,0,1,1)

        spacerItem20 = QtGui.QSpacerItem(20,16,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout18.addItem(spacerItem20,2,0,1,1)

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_progress = QtGui.QLabel(self.progress)
        self.label_progress.setMinimumSize(QtCore.QSize(0,50))
        self.label_progress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_progress.setObjectName("label_progress")
        self.vboxlayout1.addWidget(self.label_progress)

        self.line_4 = QtGui.QFrame(self.progress)
        self.line_4.setMinimumSize(QtCore.QSize(0,16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.vboxlayout1.addWidget(self.line_4)

        self.progressBar = QtGui.QProgressBar(self.progress)
        self.progressBar.setProperty("value",QtCore.QVariant(24))
        self.progressBar.setObjectName("progressBar")
        self.vboxlayout1.addWidget(self.progressBar)
        self.gridlayout18.addLayout(self.vboxlayout1,3,0,1,1)

        spacerItem21 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Preferred)
        self.gridlayout18.addItem(spacerItem21,4,0,1,1)
        self.stackedWidget.addWidget(self.progress)
        self.gridlayout.addWidget(self.stackedWidget,0,0,1,1)

        self.label_start = QtGui.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_start.setFont(font)
        self.label_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_start.setOpenExternalLinks(True)
        self.label_start.setObjectName("label_start")
        self.gridlayout.addWidget(self.label_start,1,0,1,1)

        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line,2,0,1,1)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.pushButton_exit = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setDefault(True)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.hboxlayout8.addWidget(self.pushButton_exit)

        spacerItem22 = QtGui.QSpacerItem(181,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem22)

        self.pushButton_prev = QtGui.QPushButton(self.centralwidget)
        self.pushButton_prev.setEnabled(True)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_prev.setFont(font)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.hboxlayout8.addWidget(self.pushButton_prev)

        self.pushButton_next = QtGui.QPushButton(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_next.setObjectName("pushButton_next")
        self.hboxlayout8.addWidget(self.pushButton_next)
        self.gridlayout.addLayout(self.hboxlayout8,3,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,637,27))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")

        self.menuDatei = QtGui.QMenu(self.menubar)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuDatei.setFont(font)
        self.menuDatei.setObjectName("menuDatei")

        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.action_Help = QtGui.QAction(MainWindow)
        self.action_Help.setMenuRole(QtGui.QAction.AboutRole)
        self.action_Help.setObjectName("action_Help")
        self.menuDatei.addAction(self.actionExit)
        self.menu_Help.addAction(self.action_Help)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label.setBuddy(self.label)
        self.label_8.setBuddy(self.label)
        self.label_5.setBuddy(self.label)
        self.label_7.setBuddy(self.label)
        self.label_10.setBuddy(self.label)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit,QtCore.SIGNAL("activated(int)"),MainWindow.close)
        QtCore.QObject.connect(self.pushButton_exit,QtCore.SIGNAL("clicked()"),MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_exit,self.pushButton_next)
        MainWindow.setTabOrder(self.pushButton_next,self.pushButton_prev)
        MainWindow.setTabOrder(self.pushButton_prev,self.textBrowser_disclaimer)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "sidux HD-Installation", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "http://sidux.com", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setWhatsThis(QtGui.QApplication.translate("MainWindow", "install sidux to your harddisk", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://sidux.com/\"><span style=\" font-weight:400; text-decoration: underline; color:#5c5c5c;\">sidux homepage</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://manual.sidux.com/\"><span style=\" font-weight:400; text-decoration: underline; color:#5c5c5c;\">sidux manual</span></a><span style=\" font-weight:400; color:#5c5c5c;\"> </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://sidux.com/module-PNphpBB2.html\"><span style=\" font-weight:400; text-decoration: underline; color:#5c5c5c;\">sidux forum</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://sidux.com/module-pnWikka.html\"><span style=\" font-weight:400; text-decoration: underline; color:#5c5c5c;\">sidux wiki</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://sidux-ev.de/\"><span style=\" font-weight:400; text-decoration: underline; color:#5c5c5c;\">sidux e.V.</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><a href=\"http://www.linux-versand.org/index.php/cat/c75_All-for-sidux.html\"><span style=\" font-weight:400; text-decoration: underline; color:#565c5c;\">sidux webshop</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_disclaimer.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline; color:#c0c0c0;\"><span style=\" font-size:12pt; color:#000000;\">Disclaimer</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600; text-decoration: underline; color:#c0c0c0;\"><span style=\" font-size:11pt; font-weight:400; text-decoration:none; color:#000000;\">sidux is a ...</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#000000;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_partition.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">partition your harddisk</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\">sidux prefers ext3.</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; text-decoration: underline; color:#0000ff;\"><a href=\"http://manual.sidux.com/en/part-gparted-en.html#partition\"><span style=\" color:#0057ae;\">How to partition your HD</span></a></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Partition Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_gparted.setText(QtGui.QApplication.translate("MainWindow", "&gparted", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_cfdisk.setText(QtGui.QApplication.translate("MainWindow", "&cfdisk", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_fdisk.setText(QtGui.QApplication.translate("MainWindow", "&fdisk", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_patition.setText(QtGui.QApplication.translate("MainWindow", "&Start gparted", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_bootdisk.setText(QtGui.QApplication.translate("MainWindow", "create a bootdisk", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Installation target</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><span style=\" font-size:10pt; font-weight:400;\">MBR (Master Boot Record) or root-partition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Set mountpoints", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_mountpoints.clear()
        self.tableWidget_mountpoints.setColumnCount(0)
        self.tableWidget_mountpoints.setRowCount(0)
        self.textBrowser_password.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter the Password</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Root-password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Root-password again:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Realname:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Password again:", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_hostname.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Network and services</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Hostname:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_services.setTitle(QtGui.QApplication.translate("MainWindow", "start services", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cupsys.setText(QtGui.QApplication.translate("MainWindow", "cupsys (Printing System)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ssh.setText(QtGui.QApplication.translate("MainWindow", "ssh (Secure shell server and client)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Timezone", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_timezone.setText(QtGui.QApplication.translate("MainWindow", "Timezone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_progress.setText(QtGui.QApplication.translate("MainWindow", "lölöl", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev.setText(QtGui.QApplication.translate("MainWindow", "&Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next.setText(QtGui.QApplication.translate("MainWindow", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.menuDatei.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Help.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
