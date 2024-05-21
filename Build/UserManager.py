import os
import sys
from typing import List
from FlightManager import FlightManager
from Flight import Flight
from User import User
from UserManager import UserManager
class UserManager:
    def __init__(self, System):
        self.users_ = []
        with open("Data/Passengers.txt", "r") as arquivo:
            for line in arquivo:
                data = line.split()
                if len(data) < 6:
                    print("Erro ao ler os dados do arquivo")
                    continue
                
                aux_user = User()
                aux_user.addName(data[0])
                aux_user.addEmail(data[1])
                aux_user.addPassword(data[2])
                aux_user.addCpf(int(data[3]))
                aux_user.addCreditCard(int(data[4]))
                num_tickets = int(data[5])
                for i in range(num_tickets):
                    voo = int(data[6 + i * 2])
                    seat = int(data[7 + i * 2])
                    aux_user.buyTicket(voo, seat, System)
                self.users_.append(aux_user)

    def addUser(self, passenger):
        self.users_.append(passenger)

    def returnUser(self, name, password):
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return user
        print("Não existe o usuário")
        raise ValueError("erro")

    def UpdatePassenger(self):
        with open("Data/Passengers.txt", "w") as arquivo:
            for user in self.users_:
                profile_data = user.ReturnProfile()
                arquivo.write(profile_data["name"] + "\n")
                arquivo.write(profile_data["email"] + "\n")
                arquivo.write(profile_data["password"] + "\n")
                arquivo.write(str(profile_data["cpf"]) + "\n")
                arquivo.write(str(profile_data["credit_card"]) + "\n")
                arquivo.write(str(len(profile_data["flight_info"])) + "\n")
                for flight_info in profile_data["flight_info"]:
                    arquivo.write(str(flight_info[0]) + " " + str(flight_info[1]) + "\n")

    def validName(self, name):
        for user in self.users_:
            if user.checkName(name):
                return False
        return True

    def validPassword(self, name, password):
        for user in self.users_:
            if user.checkName(name):
                if user.checkPassword(password):
                    return True
                else:
                    return False
        return False
