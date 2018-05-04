Automatisierte Datenauswertung mit Python
=========================================

Hintergrund
-----------

Der QuantiFERON-TB Gold Plus (QFT) Test ist ein von der Firma Qiagen
vertriebenes Kit, das in der medizinischen Mikrobiologie zum Nachweis von
Tuberkulose-Infektionen verwendet wird.

Tuberkulose wir durch eine Infektion mit Mykobakterien (Arten:
*M. tuberculosis*, *M. bovis*, *M. africanum*) verursacht. Im Zuge der
Infektion kommt es als Teil der Immunantwort zur Bildung von T-Zellen, die auf
Stimulation durch erregerspezifische Peptide mit der Ausschüttung von
Interferon Gamma (IFN-γ) antworten.

Der QFT-Test macht sich diesen Aspekt der Immunantwort zunutze: Vollblutproben
von Patienten mit Verdacht auf Tuberkuloseinfektion werden für 16-24h mit einem
Tuberkulose-Erreger-Peptidcocktail inkubiert. Anschließend wird der
IFN-γ-Spiegel im Plasma der Proben bestimmt.

Um die Aussagekraft des Tests zu erhöhen, werden jedem Patienten 4 Blutproben
abgenommen:

- eine Probe als Negativkontrolle, die **nicht** mit erregerspezifischen
  Peptiden stimuliert wird

  .. admonition:: Rolle im Test:
  
     Ergibt sich im weiteren Testverlauf für diese Probe ein erhöhter
     IFN-γ-Spiegel, kann der gesamte Test für diesen Patienten nicht
     interpretiert werden.
  
- eine Probe, die als Positivkontrolle mit Mitogenen inkubiert wird, die auch
  bei Nichtinfizierten die Ausschüttung von IFN-γ stimulieren
  
  .. admonition:: Rolle im Test:
  
     Ergibt sich im weiteren Testverlauf für diese Probe ein aufällig niedriger
     IFN-γ-Spiegel kann eine Tuberkuloseinfektion auch bei ansonsten negativem
     Testergebnis nicht ausgeschlossen werden. Der Patient könnte z.B.
     immunsupprimiert sein.
  
- zwei Testproben

  Diese beiden Proben werden nach der Entnahme mit leicht unterschiedlichen
  Peptidcocktails inkubiert, die verschiedene Subpopulationen von T-Zellen
  stimulieren sollen.
  
  .. admonition:: Rolle im Test:
  
     Ergibt sich für *eine* der beiden Testproben ein erhöhter IFN-γ-Spiegel,
     gilt der Test bei entsprechenden Ergebnissen der Negativ- und
     Positivkontrollen als positiv und das Vorliegen einer Tuberkuloseinfektion
     als wahrscheinlich.
  
-----

Testauswertung
--------------

Die Bestimmung der IFN-γ-Spiegel erfolgt für bis zu 22 Patienten parallel
in 96-Well-Mikrotiterplatten. Von den Details des Bestimmungsverfahrens ist in
unserem Zusammenhang lediglich von Bedeutung, dass es sich um ein
photometrisches Verfahren handelt, bei dem die optische Dichte (OD) der Proben
bei einer vorgegebenen Lichtwellenlänge bestimmt wird. Zur Umrechnung der
OD-Werte in internationale IFN-γ-Einheiten pro ml (IU/ml) müssen diese noch in
Bezug zu den OD-Werten einer Verdünnungsreihe eines IFN-γ-Standards bekannter
Konzentration gesetzt werden, die auf derselben Mikrotiterplatte gemessen
wurde.

Datenformat
...........

Eine mögliche Plattenbelegung mit den jeweils vier Proben von 22 Patienten und
4 (jeweils in Duplikaten aufgetragenen) Verdünnungen des IFN-γ-Standards sieht
z.B. so aus:

+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| <>| 1   | 2   | 3   | 4   | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   |
+===+=====+=====+=====+=====+======+======+======+======+======+======+======+======+
| A | 1-N | 3-N | 5-N | 7-N | 9-N  | S1   | S1   | 13-N | 15-N | 17-N | 19-N | 21-N |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| B | 1-1 | 3-1 | 5-1 | 7-1 | 9-1  | S2   | S2   | 13-1 | 15-1 | 17-1 | 19-1 | 21-1 |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| C | 1-2 | 3-2 | 5-2 | 7-2 | 9-2  | S3   | S3   | 13-2 | 15-2 | 17-2 | 19-2 | 21-2 |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| D | 1-M | 3-M | 5-M | 7-M | 9-M  | S4   | S4   | 13-M | 15-M | 17-M | 19-M | 21-M |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| E | 2-N | 4-N | 6-N | 8-N | 10-N | 11-N | 12-N | 14-N | 16-N | 18-N | 20-N | 22-N |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| F | 2-1 | 4-1 | 6-1 | 8-1 | 10-1 | 11-1 | 12-1 | 14-1 | 16-1 | 18-1 | 20-1 | 22-1 |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| G | 2-2 | 4-2 | 6-2 | 8-2 | 10-2 | 11-2 | 12-2 | 14-2 | 16-2 | 18-2 | 20-2 | 22-2 |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+
| H | 2-M | 4-M | 6-M | 8-M | 10-M | 11-M | 12-M | 14-M | 16-M | 18-M | 20-M | 22-M |
+---+-----+-----+-----+-----+------+------+------+------+------+------+------+------+

Dabei entspricht:

**S1**: 4,0 IU/ml IFN-γ; **S2**: 1,0 IU/ml IFN-γ; **S3**: 0,25 IU/ml IFN-γ; **S4**: 0 IU/ml IFN-γ

X-N: Patient X - Negativkontrolle; X-M: Patient X - Mitogen-(/Positiv-)Kontrolle;
X-1: Patient X - Testprobe 1; X-2: Patient X - Testprobe 2

Das Plattenmessgerät erzeugt als Ergebnis eine CSV-Datei mit den Daten einer
Testplatte. Jede solche Ergebnisdatei beginnt mit einer Beschreibung des
Plattenlayouts entsprechend obiger Tabellenform, danach folgen die
Messergebnisse in entsprechender Formatierung. Nicht verwendete Positionen auf
einer Testplatte werden durch Leerzeichen oder kein Zeichen zwischen den die
Spalten separierenden Kommata angegeben. Die Dateien enthalten auch Fußnoten
mit Angaben zum durchgeführten Test.

-> `Beispiel einer Ergebnisdatei`_

.. _Beispiel einer Ergebnisdatei: qft_1.csv

Datennormierung
...............

Die OD-Werte der 8 Standardproben werden als Grundlage für die Umrechnung der
Patientenprobenwerte in IU/ml benutzt. Dazu wird die Gleichung der sich aus
den Standardproben ergebenden Regressionsgeraden (Standardkurve) ermittelt und
zur Umrechnung der Patientenwerte verwendet.

Testergebnisbewertung
.....................

Die Ergebnisse des Tests werden für jeden Patienten (ausgehend von den 4
zugehörigen Proben) nach folgendem Entscheidungsbaum bewertet:

+--------+-----------+-----------+----------+--------------+
|  X-N   |    X-1    |    X-2    |   X-M    | Testergebnis |
+========+===========+===========+==========+==============+
|        |           |           |          |              |
|        | Δ >= 0.35 |           |          |              |
|        | und       | beliebig  |          |              |
|        | %Δ >= 25  |           |          |              |
|        |           |           |          |              |
|        +-----------+-----------+ beliebig | POSITIV      |
|        |           |           |          |              |
|        |           | Δ >= 0.35 |          |              |
|        | beliebig  | und       |          |              |
| <= 8.0 |           | %Δ >= 25  |          |              |
|        |           |           |          |              |
|        +-----------+-----------+----------+--------------+
|        |                       |          |              |
|        |                       | Δ >= 0.5 | NEGATIV      |
|        |                       |          |              |
|        | Δ < 0.35 oder %Δ < 25 +----------+--------------+
|        |                       |          |              |
|        |                       | Δ < 0.5  |              |
|        |                       |          |              |
+--------+-----------------------+----------+ Unschlüssig  |
|                                           |              |
| > 8.0                                     |              |
|                                           |              |
+-------------------------------------------+--------------+

Dabei entspricht:

**Δ** dem Unterschied in IU/ml zwischen einer Probe und der Negativkontrolle,
**%Δ** dem prozentualen Unterschied zwischen einer Probe und der
Negativkontrolle

-----

Projektziel
-----------

Wir wollen ein Programm entwickeln, das ausgehend von einer oder mehreren
Ergebnisdateien eine Zusammenfassung der Testergebnisse wie folgt erstellt:

+---------+----------+-------+-------+-------+-------+---------------+
| Patient | Ergebnis | Test1 | Test2 | Nk ok | Pk ok | Ergebnisdatei |
+=========+==========+=======+=======+=======+=======+===============+
| X       | +/-/?    | +/-   | +/-   | +/-   | +/-   | qft_1.csv     |
+---------+----------+-------+-------+-------+-------+---------------+
| ...     | ...      | ...   | ...   | ...   | ...   | ...           |
+---------+----------+-------+-------+-------+-------+---------------+

Umsetzung
.........

Die Implementierung dieses leicht zu formulierenden Ziels ist aufgrund der
Komplexität der Test-Rohdaten relativ anspruchsvoll und erfordert die
Zerlegung der Aufgabe in (mindestens) folgende Teilschritte:

1) Einlesen der Plattendaten und Umwandlung in Patienten- und Standarddatensätze
2) Umrechnung der Patienten-OD-Werte in IU/ml unter Verwendung der Standardwerte
3) Entscheidung über Verwendbarkeit und Ergebnis der Patientendatensätze
4) Berichterstellung


