# Inference Application for TensorRT Engine on NVIDIA Jetson Nano

## Installation

### Jetson Nano 2gb

To setup a [NVIDIA Jetson Nano 2gb](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/education-projects/), follow [this setup guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#intro) to image an SD card, and boot up the Jetson.\
Note that [this user guide](https://developer.nvidia.com/embedded/learn/jetson-nano-2gb-devkit-user-guide) is also a great resource.

Once you have setup the Jetson, you will need to connect to internet.\
Be sure the USB WiFi Card is plugged in.\
This can be done by running the following command:

```bash
sudo nmcli device wifi connect <ssid> password <password>
```

Alternatively, if you need to connect to a hidden network, run the following commands (from [this post](https://stackoverflow.com/questions/35476428/how-to-connect-to-hidden-wifi-network-using-nmcli)):

```bash
sudo nmcli c add type wifi con-name <connect name> ifname wlan0 ssid <ssid>
sudo nmcli con modify <connect name> wifi-sec.key-mgmt wpa-psk
sudo nmcli con modify <connect name> wifi-sec.psk <password>
sudo nmcli con up <connect name>
```

Install cscore and other dependencies with

```bash
bash <(wget -qO- https://raw.githubusercontent.com/edurso/obj-detect/master/scripts/setup.sh)
```
