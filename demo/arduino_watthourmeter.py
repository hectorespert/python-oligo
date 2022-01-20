import PyCmdMessenger
import time
from oligo import Iber

arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyACM0", baud_rate=9600)
commands = [["watt", "d"]]
c = PyCmdMessenger.CmdMessenger(arduino, commands)

connection = Iber()
connection.login("user", "password")

while True:
    watt = connection.watthourmeter()
    print(watt)
    c.send("watt", watt)
    time.sleep(300)