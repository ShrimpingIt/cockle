from deployall import run

count = 0

while True:
	print("Flashing cockle " + str(count))
	run()
	count += 1
