# Instalar os agentes do Wazuh

O que o agente faz numa máquina e porque se instala endurecido; o gerador de scripts do SecVision (gestor, portas, versão, políticas de confiança zero), a fila dos sistemas em GAP, e o assistente do próprio Wazuh, lado a lado; e onde a máquina aparece depois de instalada.

```{video} 502-instalar-os-agentes
```

No página anterior vimos máquinas monitorizadas e máquinas em GAP. Neste vemos como se fecha um GAP: instalando o agente do Wazuh, com o script que o SecVision gera, e o que o próprio Wazuh oferece.

## Onde fica no menu

**Menu:** Proteger › Soc › Wazuh Agent Builder

```{figure} /_static/capturas/wazuh-agentes/menu.jpg
:alt: Menu lateral: Proteger › Soc › Wazuh Agent Builder

O caminho no menu lateral: Proteger › Soc › Wazuh Agent Builder.
```

1. No menu lateral, abra **Proteger**.
2. Dentro dele, abra **Soc**.
3. Clique em **Wazuh Agent Builder**: abre o ecrã desta página.

## O conceito

O agente corre com privilégios elevados em todas as máquinas. É o que lhe permite ler os registos e o inventário, e é também o que o torna perigoso se estiver mal configurado.

Por omissão, o gestor pode mandar o agente executar comandos, mudar a sua configuração, ou atualizá-lo sozinho. Quem tomar o gestor toma todas as máquinas. A instalação de confiança zero corta isso: o agente só envia dados, não recebe ordens, e só fala com o gestor.

**Porque é que o agente se instala endurecido**

- O agente corre com privilégios elevados em cada máquina: é uma porta de entrada, se for mal configurado.
- Por omissão, o gestor pode mandar o agente executar comandos e atualizar-se sozinho.
- Confiança zero: o agente só envia dados, não recebe ordens, e só fala com o gestor.

## O gerador

**Menu:** Proteger › SOC › Wazuh Agent Builder

No Wazuh Agent Builder diz-se onde está o gestor: o endereço, aqui um de exemplo, e as duas portas, a 1514 para os eventos e a 1515 para o registo do agente.

E a versão do agente. Tem de ser a do gestor, ou mais antiga: um agente mais novo do que o gestor não se liga. O gestor deste ambiente está na 4.14.10, e é essa que se escreve. A configuração fica guardada sozinha.

```{figure} /_static/capturas/wazuh-agentes/builder-1.jpg
:alt: Proteger › SOC › Wazuh Agent Builder

O ecrã em Proteger › SOC › Wazuh Agent Builder.
```

1. **O endereço do gestor**
2. **1514 eventos · 1515 registo**
3. Escreva «4.14.10» neste campo.
4. **A versão do gestor, ou mais antiga**

**Menu:** Wazuh Agent Builder › Políticas Zero-Trust

Em baixo, as políticas de confiança zero, cada uma com o efeito escrito ao lado: bloquear os comandos remotos, desligar as atualizações pelo gestor e as respostas ativas, blindar as permissões dos ficheiros do agente, e a firewall do agente, que só o deixa falar com o gestor.

Sai um script por sistema operativo: Windows, as versões antigas de Windows Server, e Linux. O script descarrega o pacote oficial do Wazuh, instala-o, e aplica as políticas escolhidas.

```{figure} /_static/capturas/wazuh-agentes/zerotrust-1.jpg
:alt: Wazuh Agent Builder › Políticas Zero-Trust

O ecrã em Wazuh Agent Builder › Políticas Zero-Trust (1 de 3).
```

1. **O gestor não manda executar nada**

```{figure} /_static/capturas/wazuh-agentes/zerotrust-2.jpg
:alt: Wazuh Agent Builder › Políticas Zero-Trust

O ecrã em Wazuh Agent Builder › Políticas Zero-Trust (2 de 3).
```

1. **Só fala com o gestor**
2. Clique em **Linux — Debian/Ubuntu/RHEL (.sh)**.

```{figure} /_static/capturas/wazuh-agentes/zerotrust-3.jpg
:alt: Wazuh Agent Builder › Políticas Zero-Trust

O ecrã em Wazuh Agent Builder › Políticas Zero-Trust (3 de 3).
```

1. **Um script por sistema operativo**

## A fila

**Menu:** Proteger › Instalar agente Wazuh

A fila de integração mostra os sistemas em âmbito sem agente, por ordem: primeiro a criticidade, depois a exposição, depois os dias em GAP. Neste ambiente são três máquinas Windows.

Iniciar Integração abre o script já escolhido para o sistema operativo que o catálogo diz, com os valores do gerador. É este que se entrega a quem administra a máquina, com as credenciais dela: a plataforma não instala nada sozinha.

```{figure} /_static/capturas/wazuh-agentes/fila-1.jpg
:alt: Proteger › Instalar agente Wazuh

O ecrã em Proteger › Instalar agente Wazuh (1 de 3).
```

```{figure} /_static/capturas/wazuh-agentes/fila-2.jpg
:alt: Proteger › Instalar agente Wazuh

O ecrã em Proteger › Instalar agente Wazuh (2 de 3).
```

1. **Criticidade, exposição, dias em GAP**
2. Clique em **Iniciar Integração**.

```{figure} /_static/capturas/wazuh-agentes/fila-3.jpg
:alt: Proteger › Instalar agente Wazuh

O ecrã em Proteger › Instalar agente Wazuh (3 de 3).
```

1. **O sistema operativo do catálogo**

## No Wazuh

**Menu:** Wazuh › Endpoints › Deploy new agent

O próprio Wazuh também tem um assistente, no painel dele: escolhe-se o pacote, aqui Debian, e o endereço do gestor, e ele dá o comando de instalação, com a mesma versão.

A diferença está no que vem depois. O comando do Wazuh instala o agente com a configuração de origem; o script do SecVision instala o mesmo pacote oficial e endurece-o. Os dois servem, mas só um fecha as portas que o agente abre por omissão.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-1.jpg
:alt: Wazuh › Endpoints › Deploy new agent

O ecrã em Wazuh › Endpoints › Deploy new agent (1 de 3).
```

1. Clique em **DEB amd64**.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-2.jpg
:alt: Wazuh › Endpoints › Deploy new agent

O ecrã em Wazuh › Endpoints › Deploy new agent (2 de 3).
```

1. Escreva «10.0.0.50» no campo **Server address**.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-3.jpg
:alt: Wazuh › Endpoints › Deploy new agent

O ecrã em Wazuh › Endpoints › Deploy new agent (3 de 3).
```

1. **O comando do próprio Wazuh**

**Menu:** Wazuh › Endpoints › Agents

Corrido o script, a máquina aparece aqui, na lista de agentes do Wazuh, ativa. Os agentes deste ambiente de testes foram instalados com o mesmo pacote oficial, um por máquina Linux do catálogo.

Falta o último passo, que é do SecVision: associar o agente ao sistema do catálogo. É o que tira o sistema do GAP, e tem o seu próprio página.

```{figure} /_static/capturas/wazuh-agentes/wazuh_agentes-1.jpg
:alt: Wazuh › Endpoints › Agents

O ecrã em Wazuh › Endpoints › Agents.
```

1. **Depois de instalado, aparece aqui**

## Resumo

A plataforma gera o script certo para cada máquina e diz por que ordem se instalam.

E não instala nada sozinha. Uma ferramenta de gestão com credenciais de administrador em todas as máquinas seria, ela própria, o maior risco da organização.

**O que a plataforma faz — e o que não faz**

- Gera o script de cada sistema operativo, com o gestor, a versão e as políticas de confiança zero.
- Ordena os sistemas em GAP pela criticidade, a exposição e os dias sem monitorização.
- Não instala nada: quem corre o script é uma pessoa, com as credenciais da máquina.
