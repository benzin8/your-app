from ui.window import Ui_MainWindow,QMainWindow,QApplication
from PySide6.QtCore import QThread, Signal
import sys
from core.nettest import net_test
from core.disktest import disk_test
from core.hardwaretest import hardware_test

class Threads(QThread):
    update_signal = Signal(str) 
    def __init__(self, task):
        super().__init__()
        self.task = task
    
    def run(self):
        result = self.task()
        self.update_signal.emit(result)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connect()
#Подключение кнопок
    def setup_connect(self):
        self.net_btn.clicked.connect(self.run_net_test)
        self.disk_btn.clicked.connect(self.run_disk_test)
        self.cpu_btn.clicked.connect(self.run_hardware_test)

#Потоки    
    def run_net_test(self):
        self.worker = Threads(net_test)
        self.worker.update_signal.connect(self.update_result)
        self.worker.start()

    def run_disk_test(self):
        self.worker = Threads(disk_test)
        self.worker.update_signal.connect(self.update_result)
        self.worker.start()

    def run_hardware_test(self):
        self.worker = Threads(hardware_test)
        self.worker.update_signal.connect(self.update_result)
        self.worker.start()

#Добавление текста    
    def update_result(self, text):
        self.textEdit.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
