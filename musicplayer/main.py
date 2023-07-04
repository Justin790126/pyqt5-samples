import sys
from PyQt5.QtWidgets import *
from PlayerCtrller import PlayerCtrller

def main():
    App = QApplication(sys.argv)
    window = PlayerCtrller()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()