# Mapeamento entre referenciais e cobertura por ferramenta

Como um controlo cumprido numa norma conta para outra — a herança pelo mapeamento confirmado — e que ferramentas cobrem que controlos, lido ao contrário das tabelas das normas.

```{video} 321-mapeamento-e-ferramentas
```

Com várias normas em âmbito, o mesmo trabalho repete-se: a gestão de acessos aparece no Anexo IV, no QNRCS e na ISO 27001. Nesta página vemos como se faz uma vez e conta várias, e que ferramentas ajudam.

## Onde fica no menu

**Menu:** Governar › Grc — conformidade › Mapeamento entre referenciais

```{figure} /_static/capturas/mapeamento-ferramentas/menu.jpg
:alt: Menu lateral: Governar › Grc — conformidade › Mapeamento entre referenciais

O caminho no menu lateral: Governar › Grc — conformidade › Mapeamento entre referenciais.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Grc — conformidade**.
3. Clique em **Mapeamento entre referenciais**: abre o ecrã desta página.

## A herança

A regra é esta: um controlo conta como implementado se houver um mapeamento confirmado, de cobertura total, para outro controlo, noutra norma, que seja aplicável e esteja implementado.

E é uma regra estreita, de propósito: um mapeamento proposto, uma cobertura parcial, ou uma cadeia de dois saltos não herdam nada. E o que alguém declarou ganha sempre à herança.

**A herança de conformidade**

- Um controlo conta como implementado se houver um mapeamento confirmado, de cobertura total, para um controlo aplicável e implementado noutra norma.
- Não herdam: mapeamentos propostos ou rejeitados, coberturas parciais, origens não aplicáveis.
- Não há transitividade: de A para B e de B para C não faz C implementado.
- O estado declarado ganha sempre; a herança só preenche o que está em branco.

## O mapeamento

**Menu:** Governar › GRC — Conformidade › Mapeamento entre referenciais

No menu Governar, GRC, Conformidade, Mapeamento entre referenciais. Os cruzamentos que as normas já trazem chegam como propostas, por confirmar. Confirma-se, rejeita-se, ou acrescenta-se o que faltar, com a cobertura total ou parcial.

O separador Lado a lado mostra as duas normas em paralelo, e Referências externas conta as remissões para legislação que a plataforma ainda não tem.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-1.jpg
:alt: Governar › GRC — Conformidade › Mapeamento entre referenciais

O ecrã em Governar › GRC — Conformidade › Mapeamento entre referenciais (1 de 3).
```

1. Clique em **Lado a lado**.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-2.jpg
:alt: Governar › GRC — Conformidade › Mapeamento entre referenciais

O ecrã em Governar › GRC — Conformidade › Mapeamento entre referenciais (2 de 3).
```

1. Clique em **Referências externas**.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-3.jpg
:alt: Governar › GRC — Conformidade › Mapeamento entre referenciais

O ecrã em Governar › GRC — Conformidade › Mapeamento entre referenciais (3 de 3).
```

## As ferramentas

**Menu:** Governar › GRC — Conformidade › Cobertura por ferramenta

A Cobertura por ferramenta lê ao contrário as tabelas que as normas trazem: cada controlo nomeia as ferramentas que o cobrem, e aqui vê-se por ferramenta — que normas cobre, que controlos, e que percentagem do que a organização declarou aplicável.

O seletor Universo decide contra o quê se mede: as normas em âmbito, as de fora, ou todas. Filtra-se por tipo, código aberto ou comercial, e sai em relatório para Word ou folha de cálculo — útil antes de uma compra.

```{figure} /_static/capturas/mapeamento-ferramentas/ferramentas-1.jpg
:alt: Governar › GRC — Conformidade › Cobertura por ferramenta

O ecrã em Governar › GRC — Conformidade › Cobertura por ferramenta (1 de 2).
```

1. **Universo — contra o quê se mede**

```{figure} /_static/capturas/mapeamento-ferramentas/ferramentas-2.jpg
:alt: Governar › GRC — Conformidade › Cobertura por ferramenta

O ecrã em Governar › GRC — Conformidade › Cobertura por ferramenta (2 de 2).
```

## Resumo

A plataforma propõe mapeamentos, mas só os confirmados contam, e a herança calcula-se na leitura, nunca se grava. Sobre as ferramentas, mostra o que as normas dizem que cada uma cobre — não recomenda marcas.

**O que a plataforma faz — e o que não faz**

- Propõe os mapeamentos que as normas trazem; só os confirmados contam.
- Calcula a herança na leitura — nunca a grava.
- Mostra que ferramentas cobrem o quê; não recomenda marcas nem substitui uma análise de mercado.
