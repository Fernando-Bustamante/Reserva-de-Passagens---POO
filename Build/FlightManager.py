import sys
import os
from FlightManager import FlightManager
from Flight import Flight
class FlightManager:
    def __init__(self):
        self.flights_ = []

        with open("Data/voos.txt", "r") as arquivo:
            for line in arquivo:
                data = line.split()
                if len(data) != 9:
                    print("Erro ao ler os dados do arquivo")
                    continue
                
                flight = Flight()
                flight.addFlightCode(int(data[0]))
                flight.addOriginCity(data[1])
                flight.addOriginCountry(data[2])
                flight.addDestinationCity(data[3])
                flight.addDestinationCountry(data[4])
                flight.addTimeHour(int(data[5]))
                flight.addTimeMinute(int(data[6]))
                flight.addPrice(float(data[7]))
                flight.addSeat(int(data[8]))
                
                self.flights_.append(flight)

    def changeFlight(self, codigo, seat):
        self.flights_[codigo - 1].getSeat(seat)

    # As outras funções da classe continuariam aqui

