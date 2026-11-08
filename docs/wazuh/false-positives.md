# Falsos positivos no Wazuh

Definição de falso positivo e motivo da reclassificação em alternativa à eliminação; um alerta real do Wazuh de testes, o pedido anonimizado à IA e a resposta real com as etiquetas repostas, a regra-filha, a validação e a aplicação ao gestor com cópia de segurança, reinício e confirmação pelo logtest; e o histórico das regras.

```{video} 506-falsos-positivos
```

Um centro de operações que recebe mil alertas por dia, dos quais novecentos são recorrentes e inofensivos, deixa de analisar os alertas com atenção. Esta página descreve a supressão desse ruído no Wazuh, sem ocultar os alertas relevantes.

## Conceito

Um falso positivo é um alerta correto sobre um evento inofensivo. A regra funcionou como previsto (por exemplo, detetou uma tentativa de acesso com um utilizador inexistente), mas o contexto invalida o alerta: trata-se do scanner interno, que testa contas diariamente.

A regra original não é eliminada, uma vez que deteta ataques reais. É criada uma regra-filha, que herda da regra original e se aplica apenas a esse caso, com nível baixo. O evento mantém-se no arquivo, para efeitos de auditoria, mas deixa de gerar alerta. A regra deve ser tão restrita quanto possível: um endereço, uma conta ou uma máquina, e nunca a regra completa.

**Definição de falso positivo**

- Um alerta correto sobre um evento inofensivo: a regra funcionou como previsto, mas o contexto invalida o alerta.
- A regra original não é eliminada: é criada uma regra-filha, apenas para esse caso.
- A regra-filha herda da regra original (if_sid) e reduz o nível: o evento mantém-se no arquivo, mas deixa de gerar alerta.
- A regra deve ser tão restrita quanto possível: um endereço, um utilizador, uma máquina, e nunca a regra completa.

## Informação a solicitar

Antes de abrir o ecrã, são necessários três elementos: o alerta e a fundamentação da sua classificação como falso, fornecidos pela equipa de análise; a confirmação da legitimidade da origem, pelo responsável do sistema; e a aprovação do responsável de cibersegurança, uma vez que uma regra de falso positivo constitui uma decisão de supressão com responsável identificado.

A aplicação no gestor só pode ser efetuada por um administrador do SecVision, uma vez que implica o reinício do Wazuh.

**Responsáveis**

| Informação | Responsável |
|---|---|
| Alerta, em JSON, e fundamentação da classificação como falso | equipa de análise de alertas |
| Confirmação da legitimidade da origem (scanner, serviço) | responsável do sistema |
| Aprovação da alteração das regras do gestor | responsável de cibersegurança |
| Aplicação no gestor | administrador do SecVision |

## No Wazuh

**Wazuh** > **Threat Hunting** > **Events**

O processo começa no painel do Wazuh utilizado pela equipa de análise. Em **Threat Hunting**, nos eventos, é pesquisada a regra 5710 numa máquina do ambiente de testes, a base de dados 003: uma tentativa de acesso com uma conta inexistente, a cada dois minutos, sempre a partir do mesmo endereço.

No separador **JSON** do alerta encontra-se o documento completo, tal como guardado pelo Wazuh. O botão de cópia coloca-o na área de transferência, para utilização no SecVision.

```{figure} /_static/capturas/wazuh-fp/wazuh-1.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events** (1 de 3).
```

1. Introduza «rule.id : 5710 and agent.name : "base-de-dados-003"» no campo de pesquisa **Start typing to search and filter the wazuh-discover-search-**.

```{figure} /_static/capturas/wazuh-fp/wazuh-2.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events** (2 de 3).
```

```{figure} /_static/capturas/wazuh-fp/wazuh-3.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events** (3 de 3).
```

1. **Periodicidade:** A cada dois minutos, sempre a partir da mesma origem.

## Alerta

**Proteger** > **SOC** > **Falsos Positivos**

No ecrã **Falsos Positivos** do SecVision, o alerta é colado na primeira caixa, sem alterações.

O ecrã lê o alerta e apresenta os elementos essenciais: a regra que disparou (5710), o nível, a máquina e a origem, bem como o número de disparos da regra registados no arquivo do Wazuh. Um número elevado, sempre a partir da mesma origem, é o primeiro indício de um falso positivo.

```{figure} /_static/img/506-falsos-positivos/02.jpg
:alt: Proteger > SOC > Falsos Positivos

Ecrã **Proteger** > **SOC** > **Falsos Positivos**.
```

## Pedido à IA

**Falsos Positivos** > **Gerar prompt para IA**

A redação da regra pode ser pedida a um serviço de IA. O botão prepara o pedido com o alerta, que é copiado para o serviço de IA da organização.

O pedido é anonimizado: os endereços e os nomes das máquinas e das contas são substituídos por etiquetas antes do envio e repostos na resposta. O botão apresenta as substituições efetuadas.

```{figure} /_static/img/506-falsos-positivos/03.jpg
:alt: Falsos Positivos > Gerar prompt para IA

Ecrã **Falsos Positivos** > **Gerar prompt para IA**.
```

### No assistente de IA

Fora da plataforma, o pedido é colado no assistente de inteligência artificial e enviado. O endereço de origem é enviado como `[IP_1]`, a máquina como `[SISTEMA_1]` e a conta como `[UTILIZADOR_1]`; não é enviada qualquer outra informação.

```{figure} /_static/img/506-falsos-positivos/04.jpg
:alt: O pedido pseudonimizado, colado no assistente de IA

O pedido colado no assistente de IA. A janela foi criada para o vídeo; o pedido é o copiado pela plataforma e foi processado por um modelo de IA real.
```

A resposta contém uma regra XML, filha da regra que disparou, restrita àquele sistema, àquela conta e àquela origem, com as mesmas etiquetas: o modelo não teve acesso ao endereço real. A resposta é então copiada.

```{figure} /_static/img/506-falsos-positivos/05.jpg
:alt: A resposta do assistente, ainda com as etiquetas

A resposta real do modelo, ainda com as etiquetas.
```

## Regra

Na plataforma, a resposta é colada na segunda caixa, ainda com as etiquetas. O botão de validação da sintaxe efetua primeiro a substituição inversa: com o registo do pedido, cada etiqueta é substituída pelo valor real, e o ecrã indica o número de substituições. Em seguida, o XML é verificado.

Esta substituição é indispensável: uma regra com a etiqueta `[IP_1]` em vez do endereço não corresponderia a nenhum tráfego. O número e o nível indicados na regra são irrelevantes, uma vez que são atribuídos pela plataforma na aplicação.

```{figure} /_static/img/506-falsos-positivos/06.jpg
:alt: A resposta colada, com as etiquetas repostas e a sintaxe válida

A resposta colada: «10 etiqueta(s) reposta(s) com os valores reais», e a sintaxe válida.
```

## Aplicação

**Falsos Positivos** > **Aplicar ao Wazuh**

O botão **Testar permissões** confirma, antes de qualquer alteração, que as credenciais permitem ler e escrever regras e reiniciar o gestor.

```{figure} /_static/img/506-falsos-positivos/07.jpg
:alt: Falsos Positivos > Aplicar ao Wazuh

Ecrã **Falsos Positivos** > **Aplicar ao Wazuh**.
```

O botão **Aplicar** executa as seguintes operações, por ordem, apresentando cada passo no ecrã: cópia de segurança do ficheiro de regras, escrita da regra, validação da configuração pelo gestor, reinício e confirmação da reposição dos serviços.

Se o gestor recusar a regra ou não for reposto após o reinício, a plataforma repõe o ficheiro original e indica o motivo. O gestor nunca fica com uma regra parcialmente aplicada.

```{figure} /_static/img/506-falsos-positivos/08.jpg
:alt: Falsos Positivos > Aplicar ao Wazuh

Ecrã **Falsos Positivos** > **Aplicar ao Wazuh**.
```

O passo final é o logtest: o gestor recebe a linha do alerta original e indica a regra que passa a disparar. A resposta identifica a nova regra, com nível baixo, o que confirma que o falso positivo deixou de gerar alerta.

```{figure} /_static/img/506-falsos-positivos/09.jpg
:alt: Falsos Positivos > Aplicar ao Wazuh

Ecrã **Falsos Positivos** > **Aplicar ao Wazuh**.
```

## Regra no Wazuh

**Wazuh** > **Server management** > **Rules**

Nas regras do gestor, com o filtro das regras personalizadas, é apresentado o ficheiro gerido pelo SecVision, com a nova regra, o número atribuído e o nível um.

O SecVision escreve exclusivamente no seu próprio ficheiro. As regras de origem do Wazuh e as regras locais da equipa não são alteradas.

```{figure} /_static/img/506-falsos-positivos/10.jpg
:alt: Wazuh > Server management > Rules

Ecrã **Wazuh** > **Server management** > **Rules**.
```

## Histórico

**Falsos Positivos** > **Histórico**

O histórico regista cada regra: autor, data de aplicação, número atribuído e estado. A partir deste ecrã, a regra pode ser editada e aplicada novamente, ou removida do gestor.

A contagem de disparos de cada regra aplicada permite verificar a sua eficácia. Uma regra de falso positivo que nunca dispara é desnecessária; uma regra que dispara com demasiada frequência pode estar a ocultar um ataque.

```{figure} /_static/img/506-falsos-positivos/11.jpg
:alt: Falsos Positivos > Histórico

Ecrã **Falsos Positivos** > **Histórico**.
```

## Verificação no Wazuh

**Wazuh** > **Threat Hunting** > **Events**

Cinco minutos depois, a mesma pesquisa no Wazuh confirma que a máquina continua a tentar o acesso a cada dois minutos, mas o último alerta é anterior à regra.

Os eventos não foram perdidos: estão no arquivo, associados à nova regra, mas deixaram de gerar alertas.

```{figure} /_static/img/506-falsos-positivos/12.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events**.
```

## Resumo

A plataforma executa as operações sensíveis: pedido anonimizado, validação, aplicação com cópia de segurança e reversão, e confirmação pelo logtest.

A plataforma não decide que um alerta é falso. Essa decisão compete à equipa de análise, com aprovação do responsável de cibersegurança, e fica registada no histórico.

**Funcionalidades e limitações**

- Lê o alerta, prepara o pedido anonimizado à IA, valida, aplica com cópia de segurança e reverte em caso de falha.
- Confirma pelo logtest que a nova regra é a que dispara.
- Não decide se um alerta é falso: a decisão compete à equipa de análise, com aprovação do responsável de cibersegurança.
