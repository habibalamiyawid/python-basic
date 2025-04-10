
day = int(input("Enter number of the day: "))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid Number,Because there are 7 days in a week,which starts from Monday")
    #underscore character _ as the last case value if you want a code block to execute when there are not other matches