Raspberry Pi ko **Wireless Access Point (WAP/Hotspot)** banana chahte ho.
Ye bahut useful hota hai agar tum Raspberry Pi ko ek **Wi-Fi router** jaisa use karna chahte ho (IoT projects, local server, captive portal, etc.).

---

## ✅ Steps: Raspberry Pi as Wireless Access Point (AP mode)

### 1. **Update system**

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. **Install required packages**

* `hostapd` → Access Point service
* `dnsmasq` → DHCP server

```bash
sudo apt install hostapd dnsmasq -y
```

Stop services for now:

```bash
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

---

### 3. **Configure static IP for wlan0**

Edit dhcpcd config:

```bash
sudo nano /etc/dhcpcd.conf
```

Add at the bottom:

```
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
```

Restart dhcpcd:

```bash
sudo service dhcpcd restart
```

---

### 4. **Configure dnsmasq (DHCP server)**

Backup old config:

```bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```

Create new config:

```bash
sudo nano /etc/dnsmasq.conf
```

Add:

```
interface=wlan0      # Use the Pi’s WiFi interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

---

### 5. **Configure hostapd (Wi-Fi settings)**

Create config:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Add:

```
interface=wlan0
driver=nl80211
ssid=RaspberryPi-AP
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=12345678
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

👉 Replace `ssid` and `wpa_passphrase` with your Wi-Fi name & password.

Tell system where config is:

```bash
sudo nano /etc/default/hostapd
```

Find line:

```
#DAEMON_CONF=""
```

Change to:

```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

---

### 6. **Enable services**

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

---

### 7. **(Optional) Enable Internet Sharing**

If you want your AP to share internet (Pi connected via Ethernet):

```bash
sudo nano /etc/sysctl.conf
```

Uncomment:

```
net.ipv4.ip_forward=1
```

Apply:

```bash
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
```

Set up NAT:

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

Make it permanent:

```bash
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

Add this line in `/etc/rc.local` **before `exit 0`:**

```
iptables-restore < /etc/iptables.ipv4.nat
```

---

### 8. **Reboot**

```bash
sudo reboot
```

After reboot, your Raspberry Pi will broadcast Wi-Fi **`RaspberryPi-AP`** with password **`12345678`**.

---

⚡ Now your Pi works as a **Wi-Fi Access Point (AP)**.

* If Pi is connected to **Ethernet**, devices connected to AP will get **Internet**.
* If not, Pi acts as a **local-only hotspot** (useful for IoT/attendance projects).

---

