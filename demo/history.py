from oligo import Iber
from datetime import date, timedelta

import os

connection = Iber()
connection.login(os.environ['IDE_USER'], os.environ['IDE_PASSWORD'])

from_date = date.today() - timedelta(days=2)
until_date = date.today() - timedelta(days=2)

print("instantaneo:")

consumo = connection.watthourmeter()
print(consumo)
print("")


print("consumption_period hours:")

print(from_date)
print(until_date)

consumo = connection.consumption_period("hours", from_date, until_date)
print(consumo)
print("")

print("total_consumption:")

consumo = connection.total_consumption(from_date, until_date)
print(consumo)
print("")

print("total_consumption periods:")

consumo = connection.total_consumption_period("hours", from_date, until_date)
print(consumo)
print("")

print("consumption_period days:")

from_date = date.today() - timedelta(days=30)
until_date = date.today() - timedelta(days=1)
print(from_date)
print(until_date)
consumo = connection.consumption_period("days", from_date, until_date)
print(consumo)
print("")

consumo = connection.total_consumption_period("days", from_date, until_date)
print(consumo)
print("")
