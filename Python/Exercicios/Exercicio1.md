# Classes e Objetos. Single Responsibility Principle

Adalberto recém se mudou e comprou 3 pratos e uma garrafa térmica. Ele também comprou um detergente de 250ml.
Adalberto gosta muito de sopa, então seus pratos são todos fundos. 
Ele tem: 
- Um prato verde com capacidade para 300 ml de sopa
- Um prato azul com capacidade para 250 ml de sopa
- Um prato amarelo, com capacidade para 350 ml de sopa

A garrafa térmica de Adalberto comporta 500 ml de café.

Com base nessas informações, faça um programa que permita:
- encher um prato de sopa. Para isso, eu devo indicar qual prato eu quero encher. Se o prato estiver sujo, eu devo avisar que não é possível encher um prato sujo. Se o prato estiver cheio, eu devo avisar que o prato já está cheio
- encher uma garrafa de café. Se a garrafa estiver suja, eu devo avisar que não é possível encher uma garrafa suja. Se a garrafa estiver cheia, eu devo avisar que a garrafa está cheia
- limpar um prato de sopa. Para limpar um prato eu devo usar 10% da sua capacidade em detergente (se o prato tem capacidade para 300ml, eu gasto 30ml de detergente para limpar ele). Ao terminar de lavar, eu devo indicar quanto de detergente eu ainda tenho. Se eu não tiver mais detergente, devo avisar que acabou o detergente.
- limpar uma garrafa de café. Para limpar uma garrafa eu devo usar 20% da sua capacidade em detergente (se a garrafa tem capacidade para 500ml, eu gasto 100ml de detergente para limpar ela). Ao terminar de lavar, eu devo indicar quanto de detergente eu ainda tenho. Se eu não tiver mais detergente, devo avisar que acabou o detergente.
- tomar a sopa de um prato. Se o prato estiver vazio, avisar que o prato está vazio. Se o prato estiver vazio e sujo, avisar que o prato está vazio e sujo.
- tomar café da garrafa. Se a garrafa estiver vazia, avisar que a garrafa está vazia. Se a garrafa estiver vazia e suja, avisar que a garrafa está vazia e suja.
- listar quais pratos estão limpos
- listar quais garrafas estão limpas

Lembre-se de fazer as funções segundo o *Princípio da Responsabilidade Única* (Single Responsibility Principle), que aprendemos na última aula.
Lembre-se também de criar atributos e métodos para as classes do programa, bem como isolar cada classe em seu próprio arquivo.
