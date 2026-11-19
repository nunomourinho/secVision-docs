# O whodata do FIM

Porque é que uma atualização gera centenas de alertas de integridade, o que o whodata acrescenta (o processo que escreveu cada ficheiro), porque é que o agente só o liga com o que a máquina já tem, o instalador interativo que prepara a máquina com autorização item a item, e o modelo de falso positivo que baixa a nível 1 o que o gestor de pacotes escreveu.

```{video} 515-o-whodata-do-fim
```

Numa atualização do sistema, o Wazuh alerta em cada ficheiro que muda: centenas de alertas, todos verdadeiros e quase todos inofensivos. Esta página mostra como o Wazuh passa a saber que processo fez cada alteração, e como isso permite calar só o que o gestor de pacotes escreveu. Tudo foi feito em máquinas reais do laboratório: um Debian 12, o Wazuh de teste com o seu painel e o SecVision de teste.

## O problema

O FIM, a monitorização da integridade dos ficheiros, vigia as pastas do sistema e alerta em cada ficheiro que muda. No laboratório, instalar três pacotes num Debian deu 474 alertas.

O problema não é o número: é que nenhum desses alertas dizia quem escreveu o ficheiro. Sem essa informação, nenhuma regra consegue separar uma atualização de uma alteração maliciosa, e a equipa acaba por ignorar o FIM.

## O whodata

O whodata acrescenta ao alerta o processo que alterou o ficheiro e o processo que o lançou: por exemplo, o `dpkg`, a pedido do `apt-get`. Com isso, já se pode escrever uma regra que reconhece uma atualização.

Há duas formas de o obter:

- **eBPF:** precisa do agente Wazuh 4.14 ou posterior, de um kernel com BTF e da biblioteca `libelf`;
- **auditd:** o serviço de auditoria do Linux.

O agente do SecVision só liga o whodata com o que a máquina já tem, e **nunca instala nada**: uma biblioteca a mais num servidor de produção é uma decisão do seu administrador. Para essa decisão existe o instalador interativo, descrito abaixo.

## Informação a solicitar

| Informação | Responsável |
|---|---|
| Que servidores vão ter o whodata, e com que perfil de agente | responsável de cibersegurança |
| Autorização para instalar o que falta (o `libelf`, o `auditd`) | administrador de cada servidor |
| Um alerta FIM real de cada família de sistemas, como prova | equipa de análise de alertas |
| Aplicação das regras no gestor do Wazuh | administrador do SecVision |

## 1. O ruído, no Wazuh

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/515-o-whodata-do-fim/01.jpg
:alt: Alertas FIM de um servidor Debian no painel do Wazuh

Os alertas FIM de um servidor Debian, depois de instalar três pacotes: um por ficheiro alterado.
```

No separador **JSON** do alerta vê-se que ficheiro mudou e como, mas não que processo o alterou: o agente ainda não tem whodata.

## 2. O mesmo alerta, no SecVision

**Proteger** > **SOC** > **Falsos Positivos**

```{figure} /_static/img/515-o-whodata-do-fim/02.jpg
:alt: Aviso de alerta FIM sem processo no ecrã dos falsos positivos

O ecrã reconhece um alerta FIM sem processo e oferece o instalador do whodata.
```

Colado o alerta no ecrã dos falsos positivos, o SecVision avisa que é um alerta FIM sem processo: uma regra que olhe ao processo não lhe vai corresponder. O aviso oferece **Descarregar o instalador do whodata**, com o sha256 à vista, para conferir antes de o correr.

## 3. O perfil do agente

**Proteger** > **SOC** > **Wazuh Agent Builder**

```{figure} /_static/img/515-o-whodata-do-fim/03.jpg
:alt: A opção Whodata no FIM no perfil do agente

A opção **Whodata no FIM** do perfil do agente.
```

O whodata é uma opção do perfil de agente: **Whodata no FIM**. Ao contrário das outras opções, que limitam o agente, esta ativa uma capacidade, e vem desligada em todos os perfis. Com a opção ligada, o agente verifica, na instalação, se a máquina tem o eBPF ou o auditd ativo. Se não tiver, diz o que falta e deixa a máquina exatamente como estava.

## 4. Preparar a máquina

O instalador interativo existe em duas formas, com o mesmo comportamento:

- `sudo secvision-agente whodata preparar`, nas máquinas com o agente do SecVision;
- `sudo bash whodata-preparar.sh`, nas outras e no gestor do Wazuh. Descarrega-se no SecVision (aviso acima, ou no perfil da máquina) ou do depósito da rede privada, depois de **Publicar os instaladores**.

```{figure} /_static/img/515-o-whodata-do-fim/05.jpg
:alt: O inventário do instalador do whodata

Primeiro, o inventário: só leituras, nada foi mudado.
```

Primeiro, um **inventário**, só com leituras: a versão do agente, o BTF do kernel, o `ldd`, as bibliotecas do eBPF, o `auditd`, os ficheiros imutáveis e o bloco no `ossec.conf`. O que não se muda dali, como um kernel sem BTF, aparece como **não instalável aqui**, com o que fazer.

```{figure} /_static/img/515-o-whodata-do-fim/06.jpg
:alt: A pergunta para instalar o libelf1

Cada pergunta diz o que o item faz, porque é preciso e o comando exato.
```

Depois, **um a um**, o que falta. A resposta por omissão é **não**. Sem terminal, o instalador recusa: não há forma de instalar nada sem uma pessoa a ler as perguntas.

```{figure} /_static/img/515-o-whodata-do-fim/07.jpg
:alt: O bloco whodata mostrado antes de ser escrito

A configuração é mostrada antes de pedir autorização.
```

Por fim, a configuração: um bloco assinado no `ossec.conf`, que repete as pastas já vigiadas com o whodata ligado. Se o ficheiro estiver protegido (`chattr +i`), o instalador tira a proteção só para escrever e volta a pô-la. Escrito o bloco, o agente reinicia e o instalador lê o registo do Wazuh durante 90 segundos: se o whodata não arrancar, tira o bloco e devolve a máquina ao que era.

```{figure} /_static/img/515-o-whodata-do-fim/08.jpg
:alt: Whodata ativo e o resumo do instalador

O whodata ativo, e o resumo: o que se instalou e como se remove.
```

Os pacotes instalados ficam, mesmo que o whodata não arranque; o resumo diz como os remover. No **gestor** do Wazuh, o mesmo script (`--gestor`) liga o `logall_json` e os arquivos no filebeat, de que o contador de disparos do SecVision precisa, cada um com cópia de segurança, validação e reposição se falhar (o guia do administrador, que acompanha a instalação, descreve-o em pormenor).

## 5. O processo no alerta

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/515-o-whodata-do-fim/09.jpg
:alt: Alertas FIM com o processo dpkg

Depois de mais uma instalação, os alertas FIM trazem o processo.
```

Depois de mais uma instalação no servidor, os alertas FIM trazem o processo: o `dpkg`, lançado pelo `apt-get`. No JSON do alerta, a secção `audit` tem o nome do processo, o processo pai e o utilizador. Este alerta serve de prova para a regra.

## 6. Calar a atualização

**Proteger** > **SOC** > **Falsos Positivos**

```{figure} /_static/img/515-o-whodata-do-fim/10.jpg
:alt: O modelo FIM dpkg pelo apt no ecrã dos falsos positivos

O modelo **FIM: dpkg pelo apt** carrega a regra no segundo passo.
```

Com o alerta colado, o aviso desapareceu, porque agora há processo. O modelo **FIM: dpkg pelo apt (Debian/Ubuntu)** carrega a regra; para RHEL, Rocky e Alma há o modelo **FIM: dnf/yum**. A regra baixa para **nível 1** os eventos em que o `dpkg` alterou um ficheiro a pedido do `apt`. Nível 1, e não 0: o evento fica nos arquivos com a regra que o apanhou, e o contador de disparos funciona.

```{figure} /_static/img/515-o-whodata-do-fim/11.jpg
:alt: A regra aplicada ao Wazuh

Cópia de segurança, escrita, validação, reinício e confirmação.
```

**Validar sintaxe** e **Aplicar ao Wazuh**: o SecVision faz uma cópia de segurança, escreve a regra, valida a configuração do gestor, reinicia-o e confirma. O passo do logtest diz que não se aplica: o logtest repete uma linha de registo, e um evento FIM não é uma linha de registo. Não é um defeito da regra.

## 7. No Wazuh

**Wazuh** > **Server management** > **Rules**

```{figure} /_static/img/515-o-whodata-do-fim/12.jpg
:alt: A regra no ficheiro das regras do SecVision, no painel do Wazuh

A regra, já no gestor.
```

A regra está no ficheiro onde o SecVision escreve as suas regras de falso positivo, tal como o SecVision a escreveu: com o número que lhe foi atribuído, o nível 1, e os dois campos, o processo e o processo pai.

```{figure} /_static/img/515-o-whodata-do-fim/13.jpg
:alt: Nenhum alerta FIM depois de instalar outro pacote

Depois de instalar outro pacote, o que o dpkg escreveu já não aparece nos alertas.
```

Instalado outro pacote no servidor, o `htop`, já não aparece nos alertas FIM o que o `dpkg` escreveu: os quatro eventos do `dpkg` estão nos arquivos do gestor, a nível 1, com a regra que os reconheceu. Os três alertas que ficam são do `ldconfig`, chamado pelo script de instalação da `libc-bin`. Os scripts de instalação dos pacotes não se silenciam, de propósito: são poucos, e é aí que um pacote cria utilizadores ou grupos, ou muda a configuração do sistema.

## Limites

```{figure} /_static/img/515-o-whodata-do-fim/14.jpg
:alt: Os limites do whodata e do modelo

O que fica a saber.
```

- Um pacote malicioso instalado pelo `apt` também é silenciado; no Debian, os alertas do `dpkg.log` continuam a dizer o nome de cada pacote instalado.
- O nome do processo pode ser falsificado por quem já controla a máquina: uma cópia do `dash` chamada `dpkg` passa.
- Com o `auditd`, o `dnf` aparece como o interpretador Python, e a regra do dnf não o cobre. A regra do apt com o `auditd` foi medida num Debian 12.
- Num RHEL ou Rocky com SELinux em modo *enforcing*, o whodata pelo `auditd` não arrancou no laboratório; o eBPF, sim.
- No Windows o whodata não se aplica: mudaria a política de auditoria do sistema, um efeito que não foi medido.
