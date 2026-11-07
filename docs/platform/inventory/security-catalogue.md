# O catálogo de segurança e a cobertura

Os sistemas que a instituição opera, com o nível de criticidade de N1 a N4, se estão em âmbito e se têm monitorização — e a taxa de cobertura que daí sai, no ponto de situação.

```{video} 313-catalogo-de-seguranca
```

O inventário diz que equipamentos existem. O catálogo de segurança diz que sistemas a instituição opera, quão críticos são, e se têm monitorização de segurança. Daí sai a cobertura.

## Onde fica no menu

**Menu:** Identificar › Inventário › Catálogo de Segurança

```{figure} /_static/capturas/catalogo/menu.jpg
:alt: Menu lateral: Identificar › Inventário › Catálogo de Segurança

O caminho no menu lateral: Identificar › Inventário › Catálogo de Segurança.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Inventário**.
3. Clique em **Catálogo de Segurança**: abre o ecrã desta página.

## Os níveis

Cada sistema tem um nível: N1 crítico, N2 estratégico, N3 operacional, N4 secundário. A cobertura conta os três primeiros; o N4 fica de fora por omissão.

E cada sistema está monitorizado, ou em GAP — em âmbito, mas sem monitorização de segurança ativa. Os dias em GAP contam-se desde a transição, no momento da leitura; nunca se gravam.

**Os quatro níveis**

| Nível | Quer dizer | Conta para a cobertura |
|---|---|---|
| N1 | crítico — sem ele a missão para | sim |
| N2 | estratégico | sim |
| N3 | operacional | sim |
| N4 | secundário | não, por omissão |

```{tip}
A exclusão do N4 configura-se em Administração › Cobertura. Um sistema em GAP é um sistema em âmbito sem monitorização ativa.
```

## O catálogo

**Menu:** Identificar › Inventário › Catálogo de Segurança

No menu Identificar, Inventário, Catálogo de Segurança. Os filtros escolhem por nível, por estado, pela rede, e por uma coisa importante: se o sistema já tem um ativo de informação ligado.

Um sistema sem nenhum ativo de informação aparece a âmbar. Não quer dizer risco zero: quer dizer que ninguém apreciou ainda o risco do que lá está. É o assunto da próxima página.

```{figure} /_static/capturas/catalogo/abrir-1.jpg
:alt: Identificar › Inventário › Catálogo de Segurança

O ecrã em Identificar › Inventário › Catálogo de Segurança.
```

1. **Nível**
2. **Monitorizado ou GAP**
3. **Com ou sem ativo de informação**

## O ponto de situação

**Menu:** Identificar › Inventário › Visão Geral

A Visão Geral é a leitura de toda esta fase. Quatro números: sistemas em âmbito, com monitorização, em GAP, e a taxa de cobertura global. Por baixo, a cobertura por camada, de N1 a N4, e os sistemas em GAP por sistema operativo e por tipo.

É isso que transforma «temos sistemas em GAP» em, por exemplo, «são todos servidores do mesmo tipo, e fecham-se da mesma maneira». Enquanto houver sistemas em GAP, um aviso leva direito ao ecrã onde se instala o agente de monitorização.

```{figure} /_static/capturas/catalogo/dashboard-1.jpg
:alt: Identificar › Inventário › Visão Geral

O ecrã em Identificar › Inventário › Visão Geral (1 de 2).
```

1. **Direito ao instalador do agente**

```{figure} /_static/capturas/catalogo/dashboard-2.jpg
:alt: Identificar › Inventário › Visão Geral

O ecrã em Identificar › Inventário › Visão Geral (2 de 2).
```

## Resumo

O nível de cada sistema é uma decisão de negócio, não técnica: pergunte à direção e aos donos dos serviços. Que sistemas estão monitorizados, pergunte à informática.

E a taxa de cobertura diz sempre, em rodapé, que níveis ficaram de fora. Uma taxa sem o denominador à vista não se leva a uma reunião.

**O que pedir a quem — e o que a plataforma faz**

- À direção e aos donos dos serviços: o nível de cada sistema — é uma decisão de negócio, não técnica.
- À informática: que sistemas têm monitorização de segurança ativa.
- A taxa diz sempre que níveis exclui: uma taxa sem denominador à vista não se leva a uma reunião.
