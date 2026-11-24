# A evidência de processos no Windows

Quem executou cada processo, a partir de que processo e com que linha de comandos: o evento 4688 do próprio Windows, ligado pelo instalador interativo com autorização, e a cadeia de uma ação suspeita no painel do Wazuh, do ficheiro alterado ao processo que o lançou.

```{video} 518-a-evidencia-de-processos-no-windows
```

A página {doc}`whodata-on-windows` mostra o whodata, que diz que processo alterou cada ficheiro. Esta mostra a segunda parte do mesmo instalador interativo, a evidência de processos, num **Windows 10 22H2** com o agente do SecVision 0.5.9, e a cadeia que as duas formam no painel do Wazuh. Tudo foi feito em máquinas reais do laboratório e no Wazuh de teste.

## O conceito

O Windows regista no registo **Security** um evento por cada processo criado: o **4688**. Diz a conta que o executou, o executável, o processo pai e, se se pedir, a linha de comandos inteira.

O agente Wazuh já lê o registo Security. O que falta é a **política de auditoria**, que nos Windows 10 e 11 vem desligada. Não há nada a instalar: é o próprio Windows.

O instalador interativo (`secvision-agente whodata preparar`, ou o `whodata-preparar.ps1`) liga-a com o mesmo contrato do whodata:

- primeiro um inventário, só com leituras;
- uma pergunta por item, com o que faz, porquê e o comando exato; a resposta por omissão é «não»;
- antes de mudar, guarda uma cópia da política (`auditpol /backup`);
- no fim, o resumo diz o que mudou e o comando `auditpol /restore` que repõe a política de antes.

São dois itens, perguntados à parte:

| Item | O que muda |
|---|---|
| Auditar a criação de processos | a subcategoria **Process Creation** (`{0CCE922B-69AE-11D9-BED3-505054503030}`), sucessos |
| Incluir a linha de comandos | a chave `ProcessCreationIncludeCmdLine_Enabled = 1` em `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit` |

## Informação a solicitar

| Informação | Responsável |
|---|---|
| A autorização para mudar a política de auditoria da máquina | administrador da máquina |
| Se a linha de comandos pode ir para o gestor (pode levar palavras-passe) | responsável de cibersegurança e encarregado de proteção de dados |
| Se uma GPO do domínio define a auditoria | administrador do domínio |

A linha de comandos merece uma decisão à parte: tudo o que se escrever nela, incluindo palavras-passe passadas como argumento, vai para o gestor.

## 1. Ligar a evidência

Na máquina, numa janela do PowerShell como administrador

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/01.jpg
:alt: O instalador interativo a arrancar num Windows 10

O instalador interativo, num PowerShell como administrador.
```

Neste Windows 10 o agente já está instalado e o whodata já está ligado. Corra:

```powershell
& 'C:\Program Files\SecVision\secvision-agente.exe' whodata preparar
```

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/02.jpg
:alt: O inventário da evidência de processos

O inventário: o que falta.
```

O whodata está pronto, e o instalador passa à segunda parte: a evidência de processos. O inventário diz o que falta: a subcategoria de criação de processos e a linha de comandos.

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/03.jpg
:alt: A pergunta sobre a criação de processos

Uma pergunta por item.
```

A primeira pergunta: auditar a criação de processos. Diz o que faz, porquê, e o comando exato. Antes de mudar, guarda uma cópia da política. Responda `s`.

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/04.jpg
:alt: A pergunta sobre a linha de comandos

A linha de comandos, à parte.
```

A segunda: incluir a linha de comandos. O aviso está na própria pergunta: o que se escrever na linha de comandos vai para o gestor. Responda `s` só se foi autorizado.

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/05.jpg
:alt: O resumo com o comando auditpol /restore

O resumo.
```

O resumo diz o que mudou, e o comando `auditpol /restore` que repõe a política de antes.

## 2. A cadeia, no Wazuh

Para ver o efeito, fizemos o que um atacante faz muitas vezes: na sessão do administrador, um PowerShell lançou uma linha de comandos (`cmd.exe`) que acrescentou uma linha ao ficheiro `hosts`, para desviar um nome.

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/06.jpg
:alt: Os eventos 4688 da linha de comandos no painel do Wazuh

Os eventos 4688 da linha de comandos.
```

No painel do Wazuh, procure os eventos 4688 da máquina em que o processo criado é a linha de comandos:

```text
agent.name : "win10" and data.win.system.eventID : 4688 and data.win.eventdata.newProcessName : *cmd.exe*
```

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/07.jpg
:alt: A conta, o processo pai, a linha de comandos e o número do processo

No evento: quem, a partir de que processo, com que comando.
```

No evento:

- `data.win.eventdata.commandLine`: a linha de comandos inteira, com o que foi escrito no `hosts`;
- `data.win.eventdata.parentProcessName`: o processo pai, o PowerShell;
- `data.win.eventdata.subjectUserName`: a conta que o executou;
- `data.win.eventdata.newProcessId`: o número do processo novo, que o Windows escreve em hexadecimal (no laboratório, `0x1424`). É ele que liga este evento ao alerta de integridade.

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/08.jpg
:alt: O alerta de integridade do hosts com o mesmo número de processo

O alerta de integridade do hosts, com o mesmo número de processo.
```

E o alerta de integridade do ficheiro `hosts`:

```text
rule.groups : syscheck and agent.name : "win10" and syscheck.path : *hosts*
```

O whodata diz o processo que o escreveu (`syscheck.audit.process.name`) e o mesmo número de processo (`syscheck.audit.process.id`), aqui em decimal (`5156`, que é `0x1424`). Do ficheiro alterado chega-se a quem o lançou, e com que comando.

## O que fica de fora

```{figure} /_static/img/518-a-evidencia-de-processos-no-windows/09.jpg
:alt: O que fica de fora

Os limites.
```

- Cada processo criado gera um alerta no Wazuh (regra 67027, nível 3): num computador de utilizador, dezenas por minuto. Baixá-lo é uma decisão no ecrã de falsos positivos ({doc}`false-positives`); o evento continua nos arquivos.
- O número do processo repete-se ao longo do tempo: liga eventos próximos, não de dias diferentes.
- Para o SHA256 do executável e uma cadeia que não dependa do número do processo, há o Sysmon, à parte: {doc}`sysmon`.
