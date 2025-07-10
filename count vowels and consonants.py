#Count Vowels and Consonants

str=input("enter str:")
vowel_count=0
consonants_count=0
vowels="aeiouAEIOU"
for char in str:
    if char in vowels:
        vowel_count+=1
    else:
        consonants_count+=1
print("vowel_count:",vowel_count)
print("consonants_count:",consonants_count)
