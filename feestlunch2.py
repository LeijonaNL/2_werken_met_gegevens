# Feestlunch opdracht

# De aantallen van onderdelen die gebruikt worden in de opdracht.
aantal_c = 17
aantal_b = 2
aantal_k = 3

# De prijzen en aftrek van onderdelen die gebruikt worden in de opdracht.
prijs_c = 0.39
prijs_b = 2.78
aftrek_k = 0.50

# Test
total_c = aantal_c * prijs_c
total_b = aantal_b * prijs_b
korting = aantal_k * aftrek_k


print(total_c + total_b - korting)