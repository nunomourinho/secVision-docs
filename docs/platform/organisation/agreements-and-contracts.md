# Acordos e contratos

Registo centralizado dos contratos, acordos de confidencialidade e acordos de subcontratação de dados, com as cláusulas de segurança registadas como campos (para permitir a sua contagem) e os prazos de denúncia visíveis.

```{video} 309-acordos-e-contratos
```

Os fornecedores acedem aos sistemas, tratam dados e podem constituir a porta de entrada de um ataque. As suas obrigações decorrem do contrato. Esta página descreve o registo dos acordos e das respetivas cláusulas de segurança.

## Acesso

**Governar** > **Obrigações e terceiros** > **Acordos e contratos**

```{figure} /_static/capturas/acordos/menu.jpg
:alt: Menu lateral: Governar > Obrigações e terceiros > Acordos e contratos

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

Este ecrã responde aos controlos da ISO 27001 sobre fornecedores e serviços em nuvem, ao registo centralizado dos acordos de confidencialidade e ao artigo 28.º do Regulamento Geral sobre a Proteção de Dados, que exige contrato com quem trata dados por conta da organização.

**Finalidade**

- Controlos 5.20 e 5.23 da ISO/IEC 27001: cláusulas de segurança nos acordos com fornecedores e nos serviços em nuvem.
- Controlo 6.6: registo centralizado dos acordos de confidencialidade e dos respetivos prazos.
- Art. 28.º do RGPD: contrato com quem trata dados pessoais por conta da organização.
- Nas entidades públicas relevantes, a política de segurança de fornecedores (O.PSF, Grupo A).

## Informação a solicitar

Solicite ao serviço de compras e ao serviço jurídico os contratos em vigor, com as datas e o aviso prévio, e a análise do clausulado: existência de cláusulas de segurança, direito de auditoria e prazo de notificação de incidentes.

**Responsáveis**

| Informação | Responsável |
|---|---|
| Contratos em vigor, com datas e aviso prévio | serviço de compras; serviço jurídico |
| Cláusulas de segurança, auditoria, notificação de incidentes e saída | serviço jurídico, com base no clausulado |
| Contratos que envolvem dados pessoais | encarregado de proteção de dados |
| Acordos de confidencialidade assinados | recursos humanos |

## Configuração do ecrã

São apresentados cinco indicadores, cada um com filtro: acordos em vigor, a expirar nos próximos noventa dias, sem cláusulas de segurança, sem direito de auditoria e com tratamento de dados pessoais sem o contrato de subcontratação do artigo 28.º do RGPD.

O aviso prévio alarga o horizonte do alerta: um contrato com cento e oitenta dias de aviso prévio é assinalado cento e oitenta dias antes. Um contrato com renovação automática renova-se se não for denunciado, pelo que a lista o indica expressamente.

```{figure} /_static/capturas/acordos/abrir-1.jpg
:alt: Governar > Obrigações e terceiros > Acordos e contratos

Ecrã **Governar** > **Obrigações e terceiros** > **Acordos e contratos**.
```

No ecrã, encontra os seguintes elementos:

1. **A expirar:** Acordos a expirar, considerando o aviso prévio.
2. **Sem cláusulas de segurança.**
3. **Sem direito de auditoria.**

## Ficha do acordo

As cláusulas são registadas como campos: cláusulas de segurança, direito de auditoria, prazo de notificação de incidentes (em horas), cláusula de saída e portabilidade, envolvimento de dados pessoais e transferência para fora da União.

O registo em campos, e não em texto livre, permite contabilizar, por exemplo, os fornecedores críticos obrigados a comunicar um incidente e o respetivo prazo. Associe também os processos suportados pelo acordo, para identificar o impacto da cessação do contrato.

```{figure} /_static/capturas/acordos/acordo-1.jpg
:alt: As cláusulas, como campos

As cláusulas como campos (1 de 3).
```

1. Selecione o acordo (neste exemplo, **AC-001**).

```{figure} /_static/capturas/acordos/acordo-2.jpg
:alt: As cláusulas, como campos

As cláusulas como campos (2 de 3).
```

```{figure} /_static/capturas/acordos/acordo-3.jpg
:alt: As cláusulas, como campos

As cláusulas como campos (3 de 3).
```

## Resumo

A plataforma contabiliza e filtra os acordos pelos campos e alerta para os prazos. Permite converter contratos públicos importados do portal BASE em acordos; estes acordos são criados sem cláusulas assinaladas, uma vez que o portal publica valores e adjudicatários, mas não o conteúdo do contrato.

As cláusulas são assinaladas após a leitura do contrato. A sua marcação sem leitura prévia tornaria os indicadores do painel incorretos.

**Funcionalidades e limitações**

- Contabiliza e filtra os acordos pelas cláusulas em falta e alerta para os prazos de denúncia.
- Converte contratos públicos do portal BASE em acordos, sem cláusulas assinaladas.
- Não analisa o clausulado: as cláusulas são assinaladas após a leitura do contrato.
