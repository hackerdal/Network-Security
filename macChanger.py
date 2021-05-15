import subprocess
import optparse
import re
import time


print("@Created by hackiran ")

ifconfig = subprocess.check_output(["ifconfig"])
permanent_mac_address = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}",str(ifconfig)).group(0)
#take inputs from terminal
def user_inputs():

    parse_object = optparse.OptionParser() #create instance

    parse_object.add_option("-i","--interface", dest = "interface", help = "current interface")
    parse_object.add_option("-m","--mac", dest = "mac_address", help = "new mac address")
    #(user_input, arguments) = parse_object.parse_args()
    #interface = user_input.interface
    #parse_object.add_option("-p","--permanent", action= "store_true", dest = restart(permanent_mac_address, interface), help = "permanent mac address")

    return parse_object.parse_args()

def terminal_commands(user_input_interface, user_input_mac_address):
    subprocess.call(["ifconfig", user_input_interface, "down"])
    subprocess.call(["ifconfig", user_input_interface, "hw", "ether", user_input_mac_address])
    subprocess.call(["ifconfig", user_input_interface, "up"])

def show_info(mac_address, new_mac_address):
    print("Original mac address: ",permanent_mac_address)
    print("new mac address: ",new_mac_address)

def status(new_mac_address):
    if new_mac_address:
        print("Successfull!")
    else:
        print("Error")

"""def restart(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface,"up"])

    ifconfig = subprocess.check_output(["ifconfig",interface])
    control_new_mac = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}",str(ifconfig)).group(0)

    if control_new_mac == mac_address:
        print("Mac address is changed to permanent value! Successfull!")
"""


(user_input, arguments) = user_inputs()

terminal_commands(user_input.interface, user_input.mac_address)
time.sleep(1)
ifconfig = subprocess.check_output(["ifconfig",user_input.interface])
new_mac_address = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}",str(ifconfig)).group(0)
time.sleep(1)
show_info(permanent_mac_address,new_mac_address)
status(new_mac_address)




