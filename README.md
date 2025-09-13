# ⏰ Smart Multi-Alarm Clock with Snooze

A modern Python GUI Alarm Clock built with Tkinter, featuring:

- Multiple alarms 📅
- Smart scheduling (automatically sets for tomorrow if time has passed) 🔮
- Snooze support 😴
- Live clock ⌚
- Alarm sound loop 🔊

---

## ✨ Features

✅ Add unlimited alarms  
✅ Remove alarms easily  
✅ Smart scheduling (today or tomorrow)  
✅ Snooze alarms (default 5 minutes, customizable)  
✅ Stop alarms manually  
✅ Beautiful Tkinter interface  
✅ Status messages and real-time clock  

---

## 📸 Screenshots

_Add your screenshots here_

- Main Interface  
- Alarm Ringing  

---

## 🚀 Installation

### Requirements
- Python 3.7+  
- Windows (uses `winsound` for alarm sound)  
- On Linux/macOS, replace `winsound` with `playsound` or `pygame`.  

### Clone the Repository
```bash
git clone https://github.com/yourusername/alarm-clock.git
cd alarm-clock
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Requirements File
`requirements.txt` should include:

```
tk
```

(`winsound` is built into Windows, no install needed)

---

## 🎵 Setup Alarm Sound

Place a sound file named `sound.wav` in the project folder.  
You can use any `.wav` file, for example a ringtone or beep sound.

---

## ▶️ Usage

Run the script:

```bash
python alarm_clock.py
```

### How It Works
- Choose Hour, Minute, Second from the dropdown menus.  
- Click **Add Alarm ➕** to schedule it.  
- Your alarms appear in the list.  
- When the alarm time comes:  
  - The alarm rings 🔊  
  - Status label shows “⏰ Alarm Ringing!”  
  - You can Stop or Snooze it.  
  - Snoozed alarms are automatically rescheduled for +5 minutes.  

---

## ⚡ Roadmap

- Custom snooze duration input  
- Support for multiple sounds  
- Cross-platform sound support (Linux/macOS)  
- Save alarms even after closing the app  

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License © 2025 [Your Name]  
