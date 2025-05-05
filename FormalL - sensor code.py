from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

class PhidgetSensorManager:
    def __init__(self, ports, sensor_type=VoltageRatioSensorType.SENSOR_TYPE_1108):
        self.ports = ports
        self.sensors = []
        self.sensor_type = sensor_type

    def on_sensor_change(self, sensor, sensorValue, sensorUnit):
        print(f"Sensor on Hub {sensor.getHubPort()} - Value: {sensorValue} {sensorUnit.symbol}")
        print("----------")

    def setup_sensors(self):
        for port in self.ports:
            sensor = VoltageRatioInput()
            sensor.setIsHubPortDevice(True)
            sensor.setHubPort(port)
            sensor.setOnSensorChangeHandler(self.on_sensor_change)
            sensor.openWaitForAttachment(5000)
            sensor.setSensorType(self.sensor_type)
            self.sensors.append(sensor)

    def close_sensors(self):
        for sensor in self.sensors:
            sensor.close()

    def run(self):
        try:
            input("Press Enter to stop...\n")
        except (Exception, KeyboardInterrupt):
            pass
        finally:
            self.close_sensors()


# Example usage:
if __name__ == "__main__":
    manager = PhidgetSensorManager(ports=[1, 2, 3, 4])
    manager.setup_sensors()
    manager.run()

