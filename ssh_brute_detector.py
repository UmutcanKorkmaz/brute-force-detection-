# SSH/RDP Brute-Force Detection Logic - Developed by Umutcan Korkmaz
from collections import defaultdict
import datetime

# IP tabanlı başarısız giriş takibi
login_attempts = defaultdict(list)
THRESHOLD = 5  # Maksimum deneme sayısı
WINDOW_SECONDS = 60 # Zaman penceresi

def check_for_brute_force(ip_address):
    now = datetime.datetime.now()
    login_attempts[ip_address].append(now)
    
    # Eski denemeleri temizle
    recent_attempts = [t for t in login_attempts[ip_address] if (now - t).seconds < WINDOW_SECONDS]
    login_attempts[ip_address] = recent_attempts
    
    if len(recent_attempts) >= THRESHOLD:
        print(f"[CRITICAL] Brute-force attack detected from: {ip_address}")
        print(f"[ACTION] Triggering IP block for {ip_address} on Firewall.")

check_for_brute_force("10.0.0.50")
