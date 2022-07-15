#Drink Class
class Drink:
  
    def __init__(alcDrink, name, floz, alcPercent):
        alcDrink.name = name
        alcDrink.floz = floz
        alcDrink.alcPercent = alcPercent
        alcDrink.pureAlcOz = "{:.2f}".format(alcDrink.floz * alcDrink.alcPercent)
      
        
    def drinkLine(info):
        print(info.name + " is " + str(info.floz) + " fl ounces and " + str(info.alcPercent) + " percent alcohol")
        
    # def pureAlcOz(info):
    #     return "{:.2f}".format(info.floz * info.alcPercent)
        #makes the return to the clostest 2 decimal placces
        #return info.floz * info.alcPercent
        #returns the ounces of PURE alcohol
        #ex: if return == 1.7 then that means the can/bottle has 1.7 ounces of PURE alchol
    #^^^^ turns now I dont need this anymore, ill delete later!!


#make a func to compare the drinks        
    def pureAlcCompare(drinkUser, drinkCompare):
      return drinkUser.pureAlcOz / drinkCompare.pureAlcOz


  # def drinkInputToDrinkI(x):
  #   return {
  #     "Soju" : sojuI,
  #     "Bud Light" : budLightI,
  #     "Burnetts" : burnettsI,
  #   }
  # There was an attempt to make a dict but then I would need to take care of 3 Libraries of drinks. I got it down to 2, going to shoot for 1 in the future
      


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
# next time make this a for loop!!!


print("")

print(f"sojuI.floz * sojuI.alcPercent: {sojuI.floz * sojuI.alcPercent}")
#does the same as sojuI.pureAlcOz

print("")

print(f"sojuI.pureAlcOz: Soju has {sojuI.pureAlcOz} oz of pure alcohol")

print(f"budLightI.pureAlcOz: Bud Light has {budLightI.pureAlcOz} oz of pure alcohol")

print(f"burnettsI.pureAlcOz: Burnetts has {burnettsI.pureAlcOz} oz of pure alcohol")

# make inputs. 
# What are you drinking? (pick one)

userDrink = input(f"What are you drinking?\n{sojuI.name}, {budLightI.name}, {burnettsI.name}\nPlease type EXACT name\n")

drinkAmount = 1


#print(f"drinkInputToDrinkI {drinkInputToDrinkI(userDrink).alcPercent}")

#we'll make the input later

# userDrink = name of drink

for x in drinkList:
  if userDrink == str(x.name):
    userDrink = x

print(f"Your drink is {userDrink.name}, with {userDrink.floz} ounces and {userDrink.alcPercent}% of alcohol")

# How many bottles/cans

#HERE make a loop that changes the string input of userDrink to the exact drink var name

#print("The type is userDrink.pureAlcOz : ", type(userDrink.pureAlcOz))


for x in drinkList:
  if userDrink.name != x.name:
    pureAlcOzDivision = "{:.2f}".format(float(userDrink.pureAlcOz) / float(x.pureAlcOz))
    print(f"{drinkAmount} {userDrink.name} is equal to {pureAlcOzDivision} {x.name}s")
#This now works!!!
#-------------------

# print: x amount of drinkAnswer is equal to x ammount of drink1 and x ammount of drink 2. #maybe do a forLoop here to cycle through the drinks when I add more
# dont print drinkAnswer since they already typed that in