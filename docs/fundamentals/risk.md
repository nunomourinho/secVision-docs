# O que é o risco

Ameaça, vulnerabilidade, impacto e probabilidade; risco inerente e residual; o apetite pelo risco como decisão de gestão; e o motivo pelo qual o risco nunca é nulo.

```{video} 103-risco
```

A legislação de cibersegurança assenta no conceito de risco. O decreto-lei obriga as entidades a gerir os riscos, as normas exigem uma apreciação de risco e o auditor solicita o registo de riscos. Esta página explica o conceito, com um exemplo.

Os exemplos utilizam sempre a mesma organização: o Instituto Politécnico de Vila Nova. Trata-se de uma organização fictícia, semelhante a muitos serviços públicos reais, com mil e duzentas pessoas, estudantes, serviços académicos, um serviço de correio eletrónico e uma rede.

## Uma perceção ou uma quantidade

Na linguagem comum, o risco é uma perceção: a avaliação de que atravessar fora da passadeira é arriscado varia de pessoa para pessoa.

Na gestão da segurança da informação, o risco é uma quantidade, que se estima, compara e sobre a qual se decide. O princípio fundamental é o seguinte: duas pessoas diferentes, com os mesmos dados e os mesmos critérios, devem obter o mesmo valor. Caso contrário, os critérios não estão corretamente definidos.

**Perceção e quantidade**

- Na linguagem comum: «isto é arriscado», uma impressão que varia de pessoa para pessoa.
- Na gestão da segurança: uma quantidade, que se estima, compara e sobre a qual se decide.
- Duas pessoas diferentes, com os mesmos dados, devem obter o mesmo valor.

## Componentes do risco

Um risco tem sempre quatro componentes:

- **Ativo:** Elemento com valor. Na segurança da informação, o ativo principal é a própria informação, seguida dos sistemas e das pessoas que a tratam.
- **Ameaça:** Causa potencial de dano. Pode ser um atacante, mas também um incêndio, uma falha de energia ou um erro humano.
- **Vulnerabilidade:** Fraqueza explorada pela ameaça; por exemplo, uma palavra-passe fraca, um servidor desatualizado ou uma cópia de segurança nunca testada.
- **Impacto:** Perda resultante da concretização do risco.

Os três primeiros componentes têm de coexistir. Uma vulnerabilidade num computador desligado, sem dados e guardado num armário, não gera um risco relevante, porque não existe um ativo com valor nem um caminho para a ameaça.

**Componentes de um risco**

Ativo
: elemento com valor: a informação e os sistemas e pessoas que a tratam

Ameaça
: causa potencial de dano: um atacante, um incêndio, um erro humano

Vulnerabilidade
: fraqueza explorada pela ameaça: uma palavra-passe fraca, um sistema desatualizado

Impacto
: perda resultante: financeira, de serviço, de confiança ou de cumprimento legal

```{figure} /_static/img/103-risco/01.jpg
:alt: As peças de um risco

Componentes de um risco.
```

No Politécnico, o ativo é o correio eletrónico de toda a instituição, que contém dados de estudantes e de pessoal. A ameaça é um ataque de ransomware: um programa malicioso que encripta os servidores e exige um resgate.

A vulnerabilidade consiste em contas de correio sem segundo fator de autenticação e em cópias de segurança guardadas no mesmo servidor, que o ataque também encripta. O impacto é uma semana sem correio, a possível exposição de dados pessoais e as notificações obrigatórias à CNPD e ao CNCS.

**Exemplo: Politécnico de Vila Nova**

- Ativo: o correio eletrónico de toda a instituição, com os dados de estudantes e de pessoal.
- Ameaça: um ataque de ransomware, que encripta os servidores e exige um resgate.
- Vulnerabilidade: contas sem segundo fator de autenticação e cópias guardadas no mesmo servidor.
- Impacto: uma semana sem correio, dados pessoais expostos e notificações à CNPD e ao CNCS.

## Medição

Para comparar riscos, cada risco é medido com duas questões: qual a probabilidade de a ameaça explorar a vulnerabilidade, e qual seria o impacto. Cada resposta é dada numa escala definida (por exemplo, de um a cinco) e o risco corresponde ao produto das duas.

O impacto é avaliado separadamente para as três propriedades da informação: confidencialidade, integridade e disponibilidade, uma vez que uma fuga de dados e uma interrupção de serviço têm perfis diferentes. No Politécnico, o ransomware tem impacto grave nas três: os dados podem ser exfiltrados e alterados, e o serviço é interrompido.

**Risco = probabilidade × impacto**

- Probabilidade: possibilidade de a ameaça explorar a vulnerabilidade, numa escala definida (por exemplo, de 1 a 5).
- Impacto: gravidade das consequências, na mesma escala, avaliada em confidencialidade, integridade e disponibilidade.
- O produto resulta num valor que permite comparar riscos de natureza muito diferente.

```{tip}
Os níveis da escala e o respetivo significado são definidos nos critérios de risco ({doc}`/platform/risk/risk-criteria`).
```

A representação habitual é uma matriz, com o impacto num eixo e a probabilidade no outro, em que cada risco ocupa uma célula. Um risco com impacto muito grave e probabilidade quase certa é crítico; um risco com impacto insignificante e probabilidade rara é baixo.

Os limites (por exemplo, o valor a partir do qual um risco é alto) não são definidos por lei: são decididos por cada organização e registados nos critérios de risco. Uma vez definidos, aplicam-se a todos os riscos da mesma forma.

**Exemplo de matriz de risco**

| Impacto ↓  ·  Probabilidade → | 1 Rara | 3 Possível | 5 Quase certa |
|---|---|---|---|
| 5 Muito grave | 5 · médio | 15 · alto | 25 · crítico |
| 3 Moderado | 3 · baixo | 9 · médio | 15 · alto |
| 1 Insignificante | 1 · baixo | 3 · baixo | 5 · médio |

```{tip}
Exemplo ilustrativo. Os limites entre baixo, médio, alto e crítico são definidos por cada organização.
```

## Risco inerente e residual

O mesmo risco tem duas medidas. O risco inerente é o risco que existiria na ausência de qualquer controlo: um valor teórico, utilizado para comparação. O risco residual é o risco que subsiste após a aplicação dos controlos efetivamente em funcionamento. As decisões baseiam-se no risco residual.

No Politécnico, a ativação do segundo fator em todas as contas e a transferência das cópias de segurança para um local separado e testado reduzem significativamente a probabilidade de sucesso do ransomware. O risco inerente mantém-se alto; o residual passa a médio ou baixo.

O apetite pelo risco define o nível de risco residual que a organização aceita de forma consciente. Esta decisão não é técnica, mas sim da direção: a equipa de informática indica o custo de reduzir um risco, e a direção decide se aprova o investimento ou se aceita o risco residual, formalizando a decisão por escrito.

**Risco inerente, residual e aceitação**

- Risco inerente: o risco que existiria sem qualquer controlo. Utilizado para comparação.
- Risco residual: o risco que subsiste após os controlos efetivamente implementados. É a base das decisões.
- Apetite pelo risco: o nível de risco residual que a organização aceita de forma consciente. É uma decisão de gestão.

O risco nunca é nulo. A tentativa de eliminar totalmente um risco constitui má gestão, porque consome num risco reduzido recursos necessários para um risco elevado.

A questão adequada não é «a organização está segura?», mas sim «que riscos foram aceites, e esta aceitação é conhecida?». Um risco aceite tem um responsável, uma data e uma justificação escrita. Um risco não identificado não está aceite: está por gerir.

```{important}
**O risco nunca é nulo**

- A tentativa de eliminar totalmente um risco constitui má gestão: consome num risco reduzido os recursos necessários para um risco elevado.
- A questão adequada não é «a organização está segura?», mas «que riscos foram aceites, e esta aceitação é conhecida?»
- Um risco aceite tem responsável, data e justificação escrita. Um risco ignorado não é um risco aceite.
```

## Informação a solicitar

A gestão do risco exige informação de diferentes responsáveis. À direção, o apetite pelo risco e a autoridade para aceitar cada tipo de risco. Aos responsáveis de serviço, a informação crítica e o custo da sua indisponibilidade durante um dia.

À equipa de informática, as vulnerabilidades conhecidas e os controlos efetivamente em funcionamento, e não apenas os documentados. Ao encarregado de proteção de dados, a localização e o tipo de dados pessoais. Nenhum destes responsáveis dispõe, isoladamente, de toda a informação.

**Responsáveis**

- Direção: apetite pelo risco e autoridade para aceitar cada tipo de risco.
- Responsáveis de serviço: informação e sistemas críticos, e custo da sua indisponibilidade durante um dia.
- Equipa de informática: vulnerabilidades conhecidas e controlos efetivamente em funcionamento.
- Encarregado de proteção de dados: localização e categorias dos dados pessoais.

Na plataforma, os critérios e o apetite são definidos em **Critérios e apetite**. Cada risco é registado no **Registo de risco**, com o ativo, a ameaça, a probabilidade e o impacto nas três propriedades. As páginas do módulo da plataforma descrevem estes ecrãs.

A plataforma não guarda o risco inerente como um valor introduzido manualmente: calcula-o sempre a partir da probabilidade e do impacto. Desta forma, o valor não pode ser alterado sem alterar também a respetiva fundamentação.

**Correspondência na plataforma**

- Os critérios e o apetite são definidos em **Identificar** > **Risco** > **Critérios e apetite** ({doc}`/platform/risk/risk-criteria`).
- Cada risco, com ativo, ameaça, probabilidade e impacto C/I/A, é registado no Registo de risco ({doc}`/platform/risk/risk-register`).
- O risco inerente é calculado automaticamente, e o residual resulta dos controlos associados ao risco.
