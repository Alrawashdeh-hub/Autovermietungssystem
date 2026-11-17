buchungen = []
autos = {
    "BMW": 80,
    "Mercedes": 100,
    "Audi": 70
}

kunde = input("Wie heißt du? ")
print(f"Wilkommen, {kunde}!")

auswahl = input("welches Auto möchten Sie mieten?")
if auswahl in autos:
    print(f"{auswahl} ist verfügbar")
    tagespreis = autos[auswahl]
    try:
        tage = int(input("Wieviele Tage möchten Sie das Auto mieten? "))
    except ValueError:
        print("ungültige Eingabe! Bitte eine zahl eingeben.")
    else:
        if tage > 0:
            print(tage)
            gesamtpreis = tage * tagespreis
            print(f"Gesamtpreis: {gesamtpreis} Euro")
            if tage >= 7:
                endpreis = gesamtpreis * 0.90
            else:
                endpreis = gesamtpreis
            print(f"Endpreis: {endpreis} Euro")
            bestaetigung = input("Möchten Sie die buchung bestätigen? (ja/nein): ")
            if bestaetigung.lower() == "ja":
                print("Buchung erfolgreich Bestätigt")
                buchung = {"kunde": kunde}
                buchung["auto"] = auswahl
                buchung["tage"] = tage
                buchung["endpreis"] = endpreis
                buchungen.append(buchung)
            else:
                print("Buchung wurde nicht Bestätigt.")
        else:
            print("ungültige Mietdauer")
else:
    print(f"{auswahl} ist nicht verfügbar")

print(autos)
for auto, preis in autos.items():
    print(f"{auto}: {preis} Euro")

for buchung in buchungen:
    print("kunde:", buchung["kunde"])
    print("auto:", buchung["auto"])
    print("tage:", buchung["tage"])
    print("endpreis:", buchung["endpreis"])
