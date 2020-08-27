from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
from open_link import open_link
from chech_time import check_time


class DistanceLearning(QMainWindow):
    def __init__(self):
        super(DistanceLearning, self).__init__()
        loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.start)
        self.show()

    @pyqtSlot()
    def start(self):
        dict = {self.firstLink.text(): self.time1_2.text(),
                self.secondLink.text(): self.time2.text(),
                self.thirdLink.text(): self.time3.text(),
                self.fourthLink.text(): self.time4.text(),
                self.fifthLink.text(): self.time5.text(),
                self.sixLink.text(): self.time6.text(),
                self.sevenLink.text(): self.time7.text()}
        print(dict)
        for i in dict:
            try:
                open_link(i)
            except:
                del dict[i]
        while dict:
            for link in dict:
                if link != 'None':
                    if check_time(dict[link]):
                        print('ok')
                        open_link(link)
                        del dict[link]

        # self.Result.setText(str(get_page(search)))


app = QApplication(sys.argv)
window = DistanceLearning()
try:
    sys.exit(app.exec_())
except:
    print('exit')
