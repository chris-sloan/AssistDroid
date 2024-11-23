
from os import system
from os import path
import sys

sys.path.append(path.dirname(path.abspath(__file__)))
from menu import MenuItem
import menu, adb_devices, create_branch, utilities

def __list_devices():
    return adb_devices.get_adb_devices()

def __setup_git_branch():
    return create_branch.create_git_branch()
    
def __run_tests():
    print("Running tests...")

def __generate_apk():
    print("Generating APK...")
    
def __open_utilities():
    utilities.display_menu(devices, ticket_number, ticket_description)
    
def display_menu():
    system("clear")

    menu_items = [
        MenuItem("List / Select Device(s)", __list_devices),
        MenuItem("Set up git branch", __setup_git_branch),
        MenuItem("Run Tests", __run_tests),
        MenuItem("Generate APK", __generate_apk),
        MenuItem("Utilities", __open_utilities),
    ]

    while True:
        menu.display_menu(menu_items, devices, ticket_number, ticket_description)
        choice = input("Select an option (1-{} or 'q' to quit): ".format(len(menu_items)))
        menu.handle_user_choice(choice, menu_items)

def main():
    global devices
    devices = []
    global ticket_number
    ticket_number = ""
    global ticket_description
    ticket_description = ""
    
    display_menu()
    
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
