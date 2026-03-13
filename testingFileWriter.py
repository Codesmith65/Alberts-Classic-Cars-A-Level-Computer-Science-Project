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
import uuid


# Creating users and staff
users = []
staffs = []
adminUser = User("admin", "admin", userID=uuid.UUID("d8eec26b-91c3-4144-b2f7-97ec1f20d064"), admin=True)
adminStaff = Staff(adminUser.userID, "admin", "admin", "admin address", "012345678", staffID=uuid.UUID("e22e4c85-589f-4370-b052-599cb3dabbc9"))
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
 
# Creating locations
locations = []
for x in range(5):
    locations.append(Location(f"location{x}"))

# Creating tasks
tasks = [Task(f"TestTask{x}", f"TestTaskDescription{x}", False, uuid.uuid4(), uuid.UUID("d8eec26b-91c3-4144-b2f7-97ec1f20d064"))]
for y in range(20):
    for x in range(20):
        tasks.append(Task(f"TestTask{x}", f"TestTaskDescription{x}", False, tasks[-1].taskID, staffs[x].staffID))


# Saving data
with open("data/users.pkl", "bw") as f:
    pickle.dump(users, f)
   
with open("data/vehicles.pkl", "bw") as f:
    pickle.dump(vehicles, f)
    
with open("data/clients.pkl", "bw") as f:
    pickle.dump(clients, f)

with open("data/staff.pkl", "bw") as f:
    pickle.dump(staffs, f)
    
with open("data/locations.pkl", "bw") as f:
    pickle.dump(locations, f)
   
with open("data/tasks.pkl", "bw") as f:
    pickle.dump(tasks, f)