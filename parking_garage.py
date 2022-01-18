class Car:
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color

    def __repr__(self):
        print(f'{self.license_plate}, {self.model}, {self.color}')
    
    @classmethod
    def user_input(cls):
        license_plate = input()
        model = input()
        color = input()
        return cls(license_plate, model, color)

                
class ParkingGarage:
    def __init__(self, cars_added, spots, car_info, bill):
        self.cars_added = cars_added
        cars_added= []
        self.spots = 20
        self.car_info = car_info
        car_info = {}
        self.bill = bill
        bill = 0
        
    def spots_available(self):
        print(self.spots)

    def add_car(self, car):
        self.identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1','K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
        if self.spots > 0:
            self.cars_added(str(car).split(', '))
            self.spots -= 1
            self.car_info = {'code': [], 'license plate': [], 'Model': [], 'Color': []}
            for index, i in enumerate(self.cars_added):
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license plate'].append(i[0])
                self.car_info['Model'].append(i[1])
                self.car_info['Color'].append(i[2])
            print("car successfully added to the parking lot")
        else:
            print(f"We have {self.spots} spots available. I am sorry ")
        
    def remove_car(self, given_code, bill_hours):
        past_len = len(self.car_info['code'])
        if given_code not in self.car_info['code']:
            print("We could not find your car. Are you sure you parked your car here? ")
        else:
            for index, value in enumerate(self.car_info['code']):
                if value == given_code:
                    print("Your car's license plate is:", self.car_info['license plate'][index])
                    print("Your car's model is:", self.car_info['Model'][index])
                    print("Your car's color is :", self.car_info['Color'][index])
                    removed_car_index = self.car_info['code'].pop(index)
                    self.car_info['license plate'].pop(index)
                    self.car_info['Model'].pop(index)
                    self.car_info['Color'].pop(index)
                    self.spots += 1
            if len(self.car_info['code']) < past_len:
                while True:
                    if bill_hours.isnumeric():
                        self.list_of_time_and_code = [bill_hours, removed_car_index]
                        break
                    else:
                        print("Your input must be an integer. Sample input: 5 ")
                        bill_hours = input("Enter for how long you were on the parking lot in hours or 'q' to quit. Example input: 5  -->  ")
                    if bill_hours in ['q', 'Q']:
                        break
                    if int(self.list_of_time_and_code[0]) < 20:
                        self.bill = int(self.list_of_time_and_code[0]) * 5
                        print(f'Your total bill is ${self.bill}')
                    else:
                        self.bill = int(self.list_of_time_and_code[0]) * 5 + 100
                        print(f'Your total bill is ${self.bill}')
    
    def cars_in_garage(self):
            for i in self.car_info.items():
                print(i)
              
def my_garage():
    spots = 20
    cars_added= []   
    car_info = {}  
    bill = 0
    identifier = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1','K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1'] 
    while True:
        add_car = input(f"Welcome to my garage. There are {spots}spots available. What would you like to do?\nType 'park' to park 'bill' to pay your bill 'exit' to leave. ")
        if add_car.lower() == 'park':
            if spots > 0:
                Car.license_plate = str(input("Enter in your 6 digit license plate number: "))
                Car.model = str(input("Enter in the model of your car: "))
                Car.color = str(input("Enter in the color of your car: "))
                cars_added.append([Car.license_plate])
                cars_added.append([Car.model])
                cars_added.append([Car.color])
                cars_added.append([identifier])
                spots -= 1
                for index, i in enumerate(cars_added):
                    car_info['code'] = identifier[index]
                    car_info['license plate'] = i
                    car_info['Model'] = i
                    car_info['Color'] = i
                    print(car_info)
            else:
                print(f"We have {spots} spots available. I am sorry ")                       
        elif add_car.lower() == 'bill':
            past_len = len(car_info['code'])
            if identifier not in car_info['code']:
                print("We could not find your car. Are you sure you parked your car here? ")
            else:
                for index, value in enumerate(car_info['code']):
                    if value == identifier:
                        print("Your car's license plate is:", car_info['license plate'][index])
                        print("Your car's model is:", car_info['Model'][index])
                        print("Your car's color is :", car_info['Color'][index])
                        removed_car_index = car_info.pop("code")
                        car_info.pop("license plate")
                        car_info.pop("model")
                        car_info.pop("color")
                        spots += 1
                if len(car_info['code']) < past_len:
                    while True:
                        if bill_hours.isnumeric():
                            list_of_time_and_code = [bill_hours, removed_car_index]
                            break
                        else:
                            print("Your input must be an integer. Sample input: 5 ")
                            bill_hours = input("Enter for how long you were on the parking lot in hours or 'q' to quit. Example input: 5  -->  ")
                        if bill_hours in ['q', 'Q']:
                            break
                        if int(list_of_time_and_code[0]) < 20:
                            bill = int(list_of_time_and_code[0]) * 5
                            print(f'Your total bill is ${bill}')
                        else:
                            bill = int(list_of_time_and_code[0]) * 5 + 100
                            print(f'Your total bill is ${bill}')
        elif add_car.lower() == 'exit':
            pass
        else:
            print("Sorry that was not a valid response. Please try again. ")
        

my_car = Car.user_input(my_garage())
       