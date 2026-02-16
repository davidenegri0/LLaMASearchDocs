import sys
import requests
import json
from PySide6 import QtCore, QtWidgets, QtGui

#App GUI per progetto LlamaSearchDocs

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("LlamaSearchDocs")
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.textbox = QtWidgets.QTextEdit()
        self.textbox.setFixedHeight(250)
        self.textbox.setMinimumWidth(1250)
        self.textbox.setLineWrapColumnOrWidth(1000)
        self.textbox.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.textbox.setPlaceholderText("Inserisci la tua quary di ricerca qui...")
        self.textbox.setAcceptRichText(False)
        
        self.textbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.textbox, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        self.numLabel = QtWidgets.QLabel("Numero di risultati:")
        
        self.number_selector = QtWidgets.QSpinBox()
        self.number_selector.setMinimum(1)
        self.number_selector.setMaximum(10)
        self.number_selector.setValue(3)
        self.number_selector.setFixedSize(50, 30)
        
        self.button = QtWidgets.QPushButton("Search!")
        self.button.setFixedHeight(50)
        
        numLayout = QtWidgets.QHBoxLayout()
        numLayout.addWidget(self.numLabel, alignment=QtCore.Qt.AlignmentFlag.AlignBaseline | QtCore.Qt.AlignmentFlag.AlignLeft)
        numLayout.addWidget(self.number_selector, alignment=QtCore.Qt.AlignmentFlag.AlignBaseline | QtCore.Qt.AlignmentFlag.AlignLeading)
        numLayout.addWidget(self.button, alignment=QtCore.Qt.AlignmentFlag.AlignBaseline | QtCore.Qt.AlignmentFlag.AlignRight) 
        
        numLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout.addLayout(numLayout)

        results = QtWidgets.QVBoxLayout()
        results.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        self.res_label = QtWidgets.QLabel("Risultati:")
        results.addWidget(self.res_label, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        
        self.textresult = QtWidgets.QTextBrowser()
        #self.textresult.setHidden(True)
        self.textresult.setFixedHeight(300)
        self.textresult.setMinimumWidth(1250)
        results.addWidget(self.textresult, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.layout.addLayout(results)

        self.button.clicked.connect(self.send)

    @QtCore.Slot()
    def send(self):
        to_send = self.textbox.toPlainText().replace(" ", "+")
        self.textbox.setText("")
        knn_num = self.number_selector.value()
        self.button.setDisabled(True)
        try:
            response = requests.get(f"http://10.27.1.219:5000/search?knn_num={knn_num}&document={to_send}")
            res_obj = json.loads(response.text)
            response_text = ""
            for resp in res_obj:
                score = resp["_score"]*100
                authors = resp["_source"]["authors"]
                doi = resp["_source"]["doi"]
                issues = resp["_source"]["issue"]
                keywords = resp["_source"]["keywords"]
                title = resp["_source"]["title"]
                response_text += f"Affinità: {score}%\nTitolo: {title}\nAutore: {authors}\nDOI: {doi}\nCapitoli: {issues}\nParole Chiave: {keywords}\n\n"
            self.textresult.setText(response_text)
        except requests.exceptions.Timeout:
            self.textresult.setText("Timed out")
        self.button.setDisabled(False)
        #self.textresult.setHidden(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.showMaximized()

    sys.exit(app.exec())