# Informação, ativos e as três propriedades

O que é um ativo, porque é que a informação é o ativo principal, e o que significa protegê-la: confidencialidade, integridade e disponibilidade — com exemplos de uma organização pública.

```{video} 102-informacao-e-ativos
```

Antes de falar de ameaças ou de medidas, temos de responder a uma pergunta simples: o que estamos a proteger? A resposta curta é: a informação. Nesta página vemos o que isso quer dizer, e as três propriedades que a segurança da informação procura garantir.

## Ativos

Um ativo é tudo o que tem valor para a organização e que, por isso, precisa de proteção. Na segurança da informação, o ativo principal é a própria informação: os processos dos estudantes, os salários, os contratos, os dados de investigação.

Os outros ativos — as aplicações, os servidores, a rede, os computadores, as instalações e as pessoas — existem para tratar essa informação. E cada ativo tem um dono: uma pessoa que responde por ele, e que decide quem lhe pode aceder. O dono não é a informática; é o responsável do serviço que usa o ativo.

**O que é um ativo**

- Um ativo é tudo o que tem valor para a organização e que precisa de proteção.
- O ativo principal é a informação: processos de estudantes, salários, contratos, dados de investigação.
- Os outros ativos existem para tratar essa informação: aplicações, servidores, redes, equipamentos, pessoas, instalações.
- Cada ativo tem um dono: a pessoa que responde por ele e decide quem lhe pode aceder.

É útil pensar em camadas. No topo, o processo — no politécnico, por exemplo, as matrículas e inscrições. O processo usa informação: os dados pessoais e académicos dos estudantes. A informação vive numa aplicação — o sistema de gestão académica. E a aplicação corre numa infraestrutura: um servidor, uma base de dados, a rede, as cópias de segurança.

Esta cadeia é importante: se o servidor falha, a aplicação para, a informação deixa de estar acessível, e as matrículas não se fazem. É assim que um problema técnico se torna um problema da organização.

**Do processo à máquina**

Processo ou serviço
: «Matrículas e inscrições» — o que a organização faz para os seus utilizadores

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

## C, I, A

Proteger a informação quer dizer garantir três propriedades. A confidencialidade: só quem tem autorização acede. A integridade: a informação é exata, e não foi alterada sem autorização. E a disponibilidade: está acessível quando é precisa.

No politécnico: confidencialidade é as notas de um estudante não ficarem visíveis a outros. Integridade é ninguém alterar uma nota já lançada sem deixar registo. Disponibilidade é o sistema de matrículas funcionar no período de inscrições — quando toda a gente precisa dele ao mesmo tempo.

Vai ouvir muitas vezes as iniciais: C, I e A. São estas três.

**As três propriedades da informação**

| Propriedade | Quer dizer | Exemplo no politécnico |
|---|---|---|
| Confidencialidade | só quem tem autorização acede | as notas de um estudante não ficam visíveis a outros estudantes |
| Integridade | a informação é exata e não foi alterada sem autorização | ninguém altera uma nota depois de lançada sem deixar registo |
| Disponibilidade | está acessível quando é precisa | o sistema de matrículas funciona no período de inscrições |

## Classificar

Nem toda a informação vale o mesmo. Os dados de saúde de um estudante exigem muito mais confidencialidade do que a ementa da cantina. E um serviço que pode parar uma semana não pede a mesma disponibilidade que o correio eletrónico.

Classificar a informação é decidir, para cada tipo, quanto pesam as três propriedades. Para as entidades públicas do Grupo A, isto não é opcional: o Anexo IV do Regulamento pede um processo de classificação da informação.

**Nem toda a informação vale o mesmo**

- Os dados de saúde de um estudante exigem mais confidencialidade do que a ementa da cantina.
- Um serviço que pode parar uma semana não pede a mesma disponibilidade que o correio eletrónico.
- Classificar a informação é decidir, para cada tipo, quanto pesam C, I e A.
- Para as públicas do Grupo A, o Anexo IV pede um processo de classificação da informação (O.PCF).

Entre todos os ativos, há os críticos: aqueles cuja falha impede a organização de cumprir a sua missão. Inventariar os ativos críticos é uma medida obrigatória para os dois grupos de entidades públicas relevantes.

E é o ponto de partida de tudo o resto: não se protege o que não se sabe que existe. O inventário é, quase sempre, o primeiro trabalho de um sistema de gestão da segurança da informação.

**Os ativos críticos**

- Ativos críticos: aqueles cuja falha impede a organização de cumprir a sua missão.
- Inventariá-los é uma medida para os Grupos A e B (O.IAC do Anexo IV).
- Sem inventário não há gestão de risco: não se protege o que não se sabe que existe.

## Na sua organização

Para começar o inventário, peça a cada responsável de serviço os processos que gere, a informação que usa, e quanto pesam, para essa informação, a confidencialidade, a integridade e a disponibilidade.

À informática, as aplicações e a infraestrutura onde essa informação vive. Ao encarregado de proteção de dados, onde há dados pessoais. E à direção, quais são os serviços críticos para a missão.

**O que pedir a quem**

- A cada responsável de serviço: os processos que gere, a informação que usa, e quanto pesam C, I e A.
- À informática: as aplicações e a infraestrutura onde essa informação vive.
- Ao encarregado de proteção de dados: onde há dados pessoais, e de que categorias.
- À direção: quais são os serviços críticos para a missão.

Na plataforma, cada ativo de informação regista-se com as três propriedades e o seu dono. Os processos e serviços ligam-se aos ativos que usam. E o inventário técnico — servidores e redes — pode ser importado automaticamente. Vamos ver tudo isto ecrã a ecrã.

**Onde isto entra na plataforma**

- Ativos de informação, com C, I e A e o dono de cada um ({doc}`/platform/inventory/information-assets`).
- Processos e serviços, ligados aos ativos que usam ({doc}`/platform/inventory/processes-and-services`).
- O inventário técnico — servidores, redes — importa-se automaticamente ({doc}`/platform/inventory/import` e {doc}`/platform/inventory/view-the-estate`).
