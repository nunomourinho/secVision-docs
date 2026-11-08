# Classificação de alertas e ensaio de regras

Duas ferramentas para o ajuste da deteção: a classificação de um alerta com IA (falso positivo ou alerta real, com confiança, impacto e prioridade, guardada no histórico) e o Wazuh Rule Studio, que importa as regras do gestor e as ensaia num Wazuh próprio, em Docker, sem afetar o de produção.

```{video} 508-classificar-e-studio
```

Esta é a última página do módulo sobre o Wazuh. Descreve duas ferramentas para o ajuste da deteção: uma apoia a decisão sobre a classificação de um alerta como falso, e a outra permite ensaiar regras sem afetar o gestor.

## Classificação

**Wazuh** > **Threat Hunting** > **Events**

O processo começa no Wazuh, tal como nos falsos positivos: o alerta 5710 da base de dados 003 é aberto e o documento é copiado.

```{figure} /_static/capturas/wazuh-clf-studio/wazuh-1.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events** (1 de 2).
```

1. Introduza «rule.id : 5710 and agent.name : "base-de-dados-003"» no campo de pesquisa **Start typing to search and filter the wazuh-discover-search-**.

```{figure} /_static/capturas/wazuh-clf-studio/wazuh-2.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events** (2 de 2).
```

**Proteger** > **SOC** > **Falsos Positivos** > **Classificar**

No SecVision, após a colagem do alerta, o botão **Classificar FP ou Alerta Real** prepara um pedido distinto: em vez de uma regra, solicita uma avaliação fundamentada, com evidências extraídas do próprio alerta. O pedido é anonimizado, tal como os restantes.

O pedido indica o critério à IA: em caso de dúvida, classificar como alerta real, com confiança baixa, uma vez que a investigação de um falso alarme tem um custo inferior ao de um ataque ignorado.

```{figure} /_static/img/508-classificar-e-studio/02.jpg
:alt: Proteger > SOC > Falsos Positivos > Classificar

Ecrã **Proteger** > **SOC** > **Falsos Positivos** > **Classificar**.
```

O pedido é copiado, colado no assistente de inteligência artificial e enviado. O alerta é enviado com a máquina, a conta e o endereço substituídos por etiquetas.

```{figure} /_static/img/508-classificar-e-studio/03.jpg
:alt: O pedido de classificação, pseudonimizado, colado no assistente de IA

O pedido colado no assistente de IA. A janela foi criada para o vídeo; o pedido e a resposta são reais, processados por um modelo de IA.
```

A resposta segue os blocos pedidos. Neste exemplo, a classificação é «alerta real», com sessenta por cento de confiança: um único evento com uma conta inexistente pode resultar de um erro, mas também de uma tentativa de enumeração de contas. Em caso de dúvida, o alerta é investigado.

```{figure} /_static/img/508-classificar-e-studio/04.jpg
:alt: A resposta do assistente: alerta real, sessenta por cento de confiança

A resposta real do modelo: ALERTA_REAL, com 60 % de confiança, ainda com as etiquetas.
```

Após a colagem da resposta, a plataforma repõe automaticamente os valores reais e apresenta-a em quadro: classificação, confiança, evidências, impacto, prioridade (investigar) e sugestões, começando pela pesquisa de outros eventos do mesmo endereço.

A análise guardada fica no histórico, com a identificação do autor. Se for criada posteriormente uma regra de falso positivo, fica registada a respetiva fundamentação, frequentemente solicitada pelo auditor.

```{figure} /_static/img/508-classificar-e-studio/05.jpg
:alt: A análise lida em quadro, com os valores reais

A análise apresentada em quadro, com as etiquetas repostas.
```

## Rule Studio

**Wazuh** > **Server management** > **Rules**

No painel do Wazuh, nas regras personalizadas, é apresentado o ficheiro das deteções aplicadas na página anterior.

```{figure} /_static/img/508-classificar-e-studio/06.jpg
:alt: Wazuh > Server management > Rules

Ecrã **Wazuh** > **Server management** > **Rules**.
```

**Proteger** > **SOC** > **Wazuh Rule Studio**

No Wazuh Rule Studio, a opção **Importar do servidor Wazuh** lista os ficheiros de regras e de decoders do gestor. Os ficheiros das deteções são selecionados e importados. Na vista de desenho, cada decoder e cada regra correspondem a um nó, associado ao respetivo elemento de origem.

O Studio não altera o gestor: as regras importadas são guardadas numa base própria, onde podem ser alteradas livremente.

```{figure} /_static/img/508-classificar-e-studio/07.jpg
:alt: Proteger > SOC > Wazuh Rule Studio

Ecrã **Proteger** > **SOC** > **Wazuh Rule Studio**.
```

## Ensaio

**Wazuh Rule Studio** > **Testes**

Para o ensaio, o Studio inicia um Wazuh próprio, num contentor, na mesma versão do gestor.

```{figure} /_static/img/508-classificar-e-studio/08.jpg
:alt: Wazuh Rule Studio > Testes

Ecrã **Wazuh Rule Studio** > **Testes**.
```

O contentor é iniciado, o analisador carrega as regras de origem e o estado passa a pronto.

```{figure} /_static/img/508-classificar-e-studio/09.jpg
:alt: Wazuh Rule Studio > Testes

Ecrã **Wazuh Rule Studio** > **Testes**.
```

O botão **Sincronizar** envia as regras do Studio para o Wazuh de ensaio. A linha da aplicação, quando testada, dispara a regra de deteção, tal como no gestor.

Este ambiente permite testar uma alteração antes da sua aplicação: se a regra alterada deixar de disparar ou disparar em excesso, a situação é detetada no ensaio, e o gestor não é reiniciado devido a um erro.

```{figure} /_static/img/508-classificar-e-studio/10.jpg
:alt: Wazuh Rule Studio > Testes

Ecrã **Wazuh Rule Studio** > **Testes**.
```

## Resumo

A classificação regista a fundamentação de cada decisão, e o Studio permite ensaiar regras sem risco.

A IA apresenta uma avaliação, e não uma decisão. A decisão compete ao responsável pela segurança da organização.

**Funcionalidades e limitações**

- Prepara o pedido de classificação anonimizado, lê a resposta e guarda a análise com a identificação do autor.
- O Rule Studio importa as regras do gestor e ensaia-as num Wazuh próprio, sem afetar o de produção.
- Não decide: a IA apresenta uma avaliação, e a decisão compete ao responsável pela segurança.
