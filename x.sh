#!/bin/bash
pkg update && pkg upgrade -y
pkg install nano vim
pkg install file-manager findutils which
pkg install curl wget openssh git
pkg install python make clang

# Interface utilisateur graphique (si tu veux lancer des apps GUI via VNC ou similar)
pkg install termux-api termux-widgets

# Autres utilitaires courants
pkg install proot-distro # Pour lancer Linux (Ubuntu/Kali) depuis Termux si besoin
pkg install zip unzip tar
echo "________________________"
echo "normalement c est bon."