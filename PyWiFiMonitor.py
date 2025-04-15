#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tampilkan_anonymous():
    anonymous_art = r"""
       .--.
      |o_o |
      |:_/ |
     //   \ \
    (|     | )
   /'\_   _/`\
   \___)=(___/
    """
    print(anonymous_art)

__author__ = "Teguh"  # Author diletakkan di bawah gambar ASCII

import subprocess

def enable_monitor_mode(interface):
    """
    Mengaktifkan mode monitor pada interface Wi-Fi.
    """
    try:
        print(f"Menonaktifkan proses yang mengganggu pada {interface}...")
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], check=True)
        print(f"Mengaktifkan mode monitor pada {interface}...")
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        print(f"Monitor mode diaktifkan pada {interface} (biasanya menjadi {interface}mon)")
    except subprocess.CalledProcessError as e:
        print(f"Error saat mengaktifkan monitor mode: {e}")

def disable_monitor_mode(interface):
    """
    Menonaktifkan mode monitor dan kembali ke mode managed.
    """
    try:
        print(f"Menonaktifkan mode monitor pada {interface}...")
        subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
        restart_network_manager()
        print(f"Monitor mode dinonaktifkan pada {interface}")
    except subprocess.CalledProcessError as e:
        print(f"Error saat menonaktifkan monitor mode: {e}")

def restart_network_manager():
    """
    Me-restart Network Manager untuk mengembalikan koneksi jaringan.
    """
    try:
        print("Me-restart Network Manager...")
        subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=True)
        print("Network Manager berhasil di-restart")
    except subprocess.CalledProcessError as e:
        print(f"Error saat me-restart Network Manager: {e}")

def main():
    tampilkan_anonymous()
    print(f"Author: {__author__}\n")  # Tampilkan author setelah gambar
    while True:
        print("=== Menu Monitor Mode Wi-Fi ===")
        print("1. Aktifkan Monitor Mode")
        print("2. Nonaktifkan Monitor Mode")
        print("3. Restart Network Manager")
        print("4. Keluar")
        choice = input("Pilih opsi (1-4): ").strip()

        if choice == '1':
            interface = input("Masukkan nama interface Wi-Fi (contoh: wlan0): ").strip()
            enable_monitor_mode(interface)
        elif choice == '2':
            interface = input("Masukkan nama interface monitor (contoh: wlan0mon): ").strip()
            disable_monitor_mode(interface)
        elif choice == '3':
            restart_network_manager()
        elif choice == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
