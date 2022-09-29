import ctypes


from datetime import date
today = date.today()
todayDate = today.strftime("%d-%m-%y")


lib = ctypes.windll.kernel32
 

t = lib.GetTickCount64()
print(t)


t = int(str(t)[:-3])
print(t)


minutes, seconds = divmod(t, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)


with open("timer.log", "a") as file:
	file.write(f"{todayDate} - {hours}:{minutes}:{seconds}\n")
	
print(f"{hours}:{minutes}:{seconds}")