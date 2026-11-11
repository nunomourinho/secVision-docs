# Adicionar um servidor da DMZ ao Wazuh

O percurso de um servidor que não chega ao gestor do Wazuh, com um só comando: escrever o nome do servidor no SecVision, copiar o comando que ele gera, colá-lo no servidor e confirmar que o servidor aparece na rede privada, no SecVision e no painel do Wazuh.

```{video} 510-adicionar-um-servidor
```

Esta página junta um servidor de uma zona isolada ao Wazuh, do princípio ao fim. O servidor não tem Internet, não chega ao gestor, e ninguém vai abrir portas na firewall. Todos os passos foram feitos a sério, num laboratório, e o resultado vê-se no SecVision e no painel do Wazuh. Pressupõe a rede montada, como descreve [Montar a rede privada para os agentes do Wazuh](private-network.md).

## Acesso

**Proteger** > **Rede VPN** > **Montar a rede** > **4. Adicionar um servidor**

O passo é do administrador do SecVision: gera o comando, que depois é colado no servidor por quem o administra.

## O que se faz, e o que se evita

- **No SecVision:** o nome do servidor e **Gerar o comando**.
- **No servidor:** colar esse comando, e mais nada.
- O comando já leva a rede, os instaladores e as chaves; nada disso se copia à mão.
- O comando vale uma hora e serve para um só servidor.

## Informação a solicitar

**Responsáveis**

| Elemento | A quem pedir |
|---|---|
| Nome pelo qual o servidor aparece no Wazuh e no SecVision | Responsável do servidor |
| Uma sessão de administrador no servidor (o comando usa `sudo`) | Administrador do servidor |
| O servidor tem de alcançar o Headscale (443) e o depósito (8080), e mais nada | Administrador da firewall |

## 1. Gerar o comando

```{figure} /_static/img/510-adicionar-um-servidor/01.jpg
:alt: Passo 4 do assistente: adicionar um servidor

Passo 4 do assistente **Montar a rede**: adicionar um servidor.
```

```{figure} /_static/img/510-adicionar-um-servidor/02.jpg
:alt: O nome do servidor

O único campo obrigatório: o nome do servidor.
```

1. **Nome do servidor:** o nome que a máquina vai ter no Wazuh (por exemplo, `portal-dmz-01`). Se o servidor já estiver no catálogo de sistemas do SecVision, escolha-o em **Sistema do catálogo (opcional)** e a máquina fica associada a ele desde o início.
2. Carregue em **Gerar o comando**. O SecVision cria uma chave de registo de uso único para este servidor e prepara, no depósito, o pequeno guião que o servidor vai correr.

```{figure} /_static/img/510-adicionar-um-servidor/03.jpg
:alt: Gerar o comando

Ecrã depois de **Gerar o comando**.
```

```{figure} /_static/img/510-adicionar-um-servidor/04.jpg
:alt: O comando único, pronto a copiar

O comando único. **Copiar** põe-no na área de transferência.
```

O comando descarrega o guião de instalação do depósito e corre-o com o `sudo`, porque instalar serviços exige privilégios de administrador. A parte do meio, com o `sha256`, é a impressão digital do depósito: garante ao servidor que está a falar com o depósito certo, sem instalar nenhum certificado nele. O guião só se corre depois de essa identidade ser confirmada.

O comando é de uso único e vale uma hora. Quem o tiver nesse tempo consegue ligar um servidor com este nome: cole-o logo e não o guarde num documento.

## 2. Colar no servidor

```{figure} /_static/img/510-adicionar-um-servidor/05.jpg
:alt: O servidor da DMZ

O servidor da DMZ, num terminal.
```

Abra uma sessão de administrador no servidor. Este está numa DMZ: não chega à Internet.

```{figure} /_static/img/510-adicionar-um-servidor/06.jpg
:alt: Sem Internet

Sem Internet: o acesso ao exterior falha.
```

```{figure} /_static/img/510-adicionar-um-servidor/07.jpg
:alt: Só chega ao Headscale

O que o servidor alcança é o Headscale, na própria DMZ: responde que está bem.
```

Cole o comando e carregue em Enter. É a única coisa que se faz neste servidor.

```{figure} /_static/img/510-adicionar-um-servidor/08.jpg
:alt: Colar o comando

O comando colado.
```

```{figure} /_static/img/510-adicionar-um-servidor/09.jpg
:alt: O agente junta-se à rede

O agente instala-se e entra na rede privada.
```

1. Primeiro, o agente instala-se como serviço e guarda a sua chave, só legível pelo administrador. Depois entra na rede privada, com a chave de uso único que o SecVision criou para este servidor.
2. A partir daqui, nesta máquina, as portas 1514 e 1515, locais, levam ao ponto de entrada do Wazuh pela rede privada. O Wazuh não precisa de saber que existe uma rede privada: fala com o endereço local.

```{figure} /_static/img/510-adicionar-um-servidor/10.jpg
:alt: Confere a impressão digital e instala o pacote do Wazuh

O pacote do Wazuh é descarregado do depósito e conferido.
```

3. O agente descarrega o pacote do Wazuh do depósito e confere a impressão digital. Só se for exatamente a que o SecVision declarou é que o instala.

```{figure} /_static/img/510-adicionar-um-servidor/11.jpg
:alt: O agente do Wazuh, endurecido por omissão

O agente do Wazuh fica endurecido.
```

4. O agente do Wazuh fica configurado para falar só com o endereço local, com os comandos remotos bloqueados e a configuração protegida contra alterações.

```{figure} /_static/img/510-adicionar-um-servidor/12.jpg
:alt: Instalação concluída

Instalação concluída.
```

5. No fim, o instalador verifica que o agente está a correr e ligado ao gestor pela rede privada. Se alguma verificação falhar, diz qual.

```{figure} /_static/img/510-adicionar-um-servidor/13.jpg
:alt: Os dois serviços ativos

Os dois serviços ativos e as portas do Wazuh à escuta só no endereço local.
```

Para confirmar no servidor: `systemctl is-active secvision-agente wazuh-agent` responde `active` duas vezes, e as portas 1514 e 1515 estão à escuta apenas em `127.0.0.1`.

## O resultado no SecVision

**Proteger** > **Rede VPN** > **Máquinas**

```{figure} /_static/img/510-adicionar-um-servidor/14.jpg
:alt: Proteger > Rede VPN > Máquinas

Ecrã **Proteger** > **Rede VPN** > **Máquinas**.
```

A lista já mostra o `portal-dmz-01`:

1. **Ligação:** ligado, o Headscale vê-o.
2. **Agente Wazuh:** o Wazuh recebe os dados dele pela rede privada.
3. **Acesso até:** o acesso tem validade, de um ano, a contar da instalação.

## O resultado no Wazuh

**Wazuh** > **Endpoints** > **Agents**

```{figure} /_static/img/510-adicionar-um-servidor/15.jpg
:alt: Wazuh > Endpoints > Agents

Ecrã **Wazuh** > **Endpoints** > **Agents**.
```

No painel do Wazuh, o mesmo servidor aparece como agente ativo. Para o Wazuh é um agente como os outros; a diferença é apenas o caminho que os dados fazem até lá.

## Aplicar a política com testes

**Proteger** > **Rede VPN** > **Política**

```{figure} /_static/img/510-adicionar-um-servidor/16.jpg
:alt: Proteger > Rede VPN > Política

Ecrã **Proteger** > **Rede VPN** > **Política**.
```

Agora que há um servidor na rede, a política já pode correr os testes de isolamento. No ecrã **Política**, clique em **Aplicar a política desejada** e confirme: o Headscale só a aceita se os testes passarem.

## Resumo

```{figure} /_static/img/510-adicionar-um-servidor/17.jpg
:alt: O que o servidor precisa de ter

O que o servidor precisa de ter.
```

O SecVision gera um comando para cada servidor, com uma chave de registo de uso único. Quem o corre é uma pessoa, com a sessão de administrador do servidor.

O SecVision não entra no servidor para instalar o agente: não executa o comando por si.

**Funcionalidades e limitações**

- O servidor precisa de um Linux com systemd e do pacote `lsb-release`, de que o pacote do Wazuh depende. Se faltar, o agente diz-o antes de instalar, porque sem Internet o servidor não o consegue ir buscar.
- O servidor só precisa de alcançar o Headscale (443) e o depósito (8080).
- O instalador para Windows existe mas ainda não foi provado numa máquina real: antes de o usar em produção, faça um piloto com um único servidor.
- Os servidores antigos, que não correm o cliente da rede privada, ligam-se por uma ponte: uma máquina moderna da mesma rede, instalada com a opção **Esta máquina é uma ponte**. Não está coberta por um vídeo.
- O comando curto exige o depósito que o assistente instala. Quem usa um Headscale e um depósito montados à mão continua com o comando longo, em **Proteger** > **Rede VPN** > **Convites** > **Avançado**.
