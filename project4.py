while True:
  zip_code = input("enter your zip code:  ")
  a = len(zip_code)

  if a == 5 and zip_code.isdigit():

    print("your entry is valid")
    break
  else:
    print("Please enter a valid entry")

