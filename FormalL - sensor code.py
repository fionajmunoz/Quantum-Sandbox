from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

# Callback function for handling sensor data
def onSensorChange(self, sensorValue, sensorUnit):
    print(f"Sensor on Hub {self.getHubPort()} - Value: {sensorValue} {sensorUnit.symbol}")
    print("----------")

def main():
    # Create two separate voltage ratio input objects
    voltageRatioInput3 = VoltageRatioInput()
    voltageRatioInput4 = VoltageRatioInput()
    voltagRatioInput2 = VoltageRatioInput()
    voltageRatioInput1 = VoltageRatioInput()

    # Configure Hub Port 3
    voltageRatioInput3.setIsHubPortDevice(True)
    voltageRatioInput3.setHubPort(3)
    voltageRatioInput3.setOnSensorChangeHandler(onSensorChange)

    # Configure Hub Port 4
    voltageRatioInput4.setIsHubPortDevice(True)
    voltageRatioInput4.setHubPort(4)
    voltageRatioInput4.setOnSensorChangeHandler(onSensorChange)
    
    #For Hub Port 1
    voltageRatioInput1.setHubPortDevice(True)
    voltageRatioInput1.setHubPort(1)
    voltageRatioInput1.setOnSensorChangeHandler(onSensorChange)
    
    #For Hub Port 2
    volateRatioInput2.etHubPortDevice(True)
    voltageRatioInput2.setHubPort(2)
    voltageRatioInput2.setOnSensorChangeHandler(onSensorChange)

    # Open both sensors
    voltageRatioInput3.openWaitForAttachment(5000)
    voltageRatioInput4.openWaitForAttachment(5000)
    voltageRatioInput2.openWaitForAttachment(5000)
    voltageRatioInput1.openWaitForAttachment(5000)

    # Set sensor types
    voltageRatioInput3.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1108)
    voltageRatioInput4.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1108)
    voltageRatioInput1.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1108)
    voltageRatioInput2.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1108)

    try:
        input("Press Enter to stop...\n")
    except (Exception, KeyboardInterrupt):
        pass

    # Close both sensors when exiting
    voltageRatioInput0.close()
    voltageRatioInput5.close()
    voltageRatioInput1.close()
    voltageRatioInput2.close()
    
main()
