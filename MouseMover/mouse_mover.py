from pybricks.iodevices import PUPDevice
from pybricks.pupdevices import Motor, Remote, Light
from pybricks.parameters import Port, Direction, Stop, Button, Color
from pybricks.hubs import TechnicHub
from pybricks.tools import wait
from uerrno import ENODEV


hub = TechnicHub()
hub.light.on(Color.RED)  

motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

while True:
    hub.light.on(Color.GREEN)

    motor.run_time(150, 5000, then=Stop.COAST, wait=True)

    hub.light.off()

    wait(100000)