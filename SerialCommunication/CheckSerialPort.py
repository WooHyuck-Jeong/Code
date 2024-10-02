import serial
import serial.tools
import serial.tools.list_ports

def getPortList():
    """
        사용가능한 Port 리스트 반환
        Input: None
        Output: Port device list
    """
    availablePorts = []
    ports = serial.tools.list_ports.comports()

    for p in ports:
        availablePorts.append(p.device)
    
    return availablePorts

if __name__ == "__main__":
    getPortList()