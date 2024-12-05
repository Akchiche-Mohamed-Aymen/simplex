from  PyQt5 import QtCore , QtGui , QtWidgets 
from PyQt5.QtGui import  QIcon
from solveLinear import solve_linear_problem
import sys

def ui(nbVar  = 1 , nbCons = 1):
        def solveProblem():
            senses=[]
            valuesConstr = []
            constraintsCoeff = [[]]*nbCons

            for i in range(nbCons):
                combo = combo_boxs[i].currentText()
                if combo == '<=':
                    senses.append('L')
                elif combo == '>=':
                    senses.append('G')
                elif combo == '=':
                    senses.append('E') 
                #get coefficents of obj Function
                objFun = []
                for i in range(nbVar):
                    val = float(text_inputs[i].toPlainText().replace(' ' , ''))
                    objFun.append(val)
                #get coefficents of obj Function
                for i in range(nbCons):
                    for j in range(nbVar):
                        print()
                        
            # constraints values
            for i in range(nbCons):
                val = float(values[i].toPlainText().replace(' ' , ''))
                valuesConstr.append(val)

  #=================================================================
        app = QtWidgets.QApplication(sys.argv) 
        window = QtWidgets.QMainWindow()
        window.resize(1200, 1200)  # Increase the window size to accommodate all elemen
        window.setWindowTitle("Show Result")
        option1 = QtWidgets.QRadioButton('MIN' , window)
        option1.move(120 , 50)
        text_inputs = []
        constraints = [[]]*nbCons
        fun = QtWidgets.QLabel("<h2>Enter the objectif function : </h2>", window)
        fun.resize(400 , 100)
        fun.move( 120 , 150 )
        for i in range(nbVar):
            text = QtWidgets.QTextEdit(window)
            label = QtWidgets.QLabel(f"X{i+1}", window)
            label.move( 120*(i+1),220)
            text.move(120*(i+1) , 255)
            text.setText('0')
            text_inputs.append(text)
        values = []
        combo_boxs=[] 
        con = QtWidgets.QLabel("<h2>Enter the constarints : </h2>", window)
        con.resize(400 , 100)
        con.move( 120 , 300 )
        for i in range(nbCons):
            for j in range(nbVar):
                text_input = QtWidgets.QTextEdit(window)
                label = QtWidgets.QLabel(f"X{j+1}", window)
                label.move( 120*(j+1),295 + 70*(i+1))
                text_input.move(120 * (j + 1), 325 + 70 * (i + 1))
                constraints[i].append(text_input)
                print(text_input.toPlainText())
            combo_box = QtWidgets.QComboBox(window)
            combo_box.move(120 *nbVar + 120, 325+ 70 *(i+1))
            # Add an option (similar to <option>)
            combo_box.addItem("<=", "<=")
            combo_box.addItem("=", "=")
            combo_box.addItem(">=", ">=")  
            combo_boxs.append(combo_box)
            value = QtWidgets.QTextEdit(window)
            value.move(120* nbVar + 240, 325 + 70 * (i + 1)) 
            value.setText('0')
            values.append(value)
        solveBtn = QtWidgets.QPushButton('Solve', window)
        solveBtn.move(400 , 680)
        solveBtn.resize(150 , 70)
        solveBtn.setStyleSheet('color : white ; background-color : blue ; font-size: 20px')
        solveBtn.clicked.connect(solveProblem)
        window.show()
        app.exec_()
