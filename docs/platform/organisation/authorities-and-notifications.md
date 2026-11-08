# Autoridades, designações e notificações

Registo das comunicações às autoridades: designações e respetivas datas de comunicação, notificações de incidentes com o prazo calculado e contactos autorizados.

```{video} 308-autoridades-e-notificacoes
```

O módulo da lei descreve os prazos de vinte e quatro horas, setenta e duas horas e trinta dias úteis. Esta página descreve o ecrã onde a plataforma calcula esses prazos e regista as comunicações às autoridades.

## Acesso

**Governar** > **Obrigações e terceiros** > **Autoridades e notificações**

```{figure} /_static/capturas/autoridades/menu.jpg
:alt: Menu lateral: Governar > Obrigações e terceiros > Autoridades e notificações

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

Este ecrã responde ao controlo 5.5 da ISO 27001 (contactos com as autoridades) e às obrigações de notificação: incidentes ao CNCS, violações de dados pessoais à Comissão Nacional de Proteção de Dados e designações que a lei exige comunicar.

**Finalidade**

- Controlo 5.5 da ISO/IEC 27001: contactos das autoridades, com data de atualização, e registo das notificações.
- Notificações de incidentes ao CNCS (art. 42.º a art. 44.º) e violações de dados à CNPD (art. 33.º do RGPD).
- Designações que a lei exige comunicar, nas entidades essenciais e importantes em 20 dias úteis (art. 31.º e art. 32.º).

## Informação a solicitar

Solicite à direção a identificação das pessoas autorizadas a contactar cada autoridade e dos respetivos substitutos, e à secretaria as designações e as datas da sua comunicação. Defina com a equipa de informática o registo das horas de cada incidente, que determinam os prazos.

**Responsáveis**

| Informação | Responsável |
|---|---|
| Pessoas autorizadas a contactar cada autoridade e substitutos | direção |
| Designações e data da respetiva comunicação | secretaria-geral; responsável |
| Horas de deteção e de fim do impacto de cada incidente | equipa de informática; ponto de contacto |
| Violações de dados pessoais | encarregado de proteção de dados |

## Configuração do ecrã

No topo, são apresentados cinco indicadores. Os dois primeiros distinguem as notificações com prazo ultrapassado, que constituem um incumprimento legal em curso, das notificações por submeter dentro do prazo, que constituem trabalho pendente.

Em seguida, são apresentadas as designações exigidas à entidade que estão em falta. Uma vez que o politécnico dos exemplos é uma entidade pública relevante, o responsável de cibersegurança e o ponto de contacto permanente não são incluídos, e o motivo é indicado numa linha separada.

```{figure} /_static/capturas/autoridades/abrir-1.jpg
:alt: Governar > Obrigações e terceiros > Autoridades e notificações

Ecrã **Governar** > **Obrigações e terceiros** > **Autoridades e notificações**.
```

No ecrã, encontra os seguintes elementos:

1. **Prazo ultrapassado:** Notificações em incumprimento.
2. **Por submeter:** Notificações pendentes dentro do prazo.
3. **Não exigidas a esta entidade:** Designações não aplicáveis à qualificação, com o motivo.

## Notificações

Cada notificação indica a obrigação, a autoridade e o estado: por submeter, prazo ultrapassado ou submetida no prazo. O estado não é gravado: é calculado no momento da consulta, a partir da obrigação e da hora de início da contagem.

A contagem inicia-se no momento definido por lei. A notificação inicial conta a partir da conclusão de que existe um incidente significativo; a notificação do fim do impacto, a partir do fim do impacto; o relatório final, a partir da notificação do fim do impacto. O nome do campo da data no formulário adapta-se à obrigação, para evitar erros.

```{figure} /_static/capturas/autoridades/notificacoes-1.jpg
:alt: As notificações e os seus prazos

As notificações e os respetivos prazos.
```

1. **Estado:** Calculado no momento da consulta, e não gravado.

## Designações

No separador **Designações**, cada designação indica o ato de designação, a data de início e a data de comunicação à autoridade. Nas entidades essenciais e importantes, decorridos vinte dias úteis sem comunicação, a situação é assinalada a vermelho.

```{figure} /_static/capturas/autoridades/designacoes-1.jpg
:alt: As designações

As designações (1 de 2).
```

1. Separador **Designações:** Apresenta a lista de designações.

```{figure} /_static/capturas/autoridades/designacoes-2.jpg
:alt: As designações

As designações (2 de 2).
```

## Contactos

No separador **Autoridades e contactos**, cada autoridade regista as pessoas autorizadas a contactá-la e os respetivos substitutos. Cada contacto tem um botão de confirmação, que regista a data de atualização exigida pela norma; um contacto sem confirmação há mais de um ano é considerado caducado.

As autoridades setoriais (por exemplo, o Banco de Portugal ou a ANACOM) são adicionadas com o botão do topo. O último separador regista os grupos de interesse: alertas subscritos e associações do setor.

```{figure} /_static/capturas/autoridades/contactos-1.jpg
:alt: Autoridades e contactos

Autoridades e contactos (1 de 3).
```

1. Separador **Autoridades e contactos:** Apresenta as autoridades registadas.

```{figure} /_static/capturas/autoridades/contactos-2.jpg
:alt: Autoridades e contactos

Autoridades e contactos (2 de 3).
```

1. Selecione a autoridade (neste exemplo, **Centro Nacional de Cibersegurança**).

```{figure} /_static/capturas/autoridades/contactos-3.jpg
:alt: Autoridades e contactos

Autoridades e contactos (3 de 3).
```

## Resumo

A plataforma calcula os prazos, em horas corridas ou dias úteis, e distingue o trabalho pendente do incumprimento. Os feriados não são considerados, para que o prazo calculado nunca seja posterior ao prazo real e o aviso seja sempre antecipado.

A plataforma não submete notificações às autoridades nem gere o ciclo de vida do incidente. Uma notificação é um registo com o respetivo prazo. A submissão é sempre efetuada na plataforma do CNCS ou da CNPD.

**Funcionalidades e limitações**

- Calcula os prazos das notificações, em horas corridas ou em dias úteis, consoante a obrigação.
- Distingue as notificações por submeter das notificações com prazo ultrapassado.
- Não submete notificações: estas são efetuadas na plataforma do CNCS e da CNPD.
- Não gere o ciclo de vida do incidente: uma notificação é um registo com o respetivo prazo.
- Os feriados não são considerados no cálculo, pelo que o prazo calculado nunca é posterior ao prazo real.
