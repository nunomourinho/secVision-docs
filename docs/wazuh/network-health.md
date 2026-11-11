# Quando algo falha na rede privada

Como saber, de relance, se a rede privada está bem, e o que fazer quando uma luz deixa de ser verde: rodar a chave de API do Headscale, renovar os certificados e levá-los ao servidor, sem copiar nenhuma chave nem correr nenhum comando.

```{video} 512-quando-algo-falha-na-rede-privada
```

Uma rede privada que ninguém vigia falha em silêncio: uma chave expira, um certificado chega ao fim, e um dia os servidores deixam de se ligar. O SecVision mostra a saúde da rede num só painel, e oferece o que fazer em cada caso. Pressupõe a rede montada, como descreve [Montar a rede privada para os agentes do Wazuh](private-network.md).

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/01.jpg
:alt: Uma nota sobre este laboratório

Uma nota de honestidade sobre este laboratório.
```

Esperar um ano para ver um certificado a expirar não se filma. Por isso, no laboratório do vídeo, as datas da chave de API e de um certificado foram encurtadas; tudo o que o SecVision faz a seguir é real.

## Acesso

**Proteger** > **Rede VPN** > **Estado e ligação**

O painel está no topo do ecrã e repete-se em **Montar a rede**, depois de o Headscale estar instalado. É do administrador do SecVision.

## O painel

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/02.jpg
:alt: A saúde da rede, em Estado e ligação

A saúde da rede, no topo de **Estado e ligação**.
```

São sete luzes:

1. **O Headscale:** responde, e aceita a chave de API.
2. **A chave de API:** quantos dias faltam para expirar.
3. **Os certificados:** o primeiro a expirar, e se há algum certificado novo ainda por levar ao servidor.
4. **O depósito de instaladores:** responde e apresenta o certificado do SecVision.
5. **O ponto de entrada do Wazuh:** está ligado à rede privada.
6. **A tarefa das validades:** corre todas as madrugadas e bloqueia os acessos vencidos.
7. **As máquinas:** os servidores monitorizados, e se algum está desligado ou com o acesso expirado.

Verde é em ordem, amarelo pede atenção, vermelho é um problema. A luz **cinzenta** quer dizer «não medido» (por exemplo, a tarefa das validades numa rede acabada de montar, que ainda não teve a sua primeira madrugada) e nunca quer dizer que está bem. Ao lado de cada luz que não é verde está o que fazer.

## Rodar a chave de API

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/03.jpg
:alt: Rodar a chave de API

**Rodar a chave de API**.
```

A chave de API dá ao SecVision autorização para gerir o Headscale, e expira. Antes, era preciso criar uma nova no servidor e colá-la no ecrã. Agora basta carregar em **Rodar a chave de API**: o SecVision pede ao Headscale uma chave nova, guarda-a cifrada, experimenta-a, e só depois expira a antiga. Se a nova não funcionar, a antiga fica como estava, e o SecVision diz porquê.

## Renovar os certificados

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/04.jpg
:alt: Renovar os certificados

**Renovar os certificados**: emitidos de novo, falta levá-los ao servidor.
```

Os certificados do Headscale e do depósito são emitidos pelo SecVision e duram 825 dias. Quando um chega aos 30 dias do fim, **Renovar os certificados** emite-os de novo, com os mesmos nomes, sem que nada passe pelas mãos de quem administra.

O servidor, porém, continua com o certificado antigo, e o painel di-lo: o certificado novo está por levar ao servidor. Para o levar é preciso entrar no servidor, e para isso é preciso a palavra-passe, que o SecVision nunca guardou.

## Reparar

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/05.jpg
:alt: Reparar: refazer o passo no assistente

**Reparar** leva ao assistente, no passo certo.
```

**Reparar** leva ao assistente **Montar a rede**, no passo certo. Carregue em **Refazer** no passo 1, indique o endereço e a palavra-passe, e o SecVision leva o certificado novo ao servidor: o Headscale e o depósito ficam com o certificado novo, e o SecVision confirma que continua a falar com eles. Os servidores que já estavam ligados continuam ligados.

```{figure} /_static/img/512-quando-algo-falha-na-rede-privada/06.jpg
:alt: Tudo em ordem outra vez

De volta ao painel, as luzes estão verdes.
```

## Resumo

O painel de saúde diz o que está bem, o que expira e o que falhou, e o que fazer. A chave de API e os certificados renovam-se pelo ecrã, sem copiar nada. O que exige entrar num servidor pede a palavra-passe do administrador, porque o SecVision não a guarda.

**Funcionalidades e limitações**

- Renovar os certificados só os emite de novo; levá-los ao servidor é **Reparar**.
- Uma luz cinzenta quer dizer «não medido», nunca «bem».
- Não está provado em produção.
