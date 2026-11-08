# Informação, ativos e as três propriedades

Definição de ativo, informação como ativo principal e significado da sua proteção (confidencialidade, integridade e disponibilidade), com exemplos de uma organização pública.

```{video} 102-informacao-e-ativos
```

Antes de abordar ameaças ou medidas, é necessário identificar o objeto da proteção: a informação. Esta página explica este conceito e as três propriedades que a segurança da informação procura garantir.

## Ativos

Um ativo é qualquer elemento com valor para a organização e que, por isso, necessita de proteção. Na segurança da informação, o ativo principal é a própria informação: processos dos estudantes, salários, contratos e dados de investigação.

Os restantes ativos (aplicações, servidores, rede, computadores, instalações e pessoas) existem para tratar essa informação. Cada ativo tem um dono: a pessoa responsável pelo ativo e que decide quem lhe pode aceder. O dono não é a equipa de informática, mas sim o responsável do serviço que utiliza o ativo.

**O que é um ativo**

- Um ativo é qualquer elemento com valor para a organização e que necessita de proteção.
- O ativo principal é a informação: processos de estudantes, salários, contratos e dados de investigação.
- Os restantes ativos existem para tratar essa informação: aplicações, servidores, redes, equipamentos, pessoas e instalações.
- Cada ativo tem um dono: a pessoa responsável pelo ativo e que decide quem lhe pode aceder.

Os ativos organizam-se em camadas. No topo, o processo; no politécnico, por exemplo, as matrículas e inscrições. O processo utiliza informação: os dados pessoais e académicos dos estudantes. A informação reside numa aplicação, o sistema de gestão académica, que funciona sobre uma infraestrutura: servidor, base de dados, rede e cópias de segurança.

Esta cadeia é relevante: se o servidor falhar, a aplicação para, a informação deixa de estar acessível e as matrículas ficam impedidas. Desta forma, um problema técnico torna-se um problema da organização.

**Do processo à máquina**

Processo ou serviço
: «Matrículas e inscrições»: o serviço que a organização presta aos seus utilizadores

Informação
: os dados pessoais e académicos dos estudantes

Aplicação
: o sistema de gestão académica

Infraestrutura
: o servidor, a base de dados, a rede e as cópias de segurança

```{figure} /_static/img/102-informacao-e-ativos/01.jpg
:alt: Do processo à máquina

Do processo à máquina.
```

## Confidencialidade, integridade e disponibilidade

Proteger a informação significa garantir três propriedades:

- **Confidencialidade:** Apenas as pessoas autorizadas acedem à informação.
- **Integridade:** A informação é exata e não foi alterada sem autorização.
- **Disponibilidade:** A informação está acessível quando é necessária.

No politécnico, a confidencialidade garante que as notas de um estudante não ficam visíveis para outros. A integridade garante que nenhuma nota lançada é alterada sem registo. A disponibilidade garante que o sistema de matrículas funciona durante o período de inscrições, quando é utilizado por todos em simultâneo.

Estas três propriedades são frequentemente referidas pelas iniciais C, I e A.

**As três propriedades da informação**

| Propriedade | Significado | Exemplo no politécnico |
|---|---|---|
| Confidencialidade | apenas as pessoas autorizadas acedem | as notas de um estudante não ficam visíveis para outros estudantes |
| Integridade | a informação é exata e não foi alterada sem autorização | nenhuma nota lançada é alterada sem registo |
| Disponibilidade | a informação está acessível quando é necessária | o sistema de matrículas funciona no período de inscrições |

## Classificação

O valor da informação varia. Os dados de saúde de um estudante exigem um nível de confidencialidade muito superior ao da ementa da cantina. Um serviço que pode estar parado durante uma semana não exige a mesma disponibilidade que o correio eletrónico.

Classificar a informação consiste em definir, para cada tipo, o peso das três propriedades. Para as entidades públicas do Grupo A, a classificação é obrigatória: o Anexo IV do Regulamento exige um processo de classificação da informação.

**Diferentes níveis de valor**

- Os dados de saúde de um estudante exigem mais confidencialidade do que a ementa da cantina.
- Um serviço que pode estar parado durante uma semana não exige a mesma disponibilidade que o correio eletrónico.
- Classificar a informação consiste em definir, para cada tipo, o peso de C, I e A.
- Para as entidades públicas do Grupo A, o Anexo IV exige um processo de classificação da informação (O.PCF).

Entre os ativos, distinguem-se os ativos críticos: aqueles cuja falha impede a organização de cumprir a sua missão. O inventário dos ativos críticos é uma medida obrigatória para os dois grupos de entidades públicas relevantes.

O inventário é o ponto de partida de todo o trabalho, uma vez que não é possível proteger ativos desconhecidos. É, na generalidade dos casos, a primeira tarefa de um sistema de gestão da segurança da informação.

**Ativos críticos**

- Ativos críticos: aqueles cuja falha impede a organização de cumprir a sua missão.
- O respetivo inventário é uma medida para os Grupos A e B (O.IAC do Anexo IV).
- Sem inventário, não é possível gerir o risco: não se protegem ativos desconhecidos.

## Informação a solicitar

Para iniciar o inventário, solicite a cada responsável de serviço os processos que gere, a informação que utiliza e o peso da confidencialidade, da integridade e da disponibilidade para essa informação.

Solicite à equipa de informática as aplicações e a infraestrutura onde essa informação reside; ao encarregado de proteção de dados, a localização dos dados pessoais; e à direção, os serviços críticos para a missão.

**Responsáveis**

- Responsáveis de serviço: processos geridos, informação utilizada e peso de C, I e A.
- Equipa de informática: aplicações e infraestrutura onde a informação reside.
- Encarregado de proteção de dados: localização e categorias dos dados pessoais.
- Direção: serviços críticos para a missão.

Na plataforma, cada ativo de informação é registado com as três propriedades e o respetivo dono. Os processos e serviços são associados aos ativos que utilizam. O inventário técnico (servidores e redes) pode ser importado automaticamente. As páginas do módulo da plataforma descrevem estes ecrãs.

**Correspondência na plataforma**

- Ativos de informação, com C, I e A e o dono de cada um ({doc}`/platform/inventory/information-assets`).
- Processos e serviços, associados aos ativos que utilizam ({doc}`/platform/inventory/processes-and-services`).
- O inventário técnico (servidores e redes) é importado automaticamente ({doc}`/platform/inventory/import` e {doc}`/platform/inventory/view-the-estate`).
