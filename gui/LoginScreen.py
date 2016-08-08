from PyQt4 import QtCore, QtGui
from Users import *
from gui.CustomerScreen import *
from gui.StaffScreen import *

'''
This class  is used for authentication purposes. It redirects users relevant screens according to account type
'''


class LoginScreen(QtGui.QMainWindow):
    def __init__(self, user_list, vehicles):
        super(LoginScreen, self).__init__()
        self.username_string = None
        self.password_string = None
        self.login_button = None
        self.user_list = user_list
        self.vehicles = vehicles
        self.setupUi()
        self.show()

    # initialize GUI elements (this method created with QT designer)
    def setupUi(self):
        self.resize(251, 139)
        self.centralwidget = QtGui.QWidget(self)
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(3)
        self.username_text = QtGui.QLabel(self.centralwidget)
        self.gridLayout_2.addWidget(self.username_text, 0, 0, 1, 2)
        self.username_field = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout_2.addWidget(self.username_field, 0, 2, 1, 1)
        self.password_text = QtGui.QLabel(self.centralwidget)
        self.gridLayout_2.addWidget(self.password_text, 1, 0, 1, 1)
        self.password_field = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout_2.addWidget(self.password_field, 1, 2, 1, 1)
        self.login_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.login_button, 2, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Login")
        self.username_text.setText("Username:")
        self.password_text.setText("Password:")
        self.login_button.setText("Login")
        self.login_button.clicked.connect(self.login_button_action)

    # when user clicks logout from other screens this method will be called
    def reload(self):
        # clearing username and password field otherwise we will see our login info
        self.username_field.clear()
        self.password_field.clear()
        self.show()

    def login_button_action(self):
        is_authenticated = self.authenticate()

        if is_authenticated == False:
            QtGui.QMessageBox.warning(self, "Warning", "Please enter correct username and password")

    '''
    this method authenticate user and redirects accordingly
    i.e if user is type of Customer, Customer screen will be loaded
    otherwise Staff screen will be loaded. If method works successfully it returns
    True otherwise it will return False
    '''

    def authenticate(self):
        print('authenticating...')
        string_username = self.username_field.text().strip()
        string_password = self.password_field.text().strip()

        if self.validate_authentication_input(string_username, string_password):
            for user in self.user_list:
                if user.user_name == string_username and user.password == string_password:
                    print('authentication OK...')
                    if isinstance(user, Staff):
                        print('welcome Staff...')
                        StaffScreen(self, user, self.vehicles)
                        self.hide()
                        return True
                    elif isinstance(user, Customer):
                        print('welcome Customer...')
                        CustomerScreen(self, user, self.vehicles)
                        self.hide()
                        return True
        return False

    def validate_authentication_input(self, string_username, string_password):
        if len(string_username) == 0 or len(string_password) == 0:
            QtGui.QMessageBox.warning(self, 'Warning', 'Please enter a username or password')
            return False
        else:
            print('input OK...')
            return True
