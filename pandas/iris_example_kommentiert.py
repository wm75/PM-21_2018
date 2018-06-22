# import von allem, was wir benutzen wollen
# noch so eine Konvention in Python:
# zuerst schreibt man die direkten imports,
# dann die from x import y Anweisungen

import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from scipy import stats

# einen pandas DataFrame direkt aus einer csv-Datei lesen
# den Pfad zur Datei müßt Ihr natürlich anpassen,
# ausserdem darf er anscheinend keine nich-englischen Zeichen
# enthalten.
# read_csv nimmt ein weiteres Argument sep entgegen mit dem Ihr
# das Trennzeichen, das in der Datei benutzt wird, festlegen könnt.
# Voreinstellungmäßig wird hier Komma verwendet.
# Ausser read_csv gibt es auch noch weitere read_*-Funktionen für
# andere Formate.
iris=pd.read_csv('C:/Users/wolma/Documents/Python_course_part_II/Fisher.csv')

# in der Datei sind die Iris-Arten in der Spalte "Type" durch Zahlen nach folgendem Schema kodiert:
species_code = {0: 'setosa', 1: 'virginica', 2: 'versicolor'}

# das obige Mapping können wir auch gleich verwenden, um die
# "Type"-Spalte durch eine Spalte "Species" zu ersetzen, die die
# Artbezeichnungen als Zeichenketten enthält.
# Als erstes bauen wir uns die neue Spalte als Liste auf:
species_column = []
for species_id in iris['Type']:
    species_column.append(species_code[species_id])
# Dann hängen wir die Liste als neue Spalte an den DataFrame an
iris['Species'] = species_column
# Diese beiden Schritte hätten wir mit einer list comprehension
# auch kürzer schreiben können:
# iris['Species'] = [
#     species_code[species_id] for species_id in iris['Type']
# ]

# Zuletzt löschen wir die jetzt redundante Spalte "Type"
del iris['Type']


# ein erster Plot (scatter plot von "PL" gegen "PW")
# Jeder pandas DataFrame hat eine plot-Methode, um sich
# selbst oder Teile von sich selbst darzustellen.
iris.plot(kind='scatter', x='PL', y='PW')
plt.show()

# besser wäre es, wir könnten die Punkte nach Iris-Art einfärben
# Dazu benötigen wir ein weiteres dictionary, in dem wir die
# Farbzuordnung festlegen, z.B. (pandas/matplotlib versteht viele
# englische Farbbezeichnungen):
colors = {
    'setosa': 'red', 
    'virginica': 'blue',
    'versicolor': 'yellow'
    }
# Im Prinzip könnten wir uns jetzt analog zur Spezies-Liste oben
# eine Farbliste erzeugen, die zu jeder Zeile unseres DataFrames
# die gewünschte Farbe enthält.
# Anstelle der obigen Lösung mit einer for-Schleife bietet pandas
# aber auch eine einfachere und effizientere Möglichkeit:
# die replace-Methode eines DataFrames oder einer Spalte erzeugt
# eine Kopie des Objekts, in der alle enthaltenen Elemente durch
# die durch ein Mapping vorgegebenen Austauschwerte ersetzt sind.

plot_colors = iris['Species'].replace(colors)
# diese Farbliste können wir jetzt einfach der plot-Methode über
# das Argument c mitgeben:
iris.plot(kind='scatter', x='PL', y='PW', c=plot_colors)
plt.show()

# pandas/matplotlib beherrscht noch viele weitere Darstellungsarten
# oft sehr nützlich sind z.B. boxplots
# An diesem Besipiel wollen wir ausserdem verstehen, wie man Abb.
# mit mehreren panels (sog. subplots) erzeugt.
# Wir legen zunächst eine (noch leere) Abbildung mit vier panels
# in 2x2 Anordnung an:
f, ax=plt.subplots(2,2)
# plt.subplots liefert ein tuple von zwei Werten zurück, die wir
# oben in f und ax gespeichert haben.
# Der erste Wert (jetzt in f) ist dabei das neu erzeugte
# Abbildungsobjekt, das zweite (jetzt in ax) ein Array der
# subplots. Dieses Array hat dieselben Dimensionen (hier also 2x2)
# wie die von uns gewünschte Anordnung. Als numpy-Array können wir
# seine Elemente, also die einzelnen subplots über kommagetrennte
# Reihen-, Spaltenindizes ansprechen.
# In jedem subplot stellen wir jetzt einen boxplot eines Paramters
# unseres DataFrames dar, wobei wir nach der Iris-Art gruppieren
# wollen:
iris.boxplot(column='PL', by='Species', ax=ax[0,0])
iris.boxplot(column='PW', by='Species', ax=ax[0,1])
iris.boxplot(column='SL', by='Species', ax=ax[1,0])
iris.boxplot(column='SW', by='Species', ax=ax[1,1])
f.show()

# eine sehr schicke Alternative zu boxplots, wenn man nicht
# allzuviele Einzeldatenpunkte hat, sind sog. swarmplots.
# Swarmplots können mit pandas nicht direkt erzeugt werden, werden
# aber von seaborn über eine gleichnamige Funktion unterstützt, die
# z.B. einen pandas.DataFrame als Argument akzeptiert:
sns.swarmplot(iris['Species'], iris['PL'])
plt.show()

# Einen schönen Gesamteindruck eines Datensatzes kann man übrigens
# mit der etwas versteckten Funktion scatter_matrix gewinnen:
pd.plotting.scatter_matrix(iris, c=iris['Species'].replace(colors))
plt.show()
# Alternativ kann man auch die seaborn-Funktion pairplot benutzen,
# die man sich vielleicht etwas leichter merken kann und die auch
# ein optisch ansprechenderes Ergebnis liefert:
sns.pairplot(iris, hue='Species')
plt.show()

# Filtern von Spalten nach bestimmten Kriterien:
# benutzt man pandas-Objekte in logischen Vergleichen, erhält
# man pandas-Objekte derselben Geometrie zurück, deren Elemente
# jeweils True oder False sind, je nach Ergebnis des Vergleichs
# für das jeweilige Element des Ausgangsobjekts:
logic_vector = iris['Species'] == 'versicolor'
# logic_vector ist jetzt eine pandas-Datenserie mit genausovielen
# Elementen wie die Spalte Spezies und einem True an allen Stellen,
# an denen die "Spezies"-Spalte den Wert 'versicolor' hat, überall
# sonst False.
# logic_vector kann jetzt wiederum zum Indizieren eines pandas-
# Objektes gleicher Länge verwendet werden. Nur die Elemente, deren
# entsprechende Position in logic_vector True ist, werden damit
# ausgewählt.
pl_werte_fuer_versicolor = iris[logic_vector]['PL']
# Diese zwei Schritte lassen sich auch kombinieren, z.B.
# die Spalte 'PL' für die Reihen in iris, in denen die 'Species'-
# Spalte gleich 'versicolor' ist.
pl_werte_fuer_setosa = iris[iris['Species'] == 'versicolor']['PL']
# Das ist ein in pandas und numpy sehr viel verwendetes Idiom, das
# Ihr Euch gut merken solltet.

# Wir wollen es gleich mal für einen einfachen statistischen Test 
# verwenden. Die Frage: unterscheiden sich die Durchschnitte der
# 'PL'-Werte der Arten versicolor und virginica, lässt sich durch 
# einen t-Test beantworten. Der t-Test für unabhängige Stichproben
# ist mit der Funktion ttest_ind aus dem Modul stats des scipy-
# Paketes möglich. Diese Funktion erwartet als zwei Argumente die
# beiden Stichproben, d.h. wir schreiben:
stats.ttest_ind(
    iris[iris['Species'] == 'versicolor']['PL'],
    iris[iris['Species'] == 'virginica']['PL']
    )
# und erhalten als Ergebnis ein tuple aus dem Wert der Test-
# Statistik und den sich daraus ergebenden p-Wert.

# Weil wir es mit den Daten von mehr als zwei Arten zu tun haben,
# wäre es eigentlich besser einen ANOVA durchzuführen statt 
# einzelne paarweise t-Tests. Der ANOVA beantwortet dabei die
# Frage, ob bezüglich einer Messgröße (z.B. PL) überhaupt
# signifikante Unterschiede zwischen irgendwelchen Arten bestehen.
# Nur wenn das der Fall ist, dürfen dann überhaupt paarweise sog.
# post-Tests durchgeführt werden, die dann zudem auf den Effekt
# mehrfacher Vergleiche korrigiert sein sollten.

# Der ANOVA selbst kann mit der scipy.stats-Funktion f_oneway
# durchgeführt werden.
stats.f_oneway(
    iris[iris['Species'] == 'versicolor']['PL'],
    iris[iris['Species'] == 'virginica']['PL'],
    iris[iris['Species'] == 'setosa']['PL']
    )
# Da wir einen signifikanten p-Wert erhalten, wollen wir jetzt
# einen post-test durchführen, um zu klären, welche Spezies-Paare
# signifikante Unterschiede zeigen.
# Leider geht das nicht mit scipy-Funktionalität, sondern wir
# benötigen dafür das spezialisiertere Paket statsmodels

from statsmodels.stats.multicomp import MultiComparison
# Wir wandeln die benötigten Spalten zunächst in ein von
# statsmodels definiertes MultiComparison-Objekt um:
mc = MultiComparison(iris['PL'], iris['Species'])
# Dieses Objekt bringt dann die Methode tukeyhsd mit, die einen
# der gängigsten post-tests (den sog. Tukey-Test) über die Daten
# ausführt.
result = mc.tukeyhsd()
# Druckt man das Ergebnis-Objekt, formatiert es sich recht gut
# lesbar.
print(result)
