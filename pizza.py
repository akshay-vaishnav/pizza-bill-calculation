print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# small_prize = 15
# medium_prize = 20
# large_prize = 25
Pepperoni_S = 2
Pepperoni_ML = 3
cheese = 1


if size == "S":
  if add_pepperoni == "Y":
    final_p = 15 + 2
  else :
    final_p = 15
  if extra_cheese == "Y" :
    final_p = final_p + 1
  print(f"Your final bill is: ${final_p}")

if size == "M":
  if add_pepperoni == "Y":
    final_p = 20 + 3
  else :
    final_p = 20
  if extra_cheese == "Y" :
    final_p = final_p + 1
  print(f"Your final bill is: ${final_p}")


if size == "L":
  if add_pepperoni == "Y":
    final_p = 25 + 3
  else :
    final_p = 25
  if extra_cheese == "Y" :
    final_p = final_p + 3
  print(f"Your final bill is: ${final_p}")

  # or you can do in this easy way also

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}.")

    
    
  
