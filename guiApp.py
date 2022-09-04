from xml.etree.ElementTree import tostring
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QGroupBox, QRadioButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtCore
from urllib.request import urlopen
import json
import pandas as pd
import random
from skillFinder2 import skillFinder

NUMBER_OF_QUESTIONS = 10

#read JSON file & extract data
file = open("personalityQuestions.json")
data = json.load(file)
df = pd.DataFrame(data["quiz"]).transpose()
print(df)

#load 1 instance of questions & answers at a time from the database
def preload_data(idx):
    #idx parm: selected randomly time and again at function call
    question = df["question"][idx]
    answers = df["answers"][idx]

    #store local values globally
    parameters["question"].append(question)
    parameters["answer1"].append(answers[0])
    parameters["answer2"].append(answers[1])

#dictionary to store local pre-load parameters on a global level
parameters = {
    "question": [],
    "answer1": [],
    "answer2": [],
    "answers": [],
    "index": []
    }

#dictionary to store user data
data = {
    "name": "a",
    "background": "b",
    "job": "c",
    "skill1": "d",
    "skill2": "e",
    "skill3": "f",
    "personalityAnswers": [0]
}

#global dictionary of dynamically changing widgets
widgets = {
    "box": [],
    "logo": [],
    "button": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "message": [],
    "message2": []
}

#initialliza grid layout
grid = QGridLayout()

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()
    for i in reversed(range(grid.count())): 
        grid.itemAt(i).widget().deleteLater()

def clear_parameters():
    #clear the global dictionary of parameters
    for parm in parameters:
        if parameters[parm] != []:
            for i in range(0, len(parameters[parm])):
                parameters[parm].pop()
    #populate with initial index values
    parameters["index"].append(0)
    
    for i in range(0,NUMBER_OF_QUESTIONS):
        parameters["answers"].append(0)

def start_game():
    #start the game, reset all widgets and parameters
    clear_widgets()
    clear_parameters()
    preload_data(parameters["index"][-1])
    print(parameters["index"][-1])
    #display the game frame
    frame5()

def create_buttons(answer, l_margin, r_margin):
    #create identical buttons with custom left & right margins
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        #setting variable margins
        "*{margin-left: " + str(l_margin) +"px;"+
        "margin-right: " + str(r_margin) +"px;"+
        '''
        border: 4px solid '#BC006C';
        color: white;
        font-family: 'shanti';
        font-size: 16px;
        border-radius: 25px;
        padding: 15px 0;
        margin-top: 20px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    button.clicked.connect(lambda x: store_answers(button))
    return button

def store_answers(btn):
    #a function to store users answers
    if btn.text() == parameters["answer1"][-1]:
        parameters["answers"][parameters["index"][-1]]=1
    else:
        parameters["answers"][parameters["index"][-1]]=2

    #print(parameters)

    #select a new random index and replace the old one
    parameters["index"][-1] = parameters["index"][-1] + 1
    if parameters["index"][-1] < NUMBER_OF_QUESTIONS:
        #preload data for new index value
        preload_data(parameters["index"][-1])
        #update the text of all widgets with new data
        widgets["question"][0].setText(parameters["question"][-1])
        widgets["answer1"][0].setText(parameters["answer1"][-1])
        widgets["answer2"][0].setText(parameters["answer2"][-1])
    else:
        #call next frame
        frame3()

#*********************************************
#                  FRAME 1
#*********************************************

def frame1():
    clear_widgets()
    #logo widget
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button callback
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    #place global widgets on the grid
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

#*********************************************
#                  FRAME 5
#*********************************************

def frame5():

    grid.methodBox = QGroupBox("Previous Qualifications")

    grid.methodBox.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 15px;
        color: 'white';
        padding: 20px;
        '''
    )

    grid.mb_radio1 = QRadioButton("Electronics")
    grid.mb_radio2 = QRadioButton("Mechanical")
    grid.mb_radio3 = QRadioButton("Computer")
    grid.mb_radio4 = QRadioButton("Biomedical")
    grid.mb_radio5 = QRadioButton("Architecture")
    grid.mb_radio6 = QRadioButton("Industrial")
    grid.mb_radio7 = QRadioButton("Aerospace")
    grid.mb_radio8 = QRadioButton("Civil")

    grid.mb_radio1.setChecked(True)

    grid.vbox = QVBoxLayout()
    grid.vbox.addWidget(grid.mb_radio1)
    grid.vbox.addWidget(grid.mb_radio2)
    grid.vbox.addWidget(grid.mb_radio3)
    grid.vbox.addWidget(grid.mb_radio4)
    grid.vbox.addWidget(grid.mb_radio5)
    grid.vbox.addWidget(grid.mb_radio6)
    grid.vbox.addWidget(grid.mb_radio7)
    grid.vbox.addWidget(grid.mb_radio8)
    grid.vbox.addStretch(1)

    grid.methodBox.setLayout(grid.vbox)

    widgets["box"].append(grid.methodBox)
    grid.addWidget(grid.methodBox, 0, 0)


    grid.inputBox = QGroupBox("Input Parameters")

    grid.inputBox.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 15px;
        color: 'white';
        padding: 20px;
        '''
    )

    grid.vbox = QVBoxLayout()

    grid.hbox = QHBoxLayout()
    grid.Name_label = QLabel("Name")
    grid.Name_input = QLineEdit("1")
    grid.hbox.addWidget(grid.Name_label)
    grid.hbox.addWidget(grid.Name_input)
    grid.vbox.addLayout(grid.hbox)

    grid.hbox = QHBoxLayout()
    grid.job_label = QLabel("Job Title")
    grid.job_input = QLineEdit("1")
    grid.hbox.addWidget(grid.job_label)
    grid.hbox.addWidget(grid.job_input)
    grid.vbox.addLayout(grid.hbox)

    grid.hbox = QHBoxLayout()
    grid.skill1_label = QLabel("Skill1")
    grid.skill1_input = QLineEdit("1")
    grid.hbox.addWidget(grid.skill1_label)
    grid.hbox.addWidget(grid.skill1_input)
    grid.vbox.addLayout(grid.hbox)

    grid.hbox = QHBoxLayout()
    grid.skill2_label = QLabel("Skill2")
    grid.skill2_input = QLineEdit("1")
    grid.hbox.addWidget(grid.skill2_label)
    grid.hbox.addWidget(grid.skill2_input)
    grid.vbox.addLayout(grid.hbox)

    grid.hbox = QHBoxLayout()
    grid.skill3_label = QLabel("Skill3")
    grid.skill3_input = QLineEdit("1")
    grid.hbox.addWidget(grid.skill3_label)
    grid.hbox.addWidget(grid.skill3_input)
    grid.vbox.addLayout(grid.hbox)

    grid.inputBox.setLayout(grid.vbox)

    widgets["box"].append(grid.inputBox)
    grid.addWidget(grid.inputBox, 0, 1)

    #button widget
    button = QPushButton("NEXT")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        '''
        *{
            border: 4px solid '#BC006C';
            border-radius: 45px;
            font-size: 35px;
            color: 'white';
            padding: 25px 0;
            margin: 100px 200px;
        }
        *:hover{
            background: '#BC006C';
        }
        '''
    )
    #button calls next frame
    button.clicked.connect(store_data)
    widgets["button"].append(button)

    #place button widgets on the grid
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)

def store_data():
    data["name"] = grid.Name_input.text()
    data["job"] = grid.job_input.text()
    data["skill1"] = grid.skill1_input.text()
    data["skill2"] = grid.skill2_input.text()
    data["skill3"] = grid.skill3_input.text()

    if grid.mb_radio1.isChecked():
        data["background"] = "Electronics"
    elif grid.mb_radio2.isChecked():
        data["background"] = "Mechanical"
    elif grid.mb_radio3.isChecked():
        data["background"] = "Computer"
    elif grid.mb_radio3.isChecked():
        data["background"] = "Biomedical"
    elif grid.mb_radio3.isChecked():
        data["background"] = "Architecture"
    elif grid.mb_radio3.isChecked():
        data["background"] = "Industrial"
    elif grid.mb_radio3.isChecked():
        data["background"] = "Aerospace"
    else:
        data["background"] = "Civil"

    data["personalityAnswers"] = parameters["answers"]

    print(data)
    frame2()
#*********************************************
#                  FRAME 2
#*********************************************

def frame2():
    clear_widgets()
    #question widget
    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        '''
        font-family: 'shanti';
        font-size: 25px;
        color: 'white';
        padding: 75px;
        '''
    )
    widgets["question"].append(question)

    #answer button widgets
    button1 = create_buttons(parameters["answer1"][-1], 85, 5)
    button2 = create_buttons(parameters["answer2"][-1], 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)

    #logo widget
    image = QPixmap("logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 75px; margin-bottom: 30px;")
    widgets["logo"].append(logo)

    #place widget on the grid
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["logo"][-1], 4, 0, 1,2)

#*********************************************
#             FRAME 3 - WIN GAME
#*********************************************

def frame3():
    clear_widgets()
    skills = skillFinder(data["background"], data["job"])
    print(skills)
    #skills display
    message = QLabel("Skills required are ".join(skills))
    message.setAlignment(QtCore.Qt.AlignCenter)
    message.setStyleSheet(
        "font-family: 'Shanti'; font-size: 30px; color: 'white'; margin-top:0px; margin-bottom:75px;"
        )
    widgets["message"].append(message)

    #restart widget
    message2 = QLabel("Would you like to try again?")
    message2.setAlignment(QtCore.Qt.AlignCenter)
    message2.setStyleSheet(
        "font-family: 'Shanti'; font-size: 30px; color: 'white'; margin-top:0px; margin-bottom:75px;"
        )
    widgets["message2"].append(message2)

    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        "*{background:'#BC006C'; padding:25px 0px; border: 1px solid '#BC006C'; color: 'white'; font-family: 'Arial'; font-size: 25px; border-radius: 40px; margin: 10px 300px;} *:hover{background:'#ff1b9e';}"
        )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    #logo widget
    pixmap = QPixmap('logo_bottom.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px; margin-bottom: 20px;"
    )
    widgets["logo"].append(logo)

    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 5, 0, 2, 2)


#*********************************************
#                  FRAME 4 - FAIL
#*********************************************
def frame4():

    #button widget
    button = QPushButton('TRY AGAIN')
    button.setStyleSheet(
        '''*{
            padding: 25px 0px;
            background: '#BC006C';
            color: 'white';
            font-family: 'Arial';
            font-size: 35px;
            border-radius: 40px;
            margin: 10px 200px;
        }
        *:hover{
            background: '#ff1b9e';
        }'''
        )
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.clicked.connect(frame1)

    widgets["button"].append(button)

    #logo widget
    pixmap = QPixmap('logo_bottom.png')
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "padding :10px; margin-top:75px;"
    )
    widgets["logo"].append(logo)

    #place widgets on the grid
    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 3, 0, 1, 2)
