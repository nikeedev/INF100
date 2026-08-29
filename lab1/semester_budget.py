budget = int(input("Hva er budsjettet ditt?\n"))
bolig = int(input("Hvor mye bruker du på bolig?\n"))
mat = int(input("Hvor mye bruker du på mat?\n"))

kaffe_pris = 45

igjen = budget - (bolig + mat)

print(f"Det er {igjen} NOK igjen, det er nok til {igjen//kaffe_pris} kopper kaffe!")
