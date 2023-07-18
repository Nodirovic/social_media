from PyQt5.QtWidgets import *
from os import system
system("cls")

class Button(QPushButton):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(text, oyna)
        self.setStyleSheet("""
            Button {
                position: relative;
                background-color: #4CAF50;
                border: none;
                font-size: 20px;
                width: 50px;
                height: 17px;
                padding: 10px;
                color: #FFFFFF;
                text-align: center;
            }
            Button:hover {
                color: black;
            }
            
            Button:pressed {
                color: orange;
                background-color: #7BB626;
            }
        """)


class Template(QWidget):
    def __init__(self, name: str, x: int, y: int):
        super().__init__()
        self.name = name
        self.setWindowTitle(name)

        self.label = QLabel(self)
        self.label.setText("Aziz")
        self.label.move(20, 10)
        self.label.setStyleSheet("""
            color: #3C9DD0;
            font-family: Times New Roman;
            font-size: 30px;
            background-color: #efefef;
        """)
        self.label.adjustSize()

        self.messages = QListWidget(self)
        self.messages.setGeometry(20, 50, 350, 350)

        self.editBtn = Button("Edit", self)
        self.editBtn.move(380, 50)
        self.editBtn.setText("Edit")

        self.clearBtn = Button("Clear", self)
        self.clearBtn.move(380, 100)
        self.clearBtn.setText("Clear")

        self.input = QLineEdit(self)
        self.input.setGeometry(20, 410, 270, 28)
        self.input.setPlaceholderText("Write a message...")

        self.sendBtn = Button("Send", self)
        self.sendBtn.move(300, 410)

        self.setFixedSize(490, 500)
        self.move(x, y)
        self.show()

        self.clearAll = QMessageBox()
        self.clearAll.setText("Ikkala tarafdan ham o'chirilsinmi ?")
        self.clearAll.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    

class Chat:
    def __init__(self, user_1: Template, user_2: Template):
        self.user_1 = user_1
        self.user_2 = user_2

        self.user_1.label.setText(user_2.name)
        self.user_2.label.setText(user_1.name)
        
        self.user_1.label.adjustSize()
        self.user_2.label.adjustSize()

        self.user_1.sendBtn.clicked.connect(lambda: self.sendMessage(user_1, user_2))
        self.user_2.sendBtn.clicked.connect(lambda: self.sendMessage(user_2, user_1))

        self.user_1.editBtn.clicked.connect(lambda: self.editMessage(user_1, user_2))
        self.user_2.editBtn.clicked.connect(lambda: self.editMessage(user_2, user_1))

        self.user_1.clearBtn.clicked.connect(lambda: self.clearMessages(user_1))
        self.user_2.clearBtn.clicked.connect(lambda: self.clearMessages(user_2))

        self.user_1.clearAll.buttonClicked.connect(self.func_1)
        self.user_2.clearAll.buttonClicked.connect(self.func_2)

    def sendMessage(self, from_user: Template, to_user: Template):
        txt = from_user.input.text().strip()

        if txt == "":
            from_user.input.clear()
            return
    
        from_user.messages.addItem(QListWidgetItem(f"You: {txt}"))
        to_user.messages.addItem(QListWidgetItem(f"{from_user.name}: {txt}"))
        
        from_user.input.clear()

    def editMessage(self, from_user: QListWidget, to_user: QListWidget):
        lst = from_user.messages.selectedItems()
        if not lst: return
        for item in lst:
            if item.text().count(to_user.name) > 0: return
            from_user.input.setText(item.text()[5:])
            # print(item)
            
            

    def func_1(self, btn) -> bool:
        txt = btn.text()
        if txt == "OK":
            self.user_2.messages.clear()
        self.user_1.messages.clear()

    def func_2(self, btn) -> bool:
        txt = btn.text()
        if txt == "OK":
            self.user_1.messages.clear()
        self.user_2.messages.clear()

    def clearMessages(self, user: Template):
        user.clearAll.exec_()



app = QApplication([])
user_1 = Template("Aziz", 100, 100)
user_2 = Template("Akbar", 700, 100)

chat = Chat(user_1, user_2)

app.exec_()