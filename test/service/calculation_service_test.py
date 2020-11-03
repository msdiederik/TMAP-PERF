from src.service import calculation_service as calculation_service
from tkinter import Tk

root = Tk()
service = calculation_service.CalculationService()

service.set_expression("10/10/10")
service.equalpress()
print((service.get_equation().get()) == str(10/10/10))

service.set_expression("10*9+7")
service.equalpress()
print(str(service.get_equation().get()) == "97 <:o)")

service.set_expression("10/0")
service.equalpress()
print((service.get_equation().get()) == " error ")

service.set_expression("10-10+10")
service.equalpress()
print((service.get_equation().get()) == str(10))

service.set_expression("10-10/10")
service.equalpress()
print((service.get_equation().get()) == str(10-10/10))