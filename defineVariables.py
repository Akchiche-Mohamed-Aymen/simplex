from  PyQt5 import  QtWidgets 
import sys
from main import ui
app = QtWidgets.QApplication(sys.argv) 
window = QtWidgets.QMainWindow()
window.move(600 , 200)
window.setWindowTitle("var v-1.0.0")
variables = QtWidgets.QInputDialog.getInt(window , 'number' , 'Enter number of Variables' , 1  , 1)
constraints = QtWidgets.QInputDialog.getInt(window , 'number' , 'Enter number of Constraints' , 1  , 1)
ui(variables[0] , constraints[0])
window.show()
app.exec_()

