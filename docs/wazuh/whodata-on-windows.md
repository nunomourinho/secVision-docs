# O whodata no Windows

O whodata num Windows Server: o que é a auditoria do Windows, porque é que o agente do SecVision só o liga quando a política de auditoria já o permite, o instalador interativo que a prepara com autorização e cópia da anterior, e o alerta de integridade que passa a dizer que processo escreveu cada ficheiro.

```{video} 517-o-whodata-no-windows
```

A página {doc}`whodata` mostra o whodata num servidor Linux. Esta mostra o mesmo num Windows Server 2022: o alerta de integridade passa a dizer que processo escreveu cada ficheiro, e com que utilizador. Tudo foi feito em máquinas reais do laboratório: o Windows Server 2022, o Wazuh de teste com o seu painel e o SecVision de teste.

## O conceito

No Windows, o whodata não precisa de nenhum programa a mais: é a **auditoria do próprio sistema**. Se a política de auditoria o pedir, o Windows regista no registo **Security** quem abre e quem escreve cada ficheiro.

Contam duas subcategorias da política de auditoria: **File System** e **Handle Manipulation**, com os sucessos registados. Num Windows acabado de instalar estão desligadas. No laboratório medimos que, se se pedir o whodata, **o próprio agente Wazuh as liga sozinho**, sem perguntar. Mudar a política de auditoria de um servidor é uma decisão do seu administrador, e não de um script.

Por isso, o agente do SecVision:

- só liga o whodata se a política de auditoria **já** o permitir; se não permitir, diz exatamente o que falta e deixa a máquina como estava;
- para preparar a política, há um **instalador interativo**, que pergunta um item de cada vez;
- antes de mudar a política, o instalador guarda uma **cópia** da anterior, e no fim mostra o comando que a repõe;
- depois de reiniciar, confirma no registo do agente (`ossec.log`) que o whodata arrancou; se não arrancou, tira a configuração.

## Informação a solicitar

| Informação | Responsável |
|---|---|
| Que servidores Windows vão ter o whodata, e com que perfil de agente | responsável de cibersegurança |
| A autorização para mudar a política de auditoria de cada servidor | administrador do servidor |
| Se uma GPO do domínio define a política de auditoria | administrador do domínio |
| Uma sessão no servidor, como administrador (consola ou RDP) | administrador do servidor |

Num domínio, se uma GPO definir a política de auditoria, é na GPO que se muda. Uma mudança feita só no servidor é desfeita pela GPO ao fim de algum tempo, e o agente deixa de ter o whodata em tempo real.

## 1. O comando, no SecVision

**Identificar** > **Fila de Integração**

```{figure} /_static/img/517-o-whodata-no-windows/01.jpg
:alt: Iniciar Integração de um Windows Server 2022, separador Rede VPN

Um Windows Server 2022 sem agente, no separador **Rede VPN**.
```

O caminho é o mesmo da página {doc}`install-on-windows`. Na fila de integração, escolha **Iniciar Integração** no servidor e abra o separador **Rede VPN**.

```{figure} /_static/img/517-o-whodata-no-windows/02.jpg
:alt: O perfil Bloqueado com whodata e os dois instaladores interativos

O perfil **Bloqueado + whodata** e o aviso do whodata.
```

Escolha o perfil de agente **Bloqueado + whodata**. O resumo do perfil mostra as limitações do agente e, no fim, o whodata. Logo abaixo aparece um aviso: o whodata só se liga se a máquina já tiver o necessário. No Windows, isso é a política de auditoria.

```{figure} /_static/img/517-o-whodata-no-windows/03.jpg
:alt: Os botões dos instaladores do whodata para Linux e Windows

Os dois instaladores interativos, com o sha256 para conferir.
```

Para preparar o que falta, há dois instaladores interativos: **Instalador do whodata — Linux (.sh)** e **Instalador do whodata — Windows (.ps1)**. O sha256 de cada um aparece no SecVision, para conferir antes de o correr. Nas máquinas que já têm o agente do SecVision, o próprio agente faz o mesmo com `secvision-agente whodata preparar`.

```{figure} /_static/img/517-o-whodata-no-windows/04.jpg
:alt: O comando de PowerShell gerado pelo SecVision

Uma linha de PowerShell, válida durante uma hora e só para este servidor.
```

**Gerar o comando** produz uma linha de PowerShell, válida durante uma hora e só para este servidor.

## 2. Instalar o agente

```{figure} /_static/img/517-o-whodata-no-windows/05.jpg
:alt: O PowerShell aberto como administrador no Windows Server

O PowerShell, aberto como administrador.
```

No servidor, abra o PowerShell como administrador. Neste exemplo, o Windows está como saiu da instalação, com a política de auditoria de origem.

```{figure} /_static/img/517-o-whodata-no-windows/06.jpg
:alt: O comando do SecVision a instalar o agente

O comando entra na rede privada, instala o agente Wazuh e aplica o perfil.
```

Cole o comando que o SecVision gerou. O agente entra na rede privada, instala o agente Wazuh e aplica o perfil. No fim, confirma no `ossec.log` que o gestor aceitou o registo. Se o gestor o recusar, por exemplo por já haver um agente com o mesmo nome, o comando diz porquê, em vez de dar o agente por ligado.

```{figure} /_static/img/517-o-whodata-no-windows/07.jpg
:alt: A mensagem whodata pedido pelo perfil mas não ligado

O agente ficou ligado; o whodata não, e o comando diz o que falta.
```

O agente ficou ligado, mas o whodata não: as subcategorias **File System** e **Handle Manipulation** não registam os sucessos. O agente não mudou a política de auditoria, e diz o que fazer: correr o instalador interativo, como administrador.

## 3. Preparar a política de auditoria

O instalador interativo existe em duas formas, com o mesmo comportamento:

- `secvision-agente whodata preparar`, nas máquinas com o agente do SecVision;
- `.\whodata-preparar.ps1`, nas outras. Descarrega-se no SecVision (perfil do agente, no separador **Rede VPN**, ou perfil da máquina) ou do depósito da rede privada, depois de **Publicar os instaladores**.

Corre-se numa janela do PowerShell **como administrador**, na consola do servidor ou por RDP. Lançado por uma tarefa agendada ou por uma sessão sem ecrã, recusa: não há forma de mudar a política sem uma pessoa a ler as perguntas.

```{figure} /_static/img/517-o-whodata-no-windows/08.jpg
:alt: O inventário do instalador e a primeira pergunta

Primeiro o inventário, só com leituras; depois, uma pergunta por item.
```

Primeiro, um **inventário**, só com leituras: as subcategorias em falta e o bloco de configuração que ainda não existe. Também verifica o serviço EventLog, a opção que obriga o Windows a respeitar as subcategorias (`SCENoApplyLegacyAuditPolicy`) e se o servidor pertence a um domínio.

Depois, **um a um**, o que falta: o que o item faz, porque é preciso e o comando exato, com o `auditpol`. A resposta por omissão é **não**.

```{figure} /_static/img/517-o-whodata-no-windows/09.jpg
:alt: A cópia da política e a pergunta do bloco de configuração

A configuração é mostrada antes de pedir autorização.
```

Antes da primeira mudança, a política de antes fica guardada num ficheiro em `C:\ProgramData\SecVision\` (`auditpol-antes-<data>.csv`). Por fim, o **bloco de configuração**: um bloco assinado no `ossec.conf`, que repete as pastas que o agente já vigia, agora com o whodata. Nada passa a ser vigiado que não o fosse antes.

```{figure} /_static/img/517-o-whodata-no-windows/10.jpg
:alt: A espera pela confirmação no ossec.log

O instalador espera pelo código 6019 no ossec.log.
```

O agente reinicia, e o instalador lê o `ossec.log` durante até quatro minutos. O whodata do Windows só arranca no fim do primeiro varrimento dos ficheiros, e o agente escreve então o código `(6019)`.

```{figure} /_static/img/517-o-whodata-no-windows/11.jpg
:alt: Whodata ativo e o resumo do instalador

O whodata ativo, e o resumo: o que mudou e como se repõe.
```

O resumo diz o que mudou e o comando que repõe a política de antes:

```powershell
auditpol /restore /file:"C:\ProgramData\SecVision\auditpol-antes-<data>.csv"
```

Se o whodata não tivesse arrancado, o bloco saía do `ossec.conf` e o agente voltava ao que era. Uma reinstalação posterior com o perfil **Bloqueado + whodata** mantém o whodata, porque a política já o permite.

## 4. O processo no alerta

Para ver o efeito, escreva um ficheiro numa das pastas que o agente vigia, por exemplo a pasta `drivers\etc` do Windows:

```powershell
Set-Content C:\Windows\System32\drivers\etc\relatorio-mensal.txt "versao 2"
```

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/517-o-whodata-no-windows/13.jpg
:alt: O alerta de integridade do ficheiro escrito, no painel do Wazuh

O alerta do ficheiro que se acabou de escrever.
```

No painel do Wazuh, procure os eventos de integridade deste servidor:

```text
rule.groups : syscheck and agent.name : "aplicacao-004" and syscheck.path : *relatorio-mensal*
```

```{figure} /_static/img/517-o-whodata-no-windows/14.jpg
:alt: Os campos syscheck.audit.process.name e syscheck.audit.user.name no alerta

O processo e o utilizador que escreveram o ficheiro.
```

No documento do alerta (regra 554) aparecem os campos novos: `syscheck.audit.process.name`, o processo que escreveu o ficheiro (aqui o `powershell.exe`), e `syscheck.audit.user.name`, o utilizador. O ecrã dos falsos positivos do SecVision usa estes campos para separar o que um programa conhecido escreve, como uma atualização, de uma alteração que merece atenção (ver {doc}`whodata`).

## Limites

- Ligar as subcategorias **File System** e **Handle Manipulation** aumenta os eventos no registo Security, embora só para as pastas que o agente vigia (as que têm SACL).
- Uma GPO de domínio que defina a política de auditoria repõe-na ao fim de algum tempo; o agente Wazuh escreve então o código `(6953)` e deixa de ter o whodata em tempo real. Nesse caso, a mudança faz-se na GPO.
- Com `SCENoApplyLegacyAuditPolicy` a 0, o Windows ignora as subcategorias, e o agente não liga o whodata.
- Parar o serviço do agente Wazuh repõe a política que ele próprio guardou ao arrancar.
- Os Windows Server 2012 R2 e anteriores instalam-se pela ponte ({doc}`legacy-servers`), sem whodata.
