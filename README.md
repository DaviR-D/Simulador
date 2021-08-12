# Instruções
Simulador de Autômatos Finitos

O autômato (estados, transições, etc) deve ser escrito no formato especificado (porém sem parênteses) no arquivo automatum.txt, e as entradas a serem testadas no arquivo input.txt, ao rodar o programa simulador.py ele escreve o resultado no arquivo resultados.txt

linha 1: estados  
linha 2: estado inicial  
linha 3: estados finais  
linha 4: transições  

Exemplos (alfabeto: a, b, c):

1, 2, 3  
1  
3  
1|a|1, 1|b|2, 1|c|1, 1|b|1, 2|b|3

Palavras que terminam em bb (NDFA)

------------------------------------

1, 2  
1  
1  
1|a|2, 1|b|2, 1|c|2, 2|a|1, 2|b|1, 2|c|1

Palavras de tamanho par (DFA)

------------------------------------

1, 2, 3, 4, 5  
1  
3, 5  
1|a|2, 2|a|3, 1|b|4, 4|b|5, 1|a|1, 1|b|1, 1|c|1

Palavras terminadas em aa ou bb (NDFA)


