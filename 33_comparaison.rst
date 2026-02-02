
Comparaison des interventions AGER et des événements SIRIUS, en 2024
######################################################################

Les deux tables ont des tailles comparables :

* Interventions :43 386 lignes
* Evénements : 132 000 lignes pour 40 671 événements différents

Conditions de liaison entre les tables
*****************************************
Pour mettre en correspondance les éléments des 2 tables, on doit utiliser la localisation et l'horodatage.

Localisation
===============
Pour la localisation, on retrouve les notions d'axe, de sens et de PR dans les 2 tables mais :

* les axes ne sont pas toujours désignés de la même manière.
* les notions de sens sont différentes (en particulier au niveau des accès et des échangeurs)
* la codification des PR est très différente selon l'auteur des enregistrements d'interventions.

On a créé des tables de correspondance qui permettent dans la majorités des cas de traduire les codifications dans un langage commun.  
Les correspondances ne sont cependant pas complètes et augmenter le taux de correspondance signifie allonger la table. C'est un travail assez laborieux et qui produit des rendements décroissants.

Il en résulte qu'environ 10 à 20 % des enregistrements qui pourraient être liés par une analyse fine ne le sont pas dans les résultats produit ici.

Le PR étant la données la moins bien renseignée sur les interventions, on fera des analyses avec ou sans cette variable.

Horodatage
================
Pour la date et l'heure, la liaison est plus simple même ne les heures saisies dans les deux tables ne sont pas de la même nature. En prenant une plage de +/- une heure ont pense établir les liens nécessaires. Le risque que 2 événements interviennent sur le même Axe à quelques heures d'interval est faible.

Résultat des liaisons
=======================
En faisant une liaison intégrant le PR, on trouve un événement SIRIUS pour 15 000 des 43 000 interventions.
Sans prendre en compte le PR, le nombre d'appariements passe à 26 000.

Enlever une dimension facilite les correspondances, mais cela entraine que l'on fait aussi apparaitre de fausses correspondances.

Déclinaison par CEI
======================
Les taux de liaisons peuvent dépendre de nombreux facteurs liés à des considérations géographiques et à la manière dont les données sont enregistrées dans la base.

On peut observer la manière dont ces taux dépendent des variables de la base. On fait ci-dessous, par exemple, une analyse par CEI.

.. csv-table::
   :header: CEI,Nbr d'interventions,Taux avec PR,Taux sans PR
   :width: 100%

     Brie-Comte-Robert,1429,41,68
     Champigny,4987,49,75
     Rosny,2747,37,68
     Rozay en Brie,37,5,27
     Villeparisis,2232,31,47
     Eragny,2946,19,44
     Saint-Denis,2929,33,63
     Fontenay,1087,1,37
     Nanterre,4308,39,74
     Orgeval,559,43,76
     Rocquencourt-Boulogne,3978,46,73
     Ablis,515,20,35
     Chevilly-Larue,4340,19,31
     Jouy-en-Josas,414,26,49
     Jouy-en-Josas (site de Jouy),2568,25,52
     Jouy-en-Josas (site de Plaisir),1714,23,49
     Orsay,2865,43,68
     Villabé,3731,46,76

Déclinaison par heure du jour ou de la nuit
===================================================
On ajoute une analyse par heure (de 0 à 23).

Le taux dépasse 65% en fin d'après midi. Il est en dessous de 50% au milieu de la nuit.
La variation tient au moins en partie au plus grand nombre de faux positifs aux heures qui voient le plus grand nombre d'événements.

On aurait pu s'attendre à ce que les appariements soient meilleurs quand l'activité est plus faible et qu'il est donc plus facile de la tracer. Ce n'est pas ce que l'on observe.

.. csv-table::
   :header: Heure,Nbr d'interventions,Taux avec PR,Taux sans PR
   :width: 100%
      
      0,1256,25,44
      1,1048,29,50
      2,785,28,49
      3,699,28,47
      4,699,27,47
      5,845,37,56
      6,1392,35,61
      7,1720,39,66
      8,2102,37,64
      9,2273,35,60
      10,2134,33,60
      11,2058,34,61
      12,1985,36,65
      13,2265,35,62
      14,2351,36,64
      15,2427,38,64
      16,2546,37,66
      17,2640,39,69
      18,2544,39,67
      19,2571,37,66
      20,2125,33,61
      21,1826,33,59
      22,1696,28,53
      23,1399,29,50




