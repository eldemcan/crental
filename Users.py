class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

class Customer(User):
    # rented vehicle will be dictionary
    rented_vehicle = {}

    def __init__(self, user_name, password):
        super().__init__(user_name, password)

    '''
    triggered from Customer Screen this method books the given vehicle by adding to a dictionary
    if vehicle is exists it will override it
    '''
    def book_car(self, vehicle, rent_from, rent_to):

        if vehicle.registration_number not in self.rented_vehicle:
            self.rented_vehicle[vehicle.registration_number] = vehicle

        temp_vehicle = self.rented_vehicle[vehicle.registration_number]
        temp_vehicle.is_booked = True
        temp_vehicle.rent_from = rent_from
        temp_vehicle.rent_to = rent_to
        print('booking OK...')

    '''
    this method will delete vehicle from the customer's dictionary if it is exists
    '''
    def cancel_booking(self, registration_number):
        if registration_number in self.rented_vehicle:
            del self.rented_vehicle[registration_number]

class Staff(User):
    def __init__(self, username, password, company):
        super().__init__(username, password)
        self.company = company

    '''
    this method will remove vehicle from company's dictionary if it is exists
    '''
    def delete_vehicle(self, registration_number):
        vehicle = self.company.list_of_vehicles[registration_number]
        if vehicle.is_booked == True:
            return False
        else:
            print('deleting entity...')
            del self.company.list_of_vehicles[registration_number]
            return True
    '''
    this method will update vehicle from company's dictionary if it is exists
    '''
    def update_vehicle(self, registration_number, vehicle):
        self.company.list_of_vehicles[registration_number] = vehicle
    '''
    this method will insert a vehicle from company's dictionary if there is not any vehicle with same registration number
    '''
    def insert_vehicle(self, vehicle):
        if vehicle.registration_number not in self.company.list_of_vehicles:
            self.company.list_of_vehicles[vehicle.registration_number] = vehicle
            return True
        else:
            return False


class Company:
    def __init__(self, company_name, list_of_vehicles):
        self.company_name = company_name
        self.list_of_vehicles = list_of_vehicles
