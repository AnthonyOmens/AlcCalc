#Drink Class
class Drink:
    def __init__(alcDrink, name, floz, alcPercent):
        alcDrink.name = name
        alcDrink.floz = floz
        alcDrink.alcPercent = alcPercent
      
        
    def drinkLine(info):
        print(info.name + " is " + str(info.floz) + " fl ounces and " + str(info.alcPercent) + " percent alcohol")
        
    def pureAlcOz(info):
        return "{:.2f}".format(info.floz * info.alcPercent)
        #makes the return to the clostest 2 decimal placces
        #return info.floz * info.alcPercent
        #returns the ounces of PURE alcohol
        #ex: if return == 1.7 then that means the can/bottle has 1.7 ounces of PURE alchol


#make a func to compare the drinks        
    def pureAlcCompare(drinkUser, drinkCompare):
      return drinkUser.pureAlcOz / drinkCompare.pureAlcOz
      
      


shot = 1.5
#drinkAbout = Drink("name", floz, alcPercent)

sojuI = Drink("Soju", 12.7, .14)
budLightI = Drink("Bud Light", 16, .05)
burnettsI = Drink("Burnetts", shot, .40)

drinkList= [sojuI, budLightI, burnettsI]
#make a list of drinks to easily cycle thrugh them. Maybe make a lists of drinks and their info instead of the I vars

sojuI.drinkLine()
budLightI.drinkLine()
burnettsI.drinkLine()

print("")

print(f"sojuI.floz * sojuI.alcPercent: {sojuI.floz * sojuI.alcPercent}")
#does the same as sojuI.pureAlcOz()

print("")

print(f"sojuI.pureAlcOz(): Soju has {sojuI.pureAlcOz()} oz of pure alcohol")

print(f"budLightI.pureAlcOz(): Bud Light has {budLightI.pureAlcOz()} oz of pure alcohol")

print(f"burnettsI.pureAlcOz(): Burnetts has {burnettsI.pureAlcOz()} oz of pure alcohol")

# make inputs. 
# What are you drinking? (pick one)

userDrink = input(f"What are you drinking?\n{sojuI.name}, {budLightI.name}, {burnettsI.name}\nPlease type EXACT name\n")

drinkAmount = 1
#we'll make the input later

# userDrink = name of drink

for x in drinkList:
  if userDrink == str(x.name):
    userDrink = x

print(f"Your drink is {userDrink.name}, with {userDrink.floz} ounces and {userDrink.alcPercent}% of alcohol")

# How many bottles/cans

#HERE make a loop that changes the string input of userDrink to the exact drink var name

for x in drinkList:
  print("start of For Loop")
  if x.name == userDrink:
    print("x.name = {x.name}")
    userDrink = x.name
    print(f"userDrink = {userDrink}")




for x in drinkList:
  if userDrink.name != x.name:
    print(f"{drinkAmount} {userDrink.name} is equal to {userDrink.pureAlcOz} / {x.pureAlcOz()} {x.name}s")
#fix this ^^^^
#-------------------

# print: x amount of drinkAnswer is equal to x ammount of drink1 and x ammount of drink 2. #maybe do a forLoop here to cycle through the drinks when I add more
# dont print drinkAnswer since they already typed that in