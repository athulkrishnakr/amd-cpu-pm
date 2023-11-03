#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]
  then echo "Root privileges required"
  exit
fi

# Copy files
cp $PWD/cpu_pm /usr/local/bin/

#Make it executable
chmod +x /usr/local/bin/cpu_pm