Kombinatorik
============

``itertools``- und ``random``-Funktionen zur Kombinatorik:

+------------------+--------------------+-------------------------------------+
|                  |      Anordnung ist Unterscheidungsmerkmal                |
| k Elemente       +--------------------+-------------------------------------+
| aus n            | ja                 |      nein                           |
|                  | (Permutation)      |      (Kombination)                  |
+------------------+--------------------+-------------------------------------+
|                  | ``product()``::    |``combinations_with_replacement()``::|
|                  |                    |                                     |
|                  |       n**k         |            (n+k-1)!                 |
| Mit Zurücklegen  |                    |          -----------                |
|                  |                    |          (n-1)! * k!                |
|                  +--------------------+-------------------------------------+
|                  |        nur eine zufällige mit ``random.choices()``       |
+------------------+--------------------+-------------------------------------+
|                  |``permutations()``::| ``combinations()``::                |
|                  |                    |                                     |
|                  |       n!           |               n!                    |
| Ohne Zurücklegen |     ------         |          -----------                |
|                  |     (n-k)!         |          (n-k)! * k!                |
|                  +--------------------+-------------------------------------+
|                  |        nur eine zufällige mit ``random.sample()``        |
+------------------+--------------------+-------------------------------------+
|      ein zufälliges Element aus einer Sequenz mit ``random.choice()``       |
+-----------------------------------------------------------------------------+

