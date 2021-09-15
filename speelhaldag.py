# Speelhaldag opdracht

# Values
ticket = 7.45
vr = 0.37
vr_time = 9
vr_time_min = 45


aantal_m = 4

# Totaal prijs berekening
prijs_total = aantal_m * (ticket + (vr * vr_time))

# Berekening
print(aantal_m * ticket + (vr * vr_time))

# Tekst voor vervolg opdracht
print("'Dit geweldige dagje-uit met " + str(aantal_m) +
 " mensen in de SPeelhal met " + str(vr_time_min) + 
 " minuten VR kost je maar " + str(prijs_total) + " euro'")