# Gestão de riscos e a Matriz de Risco

O que a lei pede sobre risco: medidas proporcionais, análise pelo menos anual e risco residual documentado; e como a Matriz de Risco do CNCS decide o nível de conformidade — Básico, Substancial ou Elevado — das entidades essenciais e importantes.

```{video} 207-gestao-de-riscos-e-matriz
```

em {doc}`/fundamentals/risk` vimos o que é o risco. Agora vemos o que a lei pede sobre ele. Há duas peças diferentes, que se confundem: a análise de riscos que a própria organização faz, e a Matriz de Risco, que o CNCS faz para cada setor.

## A lei

O decreto-lei pede às entidades essenciais e importantes medidas técnicas, operacionais e organizativas adequadas ao risco, e proporcionais à sua exposição, à dimensão e à gravidade possível dos incidentes.

E pede uma análise e gestão de riscos sobre todos os ativos que suportam as redes e os sistemas — por cima das medidas mínimas, e não em vez delas. Essa análise documenta-se: como se preparou, como se fez, e o que deu.

**O que o DL pede**

- Medidas técnicas, operacionais e organizativas adequadas ao risco (art. 26.º, n.º 1).
- Proporcionais à exposição, à dimensão, à probabilidade e à gravidade dos incidentes (art. 26.º, n.º 3).
- Uma análise e gestão de riscos sobre todos os ativos que suportam as redes e os sistemas, além das medidas mínimas (art. 29.º, n.º 1).
- Documentar a preparação, a execução e os resultados dessa análise (art. 29.º, n.º 3).

O Regulamento diz quando: pelo menos uma vez por ano, e sempre que o CNCS notificar um risco, uma ameaça ou uma vulnerabilidade emergente, no prazo que fixar.

E pede também a análise do risco residual — o risco que fica depois de aplicadas as medidas. É esse que a direção tem de conhecer e aceitar, ou mandar tratar.

**Quando se analisa o risco**

| Quando | Base legal |
|---|---|
| Pelo menos uma vez por ano | art. 31.º, n.º 2, do Regulamento |
| Quando o CNCS notifica um risco, ameaça ou vulnerabilidade emergente, no prazo que fixar | art. 31.º, n.º 2, do Regulamento |
| E o risco residual, depois de adotadas as medidas | art. 31.º, n.º 4, do Regulamento |

```{tip}
A análise considera, entre outros: o histórico de incidentes, os utilizadores afetados, a duração, a zona afetada e as dependências entre setores (art. 31.º, n.º 3, do Regulamento).
```

## A Matriz de Risco

A Matriz de Risco é outra coisa. Não é feita pela organização: é feita pelo CNCS, para cada setor e subsetor, a partir dos cenários de risco dominantes e do histórico de incidentes nesse setor.

O valor de risco do setor é ponderado pela dimensão da entidade e pela importância do setor. E dá um de três níveis de conformidade: Básico, Substancial ou Elevado. É o nível que decide que medidas mínimas do Anexo III a entidade essencial ou importante tem de cumprir.

- Não é a análise de riscos da organização: é feita pelo CNCS, por setor e subsetor (Anexo II do Regulamento).
- Combina cenários de risco e tipos de atores, com o histórico de incidentes no setor.
- O valor de risco do setor é ponderado pela dimensão da entidade — grande, média ou pequena — e pela importância do setor.
- O resultado é um de três níveis de conformidade: Básico, Substancial ou Elevado (art. 28.º, n.º 3, do Regulamento).

Lado a lado: a análise de riscos faz-se na organização, sobre os seus ativos, e serve para decidir medidas além das mínimas. A Matriz faz-se no CNCS, sobre o setor, e serve para decidir que medidas mínimas se aplicam.

**Duas coisas diferentes**

|  | Análise de riscos | Matriz de Risco |
|---|---|---|
| Quem faz | a organização | o CNCS |
| Sobre quê | os ativos e serviços da organização | o setor e o subsetor |
| Resultado | riscos, tratamento, risco residual | o nível de conformidade |
| Para quê | medidas além das mínimas | que medidas mínimas se aplicam |

## Públicas relevantes

Nas entidades públicas relevantes, a lógica é mais simples. Não há Matriz de Risco nem níveis: as medidas são as do Anexo IV, para o Grupo A ou para o Grupo B. E a análise anual de riscos do Regulamento é um dever das essenciais e importantes.

Mas não a dispense. Sem análise de riscos, não se sabe onde aplicar primeiro as medidas, nem que risco fica por tratar. E se a organização quiser certificar-se pela ISO 27001, a análise é obrigatória.

```{important}
**E as entidades públicas relevantes?**

- A Matriz de Risco e os níveis Básico, Substancial e Elevado são para as essenciais e importantes.
- As públicas relevantes adotam as medidas que o CNCS determina para o seu grupo — o Anexo IV (art. 26.º, n.º 7, e art. 33.º).
- A análise anual do art. 31.º do Regulamento é dever das essenciais e importantes — numa pública, é boa prática, e a ISO/IEC 27001 exige-a.
```

Na plataforma, a análise de riscos tem o seu ciclo completo: critérios e apetite, registo de risco por ativo, plano de tratamento e risco residual, com a aprovação do dono do risco.

O que a plataforma não faz é calcular o nível de conformidade pela Matriz de Risco. O nível vem na notificação do CNCS, e regista-se tal como foi notificado.

**Onde isto entra na plataforma**

- Critérios e apetite, escalas e matriz da organização ({doc}`/platform/risk/risk-criteria`).
- Registo de risco por ativo de informação, com confidencialidade, integridade e disponibilidade ({doc}`/platform/risk/risk-register`).
- Plano de tratamento, risco residual e aprovação pelo dono do risco ({doc}`/platform/risk/risk-treatment`).
- A plataforma não calcula o nível de conformidade pela Matriz: regista o que o CNCS notificou.
