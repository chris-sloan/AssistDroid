
from os import system
from os import path
import sys
sys.path.append(path.dirname(path.abspath(__file__)))
import adb_devices, create_branch

def menu():
    system("clear")
    print("=========================================")
    print("====== Android Development Helper =======")
    print("=========================================")    
    if len(devices) > 0:
        print(f"==== Devices in Use : {devices}")    
    if len(ticket_number) > 0:
        print(f"==== Current Ticket : {ticket_number}")    
    if len(ticket_description) > 0:
        print(f"==== Current Ticket : {ticket_description}")    
    if len(devices) > 0 or len(ticket_number) > 0 or len(ticket_description) > 0:
        print("=========================================")
    print("==== Menu")
    print("1. List / Select Device(s)")
    print("2. Set up git branch")
    print("3. Run Tests")
    print("4. Generate APK")
    print("5. Exit")
    print("=========================================")

def list_devices():
    return adb_devices.get_adb_devices()

def setup_git_branch():
    return create_branch.create_git_branch()
    
def run_tests():
    print("Running tests...")

def generate_apk():
    print("Generating APK...")

def main():
    global devices
    devices = []
    
    global ticket_number
    ticket_number = ""
    global ticket_description
    ticket_description = ""
    system("clear")
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        system("clear")
        try:
            choice = int(choice)
            if choice == 1:
                devices = list_devices()
            elif choice == 2:
                ticket_number, ticket_description = setup_git_branch()
            elif choice == 3:
                run_tests()
            elif choice == 4:
                generate_apk()
            elif choice == 5:
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid option, please choose between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    
    
# 1.
# Record a video to the sdcard path
# adb shell screenrecord /sdcard/screenrecord.mp4
# control bitrate, time limit and resolution from config file
# Further enhancement could be to only show the cancel option when we're recording - maybe tricky though

# 2.
# retrieve the video file ( could be part of the same fist list item)
# adb pull /sdcard/screenrecord.mp4 
# 
# 3.
# install package - would need to work out how to find the build path for the apk though 
# adb install /Users/erfan/Documents/apps/myApp.apk
# can use -r flag to not delete app data first - toggleable menu option? (or config option)
# 
# 4.
# uninstall package
# adb uninstall com.example.app
# can use -k to retain data following uninstall. - toggleable menu option (or config option, could be same config option as install)
#
# 5.
# take screenshot
# adb shell screencap /sdcard/screenshot.png
# this one could end up complex. Take a begin and an end screen shot and combine them to a single image using some image processing lib.
# then it could be useful for ticket work. 
# retrieve the screenshot
# adb pull /sdcard/screenshot.png /Users/yourusername/Desktop/screenshot.png

# 6.
# connect over wifi
# adb tcpip 5555
# this will setup the adb server to communicate on port 5555
# then 
# adb shell ip route
# to find out the devices ip address
# then
# adb connect <device_ip>:5555
#
# if there's more than one device then we should select one to connect to
# 
# to disconnect 
# adb disconnect <device_ip>:5555
#

# 7.
# Grant permissions
# adb shell pm grant <package_name> <permission>
# list out available permissions from config file
# to revoke perms
# adb shell pm revoke <package_name> <permission>

# 8.
# disable wifi 
# adb shell ifconfig wlan0 down
# enable wifi
# adb shell ifconfig wlan0 up


# with adb you can target usb device with -d and emulator with -e.
# so we could show a current config settings on device in use, network card status, recording status, etc
