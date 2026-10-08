# Mål sammenliginingsoperatorer og forstå at de gir true eller false
alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30
# Jeg tror alder >= aldersgrense blir: True
print("Er alder >= aldersgrense?", alder >= aldersgrense)
# Jeg tror alder == 31 blir: True
print("Er alder == 31?", alder == 31)   
# Jeg tror alder != aldersgrense blir: True
print("Er alder != aldersgrense?", alder != aldersgrense)   
# Jeg tror alder <= aldersgrense blir: False
print("Er alder <= aldersgrense?", alder <= aldersgrense)   
#Jeg tror navn == "Michael" blir: True
print("Er navn == 'Michael'?", navn == "Michael")
#Jeg tror navn == "michael" blir: False
print("Er navn == 'michael'?", navn == "michael")
# antall_studenter >=30 blir: True
print("Er antall_studenter >= 30?", antall_studenter >= 30) 
# alder + 5 > antall_studenter blir: True
print("Er alder + 5 > antall_studenter?", alder + 5 >   antall_studenter)           
# Uttrykk 5 og 6 er ulike fordi Python skiller mellom store og små bokstaver.   
#Forskjellen på = og == er at = brukes for å tilordne en verdi til en variabel, mens == brukes for å sammenligne to verdier.    
# Python utfører først alder + 5 og deretter sammenligner resultatet med antall_studenter.  
# True/False er nyttige slik at pyhton kan ta et valg.