# Controlos, medidas e o sistema de gestão

O que é um controlo, porque é que um controlo não é uma ferramenta, as três naturezas das medidas, e o sistema de gestão da segurança da informação com o ciclo planear, executar, verificar, agir.

```{video} 104-controlos-e-sgsi
```

Já sabemos o que se protege e o que é o risco. Agora: o que reduz o risco? A resposta são os controlos — e a forma organizada de os gerir ao longo do tempo chama-se sistema de gestão da segurança da informação.

## Controlos

Um controlo, ou medida, é algo que reduz um risco: a probabilidade de acontecer, o impacto se acontecer, ou as duas coisas. A lei portuguesa chama-lhes medidas de cibersegurança; as normas internacionais chamam-lhes controlos. É a mesma ideia.

Exemplos: autenticação com segundo fator, que torna muito mais difícil usar uma palavra-passe roubada; cópias de segurança testadas, que reduzem o impacto de um ataque; uma política de acessos; formação.

**O que é um controlo**

- Um controlo — ou medida — é algo que reduz um risco: a probabilidade, o impacto, ou os dois.
- A lei portuguesa chama-lhes «medidas de cibersegurança»; as normas chamam-lhes «controlos». É a mesma ideia.
- Exemplos: autenticação com segundo fator, cópias de segurança testadas, uma política de acessos, formação.

As medidas têm três naturezas. Organizacionais: regras, responsabilidades e processos, como uma política ou um inventário. Tecnológicas: configurações e sistemas, como as cópias de segurança ou a autenticação. E humanas: as pessoas, com formação e sensibilização.

No Anexo IV do Regulamento, que é o das entidades públicas relevantes, há trinta e uma medidas: doze organizacionais, dezasseis tecnológicas e três humanas. O código de cada uma começa pela natureza: O, T ou H. Repare que quase metade não é tecnologia.

**Três naturezas de medidas**

| Natureza | O que é | No Anexo IV |
|---|---|---|
| Organizacional (O.) | regras, responsabilidades, processos — uma política, um inventário | 12 medidas |
| Tecnológica (T.) | configurações e sistemas — cópias, autenticação, atualizações | 16 medidas |
| Humana (H.) | pessoas — formação, sensibilização, exercícios | 3 medidas |

```{tip}
As 31 medidas do Anexo IV do Regulamento 756/2026, para as entidades públicas relevantes. O código de cada uma começa pela natureza.
```

Um erro muito comum: pensar que um controlo é uma ferramenta. Comprar um antivírus não implementa o controlo de proteção contra código malicioso.

Implementa-o quem definiu a regra, a aplicou a todos os equipamentos, e consegue mostrar, numa data concreta, que equipamentos estão cobertos. A ferramenta é um meio. O controlo é a regra, aplicada, com prova.

```{important}
**Um controlo não é uma ferramenta**

- Comprar um antivírus não implementa o controlo de proteção contra código malicioso.
- Implementa-o quem definiu a regra, a aplicou a todos os equipamentos, e consegue mostrar a cobertura numa data.
- Uma ferramenta é um meio. O controlo é a regra, aplicada, com prova.
```

Todo o controlo, para ser gerível, tem quatro coisas. Um enunciado: o que se exige, por escrito. Um responsável: uma pessoa com nome, não um serviço vago. Um estado: não iniciado, em curso, ou implementado.

E prova: uma evidência de que existe e funciona — um registo, um relatório, uma configuração, sempre com data. Um controlo sem prova, para um auditor, não existe.

**As quatro coisas de um controlo**

- Um enunciado: o que se exige, escrito.
- Um responsável: uma pessoa com nome, não «a informática».
- Um estado: não iniciado, em curso, implementado.
- Prova: evidência de que existe e funciona — um registo, um relatório, uma configuração, uma data.

## O SGSI

Um sistema de gestão da segurança da informação — SGSI — não é um programa de computador. É o conjunto de políticas, processos, papéis e registos com que a organização gere a segurança da sua informação, de forma deliberada.

Todas as organizações têm alguma segurança. A diferença é que, num SGSI, está escrito o que se faz, porquê, e quem responde — e há registo de que se fez. E não promete que nada corre mal: promete que a organização sabe o que pode correr mal, decidiu o que fazer, e o consegue demonstrar.

**O sistema de gestão da segurança da informação**

- SGSI não é um software: é o conjunto de políticas, processos, papéis e registos com que a organização gere a segurança.
- A palavra que faz o trabalho é «deliberadamente»: está escrito o que se faz, porquê, quem responde, e há registo de que se fez.
- Um SGSI não promete que nada corre mal: promete que a organização sabe o que pode correr mal, decidiu o que fazer, e o pode demonstrar.

Um sistema de gestão funciona em ciclo, e o ciclo tem quatro fases. Planear: conhecer o contexto, apreciar os riscos, escolher os controlos e os objetivos. Executar: implementar, formar, operar.

Verificar: medir, auditar, e rever com a direção. E agir: corrigir o que falhou e melhorar. Depois, volta-se a planear. A ideia vem da gestão da qualidade, e é a mesma em todas as normas de gestão.

**O ciclo — planear, executar, verificar, agir**

Planear
: conhecer o contexto, apreciar os riscos, escolher os controlos e os objetivos

Executar
: implementar os controlos, formar as pessoas, operar

Verificar
: medir, auditar, rever com a direção

Agir
: corrigir o que falhou e melhorar — e voltar a planear

```{figure} /_static/img/104-controlos-e-sgsi/01.jpg
:alt: O ciclo — planear, executar, verificar, agir

O ciclo — planear, executar, verificar, agir.
```

Na plataforma, cada medida tem o enunciado, um responsável, o estado e as evidências. As políticas e os procedimentos têm a sua secção. E o ciclo completo — risco, implementação, prova, auditoria e revisão — percorre-se pela ordem dos menus, como vamos fazer no módulo da plataforma.

**Onde isto entra na plataforma**

- Cada medida ou controlo, com enunciado, responsável, estado e evidências ({doc}`/platform/compliance/statement-of-applicability` e {doc}`/platform/monitoring/evidence`).
- Políticas, procedimentos e planos do SGSI ({doc}`/platform/protect-and-detect/isms-documents`).
- O ciclo completo: risco, implementação, evidências, auditorias, revisão pela gestão ({doc}`/platform/risk/risk-criteria` a {doc}`/platform/audit/audit-dossier-and-certification`).
