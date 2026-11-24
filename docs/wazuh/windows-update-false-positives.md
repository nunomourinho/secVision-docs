# Os falsos positivos do Windows Update

Uma atualização do Windows faz o Wazuh alertar nos binários do sistema que muda. Com o whodata, o alerta diz que foi o TiWorker do Windows Update; o modelo do ecrã de falsos positivos baixa esses alertas, ancorado ao caminho do TiWorker, e um programa falso com o mesmo nome continua a alertar.

```{video} 521-falsos-positivos-do-windows-update
```

A página {doc}`false-positives` mostra o ecrã de falsos positivos e a página {doc}`whodata` a receita para as atualizações em Linux (o `dpkg` a pedido do `apt`). Esta é a metade Windows: medida numa atualização cumulativa real num Windows 11, aplicada pelo ecrã de falsos positivos e provada num Windows 10 com o whodata, nas máquinas do laboratório e no Wazuh de teste.

## O conceito

Medimos uma atualização cumulativa real num Windows 11 (KB5132061, 24/11/2026): **11 alertas de integridade** (regra 550), em binários do sistema como `cmd.exe`, `lsass.exe`, `schtasks.exe` e `sethc.exe`. São os ficheiros que a configuração de origem do Wazuh vigia em `System32`, e são exatamente os que um atacante troca. Por isso **não se pode silenciar pelo nome do ficheiro**.

Com o whodata ligado, o alerta diz que processo escreveu. Os 11 foram escritos pelo mesmo: o **TiWorker.exe**, o processo da atualização do Windows, com o caminho completo, dentro da pasta `WinSxS` do Windows, onde só o próprio Windows escreve. É por aí que a regra separa as coisas:

```xml
<rule id="__RULE_ID__" level="1">
  <if_group>syscheck</if_group>
  <field name="process_name" type="pcre2">(?i)^c:\x5cwindows\x5cwinsxs\x5camd64_microsoft-windows-servicingstack_[a-z0-9._]+\x5ctiworker\.exe$</field>
  <description>FIM: alteração feita pelo TiWorker do Windows Update (servicing stack em WinSxS).</description>
</rule>
```

- A barra vai como `\x5c`: com `\\` o Wazuh trata as barras antes do pcre2 e a regra não casa (medido).
- O caminho é ancorado do princípio ao fim: um `TiWorker.exe` noutra pasta, como `C:\windows_winsxs\…`, que qualquer utilizador cria na raiz do C:, não casa.
- Nível 1 e não 0: o evento continua nos arquivos e conta no histórico.

## Informação a solicitar

| Informação | Responsável |
|---|---|
| Que servidores têm o whodata ligado | administrador de cada servidor |
| A autorização para mudar as regras do gestor Wazuh | responsável de cibersegurança |
| Quando correm as atualizações do Windows | administrador de sistemas |

O modelo só funciona nas máquinas com o whodata ligado, porque sem ele o alerta não diz o processo. Aplicar uma regra muda o gestor Wazuh de todos.

## 1. O alerta, no Wazuh

**Wazuh** > **Threat Hunting** > **Events**

```{figure} /_static/img/521-falsos-positivos-do-windows-update/01.jpg
:alt: Alertas de integridade do Windows 11 escritos pelo TiWorker

Os alertas da atualização cumulativa, no painel do Wazuh.
```

No painel do Wazuh, procure os alertas de integridade da máquina escritos pelo TiWorker:

```text
rule.groups : syscheck and agent.name : "win11" and syscheck.audit.process.name : *TiWorker*
```

```{figure} /_static/img/521-falsos-positivos-do-windows-update/02.jpg
:alt: O processo que escreveu, com o caminho completo

O processo que escreveu, com o caminho completo, dentro do WinSxS.
```

Abra um deles: o campo `syscheck.audit.process.name` tem o processo que escreveu, com o caminho completo. No separador **JSON**, copie o documento do alerta.

## 2. A regra, no SecVision

**Proteger** > **SOC** > **Falsos Positivos**

```{figure} /_static/img/521-falsos-positivos-do-windows-update/03.jpg
:alt: O alerta colado no ecrã de falsos positivos

O alerta colado: a regra 550, um ficheiro que mudou.
```

Cole o alerta. A plataforma lê a regra que disparou: a **550**, um ficheiro que mudou.

```{figure} /_static/img/521-falsos-positivos-do-windows-update/04.jpg
:alt: O modelo FIM Windows Update (TiWorker)

O modelo da atualização do Windows.
```

Não é preciso pedir a regra a ninguém: há modelos medidos no laboratório. Escolha **FIM: Windows Update (TiWorker)** e **Validar sintaxe**.

```{figure} /_static/img/521-falsos-positivos-do-windows-update/05.jpg
:alt: Testar permissões e aplicar

Testar as permissões e aplicar.
```

Escolha **Testar permissões** e **Aplicar ao Wazuh**.

```{figure} /_static/img/521-falsos-positivos-do-windows-update/06.jpg
:alt: A regra a ser aplicada

A plataforma guarda uma cópia das regras, escreve a nova, valida-a e reinicia o gestor.
```

A plataforma guarda uma cópia das regras, escreve a nova, valida-a no próprio gestor e reinicia-o.

```{figure} /_static/img/521-falsos-positivos-do-windows-update/07.jpg
:alt: Regra aplicada

Regra aplicada.
```

## 3. O efeito, no Wazuh

Para ver o efeito, fizemos duas coisas num Windows 10 com o whodata ligado:

- o Windows ligou uma funcionalidade (o Telnet Client), e o TiWorker verdadeiro escreveu um binário novo em `System32` (`telnet.exe`, que a configuração de origem vigia: o `net.exe$` casa pelo fim do nome);
- um programa falso, também chamado `TiWorker.exe`, mas numa pasta fora do `WinSxS`, escreveu no ficheiro `hosts`.

```{figure} /_static/img/521-falsos-positivos-do-windows-update/08.jpg
:alt: Um só alerta de integridade nos minutos seguintes, o do TiWorker falso

Nos minutos seguintes, um só alerta: o do TiWorker falso.
```

De volta ao Wazuh, nos minutos seguintes, nesse Windows 10, há **um só alerta de integridade**. A escrita do TiWorker verdadeiro já não alerta: a regra baixou-a a nível 1, abaixo do limiar dos alertas, e fica só nos arquivos. Aplicar a regra reinicia o gestor: os eventos dessa janela podem chegar com uns minutos de atraso, quando o agente volta a ligar-se. O alerta que ficou é o do programa falso: o nome é TiWorker, mas o caminho não é o do Windows.

## O que fica de fora

```{figure} /_static/img/521-falsos-positivos-do-windows-update/09.jpg
:alt: O que fica de fora

Os limites do modelo.
```

- Só funciona nas máquinas com o whodata: sem ele, o alerta não diz o processo.
- O que a própria atualização do Windows trouxer passa, como numa atualização em Linux: o modelo separa quem escreveu, não o que foi escrito.
- As instalações pelo instalador de programas do Windows (`msiexec`) não são cobertas por este modelo: continuam a alertar.
