# Processos e serviços

As atividades da organização: cada processo com dono, tipo e criticidade, os serviços críticos de que dependem partes externas e as dependências de ativos, sistemas e fornecedores.

```{video} 317-processos-e-servicos
```

A fase do inventário termina com os processos e serviços da organização. Este registo relaciona a missão com a tecnologia, permitindo identificar o serviço afetado pela interrupção de cada sistema.

## Acesso

**Governar** > **Organização** > **Processos e serviços**

```{figure} /_static/capturas/processos/menu.jpg
:alt: Menu lateral: Governar > Organização > Processos e serviços

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

No Grupo A, o Anexo IV exige a identificação das funções ou atividades críticas e dos sistemas de que dependem. O QNRCS exige igualmente a identificação dos serviços críticos de que dependem partes externas e das respetivas dependências.

A continuidade do negócio exige, para cada processo crítico, o tempo máximo de interrupção e a perda de dados admissível. Estes valores resultam de uma análise de impacto no negócio e não devem ser estimados sem essa análise.

**Finalidade**

- No Grupo A, o Anexo IV exige as funções ou atividades críticas e as respetivas dependências das TIC (O.ID).
- O QNRCS exige os serviços críticos de que dependem partes externas (GR.CO-4) e as dependências (GR.CO-6).
- A continuidade exige, por processo, o tempo máximo de interrupção (RTO e RPO), determinado numa análise de impacto.

## Informação a solicitar

Solicite à direção e aos responsáveis dos serviços a lista de processos, os respetivos donos e os processos críticos para entidades externas. Solicite à equipa de informática e ao serviço de compras os sistemas e os fornecedores de que cada processo depende.

**Responsáveis**

| Informação | Responsável |
|---|---|
| Processos da organização e respetivos donos | direção; responsáveis dos serviços |
| Serviços críticos para entidades externas | direção |
| Sistemas e fornecedores de que cada processo depende | equipa de informática; serviço de compras |
| Tempo máximo de interrupção de cada processo | dono do processo, numa análise de impacto |

## Configuração do ecrã

```{figure} /_static/capturas/processos/abrir-1.jpg
:alt: Governar > Organização > Processos e serviços

Ecrã **Governar** > **Organização** > **Processos e serviços**.
```

No topo, são apresentados quatro indicadores de lacunas, que filtram a lista quando selecionados (o quarto identifica os processos sem risco apreciado). No ecrã, encontra os seguintes elementos:

1. **Serviços críticos.**
2. **Sem dono.**
3. **Críticos sem tempo de recuperação.**

## Ficha do processo

A ficha de um processo (neste exemplo, Inscrições e matrículas) indica o dono, o tipo e a criticidade, e assinala se se trata de um serviço crítico de que dependem partes externas (neste caso, os estudantes).

Seguem-se três áreas de dependências: ativos de informação, sistemas do catálogo e fornecedores, com funções de pesquisa, adição e remoção. O tempo máximo de interrupção e os objetivos de recuperação mantêm-se vazios até serem determinados numa análise de impacto; valores estimados sem análise são menos fiáveis do que a sua ausência.

```{figure} /_static/capturas/processos/processo-1.jpg
:alt: Um processo — e as suas dependências

Um processo e as respetivas dependências (1 de 3).
```

1. Selecione o processo (neste exemplo, **P-002**).

```{figure} /_static/capturas/processos/processo-2.jpg
:alt: Um processo — e as suas dependências

Um processo e as respetivas dependências (2 de 3).
```

```{figure} /_static/capturas/processos/processo-3.jpg
:alt: Um processo — e as suas dependências

Um processo e as respetivas dependências (3 de 3).
```

## Resumo

O relatório de criticidade reúne a informação numa página destinada à direção. A plataforma pode também propor processos com inteligência artificial, a partir dos dados já registados, sempre sujeitos a revisão.

A plataforma não realiza a análise de impacto no negócio: regista os respetivos resultados, quando existam.

**Funcionalidades e limitações**

- O relatório de criticidade reúne os processos, a criticidade, as dependências e o risco.
- A opção **Propor com IA** sugere processos a partir dos dados registados, sempre sujeitos a revisão.
- Não realiza a análise de impacto no negócio: regista os respetivos resultados.
