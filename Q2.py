word="Statement And Count Every Character Occurrence"
alphabets = sum(not chr.isspace() for chr in word)
word=word.lower()
s=word.count("a")
t=word.count("e")
a=word.count("i")
z=word.count("o")
u=word.count("u")
vowels=s+t+a+z+u
print(f"vowels count = {vowels}")
consonants=alphabets-vowels
print(f'The consonants are : {consonants}')

