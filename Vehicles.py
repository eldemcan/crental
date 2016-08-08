import datetime


class Vehicle:
    is_booked = False
    rent_from = datetime.date(datetime.MINYEAR, 1, 1)
    rent_to = datetime.date(datetime.MINYEAR, 1, 1)

    def __init__(self, make, model, fuel_consumption, registration_number, daily_cost, weekly_cost, weekend_cost):
        self.make = make
        self.model = model
        self.cost = Cost(daily_cost, weekly_cost, weekend_cost)
        self.fuel_consumption = fuel_consumption
        self.registration_number = registration_number

    def check_availability(self, requested_rent_from, requested_rent_to):
        if self.rent_from < requested_rent_from < self.rent_to or self.rent_from < requested_rent_to < self.rent_to:
            print("vehicle " + self.registration_number + "is not available")
            return False
        else:
            return True

    #tostring method
    def __str__(self):
        info = "Plate Number:" + self.registration_number + "\nMake:" + self.make + "\nModel:" + self.model + "\nFuel Consumption:" + str(
            self.fuel_consumption) + "\n" + self.cost.__str__()
        return info


class Cost:
    def __init__(self, daily_cost, weekly_cost, weekend_cost):
        self.daily_cost = daily_cost
        self.weekly_cost = weekly_cost
        self.weekend_cost = weekend_cost
    #tostring method
    def __str__(self):
        info = "Daily Cost:" + str(self.daily_cost) + "\nWeekly Cost:" + str(
            self.weekly_cost) + "\nWeekend Cost:" + str(self.weekend_cost)
        return info


class CamperVan(Vehicle):
    def __init__(self, make, model, fuel_consumption, number_of_bed, registration_number, daily_cost, weekly_cost,
                 weekend_cost):
        super().__init__(make, model, fuel_consumption, registration_number, daily_cost, weekly_cost, weekend_cost)
        self.number_of_bed = number_of_bed
    #tostring method
    def __str__(self):
        info = super().__str__() + "\nNumber of bed:" + str(self.number_of_bed)
        return info


class Car(Vehicle):
    def __init__(self, make, model, fuel_consumption, registration_number, number_of_passenger, number_of_doors, daily_cost,
                 weekly_cost, weekend_cost):
        super().__init__(make, model, fuel_consumption, registration_number, daily_cost, weekly_cost, weekend_cost)
        self.number_of_passenger = number_of_passenger
        self.number_of_doors = number_of_doors

    def __str__(self):
        info = super().__str__() + "\nNumber of passenger:" + str(
            self.number_of_passenger) + "\nNumber of Doors:" + str(self.number_of_doors)
        return info


class Van(Vehicle):
    def __init__(self, make, model, fuel_consumption, registration_number, number_of_passenger, daily_cost, weekly_cost,
                 weekend_cost):
        super().__init__(make, model, fuel_consumption, registration_number, daily_cost, weekly_cost, weekend_cost)
        self.number_of_passenger = number_of_passenger

    def __str__(self):
        info = super().__str__() + "\nNumber of passenger:" + str(self.number_of_passenger)
        return info
