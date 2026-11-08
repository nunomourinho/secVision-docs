# Gestão de riscos e a Matriz de Risco

Requisitos legais sobre o risco (medidas proporcionais, análise pelo menos anual e risco residual documentado) e utilização da Matriz de Risco do CNCS para determinar o nível de conformidade (Básico, Substancial ou Elevado) das entidades essenciais e importantes.

```{video} 207-gestao-de-riscos-e-matriz
```

A página {doc}`/fundamentals/risk` define o conceito de risco. Esta página descreve os requisitos legais sobre o risco, que envolvem dois instrumentos distintos e frequentemente confundidos: a análise de riscos realizada pela própria organização e a Matriz de Risco elaborada pelo CNCS para cada setor.

## Requisitos legais

O decreto-lei exige às entidades essenciais e importantes medidas técnicas, operacionais e organizativas adequadas ao risco e proporcionais à respetiva exposição, à dimensão e à gravidade potencial dos incidentes.

Exige também uma análise e gestão de riscos sobre todos os ativos que suportam as redes e os sistemas, complementar às medidas mínimas e não em sua substituição. Esta análise é documentada: preparação, execução e resultados.

**Requisitos do DL**

- Medidas técnicas, operacionais e organizativas adequadas ao risco (art. 26.º, n.º 1).
- Proporcionais à exposição, à dimensão, à probabilidade e à gravidade dos incidentes (art. 26.º, n.º 3).
- Uma análise e gestão de riscos sobre todos os ativos que suportam as redes e os sistemas, além das medidas mínimas (art. 29.º, n.º 1).
- Documentação da preparação, da execução e dos resultados dessa análise (art. 29.º, n.º 3).

O Regulamento define a periodicidade: pelo menos uma vez por ano e sempre que o CNCS notificar um risco, uma ameaça ou uma vulnerabilidade emergente, no prazo fixado.

Exige também a análise do risco residual, o risco que subsiste após a aplicação das medidas. A direção deve conhecer este risco e aceitá-lo ou determinar o seu tratamento.

**Periodicidade da análise de risco**

| Momento | Base legal |
|---|---|
| Pelo menos uma vez por ano | art. 31.º, n.º 2, do Regulamento |
| Quando o CNCS notifica um risco, ameaça ou vulnerabilidade emergente, no prazo fixado | art. 31.º, n.º 2, do Regulamento |
| Risco residual, após a adoção das medidas | art. 31.º, n.º 4, do Regulamento |

```{tip}
A análise considera, entre outros: o histórico de incidentes, os utilizadores afetados, a duração, a zona afetada e as dependências entre setores (art. 31.º, n.º 3, do Regulamento).
```

## A Matriz de Risco

A Matriz de Risco não é elaborada pela organização, mas pelo CNCS, para cada setor e subsetor, com base nos cenários de risco dominantes e no histórico de incidentes do setor.

O valor de risco do setor é ponderado pela dimensão da entidade e pela importância do setor, e resulta num de três níveis de conformidade: Básico, Substancial ou Elevado. Este nível determina as medidas mínimas do Anexo III aplicáveis à entidade essencial ou importante.

- Não corresponde à análise de riscos da organização: é elaborada pelo CNCS, por setor e subsetor (Anexo II do Regulamento).
- Combina cenários de risco e tipos de atores com o histórico de incidentes no setor.
- O valor de risco do setor é ponderado pela dimensão da entidade (grande, média ou pequena) e pela importância do setor.
- O resultado é um de três níveis de conformidade: Básico, Substancial ou Elevado (art. 28.º, n.º 3, do Regulamento).

A análise de riscos é realizada pela organização, sobre os seus ativos, e serve para definir medidas além das mínimas. A Matriz é elaborada pelo CNCS, sobre o setor, e determina as medidas mínimas aplicáveis.

**Comparação entre os dois instrumentos**

|  | Análise de riscos | Matriz de Risco |
|---|---|---|
| Responsável | a organização | o CNCS |
| Objeto | os ativos e serviços da organização | o setor e o subsetor |
| Resultado | riscos, tratamento, risco residual | o nível de conformidade |
| Finalidade | medidas além das mínimas | medidas mínimas aplicáveis |

## Entidades públicas relevantes

Nas entidades públicas relevantes, o regime é mais simples: não existe Matriz de Risco nem níveis, e as medidas são as do Anexo IV, para o Grupo A ou para o Grupo B. A análise anual de riscos prevista no Regulamento é um dever das entidades essenciais e importantes.

A análise de riscos é, ainda assim, recomendada: sem ela, não é possível definir prioridades de aplicação das medidas nem conhecer o risco por tratar. Para a certificação ISO 27001, a análise é obrigatória.

```{important}
**Entidades públicas relevantes**

- A Matriz de Risco e os níveis Básico, Substancial e Elevado aplicam-se às entidades essenciais e importantes.
- As entidades públicas relevantes adotam as medidas determinadas pelo CNCS para o seu grupo: o Anexo IV (art. 26.º, n.º 7, e art. 33.º).
- A análise anual do art. 31.º do Regulamento é um dever das entidades essenciais e importantes; numa entidade pública, constitui boa prática e é exigida pela ISO/IEC 27001.
```

Na plataforma, a análise de riscos dispõe do ciclo completo: critérios e apetite, registo de risco por ativo, plano de tratamento e risco residual, com aprovação pelo dono do risco.

A plataforma não calcula o nível de conformidade pela Matriz de Risco. O nível consta da notificação do CNCS e é registado tal como notificado.

**Correspondência na plataforma**

- Critérios e apetite, escalas e matriz da organização ({doc}`/platform/risk/risk-criteria`).
- Registo de risco por ativo de informação, com confidencialidade, integridade e disponibilidade ({doc}`/platform/risk/risk-register`).
- Plano de tratamento, risco residual e aprovação pelo dono do risco ({doc}`/platform/risk/risk-treatment`).
- A plataforma não calcula o nível de conformidade pela Matriz: regista o nível notificado pelo CNCS.
