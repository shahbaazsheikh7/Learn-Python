#Exercise 5: Write a program which prompts the user for a Celsius tem-
#perature, convert the temperature to Fahrenheit, and print out the
#converted temperature.

cel = input("Enter celsius temperature: ")
try:
    cel_i = int(cel)
    fahr = 9 * (cel_i + 32) / 5
    print("Fahrenheit temp: " + str(fahr))

except:
    print("Number dalo chupchap.")
    
