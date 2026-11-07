# A Declaração de Aplicabilidade

Controlo a controlo: aplicável ou não, porquê, de onde vem, quem responde, em que estado está e quando se revê — e o número declarado de conformidade que daí sai.

```{video} 320-declaracao-de-aplicabilidade
```

em {doc}`/fundamentals/iso-27001-inside` vimos o que é a Declaração de Aplicabilidade. Agora fazemo-la: para cada controlo de cada norma em âmbito, uma decisão escrita.

## Onde fica no menu

**Menu:** Governar › Grc — conformidade › Declaração de Aplicabilidade

```{figure} /_static/capturas/soa/menu.jpg
:alt: Menu lateral: Governar › Grc — conformidade › Declaração de Aplicabilidade

O caminho no menu lateral: Governar › Grc — conformidade › Declaração de Aplicabilidade.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Grc — conformidade**.
3. Clique em **Declaração de Aplicabilidade**: abre o ecrã desta página.

## Os campos

Para cada controlo: aplicável ou não, com justificação; a origem — risco, lei, contrato, ou boa prática —; o responsável; o estado; a maturidade; e a data da próxima revisão.

A origem «risco» obriga a apontar o risco. As outras justificam-se sozinhas: um controlo exigido por lei não precisa de um risco para ser aplicável.

**Os campos de cada controlo**

| Campo | O que diz |
|---|---|
| Aplicável | sim ou não — o «não» tem de ser justificado |
| Justificação | o que o auditor lê quando um controlo é excluído |
| Origem | porque é aplicável: risco, legal, contratual, boa prática |
| Responsável | quem responde por ele |
| Estado | não iniciado, em curso, implementado |
| Maturidade | de 1 a 5 — quão assente está |
| Próxima revisão | uma data — um controlo sem revisão marcada nunca se revê |

```{tip}
A ISO/IEC 27001 pede a Declaração no tratamento do risco; um certificado entregue ao CNCS leva-a (art. 27.º, n.º 5).
```

## O ecrã

**Menu:** Governar › GRC — Conformidade › Declaração de Aplicabilidade

No menu Governar, GRC, Conformidade, Declaração de Aplicabilidade. Uma declaração por cada norma em âmbito, com quantos controlos são aplicáveis e quantos excluídos.

```{figure} /_static/img/320-declaracao-de-aplicabilidade/01.jpg
:alt: Governar › GRC — Conformidade › Declaração de Aplicabilidade

O ecrã em Governar › GRC — Conformidade › Declaração de Aplicabilidade.
```

## Uma declaração

Abrimos as medidas das entidades públicas relevantes. Cada linha é uma medida, com a decisão, o estado e o responsável. Exporta-se para folha de cálculo.

E um controlo pode estar implementado no centro de dados e por iniciar numa escola. O detalhe por grupo cria linhas por unidade, que refinam a linha global sem lhe mexer. A percentagem declarada de conformidade sai daqui, e alimenta o painel.

```{figure} /_static/capturas/soa/norma-1.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (1 de 3).
```

1. **Filtrar por grupo do Anexo IV**

```{figure} /_static/capturas/soa/norma-2.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (2 de 3).
```

```{figure} /_static/capturas/soa/norma-3.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (3 de 3).
```

1. **Exportar**

## Resumo

A cada responsável, peça o estado real do seu controlo — e a prova, que vem na página das evidências. A plataforma guarda versões da Declaração: a que se entrega numa auditoria fica fixada, e não muda com o trabalho do dia seguinte.

**O que pedir a quem — e o que a plataforma faz**

- A cada responsável: o estado real do seu controlo, com a prova que o sustenta ({doc}`/platform/monitoring/evidence`).
- Ao jurídico: a origem legal ou contratual de cada controlo aplicável.
- A herança: um controlo implementado numa norma pode contar noutra, pelo mapeamento ({doc}`/platform/compliance/mapping-and-tools`).
- A Declaração guarda versões: a que se entrega numa auditoria fica fixada.
