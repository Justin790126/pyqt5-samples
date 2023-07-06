
import sys,os
import getopt
import shutil


initVal = {
    "gen_all": False,
    "output_folder": "./",
    "class_name": "Default"
}




def writeModelFile(folder_path, class_name):
    output_path = "{}/{}Model.py".format(folder_path, class_name)
    print(output_path)
    fp = open(output_path, "w")

    # br2_pkg_name = br2_prefix + pkg_name.upper()
    
    fp.write(
        "from PyQt5.QtWidgets import *\n"
        "from PyQt5.QtGui import *\n"
        "from PyQt5.QtCore import *\n"
        "#from utils.db import *\n"
        "########## import DB / utils here ##########\n"
        "\n"
        f"class {class_name}Model(QObject):\n"
        "\n"
        "    ########## #add custom signal here ##########\n"
        "    customSignal = pyqtSignal(tuple)\n"
        "\n"
        "    def __init__(self):\n"
        "        super().__init__()\n"
        "\n"
        "\n"
        "    def query_db(self, queryArgs):\n"
        "        pass\n"
        "\n"
    )
    fp.close()

def writeViewFile(folder_path, class_name):
    output_path = "{}/{}View.py".format(folder_path, class_name)
    print(output_path)
    fp = open(output_path, "w")
    fp.write(
        "import os,sys\n"
        "from PyQt5.QtWidgets import *\n"
        "from PyQt5.QtGui import *\n"
        "from PyQt5.QtCore import *\n"
        "#import style\n"
        "#from PIL import Image\n"
        "#from interface.Widgets import UIinterface\n"
        "########## import utils here ##########\n"
        "\n"
        f"class {class_name}View(QWidget):\n"
        "\n"
        "    ########## #add custom signal here ##########\n"
        "    customSignal = pyqtSignal(tuple)\n"
        "\n"
        "    def __init__(self):\n"
        "        super().__init__()\n"
        "        self.setWindowTitle(\"Window Title here\")\n"
        "        #self.setWindowIcon(QIcon(\"icons/icon.ico\"))\n"
        "        self.setGeometry(450, 150, 350, 550)\n"
        "        self.setFixedSize(self.size())\n"
        "        self.UI()\n"
        "        self.show()\n"
        "\n"
        "\n"
        "    def UI(self):\n"
        "        self.widgets()\n"
        "        self.layouts()\n"
        "\n"
        "    def widgets(self):\n"
        "        pass\n"
        "\n"
        "    def layouts(self):\n"
        "        pass\n"
        "\n"
        "    def closeEvent(self, event):\n"
        "        pass\n"
        "\n"

    )

    fp.close()

def writeCtrllerFile(folder_path, class_name):
    output_path = "{}/{}Ctrller.py".format(folder_path, class_name)
    print(output_path)
    fp = open(output_path, "w")
    fp.write(
        "import os,sys\n"
        "from PyQt5.QtWidgets import *\n"
        "from PyQt5.QtGui import *\n"
        "from PyQt5.QtCore import *\n"
        "#import style\n"
        "#from PIL import Image\n"
        "#from interface.Widgets import UIinterface\n"
        "#from utils.db import *\n"
        f"from {class_name}.{class_name}Model import {class_name}Model\n"
        f"from {class_name}.{class_name}View import {class_name}View\n"
        "\n"
        f"class {class_name}Ctrller():\n"
        "\n"
        "    ########## #add custom signal here ##########\n"
        "    customSignal = pyqtSignal(tuple)\n"
        "\n"
        "    def __init__(self):\n"
        f"        self.model = {class_name}Model()\n"
        f"        self.view = {class_name}View()\n"
        "\n"

    )

    fp.close()


def writeInterfaceFile(folder_path):
    pass
    
def writeMVC(inputVal):
    
    class_name = "{}{}".format(
        inputVal["class_name"][0].upper(), inputVal["class_name"][1:])
    folder_path = "{}/{}".format(inputVal["output_folder"], class_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    


    writeModelFile(folder_path, class_name)
    writeViewFile(folder_path, class_name)
    writeCtrllerFile(folder_path, class_name)






def setInitVal():
    global initVal
    initVal["gen_all"] = False
    initVal["output_folder"] = "./"
  
def main():
    global initVal
    first_name = None
    last_name = None
  
    argv = sys.argv[1:]

  
    try:
        opts,args = getopt.getopt(sys.argv[1:],'hf:c:',['input=','output=','symble=','oddeven=','help'])
        print(args, opts)

      
    except:
        print("Error")
  
    setInitVal()
    print(initVal["gen_all"])
    for opt_name,opt_value in opts:

        ############## default ##############
        

        ############## parse arguments ##############
        if opt_name in ('-h','--help'):
            continue
        if opt_name in ('-f','--folder'):
            initVal["output_folder"] = opt_value
            continue
        if opt_name in ('-c','--classname'):
            initVal["class_name"] = opt_value
            continue




    ######### generate files ######################### 
    writeMVC(initVal)
    
    ############# restore init values #########################
    setInitVal()
  

if __name__ == "__main__":
    main()


# usage:
# python3 mvc_gen.py -f ./productManager/ -c ConfirmWindow