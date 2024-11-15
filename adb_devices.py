import subprocess

def get_adb_devices():
    selected_devices = []
    devices = list_adb_devices()

    if not devices:
        print("No devices found.")
        input()
        return selected_devices # will be empty

    print("Available devices:")
    for i, device in enumerate(devices, 1):
        print(f"{i}. {device}")

    while True:
        choice = input("Enter device numbers (comma-separated, or 'all' for all): ")
        if choice.lower() == 'all':
            selected_devices = devices
            break
        else:
            try:
                selected_devices = [devices[int(num) - 1] for num in choice.split(',')]
                break
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
                
    return selected_devices


def list_adb_devices():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    if result.returncode == 0:
        devices = result.stdout.strip().split('\n')[1:]
        return [device.split('\t')[0] for device in devices if device]
    else:
        print("Error: Could not get device list.")
        return []
    

def main():
    selected_devices = get_adb_devices()
    print("Selected devices:", selected_devices)

    # Now you can use the selected devices for further operations
    for device in selected_devices:
        # Example: Execute 'adb -s <device_serial> shell'
        subprocess.run(['adb', '-s', device, 'shell'])

if __name__ == "__main__":
    main()