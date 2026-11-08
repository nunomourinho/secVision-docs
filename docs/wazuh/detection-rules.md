# Regras de deteção no Wazuh

O contrário de um falso positivo: um evento que o Wazuh não conhece e que devia ser alerta. O que são decoders e regras; a linha real de uma aplicação do ambiente de testes, o pedido à IA, a resposta separada em quatro blocos, a aplicação ao gestor; e, no Wazuh, a mesma linha antes (nenhum decoder) e depois (regra e alerta), e os alertas novos a chegar.

```{video} 507-regras-de-detecao
```

No página anterior calámos um alerta. Neste fazemos o contrário: uma aplicação regista tentativas de entrada falhadas, e o Wazuh não as conhece. Vamos ensiná-lo a vê-las.

## O conceito

Cada linha que chega ao Wazuh passa por três fases. O pré-decoder separa a data, a máquina e o programa. O decoder reconhece o programa e tira os campos que importam. E as regras decidem se aquilo é um alerta, e com que nível.

Para uma aplicação que o Wazuh nunca viu, faltam o decoder e a regra. É isso que se escreve: um decoder que reconhece o programa e extrai os campos, e uma regra que dispara com eles.

**Do registo ao alerta**

Pré-decoder
: separa a linha — data, máquina, programa

Decoder
: reconhece o programa e tira os campos — a ação, a conta, a origem

Regra
: decide, com os campos, se é alerta e com que nível

Alerta
: vai para o Indexer e para o painel de quem analisa

```{figure} /_static/img/507-regras-de-detecao/01.jpg
:alt: Do registo ao alerta

Do registo ao alerta.
```

## No Wazuh, antes

**Menu:** Wazuh › Ruleset Test

Primeiro, no Wazuh. O Ruleset Test, no painel dele, mostra o que o gestor faz com uma linha. Esta é real: a aplicação secvision-app de uma máquina do ambiente de testes regista uma entrada falhada, com a conta e o endereço.

O resultado diz tudo: o pré-decoder separou a máquina e o programa, mas nenhum decoder a reconheceu. Para o Wazuh, esta linha não quer dizer nada, e nunca vai ser alerta.

```{figure} /_static/capturas/wazuh-deteccao/antes-1.jpg
:alt: Wazuh › Ruleset Test

O ecrã em Wazuh › Ruleset Test.
```

1. Escreva no campo **Type one log per line...**.
2. Clique em **Test**.

## No SecVision

**Menu:** Proteger › SOC › Regras de Deteção

No SecVision, em Regras de Deteção, cola-se a linha. O botão da IA prepara o pedido, com as instruções de formato que o Wazuh exige, e anonimizado, como nos falsos positivos.

```{figure} /_static/img/507-regras-de-detecao/03.jpg
:alt: Proteger › SOC › Regras de Deteção

O ecrã em Proteger › SOC › Regras de Deteção.
```

Copia-se o pedido.

### No assistente de IA

No assistente de inteligência artificial, cola-se o pedido e envia-se. A linha de registo vai com a máquina, a conta e o endereço trocados por etiquetas.

```{figure} /_static/img/507-regras-de-detecao/04.jpg
:alt: O pedido pseudonimizado, colado no assistente de IA

O pedido, colado no assistente de IA. A janela é desenhada para o vídeo; o pedido e a resposta são reais, processados por um modelo de IA.
```

A resposta vem no formato que o pedido exige: quatro blocos marcados. Um decoder que reconhece o programa, outro que tira o evento, a conta e a origem, uma regra que agrupa os eventos da aplicação, e a regra de deteção, que dispara no login falhado. Copia-se tudo.

```{figure} /_static/img/507-regras-de-detecao/05.jpg
:alt: A resposta do assistente, em quatro blocos e ainda com as etiquetas

A resposta real do modelo, em quatro blocos e ainda com as etiquetas.
```

### A resposta, de volta

A resposta cola-se inteira, ainda com as etiquetas, e o ecrã avisa. **Separar componentes** faz primeiro a troca ao contrário, com o cofre do pedido, e só depois põe cada bloco na sua caixa, já com os valores reais.

Sem esta troca, o decoder iria para o Wazuh com etiquetas lá dentro, e não reconheceria linha nenhuma. Por isso, se faltar o cofre — por exemplo, se a página foi recarregada depois de gerar o pedido —, ou se a resposta trouxer etiquetas que o pedido não tinha, o ecrã diz quais e recusa validar e aplicar. Os números das regras ficam por preencher: atribui-os a plataforma.

```{figure} /_static/img/507-regras-de-detecao/06.jpg
:alt: A resposta separada nos quatro blocos, com os valores reais

A resposta separada nos quatro blocos, com as etiquetas repostas.
```

## Aplicar

**Menu:** Regras de Deteção › Aplicar ao Wazuh

Validados os quatro blocos, aplica-se ao gestor.

```{figure} /_static/img/507-regras-de-detecao/07.jpg
:alt: Regras de Deteção › Aplicar ao Wazuh

O ecrã em Regras de Deteção › Aplicar ao Wazuh.
```

**Menu:** Regras de Deteção › Aplicar ao Wazuh

É o mesmo cuidado dos falsos positivos, agora com dois ficheiros: os decoders e as regras. Cópia de segurança dos dois, escrita, validação pelo gestor, reinício, confirmação.

E se o Wazuh recusar alguma coisa, a plataforma repõe os dois ficheiros e mostra a razão que o gestor deu, palavra por palavra.

```{figure} /_static/img/507-regras-de-detecao/08.jpg
:alt: Regras de Deteção › Aplicar ao Wazuh

O ecrã em Regras de Deteção › Aplicar ao Wazuh.
```

**Menu:** Regras de Deteção › Aplicar ao Wazuh

Aplicada, com o logtest a confirmar que a linha dispara a regra nova.

```{figure} /_static/img/507-regras-de-detecao/09.jpg
:alt: Regras de Deteção › Aplicar ao Wazuh

O ecrã em Regras de Deteção › Aplicar ao Wazuh.
```

## No Wazuh, depois

**Menu:** Wazuh › Ruleset Test

De volta ao Wazuh, a mesma linha no Ruleset Test. Agora o decoder reconhece a aplicação, tira a conta e o endereço, e a regra nova dispara, com nível oito: vai ser gerado um alerta.

```{figure} /_static/img/507-regras-de-detecao/10.jpg
:alt: Wazuh › Ruleset Test

O ecrã em Wazuh › Ruleset Test.
```

**Menu:** Wazuh › Threat Hunting › Events

Cinco minutos depois, nos eventos do Wazuh, os alertas da regra nova, de todas as máquinas onde a aplicação corre. O que era uma linha sem sentido é agora um alerta, com a conta e a origem.

E como qualquer alerta, conta para os indicadores, e pode ser classificado, ou calado com um falso positivo, se um dia se provar inofensivo.

```{figure} /_static/img/507-regras-de-detecao/11.jpg
:alt: Wazuh › Threat Hunting › Events

O ecrã em Wazuh › Threat Hunting › Events.
```

## Resumo

A plataforma trata do formato, da aplicação segura e da confirmação.

O que não sabe é que eventos importam a esta organização. Essa escolha é de quem conhece os sistemas, e é o que faz uma boa regra de deteção.

**O que a plataforma faz — e o que não faz**

- Prepara o pedido à IA com o formato do Wazuh, separa a resposta e valida cada bloco.
- Aplica decoders e regras com cópia de segurança, validação, reinício, logtest e reversão.
- Não sabe que eventos importam à organização: isso decide quem conhece os sistemas.
