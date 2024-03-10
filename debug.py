zip_code = input("Enter your zip code: ").strip()

if len(zip_code) == 5 and zip_code.isdigit():
    print("Your entry is valid")
else:
    print("Please enter a valid entry")
