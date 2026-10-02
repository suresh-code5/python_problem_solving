word=input("enter a word : ")
digit_count=0
vowel_count=0
consonent_count=0
special_char_count=0
digits=["0","1","2","3","4","5","6","7","8","9"]
special_char=["!","@","#","₹","%","^","&","*","(",")","-",":",";","?","<",">"]
vowels=["a","e","i","o","u"]
for char in word:
	if char in digits:
		digit_count+=1
	elif char in special_char:
		special_char_count+=1			
	elif char in vowels:
		vowel_count+=1
	else:
			consonent_count+=1
print(f"no.of digits are {digit_count}")
print(f"no.of special characters are {special_char_count}")			
print(f"no.of vowels are {vowel_count}")			
print(f"no.of consonents are {consonent_count}")			
			
















