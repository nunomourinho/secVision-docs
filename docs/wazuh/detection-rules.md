# Regras de deteção no Wazuh

O processo inverso de um falso positivo: um evento desconhecido do Wazuh que deveria gerar alerta. Definição de decoders e regras; a linha real de uma aplicação do ambiente de testes, o pedido à IA, a resposta separada em quatro blocos e a aplicação ao gestor; e, no Wazuh, a mesma linha antes (sem decoder) e depois (regra e alerta), com os novos alertas recebidos.

```{video} 507-regras-de-detecao
```

A página anterior descreve a supressão de um alerta. Esta página descreve o processo inverso: uma aplicação regista tentativas de acesso falhadas que o Wazuh não reconhece, e é configurada a sua deteção.

## Conceito

Cada linha recebida pelo Wazuh passa por três fases. O pré-decoder separa a data, a máquina e o programa. O decoder reconhece o programa e extrai os campos relevantes. As regras determinam se a linha constitui um alerta e com que nível.

Para uma aplicação desconhecida do Wazuh, faltam o decoder e a regra. São estes os elementos a criar: um decoder que reconhece o programa e extrai os campos, e uma regra que dispara com base nesses campos.

**Do registo ao alerta**

Pré-decoder
: separa a linha: data, máquina, programa

Decoder
: reconhece o programa e extrai os campos: ação, conta, origem

Regra
: determina, com base nos campos, se é alerta e com que nível

Alerta
: é enviado para o Indexer e para o painel da equipa de análise

```{figure} /_static/img/507-regras-de-detecao/01.jpg
:alt: Do registo ao alerta

Do registo ao alerta.
```

## No Wazuh, antes

**Wazuh** > **Ruleset Test**

O **Ruleset Test**, no painel do Wazuh, apresenta o processamento de uma linha pelo gestor. Neste exemplo, a linha é real: a aplicação secvision-app de uma máquina do ambiente de testes regista um acesso falhado, com a conta e o endereço.

O resultado indica que o pré-decoder separou a máquina e o programa, mas nenhum decoder reconheceu a linha. Para o Wazuh, esta linha não tem significado e nunca gerará alerta.

```{figure} /_static/capturas/wazuh-deteccao/antes-1.jpg
:alt: Wazuh > Ruleset Test

Ecrã **Wazuh** > **Ruleset Test**.
```

1. Introduza a linha de registo no campo **Type one log per line...**.
2. Clique em **Test**.

## No SecVision

**Proteger** > **SOC** > **Regras de Deteção**

No ecrã **Regras de Deteção** do SecVision, a linha é colada e o botão da IA prepara o pedido, com as instruções de formato exigidas pelo Wazuh, anonimizado tal como nos falsos positivos. Em seguida, o pedido é copiado.

```{figure} /_static/img/507-regras-de-detecao/03.jpg
:alt: Proteger > SOC > Regras de Deteção

Ecrã **Proteger** > **SOC** > **Regras de Deteção**.
```

### No assistente de IA

No assistente de inteligência artificial, o pedido é colado e enviado. A linha de registo é enviada com a máquina, a conta e o endereço substituídos por etiquetas.

```{figure} /_static/img/507-regras-de-detecao/04.jpg
:alt: O pedido pseudonimizado, colado no assistente de IA

O pedido colado no assistente de IA. A janela foi criada para o vídeo; o pedido e a resposta são reais, processados por um modelo de IA.
```

A resposta segue o formato exigido no pedido, com quatro blocos assinalados: um decoder que reconhece o programa, um decoder que extrai o evento, a conta e a origem, uma regra que agrupa os eventos da aplicação e a regra de deteção, que dispara no acesso falhado. A resposta completa é copiada.

```{figure} /_static/img/507-regras-de-detecao/05.jpg
:alt: A resposta do assistente, em quatro blocos e ainda com as etiquetas

A resposta real do modelo, em quatro blocos e ainda com as etiquetas.
```

### Importação da resposta

A resposta é colada na íntegra, ainda com as etiquetas, e o ecrã apresenta um aviso. O botão **Separar componentes** efetua primeiro a substituição inversa, com o registo do pedido, e só depois coloca cada bloco na respetiva caixa, já com os valores reais.

Sem esta substituição, o decoder seria enviado para o Wazuh com etiquetas e não reconheceria nenhuma linha. Por este motivo, se o registo do pedido não estiver disponível (por exemplo, se a página tiver sido recarregada após a geração do pedido) ou se a resposta contiver etiquetas inexistentes no pedido, o ecrã identifica-as e não permite a validação nem a aplicação. Os números das regras ficam por preencher, uma vez que são atribuídos pela plataforma.

```{figure} /_static/img/507-regras-de-detecao/06.jpg
:alt: A resposta separada nos quatro blocos, com os valores reais

A resposta separada nos quatro blocos, com as etiquetas repostas.
```

## Aplicação

**Regras de Deteção** > **Aplicar ao Wazuh**

Após a validação dos quatro blocos, os componentes são aplicados ao gestor.

```{figure} /_static/img/507-regras-de-detecao/07.jpg
:alt: Regras de Deteção > Aplicar ao Wazuh

Ecrã **Regras de Deteção** > **Aplicar ao Wazuh**.
```

O procedimento é o mesmo dos falsos positivos, aplicado a dois ficheiros (decoders e regras): cópia de segurança de ambos, escrita, validação pelo gestor, reinício e confirmação.

Se o Wazuh recusar algum componente, a plataforma repõe os dois ficheiros e apresenta o motivo indicado pelo gestor, na íntegra.

```{figure} /_static/img/507-regras-de-detecao/08.jpg
:alt: Regras de Deteção > Aplicar ao Wazuh

Ecrã **Regras de Deteção** > **Aplicar ao Wazuh**.
```

Após a aplicação, o logtest confirma que a linha dispara a nova regra.

```{figure} /_static/img/507-regras-de-detecao/09.jpg
:alt: Regras de Deteção > Aplicar ao Wazuh

Ecrã **Regras de Deteção** > **Aplicar ao Wazuh**.
```

## No Wazuh, depois

**Wazuh** > **Ruleset Test**

No Ruleset Test do Wazuh, a mesma linha é agora reconhecida pelo decoder, que extrai a conta e o endereço, e a nova regra dispara com nível oito, gerando um alerta.

```{figure} /_static/img/507-regras-de-detecao/10.jpg
:alt: Wazuh > Ruleset Test

Ecrã **Wazuh** > **Ruleset Test**.
```

**Wazuh** > **Threat Hunting** > **Events**

Cinco minutos depois, os eventos do Wazuh apresentam os alertas da nova regra, de todas as máquinas onde a aplicação é executada. A linha anteriormente sem significado passa a constituir um alerta, com a conta e a origem.

Tal como qualquer alerta, é contabilizado nos indicadores e pode ser classificado ou suprimido através de uma regra de falso positivo, caso se comprove inofensivo.

```{figure} /_static/img/507-regras-de-detecao/11.jpg
:alt: Wazuh > Threat Hunting > Events

Ecrã **Wazuh** > **Threat Hunting** > **Events**.
```

## Resumo

A plataforma assegura o formato, a aplicação segura e a confirmação.

A seleção dos eventos relevantes para a organização compete às pessoas que conhecem os sistemas, e é esta seleção que determina a qualidade de uma regra de deteção.

**Funcionalidades e limitações**

- Prepara o pedido à IA com o formato do Wazuh, separa a resposta e valida cada bloco.
- Aplica decoders e regras com cópia de segurança, validação, reinício, logtest e reversão.
- Não determina os eventos relevantes para a organização: esta decisão compete a quem conhece os sistemas.
