import subprocess
import optparse
import time

parseObject=optparse.OptionParser()
# to add options to the terminal
parseObject.add_option("-i","--i",dest="interface",help="interface that mac address' to be changed")
parseObject.add_option("-m","--mac",dest = "mac_address", help = "new mac address")

user_inputs = parseObject.parse_args()
input_interface = user_inputs.interface
input_mac = user_inputs.mac_address

subprocess.call(["ifconfig",input_interface, "down"]) #down the connection first
subprocess.call(["ifconfig",input_interface,"hw", "ether", input_mac])
subprocess.call(["ifconfig",input_interface,"up"]) #up the connection again

#control mac address

time.sleep(2)
subprocess.call(["ifconfig"])

#control the connection

time.sleep(2)

subprocess.call(["ping","google.com"])







