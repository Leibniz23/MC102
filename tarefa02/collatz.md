# Algoritmo contador de Collatz

* Receba a entrada *n*.
* Verifique o valor de *n*.
* Atribua uma variável *cont*. Caso *n*!=1, atribua o valor 1 a *cont*, caso *n*=1, atribua o valor 0 a cont.
* Enquanto *n*!=1, analise:
    * Se *n* é par
        * Divida *n* por 2, então atribua esse novo valor a *n*
        * Atribua cont+1 ao valor de cont
    * Senão
        * Multiplique *n* por 3 e some 1, então atribua esse novo valor a *n*
        * Atribua cont+1 ao valor de cont
* Mostre o valor de cont

# Estruturas de controle

Da linha 3 à linha 5 foi usado o *sequenciamento direto*. Na linha 6, utilizei a *iteração condicional*, já da linha 7 à linha 12 utilizei *desvio condicional* e na linha 13 foi novamente usado o *sequenciamento direto*.