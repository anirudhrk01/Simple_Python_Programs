s=str(input("enter a string :"))



def count_vowels_and_consonants(s):
    
    vowels="aeiouAEIOU"
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count=0
    consonant_count=0
    
    for char in s:
        if char in vowels:
            vowel_count+=1
        elif char in consonants:
            consonant_count+=1
        
    return vowel_count, consonant_count

print("vowel count and consonant count is :",count_vowels_and_consonants(s))
       