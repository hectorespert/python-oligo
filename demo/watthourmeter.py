import PyCmdMessenger
import time
from oligo import iber

arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyACM0", baud_rate=9600)
commands = [["watt", "d"]]
c = PyCmdMessenger.CmdMessenger(arduino, commands)

while True:
    watt = iber.watthourmeter("tu_usuario", "tu_contraseña")
    c.send("watt", watt)
    time.sleep(300)
