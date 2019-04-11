#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig | sed -n -e 's/^.*HWaddr //p'", shell=True)
subprocess.call("ifconfig enp0s3 down", shell=True)
subprocess.call("ifconfig enp0s3 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig enp0s3 up", shell=True)
subprocess.call("ifconfig | sed -n -e 's/^.*HWaddr //p'", shell=True)

