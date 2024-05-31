# Calculadora de datas

a) O problema consiste em somar um número *n* de dias a uma data *d*, obtendo assim uma data *d'* determinada pela soma de *d* e *n*, respeitando os limites de 30 ou 31 dias do mês e de 365 dias de um ano não-bissexto.\
A relação entre as entradas e saídas é que as entradas (data *d* e o número *n* de dias a serem somados), resultam na saída (a data *d'*), que é obtida diretamente a partir da soma das entradas fornecidas e do processamento desses dados, no caso sua soma

b)  *d*= data inicial; *n*= número de dias a serem somados; *d'*= data final com a soma já realizada ; O ano não é bissexto e a soma não poderá ultrapassar o próximo ano bissexto.

### Instruções elementares
* Coletar entradas
* Realizar somas
* Verificar o mês da data fornecida
* Verificar se o número de dias após a soma é > 31, > 30 ou > 28 e associar esses dados aos valores armazenados
* Verificar e definir o mês, dia e ano para a forma correta, baseada no calendário vigente, afim de não criar datas inexistentes (especialmente essa aqui eu não tenho certeza se esta certa.)
* Armazenar (ou não) valores
* Mostrar saídas
 
 ### Algoritmo
* Coletar a data *d* de entrada
* Coletar o número *n* de dias
* Verificar qual o mês da data *d*
* Definir o valor 0 caso o mês de *d* seja de 30 dias, 1 caso seja de 31 dias e não definir valor algum caso o mês tenha 28 dias
* Somar o número *n* de dias a data *d*
* Verificar se, após a soma, o número de dias é > 30, caso o valor pré definido seja 0, > 31, caso o valor definido seja 1, ou ainda > 28 caso não haja um valor definido
* Se, após a soma, o número de dias for inferior a 30, quando o valor definido é 0, ou inferior a 31 caso o valor definido seja 1, ou ainda inferior a 28 caso não haja valor definido, pular as próximas três instruções
* Se for > 31 com o valor 1 definido, verificar e definir em qual mês, dia e ano a data *d'* irá cair, considerando a quantidade de dias (30, 31 ou 28) dos meses subsequentes até o mês definitivo de *d'*. Se esse não for o caso, realizar a próxima instrução
* Se for > 30 com o valor 0 definido, verificar e definir em qual mês, dia e ano a data *d'* irá cair, considerando a quantidade de dias dos meses subsequentes (30, 31 ou 28) até o mês definitivo de *d'*. Se esse não for o caso, realizar a próxima instrução
* Se for > 28 e não houver qualquer valor definido, verificar e definir em qual mês, dia e ano a data *d'* irá cair, considerando a quantidade de dias (30, 31 ou 28) dos meses subsequentes até o mês definitivo de *d'*. Se esse não for o caso, realizar a próxima instrução
* Mostrar a data *d'*

c) Nesse caso as entradas seriam as datas iniciais, digamos *D*, e um número de dias úteis a serem somados, *N*, e a saída seria o total já somado destas duas entradas, digamos *D'*. Este problema consistem em transformar estas entradas na nova saída, porém levando em conta que nesse número de dias *N* devem ser considerados apenas dias que não sejam sábados, domingo, feriados e pontos facultativos, diferentemente do problema anterior, em que o número *n* de dias podia envolver, também, sábados, domingos, feriados e pontos facultativos.

