from PyQt5.QtWidgets import QAction, QDesktopWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from board import Board
from score_board import ScoreBoard
from PyQt5.QtGui import QIcon


class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        # Adding title,icon, position and size for MainWindow
        self.setWindowTitle("Go BoardGame_Project")
        self.setWindowIcon(QIcon("./icons/app_icon.png"))
        self.center()
        self.resize(800,800)

        # Adding Status menu
        self.statusBar().showMessage("Go Board Game.")

        # Adding main menu
        mainMenu = self.menuBar()
        menu = mainMenu.addMenu("Menu")
        helpMenu = mainMenu.addMenu("Help")

        # Adding icons to menu
        newGame = QAction(QIcon("./icons/new_game2.png"), "New Game", self)
        quit = QAction(QIcon("./icons/exit.png"), "Quit", self)
        about = QAction(QIcon("./icons/about_us.png"), "About us", self)
        rules = QAction(QIcon("./icons/rules.png"), "Rules", self)

        # Setting shortcuts for buttons
        newGame.setShortcut("Ctrl+N")
        quit.setShortcut("Ctrl+Q")
        rules.setShortcut("Ctrl+H")

        # Setting instructions to user
        newGame.setStatusTip("Start a New Game.")
        quit.setStatusTip("Exit application.")
        about.setStatusTip("Meet our project group.")
        rules.setStatusTip("Basic rules for Go board game.")

        # Connecting buttons to methods
        newGame.triggered.connect(self.new_game)
        quit.triggered.connect(self.close)
        about.triggered.connect(self.about)
        rules.triggered.connect(self.rules)

        # Adding buttons to top menu
        menu.addAction(newGame)
        menu.addAction(quit)
        helpMenu.addAction(rules)
        helpMenu.addAction(about)

    def getBoard(self):
        return self.board

    def getScoreBoard(self):
        return self.scoreBoard

    def initUI(self):
        '''initiates application UI'''
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.scoreBoard = ScoreBoard()
        self.addDockWidget(Qt.RightDockWidgetArea, self.scoreBoard)
        self.scoreBoard.make_connection(self.board)

        self.resize(800, 800)
        self.center()
        self.setWindowTitle('Go')
        self.show()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def new_game(self):
        pass

    def closeEvent(self,event):
        # Printing exit event message to user
        message = QMessageBox.question(self, 'Exit', 'Do you really want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        # Dealing with user's choice
        if message == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def about(self):
        # Setting the about_us box message
        # Adding tittle, text and displaying icon
        msg = QMessageBox()
        msg.setWindowTitle("About us")
        msg.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vulputate turpis suscipit arcu vulputate, at rhoncus purus malesuada. ")
        msg.setIcon(QMessageBox.Information)
        x= msg.exec_()
        
    def rules(self):
        message = QMessageBox()
        message.setText("")

