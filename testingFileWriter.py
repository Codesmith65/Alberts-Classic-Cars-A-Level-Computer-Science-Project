# This file writes a set of testing data to files
# It'll overwrite any data already in the file

from dataTypes.booking import Booking
from dataTypes.client import Client
from dataTypes.location import Location
from dataTypes.staff import Staff
from dataTypes.task import Task
from dataTypes.user import User
from dataTypes.vehicle import Vehicle

import pickle


# Creating users and staff
users = []
staffs = []
adminUser = User("admin", "admin")
adminStaff = Staff(adminUser.userID, "admin", "admin", "admin address", "012345678")
users.append(adminUser)
staffs.append(adminStaff)

for x in range(20):
    user = User(f"TestUser{x}", "test")
    staff = Staff(user.userID, f"staffFirstName{x}", f"staffLastName{x}", f"staffAddress{x}", f"staffPhoneNumber{x}")
    users.append(user)
    staffs.append(staff)

# Creating vehicles
vehicles = []
for x in range(50):
    vehicles.append(Vehicle(f"VehicleMake{x}", f"VehicleModel{x}", f"VehicleColour{x}", f"VehicleReg{x}", f"VehicleVin{x}"))

# Creating clients
clients = []
for x in range(50):
    clients.append(Client(f"Firstname{x}", f"Lastname{x}", f"email{x}@max.com", f"address{x}", f"phonenumber{x}"))
 
# Creating locations - Not part of prototype
# locations = []
# for x in range(5):
#     locations.append(Location(f"location{x}"))


# Saving data
with open("data/users.pkl", "bw") as f:
    pickle.dump(users, f)
   
with open("data/vehicles.pkl", "bw") as f:
    pickle.dump(vehicles, f)
    
with open("data/clients.pkl", "bw") as f:
    pickle.dump(clients, f)

with open("data/staff.pkl", "bw") as f:
    pickle.dump(staffs, f)
    
# with open("data/locations.pkl", "bw") as f:
#     pickle.dump(locations, f)