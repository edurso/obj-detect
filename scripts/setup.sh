#!/bin/sh

# one-time setup of vision application
# installs necessary packages

# check admin
if ![ "$EUID" -eq 0 ] ; then
    echo "Please run as root by prefixing this command with sudo"
	exit 1
fi

# install robotpy-cscore
echo 'deb http://download.opensuse.org/repositories/home:/auscompgeek:/robotpy/Ubuntu_18.04_Ports/ /' | sudo tee /etc/apt/sources.list.d/home:auscompgeek:robotpy.list
wget https://download.opensuse.org/repositories/home:auscompgeek:robotpy/Ubuntu_18.04_Ports/Release.key 
cat Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_auscompgeek_robotpy.gpg > /dev/null
apt update
apt install -y python3-cscore
rm Release.key

# install v4l2 - used to set camera saturation and other params
apt install -y v4l-utils

# make app environment
mkdir -p /home/lightning/vision/
mkdir -p /home/lightning/bin/
touch /home/lightning/bin/camRunner # make sure this file exists - empty version will be overwritten on deploy

# configure app to run on boot
tempFile='randomtempfile' # This line is purely to make sure that we aren't overwriting a pre-existing file
touch $tempFile && echo '@reboot /bin/bash /home/lightning/bin/camRunner' > $tempFile
crontab $tempFile
rm $tempFile
