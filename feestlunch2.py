# Feestlunch opdracht

# De aantallen van onderdelen die gebruikt worden in de opdracht.
aantal_c = 17
aantal_b = 2
aantal_k = 3

# De prijzen en aftrek van onderdelen die gebruikt worden in de opdracht.
prijs_c = 0.39
prijs_b = 2.78
aftrek_k = 0.50

# Kortere variabelen om formules in de tekst te verminderen.
total_c = aantal_c * prijs_c
total_b = aantal_b * prijs_b
korting = aantal_k * aftrek_k

# Variabele maken voor de totale prijs
prijs_total = total_c + total_b - korting

# De totale prijs
print(total_c + total_b - korting)

# Tekst voor vervolg opdracht.
print ("'De feestlunch kost je bij de bakker "
+ str(prijs_total) + " voor de " + str(aantal_c) + 
" croissantjes en de " + str(aantal_b) + " stokbroden als de "
 + str(aantal_k) + " kortingsbonnen nog geldig zijn!'")