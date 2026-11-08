# Incidentes — notificação atempada

Critérios para classificar um incidente como significativo, as três notificações ao CNCS e os respetivos prazos (24 horas, 24 horas após o fim do impacto e 30 dias úteis), a regra das duas horas e o prazo distinto aplicável à proteção de dados.

```{video} 214-incidentes-notificar-a-tempo
```

Este é o dever com os prazos mais curtos de toda a lei. Perante um incidente significativo, a organização tem de o notificar ao CNCS em três momentos, cada um com o seu prazo. O dever aplica-se a todas as entidades: essenciais, importantes e públicas relevantes.

## Incidente significativo

Apenas os incidentes significativos são notificados. Um incidente é significativo quando causa, ou pode causar, perturbações graves dos serviços ou perdas financeiras à entidade, ou quando afeta terceiros com danos consideráveis.

Na avaliação, são ponderados o número de utilizadores afetados, o total de utilizadores do serviço, a duração, a gravidade e o impacto económico e social. O CNCS pode fixar limiares mais precisos por instrução técnica.

**Critérios de incidente significativo**

- Causa, ou pode causar, perturbações graves dos serviços ou perdas financeiras à entidade (art. 2.º).
- Ou afeta, ou pode afetar, terceiros, com danos consideráveis.
- São ponderados: utilizadores afetados, total de utilizadores, duração, gravidade e impacto económico e social (art. 40.º, n.º 3).
- O CNCS densifica os limiares por instrução técnica.

## Prazos

1. **Notificação inicial:** Até vinte e quatro horas após a conclusão de que existe, ou pode vir a existir, um incidente significativo. Quando necessário, é atualizada até às setenta e duas horas.
2. **Notificação do fim do impacto:** Até vinte e quatro horas após o fim do impacto.
3. **Relatório final:** Trinta dias úteis a contar da notificação do fim do impacto, e não do início do incidente.

Se o incidente for resolvido nas duas horas seguintes à deteção, basta a notificação do fim do impacto.

**As três notificações**

| Notificação | Prazo | Início da contagem | Base legal |
|---|---|---|---|
| Inicial | até 24 horas | conclusão de que existe, ou pode vir a existir, um incidente significativo | art. 42.º, n.º 1 |
| Atualização da inicial | até 72 horas | a mesma verificação, quando necessário | art. 42.º, n.º 3 |
| Fim do impacto significativo | até 24 horas | o fim do impacto | art. 43.º, n.º 1 |
| Relatório final | 30 dias úteis | a notificação do fim do impacto | art. 44.º, n.º 1 |

```{tip}
Incidente resolvido em duas horas após a deteção: basta a notificação do fim do impacto (art. 41.º, n.º 2).
```

A lei estabelece expressamente que a notificação não gera responsabilidade acrescida. Se o incidente ainda estiver em curso no termo do prazo do relatório final, o CNCS pode solicitar relatórios intercalares semanais.

Se a plataforma do CNCS estiver indisponível, ou se o próprio incidente impedir o acesso, a notificação é feita por correio eletrónico ou por telefone. Os alertas da plataforma não dispensam o controlo dos prazos, e a falta de notificação é tratada como infração grave.

**Disposições complementares**

- A notificação não gera responsabilidade acrescida (art. 40.º, n.º 2).
- Incidente em curso no termo do prazo do relatório final: relatório intercalar semanal, a pedido (art. 44.º, n.º 3).
- Sem acesso à plataforma do CNCS: correio eletrónico ou telefone, a título excecional (art. 20.º, n.º 4, do Regulamento).
- Os alertas automáticos da plataforma não dispensam o cumprimento dos prazos (art. 22.º, n.º 4, do Regulamento).
- A falta de notificação presume-se infração grave na determinação da coima (art. 66.º, n.º 3).

## Proteção de dados

A proteção de dados tem um prazo próprio. Se o incidente envolver dados pessoais, a violação é notificada à Comissão Nacional de Proteção de Dados no prazo de setenta e duas horas, nos termos do Regulamento Geral sobre a Proteção de Dados.

A notificação ao CNCS não substitui esta notificação, nem a participação ao Ministério Público ou à Polícia Judiciária em caso de crime. Um único ataque de ransomware pode iniciar os três prazos em simultâneo.

```{important}
**Prazo distinto para a proteção de dados**

- Uma violação de dados pessoais é notificada à CNPD em 72 horas (art. 33.º do RGPD).
- A notificação ao CNCS não substitui as restantes: CNPD, Ministério Público, Polícia Judiciária (art. 40.º, n.º 5).
- O mesmo incidente pode iniciar três prazos em simultâneo.
```

## Preparação

Estes procedimentos devem ser preparados antes de qualquer incidente. A direção define quem decide a classificação como significativo e quem assina. O ponto de contacto testa o acesso à plataforma do CNCS. A equipa de informática define o registo das horas de deteção e de fim do impacto, que determinam os prazos.

O encarregado de proteção de dados dispõe do procedimento para a CNPD, e o serviço jurídico define os casos de participação ao Ministério Público.

**Responsáveis**

| Responsável | Preparação prévia |
|---|---|
| Direção | decisão sobre a classificação como significativo e assinatura da notificação |
| Ponto de contacto | acesso à plataforma do CNCS testado e contacto alternativo |
| Equipa de informática | registo da hora de deteção e da hora de fim do impacto |
| Encarregado de proteção de dados | procedimento paralelo para a CNPD |
| Serviço jurídico | casos de participação ao Ministério Público |

Na plataforma, cada notificação é registada com o prazo calculado e o estado (dentro ou fora do prazo). As violações de dados pessoais têm o seu próprio prazo de setenta e duas horas.

A plataforma não submete notificações ao CNCS nem gere o ciclo de vida do incidente: regista as comunicações efetuadas e calcula os prazos.

**Correspondência na plataforma**

- Autoridades e notificações: cada notificação registada, com o prazo calculado e o estado, dentro ou fora do prazo ({doc}`/platform/organisation/authorities-and-notifications`).
- Proteção de dados: as violações e o prazo de 72 horas ({doc}`/platform/organisation/data-protection`).
- A plataforma não submete notificações ao CNCS nem gere o ciclo de vida de incidentes: regista as comunicações e calcula os prazos.
