Versucht Euch an der Lösung der folgenden, relativ einfachen Probleme
aus dem `Project Euler <https://projecteuler.net/>`__:

- `Largest palindrome product <https://projecteuler.net/problem=4>`__

  Hinweis: Wie aufwendig die Lösung ist, hängt stark davon ab, wierum Ihr das
  Problem angeht. Ihr könntet prinzipiell entweder:
  
  - alle palindromischen Zahlen finden und nacheinander prüfen, ob sie das
    Produkt zweier dreistelliger Zahlen sind, oder
  - alle Produkte zweier dreistelliger Zahlen berechnen und prüfen, ob sie
    palindromische Zahlen sind.
    
  Wie meistens beim Programmieren lohnt es sich, beide Möglichkeiten z.B.
  auf Papier kurz zu skizzieren, und dann nur die einfachere Variante
  umzusetzen.

- `Large sum <https://projecteuler.net/problem=13>`__

  Hinweis: Dieses Problem lässt sich entweder im interaktiven Modus lösen
  (dann ist der triple-quoted string Euer Freund!) oder in Form eines
  Hauptprogramms, das nach der Zahl fragt. Wenn Ihr den zweiten Weg gehen
  wollt, gibt es einen Trick: ``input()`` ohne prompt-String verhält sich
  nämlich still und man kann dann bei der Eingabe nicht sehen, ob sie von einem
  oder mehreren ``input()``-Aufrufen bearbeitet wird. Schreibt also eine
  Schleife, die solange neue Zeilen einliest bis sie z.B. auf eine Leerzeile
  stösst und dabei die Zeilen zu einem langen String zusammensetzt.

