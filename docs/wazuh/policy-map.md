# A política da rede privada, em mapa

O mapa das ligações que a política da rede privada permite e nega, derivado da própria política; o botão «Verificar o isolamento agora», que prova a política em vigor contra as máquinas de hoje; e o que acontece quando alguém altera a política diretamente no Headscale: a deriva, os testes a falhar e a reposição.

```{video} 516-o-mapa-da-politica
```

A rede privada dos agentes do Wazuh tem uma regra simples: cada servidor só fala com o ponto de entrada do Wazuh, e com mais nada. Esta página mostra essa regra num mapa, e como se prova, a qualquer momento, que continua a valer. Pressupõe a rede montada, como descreve [Montar a rede privada para os agentes do Wazuh](private-network.md), e servidores ligados, como em [Adicionar um servidor da DMZ ao Wazuh](connect-a-server.md). No laboratório do vídeo há seis máquinas ligadas: três servidores Linux, dois Windows e a ponte.

## Porque é preciso provar

- A política vive no Headscale, e quem tem acesso ao Headscale pode alterá-la sem passar pelo SecVision.
- Uma regra a mais deixa um servidor comprometido chegar aos outros pela rede privada.
- Os testes de isolamento corriam só no momento de aplicar a política; agora correm quando se quiser, contra a política em vigor e as máquinas que existem nesse momento.

## Acesso

**Proteger** > **Rede VPN** > **Política**

É do administrador do SecVision.

## O mapa

```{figure} /_static/img/516-o-mapa-da-politica/01.jpg
:alt: O mapa das ligações da política da rede privada

O mapa: servidores, ponte, ponto de entrada (HAProxy) e gestor do Wazuh.
```

O mapa mostra os servidores, a ponte, o ponto de entrada e o gestor do Wazuh, com o número de máquinas de cada tipo. As ligações verdes são o que a política permite (as portas 1514 e 1515 até ao ponto de entrada); as vermelhas, o que nega: entre servidores, do ponto de entrada para os servidores, e a partir de uma máquina bloqueada. O salto do ponto de entrada até ao gestor e o Headscale, que coordena a rede mas não transporta tráfego, aparecem a tracejado, fora da política.

O mapa é **derivado da própria política**, nunca desenhado à mão: se a política mudar, o mapa muda. Por baixo, cada ligação está escrita por extenso, com o seu estado.

## Verificar o isolamento agora

```{figure} /_static/img/516-o-mapa-da-politica/02.jpg
:alt: O resultado de Verificar o isolamento agora, com todos os testes confirmados

Um teste de cada vez, contra a política em vigor e as máquinas de agora.
```

**Verificar o isolamento agora** corre os testes um a um, contra a política em vigor no Headscale e as máquinas ligadas, e mostra o resultado de cada: **confirmado**, ou **FALHOU** com a razão dada pelo Headscale. Não escreve nada no Headscale, mas fica na trilha de auditoria: dizer que o isolamento foi verificado numa data, com um resultado, é uma prova. Prova a regra do Headscale, não a firewall da rede.

## Quando alguém mexe na política por fora

```{figure} /_static/img/516-o-mapa-da-politica/03.jpg
:alt: A deriva da política e os testes de isolamento a falhar

A política em vigor já não é a desejada, e os testes entre servidores falham.
```

No vídeo, alguém altera a política diretamente no Headscale, sem passar pelo SecVision, e deixa os servidores falarem entre si. O ecrã deteta a deriva («Alguém mexeu na política fora do SecVision») e mostra o que foi acrescentado em **O que difere**. Verificado de novo o isolamento, os testes entre servidores falham, e cada linha diz porquê: o que devia ser negado é agora permitido.

```{figure} /_static/img/516-o-mapa-da-politica/04.jpg
:alt: A política reposta e o isolamento confirmado de novo

Reposta, e provada outra vez.
```

**Aplicar a política desejada** repõe a política do SecVision e apaga o que foi acrescentado por fora. Verificado de novo, todos os testes passam. As duas coisas ficam na trilha de auditoria: a política aplicada, por quem e quando, e cada verificação do isolamento, com o número de testes e de falhas.
