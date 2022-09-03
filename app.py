import sys
import numpy
import math
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider, QLabel, QHBoxLayout, QLineEdit, QMessageBox,QTabWidget)
from sympy import pretty_print as pp

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.inputTab = QWidget()
        self.outputTab = QWidget()
        self.tabs.resize(800,400)
        
        # Add tabs
        self.tabs.addTab(self.inputTab,"Inputs")
        self.tabs.addTab(self.outputTab,"Results")
        
#    def initInputUI(self):

        self.inputTab.layout = QGridLayout()

        self.methodBox = QGroupBox("Previous Qualifications")
        
        self.mb_radio1 = QRadioButton("Electronics and Communication")
        self.mb_radio2 = QRadioButton("Mechanical")
        self.mb_radio3 = QRadioButton("Computer")
        self.mb_radio4 = QRadioButton("Biomedical")
        self.mb_radio5 = QRadioButton("Architecture")
        self.mb_radio6 = QRadioButton("Industrial")
        self.mb_radio7 = QRadioButton("Aerospace")
        self.mb_radio8 = QRadioButton("Civil")

        self.mb_radio1.setChecked(True)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.mb_radio1)
        self.vbox.addWidget(self.mb_radio2)
        self.vbox.addWidget(self.mb_radio3)
        self.vbox.addWidget(self.mb_radio4)
        self.vbox.addWidget(self.mb_radio5)
        self.vbox.addWidget(self.mb_radio6)
        self.vbox.addWidget(self.mb_radio7)
        self.vbox.addWidget(self.mb_radio8)
        self.vbox.addStretch(1)

        self.methodBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.methodBox, 0, 0)
        
        self.circuitBox = QGroupBox("Personality Traits")
        
        '''
        1. At a party do you:
a. Interact with many, including strangers
b. Interact with a few, known to you
2. Are you more:
a. Realistic than speculative
b. Speculative than realistic
3. Is it worse to:
a. Have your “head in the clouds”
b. Be “in a rut”
4. Are you more impressed by:
a. Principles
b. Emotions
5. Are more drawn toward the:
a. Convincing
b. Touching
6. Do you prefer to work:
a. To deadlines
b. Just “whenever”
7. Do you tend to choose:
a. Rather carefully
b. Somewhat impulsively
8. At parties do you:
a. Stay late, with increasing energy
b. Leave early with decreased energy
9. Are you more attracted to:
a. Sensible people
b. Imaginative people
10. Are you more interested in:
a. What is actual
b. What is possible
11. In judging others are you more swayed
by:
a. Laws than circumstances
b. Circumstances than laws
12. In approaching others is your inclination
to be somewhat:
a. Objective
b. Personal
13. Are you more:
a. Punctual
b. Leisurely
14. Does it bother you more having things:
a. Incomplete
b. Completed
15. In your social groups do you:
a. Keep abreast of other’s happenings
b. Get behind on the news
16. In doing ordinary things are you more
likely to:
a. Do it the usual way
b. Do it your own way
17. Writers should:
a. “Say what they mean and mean what they
say”
b. Express things more by use of analogy
18. Which appeals to you more:
a. Consistency of thought
b. Harmonious human relationships
19. Are you more comfortable in making:
a. Logical judgments
b. Value judgments
20. Do you want things:
a. Settled and decided
b. Unsettled and undecided
21. Would you say you are more:
a. Serious and determined
b. Easy-going
22. In phoning do you:
a. Rarely question that it will all be said
b. Rehearse what you’ll say
23. Facts:
a. “Speak for themselves”
b. Illustrate principles
24. Are visionaries:
a. somewhat annoying
b. rather fascinating
25. Are you more often:
a. a cool-headed person
b. a warm-hearted person
26. Is it worse to be:
a. unjust
b. merciless
27. Should one usually let events occur:
a. by careful selection and choice
b. randomly and by chance
28. Do you feel better about:
a. having purchased
b. having the option to buy
29. In company do you:
a. initiate conversation
b. wait to be approached
30. Common sense is:
a. rarely questionable
b. frequently questionable
31. Children often do not:
a. make themselves useful enough
b. exercise their fantasy enough
32. In making decisions do you feel more
comfortable with:
a. standards
b. feelings
33. Are you more:
a. firm than gentle
b. gentle than firm
34. Which is more admirable:
a. the ability to organize and be methodical
b. the ability to adapt and make do
35. Do you put more value on:
a. infinite
b. open-minded
36. Does new and non-routine interaction
with others:
a. stimulate and energize you
b. tax your reserves
37. Are you more frequently:
a. a practical sort of person
b. a fanciful sort of person
38. Are you more likely to:
a. see how others are useful
b. see how others see
39. Which is more satisfying:
a. to discuss an issue thoroughly
b. to arrive at agreement on an issue
40. Which rules you more:
a. your head
b. your heart
41. Are you more comfortable with work that
is:
a. contracted
b. done on a casual basis
42. Do you tend to look for:
a. the orderly
b. whatever turns up
43. Do you prefer:
a. many friends with brief contact
b. a few friends with more lengthy contact
44. Do you go more by:
a. facts
b. principles
45. Are you more interested in:
a. production and distribution
b. design and research
46. Which is more of a compliment:
a. “There is a very logical person.”
b. “There is a very sentimental person.”
47. Do you value in yourself more that you
are:
a. unwavering
b. devoted
48. Do you more often prefer the
a. final and unalterable statement
b. tentative and preliminary statement
49. Are you more comfortable:
a. after a decision
b. before a decision
50. Do you:
a. speak easily and at length with strangers
b. find little to say to strangers
51. Are you more likely to trust your:
a. experience
b. hunch
52. Do you feel:
a. more practical than ingenious
b. more ingenious than practical
53. Which person is more to be complimented
– one of:
a. clear reason
b. strong feeling
54. Are you inclined more to be:
a. fair-minded
b. sympathetic
55. Is it preferable mostly to:
a. make sure things are arranged
b. just let things happen
56. In relationships should most things be:
a. re-negotiable
b. random and circumstantial
57. When the phone rings do you:
a. hasten to get to it first
b. hope someone else will answer
58. Do you prize more in yourself:
a. a strong sense of reality
b. a vivid imagination
59. Are you drawn more to:
a. fundamentals
b. overtones
60. Which seems the greater error:
a. to be too passionate
b. to be too objective
61. Do you see yourself as basically:
a. hard-headed
b. soft-hearted
62. Which situation appeals to you more:
a. the structured and scheduled
b. the unstructured and unscheduled
63. Are you a person that is more:
a. routinized than whimsical
b. whimsical than routinized
64. Are you more inclined to be:
a. easy to approach
b. somewhat reserved
65. In writings do you prefer:
a. the more literal
b. the more figurative
66. Is it harder for you to:
a. identify with others
b. utilize others
67. Which do you wish more for yourself:
a. clarity of reason
b. strength of compassion
68. Which is the greater fault:
a. being indiscriminate
b. being critical
69. Do you prefer the:
a. planned event
b. unplanned event
70. Do you tend to be more:
a. deliberate than spontaneous
b. spontaneous than deliberate
'''

        self.cb_radio1 = QRadioButton("Q1")
        self.cb_radio2 = QRadioButton("Q2")
        self.cb_radio3 = QRadioButton("Q3")
        self.cb_radio4 = QRadioButton("Q4")
        self.cb_radio5 = QRadioButton("Q5")
    
        self.cb_radio1.setChecked(True)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.cb_radio1)
        self.vbox.addWidget(self.cb_radio2)
        self.vbox.addWidget(self.cb_radio3)
        self.vbox.addWidget(self.cb_radio4)
        self.vbox.addWidget(self.cb_radio5)
        self.vbox.addStretch(1)

        self.circuitBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.circuitBox, 0, 1)


        self.frequencyBox = QGroupBox("Frequency Parameters")

        self.vbox = QVBoxLayout()

        self.fl_label = QLabel("Fl")

        self.fl_slider = QSlider(Qt.Horizontal)
        self.fl_slider.setMinimum(-10)
        self.fl_slider.setMaximum(10)
        self.fl_slider.setValue(0)
        self.fl_slider.setTickPosition(QSlider.TicksBelow)
        self.fl_slider.setTickInterval(1)
        self.fl_slider.valueChanged.connect(self.changeFl)

        self.fl_value = QLabel("0")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fl_label)
        self.hbox.addWidget(self.fl_slider)
        self.hbox.addWidget(self.fl_value)

        self.vbox.addLayout(self.hbox)
        
        self.fu_label = QLabel("Fu")

        self.fu_slider = QSlider(Qt.Horizontal)
        self.fu_slider.setMinimum(-10)
        self.fu_slider.setMaximum(10)
        self.fu_slider.setValue(6)
        self.fu_slider.setTickPosition(QSlider.TicksBelow)
        self.fu_slider.setTickInterval(1)
        self.fu_slider.valueChanged.connect(self.changeFu)

        self.fu_value = QLabel("6")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fu_label)
        self.hbox.addWidget(self.fu_slider)
        self.hbox.addWidget(self.fu_value)

        self.vbox.addLayout(self.hbox)

        self.fstep_label = QLabel("Fstep")

        self.fstep_slider = QSlider(Qt.Horizontal)
        self.fstep_slider.setMinimum(0)
        self.fstep_slider.setMaximum(20)
        self.fstep_slider.setValue(2)
        self.fstep_slider.setTickPosition(QSlider.TicksBelow)
        self.fstep_slider.setTickInterval(1)
        self.fstep_slider.valueChanged.connect(self.changeFstep)

        self.fstep_value = QLabel("2")

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.fstep_label)
        self.hbox.addWidget(self.fstep_slider)
        self.hbox.addWidget(self.fstep_value)

        self.vbox.addLayout(self.hbox)

        self.blank_label = QLabel("\t"*10+"10^")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.blank_label)
        self.vbox.addLayout(self.hbox)

        self.frequencyBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.frequencyBox, 1, 0)
        

        self.inputBox = QGroupBox("Input Parameters")

        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.F_label = QLabel("F")
        self.F_input = QLineEdit("1")
        self.hbox.addWidget(self.F_label)
        self.hbox.addWidget(self.F_input)
        self.vbox.addLayout(self.hbox)

        self.hbox = QHBoxLayout()
        self.alpha_label = QLabel("alpha")
        self.alpha_input = QLineEdit("-0.5")
        self.hbox.addWidget(self.alpha_label)
        self.hbox.addWidget(self.alpha_input)
        self.vbox.addLayout(self.hbox)
        
        self.hbox = QHBoxLayout()
        self.N_label = QLabel("N")
        self.N_input = QLineEdit("10")
        self.hbox.addWidget(self.N_label)
        self.hbox.addWidget(self.N_input)
        self.vbox.addLayout(self.hbox)
        
        self.inputBox.setLayout(self.vbox)

        self.inputTab.layout.addWidget(self.inputBox, 1, 1)


        self.simulateButton = QPushButton("Simulate")
        self.simulateButton.clicked.connect(self.simulate)
        self.inputTab.layout.addWidget(self.simulateButton,2,1)

        self.inputTab.setLayout(self.inputTab.layout)


#    def initOutputUI(self):
        self.outputTab.layout = QGridLayout()

        self.graphSelector = QGroupBox("Approximation Method")
        
        self.gs_radio1 = QRadioButton("Ideal")
        self.gs_radio2 = QRadioButton("Simulated")
        self.gs_radio3 = QRadioButton("Ideal+Simulated")
        self.gs_radio4 = QRadioButton("Error")
        
        self.gs_radio3.setChecked(True)

        self.gs_radio1.toggled.connect(self.updatePlot)
        self.gs_radio2.toggled.connect(self.updatePlot)
        self.gs_radio3.toggled.connect(self.updatePlot)
        self.gs_radio4.toggled.connect(self.updatePlot)    

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.gs_radio1)
        self.vbox.addWidget(self.gs_radio2)
        self.vbox.addWidget(self.gs_radio3)
        self.vbox.addWidget(self.gs_radio4)
        self.vbox.addStretch(1)

        self.graphSelector.setLayout(self.vbox)

        self.outputTab.layout.addWidget(self.graphSelector, 0, 0)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        
        self.outputTab.layout.addWidget(self.canvas, 0, 1)
        
        self.outputTab.setLayout(self.outputTab.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        self.setWindowTitle("Fractional Order Filters GUI Tool")
        self.resize(1000, 500)

        self.mb_radio1.toggled.connect(self.restrictions)
        self.mb_radio2.toggled.connect(self.restrictions)
        self.mb_radio3.toggled.connect(self.restrictions)
        self.mb_radio4.toggled.connect(self.restrictions)  
        self.mb_radio5.toggled.connect(self.restrictions)
        self.mb_radio6.toggled.connect(self.restrictions)
        self.mb_radio7.toggled.connect(self.restrictions)
        self.mb_radio8.toggled.connect(self.restrictions)

        self.restrictions()  

    def changeFstep(self):
        self.fstep_value.setText(str(self.fstep_slider.value()))

    def changeFl(self):
        self.fl_value.setText(str(self.fl_slider.value()))

    def changeFu(self):
        self.fu_value.setText(str(self.fu_slider.value()))

    def restrictions(self):
        if self.mb_radio1.isChecked() or self.mb_radio2.isChecked():
            self.cb_radio1.setEnabled(True)
            self.cb_radio2.setEnabled(False)
            self.cb_radio3.setEnabled(False)
            self.cb_radio4.setEnabled(False)
            self.cb_radio5.setEnabled(False)
            self.cb_radio1.setChecked(True)   
        else :
            self.cb_radio1.setEnabled(False)
            self.cb_radio2.setEnabled(True)
            self.cb_radio3.setEnabled(True)
            self.cb_radio4.setEnabled(True)
            self.cb_radio5.setEnabled(True)
            self.cb_radio2.setChecked(True)        

        if self.mb_radio8.isChecked():
            self.N_input.setText("3")
    

    def simulate(self):

        if self.mb_radio1.isChecked():
            self.method = 'adhikari'
        elif self.mb_radio2.isChecked():
            self.method = 'valsa'
        elif self.mb_radio3.isChecked():
            self.method = 'mastuda'
        elif self.mb_radio4.isChecked():
            self.method = 'TheileSecond'
        elif self.mb_radio5.isChecked():
            self.method = 'Oustaloup'
        elif self.mb_radio6.isChecked():
            self.method = 'ModiOustaloup'
        elif self.mb_radio7.isChecked():
            self.method = 'Charef'
        elif self.mb_radio8.isChecked():
            self.method = 'Carlson'

        if self.cb_radio1.isChecked():
            self.circuit = 'None'
        elif self.cb_radio2.isChecked():
            self.circuit = 'FirstFoster'
        elif self.cb_radio3.isChecked():
            self.circuit = 'SecondFoster'
        elif self.cb_radio4.isChecked():
            self.circuit = 'FirstCauer'
        elif self.cb_radio5.isChecked():
            self.circuit = 'SecondCauer'

        self.fl = 10**self.fl_slider.value()
        self.fu = 10**self.fu_slider.value()
        self.fstep = 10**self.fstep_slider.value()

        self.F = float(self.F_input.text())
        self.alpha = float(self.alpha_input.text())
        self.N = int(self.N_input.text())
        
        if (self.fl>self.fu) and ((self.fu-self.fl)%self.fstep!=0) :
            alert = QMessageBox()
            alert.setText('Invalid Input')
            alert.exec_()
        else:
            try:
                if self.circuit == 'None':
                    self.Zmagi,self.Zphai,self.Zmag,self.Zpha,self.magError,self.phaError,self.magAvgError,self.phaAvgError = calculator(self.F,self.alpha,self.fl,self.fu,self.method,self.fstep,self.N)
                else:
                    self.Zmagi,self.Zphai,self.Zmag,self.Zpha,self.magError,self.phaError,self.magAvgError,self.phaAvgError = calculator(self.F,self.alpha,self.fl,self.fu,self.method,self.fstep,self.N,self.circuit)
                self.f = numpy.logspace(numpy.log10(self.fl),numpy.log10(self.fu),((numpy.log10(self.fu / self.fl))*self.fstep) + 1).T
                
                self.updatePlot()

                self.tabs.setCurrentIndex(1) #switch to output tab
            except Exception as e: 
                print(e)
                alert = QMessageBox()
                alert.setText('Simulation Failed. Please try a different configuration.')
                alert.exec_()

    
    def updatePlot(self):
        # create an axis
        ax1 = self.figure.add_subplot(211)
        ax2 = self.figure.add_subplot(212)
        
        if self.gs_radio1.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmagi)         # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zphai)         # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio2.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmag)          # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zpha)          # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio3.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.Zmagi,self.f,self.Zmag) # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB)')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.Zphai,self.f,self.Zpha)# plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase')
        elif self.gs_radio4.isChecked():
            ax1.clear()                             # discards the old graph
            ax1.semilogx(self.f,self.magError)      # plot data
            ax1.set_xlabel('Frequency')
            ax1.set_ylabel('Magnitude(dB) \nNon Relative Error')
            ax2.clear()                             # discards the old graph
            ax2.semilogx(self.f,self.phaError)      # plot data
            ax2.set_xlabel('Frequency')
            ax2.set_ylabel('Phase \nRelative Error')
        ax1.grid()
        ax2.grid()        
        self.canvas.draw()                      # refresh canvas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    clock = Window()
    clock.show()
    sys.exit(app.exec_())