
m = int(input("Enter your obtained mark:"))

if m >= 80:
  if m >= 90:
    print("Congratulations You get Golden A+")
  else:
    print("Congratulations You get A+")
elif m>=60:
  if m>=70:
    print("You can do better i Believe, Your Obtained Grade is : B+")
  else:
    print("You can do better i Believe, Your Obtained Grade is : B")
elif m>=40:

  if m>=50:
    print("Try harder, Your Obtain Grade is : C")
  else:
    print("You Passed the Examination,Study More,I believe You can do far more better")
else:
    print("You Failed")

