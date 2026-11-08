# Ativos de informação

Do servidor à informação: cada ativo com tipo, classificação, confidencialidade, integridade e disponibilidade, dono e os sistemas em que assenta — e a árvore do que está dentro de quê.

```{video} 314-ativos-de-informacao
```

Um servidor é um bem. O que o risco aprecia é a informação que assenta nele: os dados dos estudantes, as matrículas, os vencimentos. Nesta página registamos os ativos de informação, como vimos em conceito em {doc}`/fundamentals/information-and-assets`.

## Onde fica no menu

**Menu:** Identificar › Inventário › Ativos de informação

```{figure} /_static/capturas/ativos-informacao/menu.jpg
:alt: Menu lateral: Identificar › Inventário › Ativos de informação

O caminho no menu lateral: Identificar › Inventário › Ativos de informação.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Inventário**.
3. Clique em **Ativos de informação**: abre o ecrã desta página.

## Os campos

Cada ativo tem um tipo, uma classificação, e os três valores — confidencialidade, integridade e disponibilidade. Tem um dono, que é o responsável do serviço, e os sistemas em que assenta: um serviço de correio pode assentar em três servidores.

E pode ter um tipo de catálogo, o código MONARC equivalente — um método público de análise de risco —, que traz modelos de ameaças e vulnerabilidades prontos a usar.

**Os campos de um ativo**

| Campo | O que é |
|---|---|
| Tipo | processo, base de dados, aplicação, suporte, pessoa-chave, serviço |
| Classificação | público, interno, confidencial, restrito — no Grupo A, pelo processo de classificação (O.PCF) |
| C, I, A | quanto valem a confidencialidade, a integridade e a disponibilidade |
| Dono | quem responde por ele — o responsável do serviço, não a informática |
| Sistemas | em que sistemas do catálogo assenta — vários, não um |
| Tipo do catálogo | o código MONARC equivalente, que traz modelos de risco prontos |

## O ecrã

**Menu:** Identificar › Inventário › Ativos de informação

No menu Identificar, Inventário, Ativos de informação. Filtra-se por tipo, classificação e grupo. Cada ativo tem três botões: Editar, Apreciar riscos, que leva ao registo de risco, e Contenção.

O número de riscos de cada ativo aparece na própria linha, e abre o registo de risco já filtrado.

```{figure} /_static/capturas/ativos-informacao/abrir-1.jpg
:alt: Identificar › Inventário › Ativos de informação

O ecrã em Identificar › Inventário › Ativos de informação.
```

1. **Apreciar riscos**
2. **Contenção**

## A árvore

O separador Árvore de contenção mostra o que está dentro de quê: campus, edifício, sala, servidor. Um equipamento pode estar em vários contentores ao mesmo tempo — uma sala e um circuito elétrico.

Para cada nó, um emblema conta os riscos dos contentores acima que ainda não desceram até ele. Se a sala tem risco de inundação, os servidores lá dentro herdam-no. A pesquisa não corta ramos: abre o caminho até ao que procura.

```{figure} /_static/capturas/ativos-informacao/arvore-1.jpg
:alt: A árvore de contenção

A árvore de contenção (1 de 2).
```

1. Clique em **Árvore de contenção**.

```{figure} /_static/capturas/ativos-informacao/arvore-2.jpg
:alt: A árvore de contenção

A árvore de contenção (2 de 2).
```

## Resumo

A cada responsável de serviço, pergunte que informação usa e quanto valem as três propriedades. À informática, em que sistemas assenta. E um sistema sem ativo ligado fica a âmbar no catálogo, até alguém apreciar o risco do que lá está.

**O que pedir a quem — e o que a plataforma faz**

- A cada responsável de serviço: a informação que usa, e quanto valem C, I e A.
- À informática: em que sistemas assenta cada ativo.
- Um sistema sem ativo ligado fica a âmbar no catálogo: por apreciar, não risco zero.
