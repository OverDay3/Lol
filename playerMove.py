def posX(x, arrMove, speed):
	diag = False
	if arrMove[0] != arrMove[1] and arrMove[2] != arrMove[3]: diag = True

	if diag == False:
		if arrMove[2] == True: x -= speed
		if arrMove[3] == True: x += speed
	elif arrMove[2] != arrMove[3]:
		if arrMove[2] == True: x -= speed / 1.4
		if arrMove[3] == True: x += speed / 1.4

	return x

def posY(y, arrMove, speed):
	diag = False
	if arrMove[0] != arrMove[1] and arrMove[2] != arrMove[3]: diag = True

	if diag == False:
		if arrMove[0] == True: y -= speed
		if arrMove[1] == True: y += speed
	elif arrMove[0] != arrMove[1]:
		if arrMove[0] == True: y -= speed / 1.4
		if arrMove[1] == True: y += speed / 1.4

	return y