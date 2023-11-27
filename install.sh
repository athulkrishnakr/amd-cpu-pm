#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]
  then echo "Root privileges required"
  exit
fi

#Make directory
mkdir /etc/dbus-1
mkdir /etc/dbus-1/system.d/

# Copy files
cp $PWD/cpud /usr/local/bin/
cp $PWD/cpuctl /usr/local/bin/
cp -r $PWD/pm_modules /usr/local/bin/
cp $PWD/org.cpupm.Daemon.conf /etc/dbus-1/system.d/
cp $PWD/cpu-pm.service /usr/lib/systemd/system/

#Make it executable
chmod +x /usr/local/bin/cpud
chmod +x /usr/local/bin/cpuctl

systemctl reload dbus
systemctl enable --now cpu-pm.service

