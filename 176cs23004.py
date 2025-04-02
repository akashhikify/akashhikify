def vowel(text):
    vowels="aeiou AEIOU"
    print("length=",len([letter for letter in text if letter in vowels]))
    print("vowel=",([letter for letter in text  if letter in vowels]))
vowel("computer science")
    