from calculator import QuickCalc

# On crée une instance de la calculatrice
ma_calculatrice = QuickCalc()

print("--- Bienvenue dans Quick-Calc ---")

# On fait une addition
resultat_addition = ma_calculatrice.add(5, 10)
print(f"5 + 10 = {resultat_addition}")

# On fait une division
resultat_division = ma_calculatrice.divide(20, 2)
print(f"La valeur actuelle (20 / 2) est de : {resultat_division}")

# On remet à zéro
ma_calculatrice.clear()
print(f"On a tout effacé ! La valeur est de nouveau : {ma_calculatrice.current_value}")
