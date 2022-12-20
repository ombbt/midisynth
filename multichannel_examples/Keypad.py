def readkeypad(self):
#	TRANSPOSE =int(os.getenv('TRANSPOSE'))
	global offset
	global lightonoff
	global mode
	syn = False
	for i in range(len(rows)):
		GPIO.setup(rows[i], GPIO.OUT, initial = GPIO.LOW)
		for j in range(len(cols)):
			keycode = i * len(cols) +j
			newval = GPIO.input(cols[j]) == GPIO.LOW
			keypressed = keymap[j][i]
			syn = True
			if newval and not keycode in pressed:
				pressed.add(keycode)
				if keycode == 0:  #Keypad '1'
					if mode == False:
						#initran = 5
						#tran = initran + offset
						print(type(tran))
						#os.putenv(TRANSPOSE,4)      #ddlk
						#os.environ['TRANSPOSE'] = 2
						#switch_scene(1, subscene=None)
						display.lcd_display_string("hit the road jack", 1)
						display.lcd_display_string("m:1  tr:5 ", 2)
						#print("TRANSPOSE= ", TRANSPOSE, "  initran=", initran, " offset= ", offset )
					elif mode == True:
						print('scene 13')
						display.lcd_display_string("scene 13 vide    ", 1)
						display.lcd_display_string("m:2  tr:  ", 2)

						#switch_scene(13, subscene=None)
				elif keycode == 1:
					if mode == False:
						#switch_scene(4, subscene=None)
						print("scene 4")
						display.lcd_display_string("  if you feel it  ", 1)
						display.lcd_display_string("m:1  tr:1 ", 2)

					elif mode == True:
						print("scene 16")
						display.lcd_display_string("scene 16 vide     ", 1)
						display.lcd_display_string("m:2  tr:  ", 2)

						#switch_scene(16, subscene=None)
					#switch_scene(4, subscene=None)
				elif keycode == 2:
					if mode == False:
						print("scene 7")
						display.lcd_display_string("   bad girls    ", 1)
						display.lcd_display_string("m:1  tr:10", 2)

						switch_scene(7, subscene=None)
					elif mode == True:
						print("scene 19 ")
						display.lcd_display_string("scene 19  vide   ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(19, subscene=None)
				elif keycode == 3:
					if mode == False:
						print("can't stand loosing you")
						display.lcd_display_string("   the police   ", 1)
						display.lcd_display_string("m:1  tr:10", 2)

						#switch_scene(10, subscene=None)
					elif mode == True:
						synthmode()

				elif keycode == 4:	#scene 2
					if mode == False:
						#switch_scene(2, subscene=None)
						display.lcd_display_string("   billie jean  ", 1)
						display.lcd_display_string("m:1  tr:9", 2)

					elif mode == True:
						print("scene 14")
						display.lcd_display_string("scene 14 vide    ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(, subscene=None)
				elif keycode == 5:
					if mode == False:
						#print("scene 5")
						display.lcd_display_string(" feel goood inc ", 1)
						display.lcd_display_string("m:1  tr:8 ", 2)

						#switch_scene(5, subscene=None)
					elif mode == True:
						display.lcd_display_string("scen17 vide      ", 1)
						display.lcd_display_string("m:2  tr:", 2)
						print("scene 17")
						#switch_scene(, subscene=None)
				elif keycode == 6:
					if mode == False:
						print("scene 8")
						display.lcd_display_string("loose yourself danc", 1)
						display.lcd_display_string("m:1  tr:3 ", 2)

						switch_scene(8, subscene=None)
					elif mode == True:
						display.lcd_display_string("scene 20 vide    ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(, subscene=None)
				elif keycode == 7:
					if mode == False:
						print("scene F")
						display.lcd_display_string("   solo clean   ", 1)
						display.lcd_display_string("m:1  tr:5 ", 2)

						switch_scene(11, subscene=None)
					elif mode == True:
						#display.lcd_display_string("  y.GRANPIANO   ", 1)
						#display.lcd_display_string("m:2  tr:0", 2)

						#switch_scene(23, subscene=None)
						#print("scene F mode 2 YAMAHA GRANPIANO")
						pianomode()
				elif keycode == 8: #scene 3
					if mode == False:
						display.lcd_display_string("    Automatic   ", 1)
						display.lcd_display_string("m:1  tr:7 ", 2)

						switch_scene(3, subscene=None)
					elif mode == True:
						print("scene15")
						display.lcd_display_string("scene 15 vide    ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(, subscene=None)
				elif keycode == 9:
					if mode == False:
						display.lcd_display_string("the next episode", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)

						print("scene 6")
						#switch_scene(6, subscene=None)
					elif mode == True:
						bassemode()

				elif keycode == 10:
					if mode == False:
						print("scene 9")
						display.lcd_display_string("     finaly    ", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)

						#switch_scene(9, subscene=None)
					elif mode == True:
						organmode()

				elif keycode == 11:
					if mode == False:
						print("scene E")
						display.lcd_display_string("   solo satu   ", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)

						#switch_scene(12, subscene=None)
					elif mode == True:
						print("scene E mode2, Full Talkbox")
						#switch_scene(24, subscene=None)
						display.lcd_display_string(" TalkBox Mode  ", 1)
						display.lcd_display_string("m:2  tr:0 ", 2)

				elif keycode == 12:
					display.lcd_display_string("AutoDestruction ", 1)
					display.lcd_display_string("      !!!!       ", 2)

					print("autodestruction")
					global timmer1
					timmer1 = time.process_time()
					timmer1 = timmer1 +0.09 
					print("timmer1", timmer1)
				elif keycode == 13:
					if mode == False:
						if lightonoff == False:
							lightonoff = True
							print("light On")
							display.lcd_display_string("m:1  tr:   li:ON   ", 2)

						elif lightonoff == True:
							lightonoff = False
							print("light Off")
							display.lcd_display_string("m:1  tr:   li:OFF   ", 2)

					elif mode == True:
						if offset < 11:
							offset = offset +1
							transposescene()
				elif keycode == 14: 
					if mode == False:
						print("eating banana")
						display.lcd_display_string(" Eating Banana  ", 1)

					elif mode == True:
						if offset > 0:
							offset = offset -1
							transposescene()

				elif keycode == 15:
					if mode ==False:
						mode = True
						print("switch to mode 2")
						display.lcd_display_string("m:2  tr:", 2)

					elif mode == True:
						mode = False
						print("switch to mode 1")
						display.lcd_display_string("m:1  tr:", 2)

			elif not newval and keycode in pressed:
				pressed.discard(keycode)
				syn = True
				#	print('relaese')
				global timmer2
				timmer2 = time.process_time()
				#print("timmer1:", timmer1)
				#print("timmer2:", timmer2)
				if keycode == 12 and timmer2 > timmer1:
					print("explosed")
					display.lcd_display_string("    EXPLOSED    ", 1)
					display.lcd_display_string("################", 2)

		GPIO.setup(rows[i], GPIO.IN)

