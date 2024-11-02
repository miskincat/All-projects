import requests
import calendar
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def fetch_current_date_istanbul():
    try:
        response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Europe/Istanbul")
        data = response.json()
        current_datetime = data['dateTime']
        current_datetime = current_datetime.split('.')[0]  # Noktadan sonraki kısmı atla
        istanbul_time = datetime.fromisoformat(current_datetime)
        return istanbul_time
    except Exception as e:
        messagebox.showerror("Hata", f"Tarih alınırken bir hata oluştu: {e}")
        return None

def display_calendar(year, month):
    cal_text = calendar.month(year, month)
    calendar_label.config(text=cal_text)

def show_calendar():
    current_date = fetch_current_date_istanbul()
    if current_date:
        year = current_date.year
        month = current_date.month
        date_label.config(text=f"Güncel tarih: {current_date.strftime('%Y-%m-%d')}")
        display_calendar(year, month)

# Tkinter penceresi oluştur
root = tk.Tk()
root.title("İstanbul Takvimi")

# Tarih etiketini oluştur
date_label = tk.Label(root, font=('Helvetica', 16))
date_label.pack(pady=20)

# Takvim etiketini oluştur
calendar_label = tk.Label(root, font=('Courier New', 12), justify='left')
calendar_label.pack(pady=20)

# Takvimi göster butonu
show_button = tk.Button(root, text="Takvimi Göster", command=show_calendar)
show_button.pack(pady=10)

# Uygulamayı çalıştır
root.mainloop()
