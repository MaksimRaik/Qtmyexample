from PyQt5 import QtCore, QtGui, QtWidgets
import functionSA as fsa
#import phasediog_version3 as phdv3
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import sip
import seaborn as sns


class MatplotlibCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, dpi=120):
        self.fig = Figure(figsize = ( 40, 30 ), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        #self.axes3D = Axes3D(self.fig)
        super(MatplotlibCanvas, self).__init__(self.fig)
        # self.fig.tight_layout()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 871, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.Frame_1 = QtWidgets.QWidget()
        self.Frame_1.setObjectName("Frame_1")
        self.verticalLayoutWidget_Frame1 = QtWidgets.QWidget(self.Frame_1)
        self.verticalLayoutWidget_Frame1.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.verticalLayoutWidget_Frame1.setObjectName("verticalLayoutWidget_Frame1")
        self.verticalLayout_Frame1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_Frame1)
        self.verticalLayout_Frame1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Frame1.setObjectName("verticalLayout_Frame1")
        self.tabWidget.addTab(self.Frame_1, "")
        self.Frame_2 = QtWidgets.QWidget()
        self.Frame_2.setObjectName("Frame_2")
        self.verticalLayoutWidget_Frame2 = QtWidgets.QWidget(self.Frame_2)
        self.verticalLayoutWidget_Frame2.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.verticalLayoutWidget_Frame2.setObjectName("verticalLayoutWidget_Frame2")
        self.verticalLayout_Frame2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_Frame2)
        self.verticalLayout_Frame2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Frame2.setObjectName("verticalLayout_Frame2")
        self.tabWidget.addTab(self.Frame_2, "")
        self.Frame_3 = QtWidgets.QWidget()
        self.Frame_3.setObjectName("Frame_3")
        self.verticalLayoutWidget_Frame3 = QtWidgets.QWidget(self.Frame_3)
        self.verticalLayoutWidget_Frame3.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.verticalLayoutWidget_Frame3.setObjectName("verticalLayoutWidget_Frame3")
        self.verticalLayout_Frame3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_Frame3)
        self.verticalLayout_Frame3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Frame3.setObjectName("verticalLayout_Frame3")
        self.tabWidget.addTab(self.Frame_3, "")
        self.Frame_4 = QtWidgets.QWidget()
        self.Frame_4.setObjectName("Frame_4")
        self.verticalLayoutWidget_Frame4 = QtWidgets.QWidget(self.Frame_4)
        self.verticalLayoutWidget_Frame4.setGeometry(QtCore.QRect(0, 0, 871, 531))
        self.verticalLayoutWidget_Frame4.setObjectName("verticalLayoutWidget_Frame4")
        self.verticalLayout_Frame4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_Frame4)
        self.verticalLayout_Frame4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Frame4.setObjectName("verticalLayout_Frame4")
        self.tabWidget.addTab(self.Frame_4, "")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(879, 60, 131, 531))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 595, 1000, 81))
        self.textEdit.setObjectName("textEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 1001, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon folder/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon folder/round-play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName('pushButton_2')
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuModel = QtWidgets.QMenu(self.menubar)
        self.menuModel.setObjectName("menuModel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_PVI_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_PVI_file.setObjectName("actionOpen_PVI_file")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionMaximazine_Window = QtWidgets.QAction(MainWindow)
        self.actionMaximazine_Window.setObjectName("actionMaximazine_Window")
        self.actionNormal_Window = QtWidgets.QAction(MainWindow)
        self.actionNormal_Window.setObjectName("actionNormal_Window")
        self.actionConstant_parametr = QtWidgets.QAction(MainWindow)
        self.actionConstant_parametr.setObjectName("actionConstant_parametr")
        self.actionEquation_of_State = QtWidgets.QAction(MainWindow)
        self.actionEquation_of_State.setObjectName("actionEquation_of_State")
        self.menuFile.addAction(self.actionOpen_PVI_file)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionMaximazine_Window)
        self.menuView.addAction(self.actionNormal_Window)
        self.menuModel.addAction(self.actionConstant_parametr)
        self.menuModel.addAction(self.actionEquation_of_State)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuModel.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

## New function and fitures
#############################################################################################

        self.textEdit.setText('Program run \n')

        self.filename = ''
        self.currentPT = 'gas diagram'
        self.canv1 = MatplotlibCanvas(self)

        self.actionExit.triggered.connect(MainWindow.close)  # type: ignore
        self.actionMaximazine_Window.triggered.connect(MainWindow.showMaximized)  # type: ignore
        self.actionNormal_Window.triggered.connect(MainWindow.showNormal)
        self.actionOpen_PVI_file.triggered.connect( self.getFile )

        self.PlotType = ['gas diagram', 'liquid diagram', 'gas+liquid', '3D plot']
        self.comboBox.addItems(self.PlotType)
        self.comboBox.currentIndexChanged['QString'].connect(self.changePT)
        self.pushButton.clicked.connect(self.getFile)
        self.pushButton_2.clicked.connect(self.CalculationData)
        self.pushButton_3.clicked.connect( self.SetPlot )

    def getFile(self):

        self.filename = QFileDialog.getOpenFileName(filter="PVI (*.PVI)")[0]
        self.textEdit.setText( 'File ' + self.filename + ' was opened \n' )

    def changePT(self, value):

        self.currentPT = value

    def CalculationData(self):

        if self.filename == '':

            self.textEdit.setText('File not selected')

        else:

            Const = fsa.Constant( self.filename )

            fsa.N = Const.N

            self.textEdit.setText('Calculate begin')

            self.Pbeg = 100.

            Pdew = fsa.DewPoint( Const.z, np.asarray( [ fsa.T, ] ),  Const.Pcr, Const.Tcr, Const.omega, Const.omegaA,
                                 Const.omegaB, Const.Kjk )[ 0 ] * 1.0e-5

            self.Pend = Pdew * 1.03

            print( Pdew )

            self.Pg, self.Pl, self.Sl, self.Sg, DH = fsa.PhaseDiogramSecondVersion( self.Pbeg * 1.0e5, self.Pend * 1.0e5, fsa.T, Const.z,
                                                                Const.Pcr, Const.Tcr, Const.omega, Const.omegaA,
                                                                Const.omegaB, Const.Kjk )

            self.textEdit.setText('Calculate complited')


    def SetPlot(self):

        NumberFrame = self.tabWidget.currentIndex()

        Pg, Pl, Sl, Sg = self.Pg / 1.0e5, self.Pl / 1.0e5, self.Sl, self.Sg

        if NumberFrame == 0:

            self.canv1 = MatplotlibCanvas(self)

            self.verticalLayout_Frame1.removeWidget(self.canv1)
            sip.delete(self.canv1)
            self.canv1 = None

            self.canv1 = MatplotlibCanvas(self)
            self.verticalLayout_Frame1.addWidget(self.canv1)
            self.canv1.axes.cla()

            if self.currentPT == self.PlotType[0]:

                scc1 = self.canv1.axes.contourf(Pg, Pl, Sg, np.arange( 1.0 - np.max( Sl ), np.max( Sg ), 0.001 ), cmap='BuPu')

            elif self.currentPT == self.PlotType[1]:

                scc1 = self.canv1.axes.contourf(Pg, Pl, Sl, np.arange( np.min( Sl ), np.max( Sl ) ), cmap='BuPu')

            elif self.currentPT == self.PlotType[2]:

                scc = self.canv1.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

                scc = self.canv1.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[3]:

                pass

            self.canv1.axes.set_xlabel(r'$ P_{gas} $')
            self.canv1.axes.set_ylabel(r'$ P_{liq} $')
            self.canv1.axes.grid()
            self.canv1.fig.colorbar(scc1, ax=self.canv1.axes)
            self.textEdit.setText(' plot diagram on Frame =' + str( NumberFrame + 1 ) + ' with PlotType = ' + self.currentPT + ' was complited' )
            self.canv1.draw()

        if NumberFrame == 1:

            self.canv2 = MatplotlibCanvas(self)

            self.verticalLayout_Frame2.removeWidget(self.canv2)
            sip.delete(self.canv2)
            self.canv2 = None

            plt.clf()
            self.canv2 = MatplotlibCanvas(self)
            self.verticalLayout_Frame2.addWidget(self.canv2)
            self.canv2.axes.cla()

            if self.currentPT == self.PlotType[0]:

                scc2 = self.canv2.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

            elif self.currentPT == self.PlotType[1]:

                scc2 = self.canv2.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[2]:

                scc = self.canv2.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

                scc = self.canv2.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[3]:

                pass

            self.canv2.axes.set_xlabel(r'$ P_{gas} $')
            self.canv2.axes.set_ylabel(r'$ P_{liq} $')
            self.canv2.axes.grid()
            self.canv2.fig.colorbar(scc2, ax=self.canv2.axes)
            self.textEdit.setText(' plot diagram on Frame =' + str( NumberFrame + 1 ) + ' with PlotType = ' + self.currentPT + ' was complited' )
            self.canv2.draw()

        if NumberFrame == 2:
            scc = None

            self.canv3 = MatplotlibCanvas(self)

            self.verticalLayout_Frame3.removeWidget(self.canv3)
            sip.delete(self.canv3)
            self.canv3 = None

            plt.clf()
            self.canv3 = MatplotlibCanvas(self)
            self.verticalLayout_Frame3.addWidget(self.canv3)
            self.canv3.axes.cla()
            Pg, Pl, Sl, Sg = self.CalculationData()

            if self.currentPT == self.PlotType[0]:

                scc = self.canv3.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

            elif self.currentPT == self.PlotType[1]:

                scc = self.canv3.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[2]:

                scc = self.canv3.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

                scc = self.canv3.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[3]:

                pass

            self.canv3.axes.set_xlabel(r'$ P_{gas} $')
            self.canv3.axes.set_ylabel(r'$ P_{liq} $')
            self.canv3.axes.grid()
            self.canv3.fig.colorbar(scc, ax=self.canv3.axes)
            self.textEdit.setText(' plot diagram on Frame =' + str( NumberFrame + 1 ) + ' with PlotType = ' + self.currentPT + ' was complited' )
            self.canv3.draw()

        if NumberFrame == 4:

            self.canv4 = MatplotlibCanvas(self)

            self.verticalLayout_Frame4.removeWidget(self.canv4)
            sip.delete(self.canv4)
            self.canv4 = None

            plt.clf()
            self.canv4 = MatplotlibCanvas(self)
            self.verticalLayout_Frame4.addWidget(self.canv4)
            self.canv4.axes.cla()

            if self.currentPT == self.PlotType[0]:

                scc = self.canv4.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

            elif self.currentPT == self.PlotType[1]:

                self.scc = self.canv4.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[2]:

                scc = self.canv4.axes.contourf(Pg, Pl, Sg, cmap='BuPu')

                scc = self.canv4.axes.contourf(Pg, Pl, Sl, cmap='BuPu')

            elif self.currentPT == self.PlotType[3]:

                pass

            self.canv4.axes.set_xlabel(r'$ P_{gas} $')
            self.canv4.axes.set_ylabel(r'$ P_{liq} $')
            self.canv4.axes.grid()
            self.canv4.fig.colorbar(scc, ax=self.canv4.axes)
            self.textEdit.setText(' plot diagram on Frame =' + str( NumberFrame + 1 ) + ' with PlotType = ' + self.currentPT + ' was complited' )
            self.canv4.draw()

#############################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_1), _translate("MainWindow", "Frame 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_2), _translate("MainWindow", "Frame 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_3), _translate("MainWindow", "Frame 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Frame_4), _translate("MainWindow", "Frame 4"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Pressure"))
        self.label_3.setText(_translate("MainWindow", "Temperature"))
        self.label.setText(_translate("MainWindow", "Plot Type"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate('MainWindow', 'Plot Graph'))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuModel.setTitle(_translate("MainWindow", "Model"))
        self.actionOpen_PVI_file.setText(_translate("MainWindow", "Open PVI file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMaximazine_Window.setText(_translate("MainWindow", "Maximazine Window"))
        self.actionNormal_Window.setText(_translate("MainWindow", "Normal Window"))
        self.actionConstant_parametr.setText(_translate("MainWindow", "Constant parametr"))
        self.actionEquation_of_State.setText(_translate("MainWindow", "Equation of State"))
