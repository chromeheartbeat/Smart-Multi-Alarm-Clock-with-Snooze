import datetime
import time
import winsound
import threading
from tkinter import *

# Create Object
root = Tk()
root.geometry("520x430")
root.title("Smart Multi-Alarm Clock with Snooze")

alarms = []   # list to store alarms as datetime objects
ringing_alarm = None  # keeps track of which alarm is ringing

# --- FUNCTIONS ---
def update_time():
    """Update current time label every second."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lbl_current_time.config(text=f"Current Time: {current_time}")
    root.after(1000, update_time)

def add_alarm():
    """Add new alarm to list (handles tomorrow scheduling)."""
    now = datetime.datetime.now()
    set_time_str = f"{hour.get()}:{minute.get()}:{second.get()}"
    set_time = datetime.datetime.strptime(set_time_str, "%H:%M:%S").time()

    # Combine today's date with chosen time
    alarm_datetime = datetime.datetime.combine(now.date(), set_time)

    # If time already passed today, schedule for tomorrow
    if alarm_datetime <= now:
        alarm_datetime += datetime.timedelta(days=1)

    # Add to list if not already present
    if alarm_datetime not in alarms:
        alarms.append(alarm_datetime)
        alarms.sort()
        update_alarm_listbox()
        lbl_status.config(text=f"Alarm set for {alarm_datetime}", fg="green")
    else:
        lbl_status.config(text=f"Alarm already exists!", fg="orange")

def remove_alarm():
    """Remove selected alarm from list."""
    selected = alarm_listbox.curselection()
    if selected:
        index = selected[0]
        alarm_time = alarms[index]
        alarms.remove(alarm_time)
        update_alarm_listbox()
        lbl_status.config(text=f"Removed alarm: {alarm_time}", fg="red")
    else:
        lbl_status.config(text="No alarm selected", fg="orange")

def update_alarm_listbox():
    """Refresh the alarm list display."""
    alarm_listbox.delete(0, END)
    for alarm in alarms:
        alarm_listbox.insert(END, alarm.strftime("%Y-%m-%d %H:%M:%S"))

def start_alarm_checker():
    """Start background thread for checking alarms."""
    t1 = threading.Thread(target=check_alarms, daemon=True)
    t1.start()

def check_alarms():
    """Continuously check if any alarm matches current time."""
    global ringing_alarm
    while True:
        time.sleep(1)
        now = datetime.datetime.now().replace(microsecond=0)
        if now in alarms:
            ringing_alarm = now
            lbl_status.config(text=f"⏰ Alarm ringing: {now.strftime('%H:%M:%S')}", fg="red")
            winsound.PlaySound("sound.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            alarms.remove(now)
            update_alarm_listbox()

def stop_alarm():
    """Stop alarm sound."""
    global ringing_alarm
    winsound.PlaySound(None, winsound.SND_PURGE)
    if ringing_alarm:
        lbl_status.config(text=f"Alarm at {ringing_alarm.strftime('%H:%M:%S')} stopped", fg="black")
        ringing_alarm = None
    else:
        lbl_status.config(text="No alarm ringing", fg="black")

def snooze_alarm(minutes=5):
    """Snooze current ringing alarm by X minutes."""
    global ringing_alarm
    if ringing_alarm:
        stop_alarm()
        new_alarm = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
        alarms.append(new_alarm.replace(microsecond=0))
        alarms.sort()
        update_alarm_listbox()
        lbl_status.config(text=f"Snoozed for {minutes} minutes (next at {new_alarm.strftime('%H:%M:%S')})", fg="blue")
    else:
        lbl_status.config(text="No alarm ringing to snooze", fg="orange")

# --- UI ELEMENTS ---
Label(root, text="Smart Multi-Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)

lbl_current_time = Label(root, text="", font=("Helvetica 12"))
lbl_current_time.pack()

Label(root, text="Set Time:", font=("Helvetica 15 bold")).pack(pady=5)

frame = Frame(root)
frame.pack()

# Hour dropdown
hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]  # 00–23
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minute dropdown
minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]  # 00–59
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Second dropdown
second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]  # 00–59
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

# Buttons
Button(root, text="Add Alarm", font=("Helvetica 12"), command=add_alarm).pack(pady=5)
Button(root, text="Remove Selected Alarm", font=("Helvetica 12"), command=remove_alarm).pack(pady=5)
Button(root, text="Stop Alarm", font=("Helvetica 12"), command=stop_alarm).pack(pady=5)
Button(root, text="Snooze 5 min", font=("Helvetica 12"), command=lambda: snooze_alarm(5)).pack(pady=5)

# Alarm List
Label(root, text="Your Alarms:", font=("Helvetica 12 bold")).pack(pady=5)
alarm_listbox = Listbox(root, width=35, height=6, font=("Helvetica 12"))
alarm_listbox.pack()

lbl_status = Label(root, text="", font=("Helvetica 12"))
lbl_status.pack(pady=5)

# Start updating time & checking alarms
update_time()
start_alarm_checker()

# Run Tkinter loop
root.mainloop()
