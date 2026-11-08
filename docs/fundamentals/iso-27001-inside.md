# A ISO/IEC 27001 por dentro

Organização da ISO/IEC 27001: as cláusulas 4 a 10 do sistema de gestão, os 93 controlos do Anexo A e a Declaração de Aplicabilidade, apresentados em conceitos, sem o texto da norma.

```{video} 106-iso-27001-por-dentro
```

A ISO/IEC 27001 é a norma de referência para o sistema de gestão da segurança da informação. Esta página descreve a sua organização. O texto da norma não é citado, uma vez que é licenciado e deve ser adquirido; a estrutura é pública e suficiente para efeitos de orientação.

## Estrutura

A norma tem duas partes. As cláusulas 4 a 10 definem os requisitos do sistema de gestão; para a certificação, todos são obrigatórios, sem exceção.

O Anexo A contém noventa e três controlos de referência. Estes controlos não são todos obrigatórios: são selecionados com base na apreciação de risco, e a exclusão de um controlo tem de ser justificada.

**Duas partes**

Cláusulas 4 a 10
: requisitos do sistema de gestão, todos obrigatórios para a certificação

Anexo A
: lista de 93 controlos de referência, selecionados com base na apreciação de risco

```{figure} /_static/img/106-iso-27001-por-dentro/01.jpg
:alt: Duas partes

As duas partes da norma.
```

As cláusulas seguem o ciclo descrito em {doc}`/fundamentals/controls-and-isms`:

- **Cláusula 4 (contexto):** A organização, as partes envolventes, as respetivas expectativas e o âmbito do sistema.
- **Cláusula 5 (liderança):** O compromisso da direção e a aprovação da política.
- **Cláusula 6 (planeamento):** Riscos, tratamento e objetivos.
- **Cláusula 7 (suporte):** Recursos, competências, sensibilização, comunicação e documentos.
- **Cláusula 8 (operação):** Execução do planeado.
- **Cláusula 9 (avaliação):** Medição, auditoria e revisão pela gestão.
- **Cláusula 10 (melhoria):** Tratamento das não conformidades e melhoria.

**As cláusulas do sistema de gestão**

| Cláusula | Tema | Resumo |
|---|---|---|
| 4 | Contexto | a organização, as partes envolventes, as respetivas expectativas e o âmbito |
| 5 | Liderança | compromisso da direção, aprovação da política, atribuição de papéis |
| 6 | Planeamento | riscos e oportunidades, tratamento do risco, objetivos |
| 7 | Suporte | recursos, competências, sensibilização, comunicação, documentos |
| 8 | Operação | execução do planeado; apreciação e tratamento do risco na prática |
| 9 | Avaliação do desempenho | medição, auditoria interna, revisão pela gestão |
| 10 | Melhoria | não conformidades, ações corretivas, melhoria contínua |

## O Anexo A

Os noventa e três controlos do Anexo A estão organizados em quatro temas: trinta e sete organizacionais (políticas, papéis, inventário, fornecedores, incidentes, continuidade), oito relativos a pessoas (verificação na contratação, formação, teletrabalho), catorze físicos (perímetros, entradas, equipamentos) e trinta e quatro tecnológicos (acessos, autenticação, cópias de segurança, registos, encriptação, desenvolvimento seguro).

Esta organização corresponde às três naturezas das medidas do Anexo IV da lei, com uma distribuição diferente.

**Os quatro temas do Anexo A**

| Tema | Controlos | Exemplos |
|---|---|---|
| Organizacionais | 37 | políticas, papéis, inventário de ativos, fornecedores, incidentes, continuidade |
| Pessoas | 8 | verificação na contratação, formação e sensibilização, teletrabalho |
| Físicos | 14 | perímetros, controlo de entradas, equipamentos, secretária limpa |
| Tecnológicos | 34 | acessos, autenticação, cópias de segurança, registos, encriptação, desenvolvimento seguro |

```{tip}
Edição de 2022, com 93 controlos. A ISO/IEC 27002 contém a orientação para cada controlo.
```

## A Declaração de Aplicabilidade

A Declaração de Aplicabilidade é o documento central de uma certificação. Enumera os noventa e três controlos e indica, para cada um, se é aplicável, a respetiva justificação e o estado de implementação. É exigida pela própria norma, no planeamento do tratamento do risco.

Em inglês, designa-se Statement of Applicability, pelo que é frequentemente referida como SoA. A lei portuguesa reforça a sua importância: o certificado ISO 27001 entregue ao CNCS é acompanhado da Declaração de Aplicabilidade, nos termos do artigo 27.º do Regulamento.

**A Declaração de Aplicabilidade**

- Documento com os 93 controlos: aplicabilidade, justificação e estado de implementação de cada um.
- É exigida pela própria norma, no planeamento do tratamento do risco.
- Em inglês, designa-se Statement of Applicability (SoA).
- A lei portuguesa exige-a junto do certificado ISO/IEC 27001 entregue ao CNCS (art. 27.º, n.º 5, do Regulamento).

## Certificação

Para obter o certificado, a organização implementa o sistema de gestão e opera-o durante um período, com registos. Realiza uma auditoria interna e uma revisão pela gestão e, só depois, contacta o organismo de certificação.

O certificador audita em duas fases: primeiro, os documentos e a preparação; depois, a implementação no terreno, com entrevistas e evidências. O certificado é válido por três anos, com auditorias de acompanhamento anuais.

**Obtenção do certificado**

- A organização implementa o sistema de gestão e opera-o durante um período, com registos.
- Realiza uma auditoria interna e uma revisão pela gestão antes de contactar o certificador.
- O organismo acreditado audita em duas fases: primeiro os documentos e a preparação, depois a implementação no terreno.
- O certificado é válido por três anos, com auditorias de acompanhamento anuais.

Na plataforma, cada cláusula tem um ecrã próprio: contexto, âmbito, políticas, riscos, auditorias e revisão pela gestão. A Declaração de Aplicabilidade é gerada a partir das normas em âmbito, e o dossier de auditoria reúne os elementos solicitados pelo certificador.

Se a licença da ISO não estiver instalada, a plataforma utiliza o QNRCS e a lei, e identifica a norma em falta.

**Correspondência na plataforma**

- As cláusulas 4 a 10 têm ecrã próprio: contexto, âmbito, políticas, riscos, auditorias e revisão (módulo C).
- A Declaração de Aplicabilidade é gerada a partir das normas em âmbito e do risco ({doc}`/platform/compliance/statement-of-applicability`).
- O dossier de auditoria reúne os elementos solicitados pelo certificador ({doc}`/platform/audit/audit-dossier-and-certification`).
- Sem a licença ISO instalada, a plataforma utiliza o QNRCS e a lei, e identifica a norma em falta.
