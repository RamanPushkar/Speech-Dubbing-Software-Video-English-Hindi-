# importing libraries
import shutil
from PyQt5.QtWidgets import QMessageBox
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMenu, QPushButton
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QToolBar
from Main_SDSoftware import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


#__________________________________________________________________________________
class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Speech Dubbing Software")
        self.resize(500, 350)
        self.setMinimumWidth(500)
        self.setMinimumHeight(350)
        self.centralWidget = QLabel("Welcome to Speech Dubbing")
        self.centralWidget.setAlignment(Qt.AlignBottom)
        self.setCentralWidget(self.centralWidget)



# function for dashboard

#///////////////////////////////////////////////////////////////////////////////////


#________call_method_for_ui________________________________________________________
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._createContextMenu()
        #self._connectActions()
        self._createStatusBar()
        self.crete_dashboard()
#///////////////////////////////////////////////////////////////////////////////////////


    def crete_dashboard(self):


        widget = QLabel("Convert [.MP4_english-.MP4_hindi]")
        font = widget.font()
        font.setPointSize(15)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignTop|Qt.AlignHCenter)
        self.setCentralWidget(widget)



        chooseButton= QPushButton('Choose File', self)
        chooseButton.resize(100, 32)
        chooseButton.move(100, 100)
        chooseButton.clicked.connect(self.chooseFile_)




        saveButton = QPushButton('Save', self)
        saveButton.resize(100, 32)
        saveButton.move(100, 200)
        saveButton.clicked.connect(self.saveFile_)

        quitButton = QPushButton('Quit', self)
        quitButton.resize(60, 25)
        quitButton.move(420, 280)

        quitButton.clicked.connect(self.quiteApp)

    def quiteApp(self):
        userInfo = QMessageBox.question(self, "Conformation", "Do you want the exit the Application",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            app.quit()
        elif userInfo == QMessageBox.No:
            pass
    def chooseFile_(self):
        mainSDS()# calling mainSDS file for converting





    def saveFile_(self):
        userInfo = QMessageBox.question(self, "Conformation", "Your file Converted.mp4 is Save at DEFAULT LOCATION(D:\Speech Dubbing)!",
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            original = r'F:\work\Major Project\Converted.mp4'
            target = 'D:\Speech Dubbing'
            shutil.move(original, target)
            print("Saving file at the desire location is SUCCESSFULLY done.")

        elif userInfo == QMessageBox.No:
            pass


    #________createToolBars____________________________________________________________________
    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(True)#fix tool
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Using a QToolBar object
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        # Using a QToolBar object and a toolbar area
        helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)
        # Adding a widget to the Edit toolbar
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)


#__________createMenuBar_________________________________________________________________________________
    def _createMenuBar(self):
        menuBar = self.menuBar()

        # File menu
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        # Adding an Open Recent submenu
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
        fileMenu.addAction(self.saveAction)
        # Adding a separator
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        # Edit menu
        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        # Adding a separator
        editMenu.addSeparator()
        # Find and Replace submenu in the Edit menu
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")
        # Help menu
        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)
#////////////////////////////////////////////////////////////////////////////////////////////////////////


#___________createActions________________________________________________________________________________
    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":Framework/file-new_.svg"))
        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"), "&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        # Adding help tips
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#________createContextMenu____________________________________________________________________________________________________
    def _createContextMenu(self):
        # Setting contextMenuPolicy
        self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        # Populating the widget with actions
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        self.centralWidget.addAction(self.cutAction)
#//////////////////////////////////////////////////////////////////////////////////////////////////////


#________createContextMenu_____________________________________________________________________________
    def contextMenuEvent(self, event):
        # Creating a menu object with the central widget as parent
        menu = QMenu(self.centralWidget)
        # Populating the menu with actions
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        # Creating a separator action
        separator = QAction(self)
        separator.setSeparator(True)
        # Adding the separator to the menu
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        # Launching the menu
        menu.exec(event.globalPos())
#///////////////////////////////////////////////////////////////////////////////////////////////////////


#_______newFile_________________________________________________________________________________________
    def newFile(self):

     self.centralWidget.setText("<b>File > New</b> clicked")


    #////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______openFile________________________________________________________________________________________________
    def openFile(self):
        # Logic for opening an existing file goes here...
        self.centralWidget.setText("<b>File > Open...</b> clicked")

#////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______saveFile_________________________________________________________________________________________________
    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////


 #______copyContent__________________________________________________________________________________________________
    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______pasteContent____________________________________________________________________________________________
    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Paste</b> clicked")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______cutContent________________________________________________________________________________________________
    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______helpContent________________________________________________________________________________________________
    def helpContent(self):
        # Logic for launching help goes here...
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_________about_______________________________________________________________________________________________________
    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#________connectActions____________________________________________________________________________________________________











#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#______populateOpenRecent___________________________________________________________________________________________
    def populateOpenRecent(self):
        # Step 1. Remove the old options from the menu
        self.openRecentMenu.clear()
        # Step 2. Dynamically create the actions
        actions = []
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)
        # Step 3. Add the actions to the menu
        self.openRecentMenu.addActions(actions)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



#________openRecentFile______________________________________________________________________________________
    def openRecentFile(self, filename):
        # Logic for opening a recent file goes here...
        self.centralWidget.setText(f"<b>{filename}</b> opened")
#////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______getWordCount_________________________________________________________________________________________
    def getWordCount(self):
        # Logic for computing the word count goes here...
        return 1.0
#////////////////////////////////////////////////////////////////////////////////////////////////////////////


#_______createStatusBar______________________________________________________________________________________-
    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusbar.showMessage("Ready", 3000)
        # Adding a permanent message
        self.wcLabel = QLabel(f"{self.getWordCount()} Version")
        self.statusbar.addPermanentWidget(self.wcLabel)
#////////////////////////////////////////////////////////////////////////////////////////////////////////


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
#@@@@@@@@____END___@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@