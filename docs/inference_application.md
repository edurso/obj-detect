# Inference Application for [TensorRT](https://developer.nvidia.com/tensorrt) Engine on [NVIDIA Jetson Nano](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/education-projects/)

Now that the local repository has a [TensorRT](https://developer.nvidia.com/tensorrt) engine, the application can be deployed to the Jetson. The application lives in the `vision/` directory.

## Jetson Nano 2GB

To setup a [NVIDIA Jetson Nano 2gb](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/education-projects/), follow [this setup guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#intro) to image an SD card, and boot up the Jetson.
Note that [this user guide](https://developer.nvidia.com/embedded/learn/jetson-nano-2gb-devkit-user-guide) is also a great resource.

## Set Up

The first step here is to configure the IP of the Jetson on the robot network. The IP should be something like `10.8.62.3`. This can be done through the GUI network settings.

Next, a set of tools need to be installed on the Jetson. Ensure the device with this repository is on the same network as the Jetson (likely the robot network) and run the [install script](https://github.com/edurso/obj-detect/blob/master/install.sh) by executing the command below from the rood directory of the repository.

```bash
sudo ./install.sh {remote username} {remote ip}
```

If the username and IP address of the Jetson are not specified, it will default to `lightning@10.8.62.3`.

This script will send another script to the Jetson, and it will install all of the necessary dependencies.

### Desktop Setup

If, for whatever reason there is a need to connect the Jetson to the internet and access the GUI, the Jetson can be connected to the internet with the USB WiFi Card it came with. Plug this in, and run

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

## Deploying the Application

To deploy the application, run the [deploy script](https://github.com/edurso/obj-detect/blob/master/deploy.sh) from the root directory of the project.

```bash
sudo ./deploy.sh {remote username} {remote ip}
```

If the username and IP address of the Jetson are not specified, it will default to `lightning@10.8.62.3`.

This will run another script on the Jetson that will install the application as a python command line tool. In the configuration step above, the Jetson has been configured to run this application on startup.

## Updating the Application and Adding Pipelines

The application can be changed as needed and deployed with the [deploy script](https://github.com/edurso/obj-detect/blob/master/deploy.sh).

Additional pipelines can be configured in the `bin/config.json` file provided the pipeline extends the `VisionPipeline` type.

Note that the `CFG` constant in `__main__.py` needs to be changed to reflect the users home directory.
