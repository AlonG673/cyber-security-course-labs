#!/bin/bash

echo "================================="
echo "   SSH Service Manager for Lab   "
echo "================================="
echo "1) Start SSH (Open Port 22)"
echo "2) Stop SSH (Close Port 22)"
echo "3) Check SSH Status"
echo "4) Show My IP Address"
echo "5) Exit"
echo "================================="
read -p "Choose an option [1-5]: " option

case $option in
    1)
        echo "[+] Starting SSH service..."
        sudo systemctl start ssh
        echo "[!] SSH is now running. Port 22 is OPEN."
        ;;
    2)
        echo "[-] Stopping SSH service..."
        sudo systemctl stop ssh
        echo "[!] SSH has stopped. Port 22 is CLOSED."
        ;;
    3)
        echo "[*] Checking SSH status:"
        sudo systemctl status ssh | grep -E "Active:"
        ;;
    4)
        echo "[*] Your local IP address is:"
        ip route get 1 | awk '{print $7; exit}'
        ;;
    5)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option!"
        ;;
esac
