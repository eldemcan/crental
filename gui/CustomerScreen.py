from PyQt4 import QtCore, QtGui
from Vehicles import *
import datetime

'''
This class designed to maintain customer related GUI operations.
'''
class CustomerScreen(QtGui.QMainWindow):
    combo_box_items = ["Car", "Van", "Camper Van"]

    #Class constructor parent represents login screen
    def __init__(self, parent, customer_user, vehicles):
        super(CustomerScreen, self).__init__(parent)
        self.login_button = None
        self.customer_user = customer_user
        self.vehicles = vehicles
        self.setupUi()
        #method below populates user's list view if user has previous bookings
        self.add_vehicles_to_list()
        self.show()

    # initialize GUI elements (this method created with QT designer)
    def setupUi(self):
        self.resize(798, 600)
        self.centralwidget = QtGui.QWidget(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.welcome_label = QtGui.QLabel(self.centralwidget)
        self.horizontalLayout.addWidget(self.welcome_label)
        self.logout_button = QtGui.QPushButton(self.centralwidget)
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.rent_from_date = QtGui.QDateEdit(self.centralwidget)
        self.gridLayout.addWidget(self.rent_from_date, 0, 1, 1, 2)
        self.vehicle_type_comboBox = QtGui.QComboBox(self.centralwidget)

        self.vehicle_type_comboBox.addItems(self.combo_box_items)
        self.gridLayout.addWidget(self.vehicle_type_comboBox, 1, 3, 1, 1)
        self.search_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.search_button, 2, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.rent_to_date = QtGui.QDateEdit(self.centralwidget)
        self.gridLayout.addWidget(self.rent_to_date, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.available_car_list_widget = QtGui.QListWidget(self.centralwidget)

        item = QtGui.QListWidgetItem()
        self.available_car_list_widget.addItem(item)
        self.gridLayout_2.addWidget(self.available_car_list_widget, 1, 0, 2, 1)
        self.quote_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.quote_button, 1, 2, 1, 1)
        self.book_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.book_button, 2, 2, 1, 1)
        self.rental_car_display_info_widget = QtGui.QTextEdit(self.centralwidget)
        self.gridLayout_2.addWidget(self.rental_car_display_info_widget, 1, 1, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.my_vehicle_list_widget = QtGui.QListWidget(self.centralwidget)
        self.gridLayout_3.addWidget(self.my_vehicle_list_widget, 1, 0, 1, 1)
        self.my_vehicle_display_info_widget = QtGui.QTextEdit(self.centralwidget)
        self.gridLayout_3.addWidget(self.my_vehicle_display_info_widget, 1, 1, 1, 1)
        self.cancel_booking_button = QtGui.QPushButton(self.centralwidget)
        self.gridLayout_3.addWidget(self.cancel_booking_button, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.setCentralWidget(self.centralwidget)

        self.setWindowTitle("Customer Window")
        #set username to welcome user
        self.welcome_label.setText("Welcome "+self.customer_user.user_name)
        self.logout_button.setText("Logout")
        self.label_2.setText("Pickup:")
        self.label_4.setText("Vehicle Tyle:")

        self.search_button.setText("Search")
        self.label_3.setText("Drop off:")
        self.label_5.setText("Available Vehicles")
        __sortingEnabled = self.available_car_list_widget.isSortingEnabled()
        self.available_car_list_widget.setSortingEnabled(False)
        self.available_car_list_widget.setSortingEnabled(__sortingEnabled)
        self.quote_button.setText("Quote")
        self.book_button.setText("Book")
        self.label_6.setText("My Vehicles")
        self.cancel_booking_button.setText("Cancel Booking")

        # events (http://pyqt.sourceforge.net/Docs/PyQt4/)
        self.search_button.clicked.connect(self.search_vehicle)
        self.book_button.clicked.connect(self.booking_button_action)
        self.cancel_booking_button.clicked.connect(self.cancel_button_action)
        self.quote_button.clicked.connect(self.quote_button_action)
        self.logout_button.clicked.connect(self.logout_button_action)
        self.available_car_list_widget.itemClicked.connect(self.display_rental_information)
        self.my_vehicle_list_widget.itemClicked.connect(self.display_rented_car_information)

    '''
     code sample for dialog box  taken from http://zetcode.com/gui/pyqt4/firstprograms/
     this method logs user out from the system. basically it loads login screen again while hiding current screen
     '''
    def logout_button_action(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to logout?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.parent().reload()
            self.hide()
    '''
    this method calculates the cost of the vehicle and displays result in message box
    '''
    def quote_button_action(self):
        registration_number = self.get_registration_number_for_rent()
        if registration_number:
            try:
                cost = 0
                from_date = self.rent_from_date.date().toPyDate()
                to_date = self.rent_to_date.date().toPyDate()
                vehicle = self.vehicles[registration_number]
                number_of_days = int((to_date - from_date).days)
                number_of_weeks = int((number_of_days / 7))
                if number_of_weeks > 0:
                    cost = cost + (number_of_weeks * vehicle.cost.weekly_cost)

                    from_date = from_date + datetime.timedelta(days=(number_of_weeks * 7))
                    while from_date <= to_date:
                        if from_date.date.weekday() == 5 or from_date.date.weekday == 6:
                            cost = cost + vehicle.cost.weekend_cost
                        else:
                            cost = cost + vehicle.cost.daily_cost
                        from_date = from_date + datetime.timedelta(days=1)
                else:
                    while from_date <= to_date:
                        if from_date.weekday() == 5 or from_date.weekday() == 6:
                            cost = cost + vehicle.cost.weekend_cost
                        else:
                            cost = cost + vehicle.cost.daily_cost
                        from_date = from_date + datetime.timedelta(days=1)

                QtGui.QMessageBox.information(self, "Information", "Total cost:" + str(cost))
            except ValueError:
                 QtGui.QMessageBox.warning(self, "Warning", "Please enter correct date format")

    '''
    this method cancels customer's booking. Vehicle which customer wants to cancel must be selected from
    the list view widgets
    '''
    def cancel_button_action(self):
        if not self.my_vehicle_list_widget or not self.my_vehicle_list_widget.currentItem().text():
            QtGui.QMessageBox.warning(self, 'Warning', 'Please choose a vehicle for canceling')

        else:
            selected_registration_number = self.my_vehicle_list_widget.currentItem().text()
            self.customer_user.cancel_booking(selected_registration_number)
            '''
            we updated customer dictionary however, we also need to update
            general dictionary vehicles dates for other customers to see availability of vehicles
            '''
            temp_vehicle = self.vehicles[selected_registration_number]
            temp_vehicle.rent_from = datetime.date(datetime.MINYEAR, 1, 1)
            temp_vehicle.rent_to = datetime.date(datetime.MINYEAR, 1, 1)
            temp_vehicle.is_booked = False
            self.reload_my_booking_list_gui()
            QtGui.QMessageBox.information(self, 'Info', 'Cancel operation completed')

    """
    this method reloads my booking list section
    after canceling booking operation
    """

    def reload_my_booking_list_gui(self):
        self.my_vehicle_list_widget.clear()
        self.my_vehicle_display_info_widget.clear()
        # if there is not any vehicle left on customer side there is no need to add item to list widget
        if len(self.customer_user.rented_vehicle.keys()) > 0:
            self.my_vehicle_list_widget.addItems(list(self.customer_user.rented_vehicle.keys()))

    def booking_button_action(self):
        registration_number = self.get_registration_number_for_rent()
        if registration_number:
            self.customer_user.book_car(self.vehicles[registration_number], self.rent_from_date.date().toPyDate(),
                                        self.rent_to_date.date().toPyDate())
            '''
            we updated customer dictionary however, we also need to update
            general dictionary vehicles dates for other customers to see availability of vehicles
            '''
            temp_vehicle = self.vehicles[registration_number]
            temp_vehicle.rent_from = self.rent_from_date.date().toPyDate()
            temp_vehicle.rent_to = self.rent_to_date.date().toPyDate()
            QtGui.QMessageBox.information(self, "Information", "Booking has completed")

            self.my_vehicle_list_widget.clear()
            self.my_vehicle_list_widget.addItems(list(self.customer_user.rented_vehicle.keys()))

    def get_registration_number_for_rent(self):
        if not self.available_car_list_widget.currentItem():
            QtGui.QMessageBox.warning(self, 'Warning', 'Please choose a vehicle from the list')
        else:
            selected_text = self.available_car_list_widget.currentItem().text()
            '''
             we use split because we need to separate between car registration number and make-model because we will
             use registration number as key in dictionary
            '''
            selected_registration_number = selected_text.split("*")[0]
            print('registration number:' + selected_registration_number)
            return selected_registration_number

    #when user clicks an item from the list this method displays detailed information
    def display_rented_car_information(self):
        selected_vehicle = self.vehicles[self.my_vehicle_list_widget.currentItem().text()]
        self.my_vehicle_display_info_widget.clear()
        self.my_vehicle_display_info_widget.setText(selected_vehicle.__str__())
    #when user clicks an item from the list this method displays detailed information.
    def display_rental_information(self):
        selected_vehicle = self.vehicles[self.get_registration_number_for_rent()]
        self.rental_car_display_info_widget.clear()
        self.rental_car_display_info_widget.setText(selected_vehicle.__str__())

    '''
    This method searches available vehicles according to given criteria and lists them in the listview
    '''
    def search_vehicle(self):
        print('Searching vehicle....')
        car_type_string = str(self.vehicle_type_comboBox.currentText())

        # clearing information from previous search
        self.available_car_list_widget.clear()
        self.rental_car_display_info_widget.clear()

        print('Selected vehicle type:' + car_type_string)

        if self.check_valid_date():
            for vehicle in self.vehicles:
                temp_vehicle = self.vehicles[vehicle]
                print(vehicle)
                if temp_vehicle.check_availability(self.rent_from_date.date().toPyDate(),
                                                   self.rent_to_date.date().toPyDate()):
                    if (car_type_string == "Car" and isinstance(temp_vehicle, Car)) or (
                                    car_type_string == "Van" and isinstance(temp_vehicle, Van)) or (
                                    car_type_string == "Camper Van" and isinstance(temp_vehicle, CamperVan)):
                        print('Vehicle found ...')
                        self.available_car_list_widget.addItem(
                            temp_vehicle.registration_number + '*' + temp_vehicle.model + "-" + temp_vehicle.make)

    '''
    this methods checks whether customer enters valid data for rent request
    if requested from date is bigger than to date it will return false
    '''
    def check_valid_date(self):
        if self.rent_from_date.date().toPyDate() > self.rent_to_date.date().toPyDate():
            QtGui.QMessageBox.warning(self, 'Warning', 'Please enter enter valid day range')
            return False
        else:
            return True

    '''
    this method will populate list view whenever customer books a car.
    that list view will indicate list of vehicles that customer has
    '''
    def add_vehicles_to_list(self):
        print('Creating vehicle list for customer....')

        if len(self.customer_user.rented_vehicle) > 0:
            self.my_vehicle_list_widget.clear()
            self.my_vehicle_list_widget.addItems(list(self.customer_user.rented_vehicle.keys()))
