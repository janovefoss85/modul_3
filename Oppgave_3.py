#Mål: bruke aritmetiske operatorer (+,-,*,/) på variabler.
brus = 24.90
smørbrød = 45
banan = 8.50
#regn ut og skriv ledeteksten på hver utskrift
# Totalsum alle tre varene
total = brus + smørbrød + banan
print("Totalsum:", total)
total_mva = total * 1.25
print("Totalsum med mva:", total_mva)
per_person = total / 4
print("Pris per person:", per_person)
forskjell = smørbrød - banan
print("Prisforskjell:", forskjell)
# --- Refleksjon ---
# Når jeg la sammen heltall og desimaltall ble resultatet float.
# Når jeg delte på fire ble det også float, fordi / alltid gir desimaltall.
# Variabler er nyttige fordi jeg kan endre prisen ett sted, og alt oppdateres automatisk.