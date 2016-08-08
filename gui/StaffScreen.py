from PyQt4 import QtCore, QtGui
from Vehicles import *


class StaffScreen(QtGui.QMainWindow):
    combo_box_items = ["Car", "Van", "Camper Van"]

    # Class constructor parent represents login screen
    def __init__(self, parent, staff_user, vehicles):
        super(StaffScreen, self).__init__(parent)
        self.staff_user = staff_user
        self.vehicles = vehicles
        self.setupUi()
        self.load_vehicles_to_list()
        self.show()

    '''
    this method loads available vehicles into list so that staff user can
    make operations such as delete,update on the vehicle
    '''

    def load_vehicles_to_list(self):
        self.available_cars_list_widget.clear()

        for key in self.vehicles:
            self.available_cars_list_widget.addItem(str(key))

    # initialize GUI elements (this method created with QT designer)
    def setupUi(self):
        self.resize(608, 494)
        self.centralwidget = QtGui.QWidget(self)
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.welcome_label = QtGui.QLabel(self.centralwidget)
        self.horizontalLayout.addWidget(self.welcome_label)
        self.company_name_label = QtGui.QLabel(self.centralwidget)
        self.horizontalLayout.addWidget(self.company_name_label)
        self.logout_button = QtGui.QPushButton(self.centralwidget)
        self.horizontalLayout.addWidget(self.logout_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.available_cars_list_widget = QtGui.QListWidget(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.available_cars_list_widget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.verticalLayout.addWidget(self.label_12)
        self.type_list_widget = QtGui.QListWidget(self.centralwidget)
        self.type_list_widget.setEnabled(True)
        self.verticalLayout.addWidget(self.type_list_widget)
        self.gridLayout = QtGui.QGridLayout()
        self.daily_cost_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.daily_cost_text_box, 4, 1, 1, 1)
        self.weekend_cost_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.weekend_cost_text_box, 6, 1, 1, 1)
        self.number_of_doors_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.number_of_doors_text_box, 9, 1, 1, 1)
        self.number_of_passenger_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.number_of_passenger_text_box, 8, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.number_of_bed_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.number_of_bed_text_box, 7, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.weekly_cost_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.weekly_cost_text_box, 5, 1, 1, 1)
        self.fuel_consumption_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.fuel_consumption_text_box, 3, 1, 1, 1)
        self.model_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.model_text_box, 2, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.registration_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.registration_text_box, 0, 1, 1, 1)
        self.make_text_box = QtGui.QLineEdit(self.centralwidget)
        self.gridLayout.addWidget(self.make_text_box, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.delete_button = QtGui.QPushButton(self.centralwidget)
        self.horizontalLayout_3.addWidget(self.delete_button)
        self.insert_button = QtGui.QPushButton(self.centralwidget)
        self.horizontalLayout_3.addWidget(self.insert_button)
        self.update_button = QtGui.QPushButton(self.centralwidget)
        self.horizontalLayout_3.addWidget(self.update_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.welcome_label.raise_()
        self.logout_button.raise_()
        self.company_name_label.raise_()
        self.available_cars_list_widget.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.delete_button.raise_()
        self.update_button.raise_()
        self.insert_button.raise_()
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Staff Screen")

        self.welcome_label.setText("Welcome:" + self.staff_user.user_name)
        self.company_name_label.setText("Company:" + self.staff_user.company.company_name)

        self.logout_button.setText("Logout")
        self.label_14.setText("Registration Number:")
        self.label_12.setText("Type:")
        self.label_3.setText("Make:")
        self.label_7.setText("Weekly Cost:")
        self.label_6.setText("Daily Cost:")
        self.label_4.setText("Model:")
        self.label_11.setText("Number of Doors:")
        self.label_5.setText("Fuel Consumption:")
        self.label_10.setText("Number of Passenger:")
        self.label_8.setText("Weekend Cost:")
        self.label_9.setText("Number of Bed:")
        self.delete_button.setText("Delete ")
        self.insert_button.setText("Insert")
        self.update_button.setText("Update")
        self.type_list_widget.addItems(self.combo_box_items)

        # adding events to buttons and lists
        self.available_cars_list_widget.itemClicked.connect(self.display_vehicle_info)
        self.logout_button.clicked.connect(self.logout_button_action)
        self.delete_button.clicked.connect(self.delete_button_action)
        self.update_button.clicked.connect(self.update_button_action)
        self.insert_button.clicked.connect(self.insert_button_action)

    def insert_button_action(self):
        if not self.type_list_widget.currentItem():
            QtGui.QMessageBox.warning(self, "Warning", "Please choose a vehicle type from the list")
        else:
            vehicle_type = self.type_list_widget.currentItem().text()
            vehicle = None
            if self.validate_essential_fields(vehicle_type):
                if vehicle_type == "Car":
                    try:
                        vehicle = Car(self.make_text_box.text().strip(), self.model_text_box.text().strip(),
                                      int(self.fuel_consumption_text_box.text().strip()),
                                      self.registration_text_box.text().strip(),
                                      int(self.number_of_passenger_text_box.text().strip()),
                                      int(self.number_of_passenger_text_box.text().strip()),
                                      int(self.daily_cost_text_box.text().strip()),
                                      int(self.weekly_cost_text_box.text().strip()),
                                      int(self.weekend_cost_text_box.text().strip()))
                    except ValueError:
                        QtGui.QMessageBox.warning(self, "Warning",
                                                  "Vehicle could not created make sure you have correct format of data")
                elif vehicle_type:
                    try:
                        vehicle = Van(self.make_text_box.text(), self.model_text_box.text().strip(),
                                      int(self.fuel_consumption_text_box.text().strip()),
                                      self.registration_text_box.text().strip(),
                                      int(self.number_of_passenger_text_box.text().strip()),
                                      int(self.daily_cost_text_box.text().strip()),
                                      int(self.weekly_cost_text_box.text().strip()),
                                      int(self.weekend_cost_text_box.text().strip()))
                    except ValueError:
                        QtGui.QMessageBox.warning(self, "Warning",
                                                  "Vehicle could not created make sure you have correct format of data")

                elif vehicle_type == "Camper Van":
                    try:
                        vehicle = CamperVan(self.make_text_box.text().strip(), self.model_text_box.text().strip(),
                                            int(self.fuel_consumption_text_box.text().strip()),
                                            int(self.number_of_bed_text_box.text().strip()),
                                            self.registration_text_box.text().strip(),
                                            int(self.daily_cost_text_box.text().strip()),
                                            int(self.weekly_cost_text_box.text().strip()),
                                            int(self.weekend_cost_text_box.text().strip()))
                    except ValueError:
                        QtGui.QMessageBox.warning(self, "Warning",
                                                  "Vehicle could not created make sure you have correct format of data")

            if vehicle is not None and self.staff_user.insert_vehicle(vehicle):
                QtGui.QMessageBox.information(self, "Information", "Vehicle has inserted")
                self.clear_all_text_fields()
                self.load_vehicles_to_list()
            else:
                QtGui.QMessageBox.warning(self, "Warning",
                                          "This registration number is exist please update the vehicle")

    '''
    this method deletes selected evehicle from the dictionary if it has not booked
    '''

    def delete_button_action(self):
        if not self.available_cars_list_widget.currentItem().text():
            QtGui.QMessageBox.warning(self, "Warning", "Please choose a vehicle from the list")
        else:
            registration_number = self.available_cars_list_widget.currentItem().text()
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               "Are you sure to you want to delete " + registration_number + " ?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                if self.staff_user.delete_vehicle(registration_number):
                    self.clear_all_text_fields()
                    self.load_vehicles_to_list()
                    QtGui.QMessageBox.information(self, "Information", "vehicle deleted")
                else:
                    QtGui.QMessageBox.warning(self, "Warning",
                                              "Vehicle has booking request please try to update entity")

    '''
    This method checks whether necessary fields are empty or not. Extra fields to be checked depends
    on the param parameter. i.e regardless of type this method checks whether model of vehicle has entered. However, if param equals to 'Car'
    it will check number of passenger and number of doors
    '''

    def validate_essential_fields(self, param):
        if not self.make_text_box.text() or not self.model_text_box.text() or not self.fuel_consumption_text_box.text() or \
                not self.daily_cost_text_box.text() or not self.weekly_cost_text_box.text() or not self.weekend_cost_text_box.text() or \
                        len(self.make_text_box.text().strip()) == 0 or len(
            self.model_text_box.text().strip()) == 0 or len(
            self.fuel_consumption_text_box.text().strip()) == 0 or \
                        len(self.daily_cost_text_box.text().strip()) == 0 or len(
            self.weekly_cost_text_box.text().strip()) == 0 or len(
            self.weekend_cost_text_box.text().strip()) == 0:
            return False
        elif param.lower() == "Car":
            if not self.number_of_passenger_text_box.text() or not self.number_of_doors_text_box.text() or len(
                    self.number_of_passenger_text_box.text().strip()) == 0 or len(
                        self.number_of_doors_text_box.text().strip() == 0):
                return False
        elif param.lower() == "Camper Van":
            if not self.number_of_bed_text_box.text() or len(self.number_of_bed_text_box.text().strip()) == 0:
                return False
        else:
            return True

    '''
    this method will update selected vehicle from the list
    '''

    def update_button_action(self):
        if not self.available_cars_list_widget.currentItem() or (self.type_list_widget.currentItem() is None):
            QtGui.QMessageBox.warning(self, "Warning", "Please choose a vehicle from the list")
        else:
            registration_number = self.available_cars_list_widget.currentItem().text().strip()
            vehicle = self.vehicles[registration_number]
            vehicle_type = self.type_list_widget.currentItem().text()
            if self.validate_essential_fields(vehicle_type):
                updated_vehicle = None
                if isinstance(vehicle, Car):
                    try:
                        updated_vehicle = Car(self.make_text_box.text().strip(), self.model_text_box.text().strip(),
                                              int(self.fuel_consumption_text_box.text().strip()), registration_number,
                                              int(self.number_of_passenger_text_box.text().strip()),
                                              int(self.number_of_doors_text_box.text().strip()),
                                              int(self.daily_cost_text_box.text().strip()),
                                              int(self.weekly_cost_text_box.text().strip()),
                                              int(self.weekend_cost_text_box.text().strip()))
                    except ValueError:
                        QtGui.QMessageBox.warning(self, "Warning",
                                                  "Vehicle could not created make sure you have correct format of data")

                elif isinstance(vehicle, Van):
                    try:
                        updated_vehicle = Van(self.make_text_box.text(), self.model_text_box.text().strip(),
                                              int(self.fuel_consumption_text_box.text().strip()), registration_number,
                                              int(self.number_of_passenger_text_box.text().strip()),
                                              int(self.daily_cost_text_box.text().strip()),
                                              int(self.weekly_cost_text_box.text().strip()),
                                              int(self.weekend_cost_text_box.text().strip()))
                    except ValueError:
                        QtGui.QMessageBox.warning(self, "Warning",
                                                  "Vehicle could not created make sure you have correct format of data")

            elif isinstance(vehicle, CamperVan):
                try:
                    updated_vehicle = CamperVan(self.make_text_box.text().strip(),
                                                self.model_text_box.text().strip(),
                                                int(self.fuel_consumption_text_box.text().strip()),
                                                int(self.number_of_bed_text_box.text().strip(), registration_number,
                                                    int(self.daily_cost_text_box.text().strip()),
                                                    int(self.weekly_cost_text_box.text().strip()),
                                                    int(self.weekend_cost_text_box.text().strip())))
                except ValueError:
                    QtGui.QMessageBox.warning(self, "Warning",
                                              "Vehicle could not created make sure you have correct format of data")

            if updated_vehicle is not None:
                self.staff_user.update_vehicle(registration_number, updated_vehicle)
                QtGui.QMessageBox.information(self, "Information", "Update process has complete")
            else:
                QtGui.QMessageBox.warning(self, "Warning",
                                          "You can not leave necessary fields blank")

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
    clears all text fields
    '''

    def clear_all_text_fields(self):
        self.registration_text_box.clear()
        self.daily_cost_text_box.clear()
        self.weekend_cost_text_box.clear()
        self.number_of_doors_text_box.clear()
        self.number_of_passenger_text_box.clear()
        self.number_of_bed_text_box.clear()
        self.weekly_cost_text_box.clear()
        self.model_text_box.clear()
        self.make_text_box.clear()
        self.fuel_consumption_text_box.clear()

    '''
    when user selects a vehicle from the list this method sets details into the text field using
    set_information_to_text_fields method
    '''

    def display_vehicle_info(self):
        self.clear_all_text_fields()

        if not self.available_cars_list_widget.currentItem():
            QtGui.QMessageBox.warning(self, "Warning", "Please choose a vehicle from the list")
        else:
            registration_number = self.available_cars_list_widget.currentItem().text()
            self.set_information_to_text_fields(registration_number)

    def set_information_to_text_fields(self, registration_number):
        vehicle = self.vehicles[registration_number]
        self.registration_text_box.setText(registration_number)
        self.make_text_box.setText(vehicle.make)
        self.model_text_box.setText(vehicle.model)
        self.fuel_consumption_text_box.setText(str(vehicle.fuel_consumption))
        self.daily_cost_text_box.setText(str(vehicle.cost.daily_cost))
        self.weekly_cost_text_box.setText(str(vehicle.cost.weekly_cost))
        self.weekend_cost_text_box.setText(str(vehicle.cost.weekend_cost))

        if isinstance(vehicle, Car):
            self.type_list_widget.setCurrentRow(0)
            self.number_of_passenger_text_box.setText(str(vehicle.number_of_passenger))
            self.number_of_doors_text_box.setText(str(vehicle.number_of_doors))
        elif isinstance(vehicle, Van):
            self.type_list_widget.setCurrentRow(1)
            self.number_of_passenger_text_box.setText(str(vehicle.number_of_passenger))
        elif isinstance(vehicle, CamperVan):
            self.type_list_widget.setCurrentRow(2)
            self.number_of_bed_text_box.setText(str(vehicle.number_of_bed))
