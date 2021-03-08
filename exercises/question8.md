## Exercício 8

Suponha um dado grafo conexo G com todas suas arestas possuindo pesos distintos. Provar que G possui apenas uma árvore geradora mínima.

#### Resolução

Segundo a propriedade do ***Cut***, sendo ***X*** pertencente ao conjunto de arestas da árvore geradora mínima de ***G***, e ***S*** um cut de ***G*** que não é atravessado por ***X***, para um dado conjunto de arestas que ligam X e S, a de menor peso faz parte da árvore geradora mínima (chamemos-a de ***e***).

Assumindo a existência de mais de uma árvore geradora mínima para ***G***, deverá existir também outra aresta ***f*** além de ***e*** que satisfaça a propriedade do ***Cut***, o que implica ***f*** possuir o mesmo peso que ***e***. Porém, assumiu-se anteriormente que todas as arestas pertencetes a **G** possuem pesos distintos, o que nos leva a uma contradição.