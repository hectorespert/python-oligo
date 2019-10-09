from oligo import Iber

connection = Iber()

connection.login("USER", "PASSWORD")

print("ICP Status")
print(connection.icpstatus())

print("Watts")
watts = connection.watthourmeter()
print(watts)

