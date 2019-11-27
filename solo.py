def make_word():
	word =""
	for ch in "сука бля пиздец":
		word +=ch
		yield word 

print(list(make_word()))