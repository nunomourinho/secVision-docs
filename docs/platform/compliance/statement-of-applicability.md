# A Declaração de Aplicabilidade

Registo controlo a controlo: aplicabilidade, justificação, origem, responsável, estado e data de revisão, e a percentagem de conformidade declarada resultante.

```{video} 320-declaracao-de-aplicabilidade
```

A página {doc}`/fundamentals/iso-27001-inside` define a Declaração de Aplicabilidade. Esta página descreve a sua elaboração: uma decisão escrita para cada controlo de cada norma no âmbito.

## Acesso

**Governar** > **GRC — Conformidade** > **Declaração de Aplicabilidade**

```{figure} /_static/capturas/soa/menu.jpg
:alt: Menu lateral: Governar > GRC — Conformidade > Declaração de Aplicabilidade

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Campos

Para cada controlo, são registados a aplicabilidade e a respetiva justificação, a origem (risco, lei, contrato ou boa prática), o responsável, o estado, a maturidade e a data da próxima revisão.

A origem «risco» exige a identificação do risco. As restantes origens são justificação suficiente: um controlo exigido por lei é aplicável independentemente de um risco.

**Campos de cada controlo**

| Campo | Descrição |
|---|---|
| Aplicável | sim ou não; a resposta negativa tem de ser justificada |
| Justificação | texto analisado pelo auditor quando um controlo é excluído |
| Origem | motivo da aplicabilidade: risco, legal, contratual, boa prática |
| Responsável | responsável pelo controlo |
| Estado | não iniciado, em curso, implementado |
| Maturidade | de 1 a 5: grau de consolidação |
| Próxima revisão | data obrigatória; sem data, o controlo não é revisto |

```{tip}
A ISO/IEC 27001 exige a Declaração no tratamento do risco; um certificado entregue ao CNCS é acompanhado da Declaração (art. 27.º, n.º 5).
```

## Configuração do ecrã

É apresentada uma declaração por cada norma no âmbito, com o número de controlos aplicáveis e excluídos.

```{figure} /_static/img/320-declaracao-de-aplicabilidade/01.jpg
:alt: Governar > GRC — Conformidade > Declaração de Aplicabilidade

Ecrã **Governar** > **GRC — Conformidade** > **Declaração de Aplicabilidade**.
```

## Declaração de uma norma

Na declaração de uma norma (neste exemplo, as medidas das entidades públicas relevantes), cada linha corresponde a uma medida, com a decisão, o estado e o responsável.

Um controlo pode estar implementado no centro de dados e por iniciar numa escola. O detalhe por grupo cria linhas por unidade, que detalham a linha global sem a alterar. A percentagem de conformidade declarada resulta deste ecrã e alimenta o painel.

```{figure} /_static/capturas/soa/norma-1.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (1 de 3).
```

1. **Filtro por grupo do Anexo IV:** Apresenta as medidas do grupo selecionado.

```{figure} /_static/capturas/soa/norma-2.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (2 de 3).
```

```{figure} /_static/capturas/soa/norma-3.jpg
:alt: As medidas do Anexo IV, uma a uma

As medidas do Anexo IV, uma a uma (3 de 3).
```

1. Botão **Exportar:** Exporta a declaração para folha de cálculo.

## Resumo

Solicite a cada responsável o estado real do respetivo controlo e a evidência correspondente, descrita na página das evidências. A plataforma guarda versões da Declaração: a versão entregue numa auditoria fica fixada e não é alterada pelo trabalho posterior.

**Informação a solicitar e funcionalidades**

- Responsáveis dos controlos: estado real de cada controlo, com a evidência correspondente ({doc}`/platform/monitoring/evidence`).
- Serviço jurídico: origem legal ou contratual de cada controlo aplicável.
- Herança: um controlo implementado numa norma pode ser contabilizado noutra, através do mapeamento ({doc}`/platform/compliance/mapping-and-tools`).
- A Declaração guarda versões: a versão entregue numa auditoria fica fixada.
