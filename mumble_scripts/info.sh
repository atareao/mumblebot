#!/bin/bash
ufw status | grep 54325
if systemctl status mumble-server | grep running > /dev/null; then echo "Mumble Server **started**";else echo "Mumble server **stopped**";fi
