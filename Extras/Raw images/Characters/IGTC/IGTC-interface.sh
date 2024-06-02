#!/bin/sh
clear
figlet -c -t IGTC
figlet -c -t -f term "Prototype 2"
figlet -c -t -f term "Mem "$(free -h | awk 'NR!=2 {print $2}')"b"
echo ""
echo ""
figlet -c -t -f term ">>Access database<<"
figlet -c -t -f term ">>Scan Universes<<"
figlet -c -t -f term ">>Enable Interactive Help System<<"
figlet -c -t -f term ">>Activate connector<<"
figlet -c -t -f term ">>Reboot<<"
echo ""
echo ""
figlet -c -t -f term "Unit is touch"
figlet -c -t -f term "screen capable"
