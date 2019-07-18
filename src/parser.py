# parses "<div class="qwe">qweqwe</div>" to "qweqwe"
def parser(tags):
	ans = []
	word = ''
	for tag in tags:
		ch = False
		uch = False
		tag = str(tag)
		for letter in tag:
			if letter == '>':
				ch = False
				uch = True
				continue
			
			if ch == True:
				continue

			if letter == '<':
				ch = True
				continue

			if uch == True:
				uch = False
				word += ' '

			word += letter

	ans = word.split(' ')

	i = 0
	while i < len(ans):
		if ans[i] == '' or ans[i] == '\n':
			ans.remove(ans[i])
			i -= 1
		i += 1 

	return ans
			