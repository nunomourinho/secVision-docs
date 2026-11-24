# O Sysmon, à parte

O Sysmon acrescenta ao evento 4688 o SHA256 do executável e uma cadeia de processos que não depende do número do processo. É software a mais na máquina, por isso fica num instalador à parte, opcional: descarrega-o da Microsoft, confere a assinatura, pergunta antes de cada passo e diz como se desfaz.

```{video} 519-o-sysmon-a-parte
```

A página {doc}`process-evidence-on-windows` mostra o evento 4688, que o próprio Windows dá. Esta mostra o Sysmon, da Microsoft, num **Windows 10 22H2** com o agente do SecVision 0.5.9: no SecVision, na consola da máquina e no painel do Wazuh. Tudo foi feito em máquinas reais do laboratório e no Wazuh de teste.

## O conceito

O Sysmon acrescenta:

- o **SHA256** de cada executável lançado, que se pode comparar com listas de programas maliciosos;
- o **ProcessGuid**, um identificador de processo que não se repete, ao contrário do número do processo, para seguir a cadeia de processos sem ambiguidade;
- os ficheiros criados nas pastas onde se instala o arranque automático.

Mas é um serviço e um controlador a mais no Windows. **O instalador do agente nunca o instala**: fica num instalador à parte, `sysmon-preparar.ps1`, que se corre só onde for preciso.

A configuração que o instalador põe é mínima de propósito, e a pessoa vê-a antes de dizer sim:

| Evento | O quê |
|---|---|
| 1 | processos criados, com o SHA256 e o processo pai |
| 2 | datas de ficheiros alteradas |
| 11 | ficheiros criados na pasta de arranque, nas tarefas agendadas e nos controladores, e scripts criados (`.ps1`, `.bat`, `.vbs`, `.hta`) |
| 13 | escritas nas chaves de arranque automático (`Run`) e de serviços |

Sem a rede (evento 3), o fim de processos (5) e o carregamento de bibliotecas (7): são os que mais volume fazem.

## Informação a solicitar

| Informação | Responsável |
|---|---|
| Que máquinas precisam do Sysmon | responsável de cibersegurança |
| A autorização para instalar software na máquina | administrador da máquina |
| A aceitação da licença da Sysinternals | quem decide as licenças na organização |

Instalar o Sysmon aceita a licença da Sysinternals, da Microsoft, em nome da máquina.

## 1. O instalador, no SecVision

**Proteger** > **SOC** > **Falsos Positivos**

```{figure} /_static/img/519-o-sysmon-a-parte/01.jpg
:alt: O instalador do Sysmon ao lado dos do whodata, com o SHA256

O instalador do Sysmon, opcional, com o SHA256 para conferir.
```

Quando um alerta de integridade colado no ecrã não diz o processo (a máquina não tem whodata), o ecrã mostra os instaladores interativos. Ao lado dos do whodata está o do Sysmon, **Instalador do Sysmon (opcional) — Windows (.ps1)**. Ao descarregá-lo, o SecVision mostra o SHA256, para o conferir na máquina com `Get-FileHash sysmon-preparar.ps1`. O instalador também fica no depósito da rede privada.

## 2. Instalar, com autorização

Na máquina, numa janela do PowerShell como administrador

```{figure} /_static/img/519-o-sysmon-a-parte/02.jpg
:alt: O inventário do instalador do Sysmon

O inventário, só com leituras.
```

Corra o instalador:

```powershell
.\sysmon-preparar.ps1
```

Primeiro o inventário, só com leituras: o Sysmon não está instalado, e o agente Wazuh ainda não lê o seu canal. Sem uma consola visível, o instalador recusa: não há opção para responder sim a tudo.

```{figure} /_static/img/519-o-sysmon-a-parte/03.jpg
:alt: Descarregar o Sysmon da Microsoft e conferir a assinatura

Descarregar e conferir.
```

A primeira pergunta: descarregar o Sysmon do site da Microsoft (`download.sysinternals.com`). Não vem com o SecVision: a licença não deixa redistribuí-lo. Antes de correr o que quer que seja, o instalador confere a **assinatura Authenticode**: tem de ser válida e emitida à Microsoft Corporation. Se não for, não instala nada.

```{figure} /_static/img/519-o-sysmon-a-parte/04.jpg
:alt: A configuração do Sysmon e a pergunta da licença

A configuração, à vista, e a licença.
```

A seguir, a configuração que vai ser instalada, à vista, e a pergunta: responder `s` aceita a licença da Sysinternals e instala o Sysmon (`Sysmon64.exe -accepteula -i`).

```{figure} /_static/img/519-o-sysmon-a-parte/05.jpg
:alt: O canal do Sysmon no agente Wazuh e o resumo

Enviar ao gestor, e o resumo.
```

Por fim, o canal do Sysmon (`Microsoft-Windows-Sysmon/Operational`) no agente Wazuh, para os eventos chegarem ao gestor: o instalador acrescenta ao `ossec.conf` um bloco assinado (`secvision:sysmon`), reinicia o agente e confirma no `ossec.log` que o canal é lido. Se não confirmar, tira o bloco.

O resumo diz como se desfaz:

1. `C:\Windows\Sysmon64.exe -u` desinstala o serviço e o controlador;
2. apague `C:\Windows\Sysmon64.exe`, que não se apaga a si próprio;
3. tire o bloco `secvision:sysmon` do `ossec.conf` e reinicie o agente (`net stop WazuhSvc` e `net start WazuhSvc`).

## 3. O evento, no Wazuh

Repetimos a ação suspeita da página {doc}`process-evidence-on-windows`: na sessão do administrador, um PowerShell lança uma linha de comandos que escreve no ficheiro `hosts`.

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/519-o-sysmon-a-parte/06.jpg
:alt: O evento 1 do Sysmon da linha de comandos no painel do Wazuh

O evento 1 do Sysmon, com o SHA256 e o identificador do processo pai.
```

```text
agent.name : "win10" and data.win.system.eventID : 1 and data.win.eventdata.image : *cmd.exe*
```

Uma regra de origem do Wazuh já o assinala (92004, «Powershell process spawned Windows command shell instance»). Além do que o 4688 já dizia, o evento traz:

- `data.win.eventdata.hashes`: o SHA256 do executável;
- `data.win.eventdata.parentProcessGuid`: o identificador do processo pai, o mesmo que identifica o PowerShell no seu próprio evento.

## O que fica de fora

```{figure} /_static/img/519-o-sysmon-a-parte/07.jpg
:alt: O que fica de fora

Os limites.
```

- Um Sysmon que já esteja instalado não é mexido: o instalador não o reinstala nem muda a configuração dele.
- Para uma versão nova, desinstala-se e corre-se o instalador outra vez. Este caminho ainda não foi medido.
- Para mudar a configuração, use `Sysmon64.exe -c` com o ficheiro que o instalador deixou em `ProgramData\SecVision`.
