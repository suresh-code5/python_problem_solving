name=input("enter a word : ")
fir_pro=0
sec_pro=0
letter=""
for char in name:
	for char2 in name:
		if char==char2:
			sec_pro+=1
	if sec_pro>=fir_pro:
		fir_pro=sec_pro
		letter=char
	sec_pro=0
print(f"The highest frequency of letters are {letter} ",fir_pro)		
		
	














