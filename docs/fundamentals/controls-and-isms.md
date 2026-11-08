# Controlos, medidas e o sistema de gestão

Definição de controlo, distinção entre controlo e ferramenta, as três naturezas das medidas e o sistema de gestão da segurança da informação, com o ciclo planear, executar, verificar e agir.

```{video} 104-controlos-e-sgsi
```

Depois de identificar o objeto da proteção e o risco, importa definir o que reduz o risco: os controlos. A gestão organizada dos controlos ao longo do tempo designa-se sistema de gestão da segurança da informação.

## Controlos

Um controlo, ou medida, é um mecanismo que reduz um risco: a probabilidade de ocorrência, o impacto ou ambos. A lei portuguesa designa-os por medidas de cibersegurança e as normas internacionais por controlos; o conceito é o mesmo.

Exemplos: autenticação com segundo fator, que dificulta a utilização de uma palavra-passe roubada; cópias de segurança testadas, que reduzem o impacto de um ataque; uma política de acessos; formação.

**O que é um controlo**

- Um controlo, ou medida, é um mecanismo que reduz um risco: a probabilidade, o impacto ou ambos.
- A lei portuguesa designa-os por «medidas de cibersegurança» e as normas por «controlos». O conceito é o mesmo.
- Exemplos: autenticação com segundo fator, cópias de segurança testadas, uma política de acessos, formação.

As medidas têm três naturezas:

- **Organizacionais:** Regras, responsabilidades e processos, como uma política ou um inventário.
- **Tecnológicas:** Configurações e sistemas, como as cópias de segurança ou a autenticação.
- **Humanas:** Formação e sensibilização das pessoas.

O Anexo IV do Regulamento, aplicável às entidades públicas relevantes, inclui trinta e uma medidas: doze organizacionais, dezasseis tecnológicas e três humanas. O código de cada medida começa pela respetiva natureza: O, T ou H. Quase metade das medidas não é tecnológica.

**Três naturezas de medidas**

| Natureza | Descrição | No Anexo IV |
|---|---|---|
| Organizacional (O.) | regras, responsabilidades e processos: uma política, um inventário | 12 medidas |
| Tecnológica (T.) | configurações e sistemas: cópias, autenticação, atualizações | 16 medidas |
| Humana (H.) | pessoas: formação, sensibilização, exercícios | 3 medidas |

```{tip}
As 31 medidas do Anexo IV do Regulamento 756/2026, para as entidades públicas relevantes. O código de cada medida começa pela respetiva natureza.
```

Um controlo não é uma ferramenta. A aquisição de um antivírus não implementa, por si só, o controlo de proteção contra código malicioso.

O controlo está implementado quando a regra está definida, aplicada a todos os equipamentos e é possível demonstrar, numa data concreta, quais os equipamentos abrangidos. A ferramenta é um meio; o controlo é a regra aplicada, com evidência.

```{important}
**Um controlo não é uma ferramenta**

- A aquisição de um antivírus não implementa o controlo de proteção contra código malicioso.
- O controlo está implementado quando a regra está definida, aplicada a todos os equipamentos, e a cobertura é demonstrável numa data.
- A ferramenta é um meio. O controlo é a regra aplicada, com evidência.
```

Para ser gerível, cada controlo tem quatro elementos:

1. **Enunciado:** O requisito, por escrito.
2. **Responsável:** Uma pessoa identificada, e não um serviço genérico.
3. **Estado:** Não iniciado, em curso ou implementado.
4. **Evidência:** Prova de que o controlo existe e funciona (um registo, um relatório, uma configuração), sempre datada. Para um auditor, um controlo sem evidência não existe.

**Os quatro elementos de um controlo**

- Enunciado: o requisito, por escrito.
- Responsável: uma pessoa identificada, e não «a informática».
- Estado: não iniciado, em curso, implementado.
- Evidência: prova de que o controlo existe e funciona (um registo, um relatório, uma configuração), com data.

## O SGSI

Um sistema de gestão da segurança da informação (SGSI) não é um programa informático. É o conjunto de políticas, processos, papéis e registos com que a organização gere a segurança da sua informação de forma deliberada.

Todas as organizações têm algum nível de segurança. Num SGSI, estão documentadas as atividades realizadas, o respetivo fundamento e os responsáveis, e existe registo da sua execução. Um SGSI não garante a ausência de incidentes: garante que a organização conhece os riscos, decidiu como os tratar e consegue demonstrá-lo.

**O sistema de gestão da segurança da informação**

- O SGSI não é um software: é o conjunto de políticas, processos, papéis e registos com que a organização gere a segurança.
- O termo determinante é «deliberadamente»: estão documentadas as atividades, o fundamento e os responsáveis, e existe registo da execução.
- Um SGSI não garante a ausência de incidentes: garante que a organização conhece os riscos, decidiu como os tratar e consegue demonstrá-lo.

Um sistema de gestão funciona em ciclo, com quatro fases:

1. **Planear:** Conhecer o contexto, apreciar os riscos e definir os controlos e os objetivos.
2. **Executar:** Implementar, formar e operar.
3. **Verificar:** Medir, auditar e rever com a direção.
4. **Agir:** Corrigir as falhas e melhorar, voltando em seguida ao planeamento.

Este ciclo tem origem na gestão da qualidade e é comum a todas as normas de sistemas de gestão.

**O ciclo planear, executar, verificar, agir**

Planear
: conhecer o contexto, apreciar os riscos, definir os controlos e os objetivos

Executar
: implementar os controlos, formar as pessoas, operar

Verificar
: medir, auditar, rever com a direção

Agir
: corrigir as falhas e melhorar, voltando ao planeamento

```{figure} /_static/img/104-controlos-e-sgsi/01.jpg
:alt: O ciclo — planear, executar, verificar, agir

O ciclo planear, executar, verificar, agir.
```

Na plataforma, cada medida tem enunciado, responsável, estado e evidências. As políticas e os procedimentos têm uma secção própria. O ciclo completo (risco, implementação, evidência, auditoria e revisão) segue a ordem dos menus, descrita no módulo da plataforma.

**Correspondência na plataforma**

- Cada medida ou controlo, com enunciado, responsável, estado e evidências ({doc}`/platform/compliance/statement-of-applicability` e {doc}`/platform/monitoring/evidence`).
- Políticas, procedimentos e planos do SGSI ({doc}`/platform/protect-and-detect/isms-documents`).
- O ciclo completo: risco, implementação, evidências, auditorias e revisão pela gestão ({doc}`/platform/risk/risk-criteria` a {doc}`/platform/audit/audit-dossier-and-certification`).
