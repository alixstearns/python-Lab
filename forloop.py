num_v=0
num_c=0
a=input("enter a string:  ")
for i in a.strip():
    print(i)
    if i in ['a', 'e', 'i', 'o', 'u']:
       print(f"{i} is a vowel")
       num_v+=1

    else:
        print(f"{i} is a consonant")
        num_c+=1
print(f"number is a vowel is: {num_v}")
print(f"number of consonant is: {num_c}")

