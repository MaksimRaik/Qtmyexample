import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class GHX:

    def __init__(self):

        self.x = np.arange( 0, 100, 10 )
        self.y = np.arange( 0, 50, 1 )

    def MassforGrapg(self):

        X, Y = np.meshgrid( self.x, self.y )

        z = X**2 + Y**2

        return X, Y, z


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        X, Y, z = GHX().MassforGrapg()
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.contourf(X, Y, z)
        self.setCentralWidget(sc)

        toolbar = Navi(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()