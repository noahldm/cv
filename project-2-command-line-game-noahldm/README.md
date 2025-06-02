# project-2-command-line-game-noahldm

Testplan voor CLI Maze Game

Testgevallen:
1. Start van het Spel
Stap 1: Start het spel.

Verwachte Uitkomst: Het spel begint in de "start" kamer. Het doel wordt duidelijk weergegeven: "Bezoek alle kamers H, T, M, L en bereik de finish."

2. Eerste Keuze: 1 of 2
Stap 1: Kies "Links" → Ga naar room2.

Stap 2: Kies "Rechts" → Ga naar room12.

Verwachte Uitkomst: De speler wordt correct naar room2 of room12 gestuurd, afhankelijk van de gemaakte keuze.

3. Navigatie in Room2
Stap 1: Keer terug naar room1.

Stap 2: Ga naar room3.

Stap 3: Ga naar room5.

Stap 4: Ga naar room4 (dead-end).

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer. Room4 is een dead-end en stuurt de speler terug naar de start.

4. Verzamelen van Letter H in Room3
Stap 1: Verzamel letter H → Ga naar roomH.

Stap 2: Keer terug naar room2.

Verwachte Uitkomst: De letter H wordt succesvol verzameld en de speler wordt naar roomH gestuurd. Terugkeren naar room2 werkt correct.

5. Navigatie in Room5
Stap 1: Ga naar room6.

Stap 2: Probeer de finish (zonder alle letters).

Stap 3: Keer terug naar room2.

Verwachte Uitkomst: De speler kan alleen naar room6 gaan of terugkeren naar room2. Pogingen om de finish te bereiken zonder alle letters moeten worden geblokkeerd.

6. Navigatie in Room6
Stap 1: Keer terug naar room5.

Stap 2: Ga naar room7.

Stap 3: Ga naar room8.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer.

7. Verzamelen van Letter T in Room7
Stap 1: Verzamel letter T → Ga naar roomT.

Stap 2: Keer terug naar room6.

Verwachte Uitkomst: De letter T wordt succesvol verzameld en de speler wordt naar roomT gestuurd. Terugkeren naar room6 werkt correct.

8. Navigatie in Room8
Stap 1: Ga naar room10.

Stap 2: Ga naar room9 (dead-end).

Stap 3: Keer terug naar room6.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer. Room9 is een dead-end en stuurt de speler terug naar de start.

9. Navigatie in Room10
Stap 1: Keer terug naar room8.

Stap 2: Ga naar room11.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer.

10. Verzamelen van Letter M in Room11
Stap 1: Verzamel letter M → Ga naar roomM.

Stap 2: Keer terug naar room10.

Verwachte Uitkomst: De letter M wordt succesvol verzameld en de speler wordt naar roomM gestuurd. Terugkeren naar room10 werkt correct.

11. Navigatie in Room12
Stap 1: Ga naar room13.

Stap 2: Keer terug naar room1.

Stap 3: Ga naar room16.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer.

12. Navigatie in Room13
Stap 1: Keer terug naar room12.

Stap 2: Ga naar room14.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer.

13. Navigatie in Room14
Stap 1: Ga naar room15 (dead-end).

Stap 2: Keer terug naar room13.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer. Room15 is een dead-end en stuurt de speler terug naar de start.

14. Navigatie in Room16
Stap 1: Ga naar room17.

Stap 2: Keer terug naar room12.

Verwachte Uitkomst: Elke keuze leidt de speler naar de juiste kamer.

15. Verzamelen van Letter L in Room17
Stap 1: Verzamel letter L → Ga naar roomL.

Stap 2: Keer terug naar room16.

Stap 3: Ga naar room18 (dead-end).

Verwachte Uitkomst: De letter L wordt succesvol verzameld en de speler wordt naar roomL gestuurd. Room18 is een dead-end en stuurt de speler terug naar de start.

16. Finish
Stap 1: Probeer de finish te bereiken zonder alle letters.

Stap 2: Verzamel alle letters (H, T, M, L) en probeer de finish te bereiken.

Verwachte Uitkomst: De speler kan alleen de finish bereiken als alle letters zijn verzameld. Anders wordt de speler teruggeleid naar room5.