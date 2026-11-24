# Os modos do agente no Windows

O que cada modo do agente deixa num Windows 10 ou 11, o que sobrevive a um reinício e como se atualizam o agente e a configuração em cada modo: o gestor Wazuh atualiza o agente Desbloqueado e não consegue atualizar o Bloqueado, que se atualiza pelo comando do SecVision.

```{video} 520-os-modos-do-agente-no-windows
```

As páginas {doc}`install-on-windows` e {doc}`whodata-on-windows` mostram a instalação e o whodata num Windows Server. Esta junta o que medimos num **Windows 10 22H2** e num **Windows 11 26H2**, com o agente do SecVision 0.5.9: em cada modo, uma fotografia do sistema antes e depois (ficheiros, serviços, chaves de registo, regras de firewall, tarefas agendadas), reinícios e atualizações. Tudo foi feito em máquinas reais do laboratório e no Wazuh de teste.

## Os quatro níveis

| Nível | O que o gestor Wazuh pode fazer | Evidência |
|---|---|---|
| Desbloqueado | atualizar o agente, mudar a configuração, mandar respostas ativas | o alerta diz que o ficheiro mudou |
| Bloqueado | nada disso: só recebe os eventos | o mesmo |
| + preparador | o mesmo do Bloqueado | + que processo e que utilizador alterou o ficheiro; + quem executou cada processo e o processo pai |
| + Sysmon | o mesmo do Bloqueado | + o SHA256 do executável e a cadeia de processos |

No **Desbloqueado**, o gestor Wazuh pode atualizar o agente, mudar a configuração e mandar respostas ativas. É cómodo, mas quem controlar o gestor controla a máquina. No **Bloqueado**, o gestor só recebe os eventos.

Os dois níveis seguintes acrescentam evidência sem mudar isso. O **preparador** (`secvision-agente whodata preparar`) liga a auditoria do próprio Windows: o whodata ({doc}`whodata-on-windows`) e a evidência de processos ({doc}`process-evidence-on-windows`). O **Sysmon** é um programa à parte, opcional ({doc}`sysmon`).

## O que cada nível deixa na máquina

| Nível | Ficheiros e serviços | Desfaz-se com |
|---|---|---|
| Desbloqueado | `secvision-agente.exe`; `ProgramData\SecVision` (token, CA, estado da rede privada); o agente Wazuh (61 ficheiros); 2 serviços | **Remover programas** e `sc delete` |
| Bloqueado | o mesmo, sem os 23 executáveis de resposta ativa; a pasta do agente só para SYSTEM e Administradores | o mesmo |
| + preparador | cópia da política de auditoria; 3 subcategorias de auditoria; 1 chave de registo (a linha de comandos); o bloco `secvision:whodata` no `ossec.conf` | `auditpol /restore` com a cópia, e tirar o bloco |
| + Sysmon | `Sysmon64.exe`, `SysmonDrv.sys`, a configuração em `ProgramData\SecVision`, o serviço `Sysmon64`, o bloco `secvision:sysmon` no `ossec.conf` | `Sysmon64.exe -u`, apagar o `Sysmon64.exe` e tirar o bloco |

**Nenhum nível cria regras de firewall nem tarefas agendadas.**

## Depois de um reinício

Reiniciámos a máquina em cada nível, também a meio de uma atualização do Windows. Em todos, a ligação à rede privada, o agente Wazuh, o whodata e o Sysmon voltaram sozinhos.

- O serviço da ligação volta a tentar até a rede estar pronta, e o Windows reinicia-o se cair.
- O primeiro arranque do whodata leva uns 4 minutos num Windows 10 ou 11.
- Para reiniciar o agente Wazuh à mão, use `net stop WazuhSvc` e `net start WazuhSvc`. Com o whodata, a paragem demora uns 30 segundos, e o `Restart-Service` do PowerShell chegou a deixar o agente parado.

## Como se atualiza, em cada modo

| O quê | Desbloqueado | Bloqueado |
|---|---|---|
| O agente, pelo gestor Wazuh | aceite | recusado |
| A configuração, pelo gestor (`agent.conf`) | aplicada | chega à máquina, não se aplica |
| O agente e o SecVision, pelo comando do SecVision | funciona | funciona, e volta a aplicar as restrições |
| Mudar de modo | o comando com outro perfil | o comando com outro perfil |

No Bloqueado, atualiza-se pelo SecVision: publica-se a versão nova no depósito e corre-se outra vez o comando curto. A reinstalação mantém o whodata e o Sysmon, e volta a aplicar as restrições.

## 1. O gestor tenta atualizar

Consola do gestor Wazuh

```{figure} /_static/img/520-os-modos-do-agente-no-windows/01.jpg
:alt: agent_control a listar os agentes win10 e win11

Os dois agentes no gestor Wazuh do laboratório.
```

No gestor Wazuh do laboratório estão os dois agentes: o do Windows 10, instalado com o perfil **Bloqueado**, e o do Windows 11, com o **Desbloqueado**. O comando de atualização do gestor (`agent_upgrade`) pede ao agente que se atualize. Forçamos a mesma versão, a 4.14.10, porque o gestor de teste também é a 4.14.10 e um agente não pode ser mais recente do que o seu gestor.

```{figure} /_static/img/520-os-modos-do-agente-no-windows/02.jpg
:alt: agent_upgrade ao agente 042 recusado

O agente Bloqueado recusa a atualização.
```

O Windows 10, o Bloqueado, **recusa**: a atualização remota está desligada no próprio agente, e nada mudou na máquina.

```{figure} /_static/img/520-os-modos-do-agente-no-windows/03.jpg
:alt: agent_upgrade ao agente 039 aceite

O agente Desbloqueado atualiza-se e volta a ligar-se.
```

O Windows 11, o Desbloqueado, **aceita**: o gestor envia o pacote, o agente instala-o e volta a ligar-se, atualizado. A configuração local do agente fica, incluindo o endereço da rede privada do SecVision. É o mesmo mecanismo que, num gestor comprometido, instalaria outra coisa: por isso o Bloqueado o desliga.

## Antes de escolher

```{figure} /_static/img/520-os-modos-do-agente-no-windows/04.jpg
:alt: Recomendações antes de escolher o modo

As recomendações.
```

- Instale e reinstale com o agente **0.5.9 ou mais recente**. Com as versões anteriores, uma reinstalação por cima do whodata podia perder, sem aviso, as restrições do Bloqueado.
- No Bloqueado, conte com o comando do SecVision como único caminho de atualização.
- Instale o Sysmon só onde o SHA256 do executável e a cadeia de processos forem precisos: é software a mais na máquina.
