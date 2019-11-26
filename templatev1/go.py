from PyQt5.QtWidgets import QAction, QDesktopWidget, QMainWindow
from PyQt5.QtCore import Qt
from board import Board
from score_board import ScoreBoard
from PyQt5.QtGui import QIcon

class Go(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    
        #Adding Status menu
        self.statusBar().showMessage("Go Board Game.")

        
        # Adding main menu
        mainMenu = self.menuBar()
        menu = mainMenu.addMenu("Menu")
        helpMenu = mainMenu.addMenu("Help")

        # Adding icons to menu
        newGame = QAction(QIcon("./icons/new_game2.png"),"New Game",self)
        quit = QAction(QIcon("./icons/exit.png"), "Quit",self)
        about = QAction(QIcon("./icons/about_us.png"),"About us",self)
        rules = QAction(QIcon("./icons/rules.png"),"Rules",self)
        
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
        quit.triggered.connect(self.close_game)
        about.triggered.connect(self.about)
        rules.triggered.connect(self.rules)

        # Adding buttons to 'Menu'
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
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

    def new_game(self):
        pass
    
    def close_game(self):
        self.close()

    def about(self):
        pass

    def rules(self):
        pass