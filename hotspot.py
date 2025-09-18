import subprocess

def create_hotspot(ssid="RPi3_AP", password="raspberry123"):
    try:
        subprocess.run([
            "nmcli", "dev", "wifi", "hotspot",
            "ifname", "wlan0", "ssid", ssid, "password", password
        ], check=True)
        print(f"\n✅ Hotspot '{ssid}' created successfully!\n")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to create hotspot:", e)

def stop_hotspot():
    try:
        # Check active connections
        result = subprocess.run(
            ["nmcli", "-t", "-f", "NAME,TYPE", "con", "show", "--active"],
            capture_output=True, text=True, check=True
        )
        for line in result.stdout.splitlines():
            if "wifi" in line:
                name = line.split(":")[0]
                subprocess.run(["nmcli", "con", "down", name], check=True)
                print(f"\n🛑 Hotspot '{name}' stopped.\n")
                return
        print("\n⚠️ No active hotspot found.\n")
    except subprocess.CalledProcessError as e:
        print("❌ Error stopping hotspot:", e)

def status_hotspot():
    print("\n📡 Device Status:\n")
    subprocess.run(["nmcli", "dev", "status"])

def menu():
    while True:
        print("\n===== Raspberry Pi Hotspot Control =====")
        print("1. Start Hotspot")
        print("2. Stop Hotspot")
        print("3. Status")
        print("4. Exit")

        choice = input("Select option: ").strip()
        if choice == "1":
            ssid = input("Enter SSID [default RPi3_AP]: ") or "RPi3_AP"
            password = input("Enter Password [default raspberry123]: ") or "raspberry123"
            create_hotspot(ssid, password)
        elif choice == "2":
            stop_hotspot()
        elif choice == "3":
            status_hotspot()
        elif choice == "4":
            print("👋 Exiting Hotspot Control. Bye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
