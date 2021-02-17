lives = int(input("Please enter the number of lives.\n"))
energy = int(input("Please enter the energy level.\n"))
shield = int(input("Please enter the shield level.\n"))

print("Beep's health has been set.")

livesHeart = "\u2764" * lives
energyDiamond = "\u2756" * energy
shieldDiamond = "\u2756" * shield

print(f"""
Lives:   {livesHeart}
Energy:  {energyDiamond}
Shield:  {shieldDiamond}
""")



