# Instalar o agente num Windows Server

O mesmo comando único do Linux, agora em PowerShell, a partir do catálogo de segurança.

## Acesso

**Proteger** > **Instalar agente Wazuh** > **Iniciar Integração** > **Rede VPN**

## O que muda num Windows

- Abre-se o **PowerShell como administrador**, em vez do terminal do Linux.
- O comando é uma linha de PowerShell. A primeira parte instala uma verificação: o PowerShell só aceita o certificado do depósito se a sua impressão digital for a que o SecVision registou.
- O guião descarrega o executável do agente do SecVision e confere-o (sha256) antes de o correr. O agente entra na rede privada, descarrega o pacote oficial do Wazuh (`.msi`), confere-o e instala-o.
- O agente aponta o gestor a `127.0.0.1`: o servidor não abre nenhuma porta de entrada.

## Sistemas em que foi provado

| Sistema | Estado |
|---|---|
| Windows Server 2019, 2022 e 2025 | Provado: o agente fica Active no gestor. |
| Windows Server 2016, Windows 10 e Windows 11 | Mesmo comando, **não testado**. |
| Windows anteriores ao Server 2016 | Não correm o agente: o guião recusa-os com a razão. Ver [Servidores Windows antigos](legacy-servers.md). |

## 1. Gerar o comando

1. Na fila de integração, **Iniciar Integração** no sistema (por exemplo, um Windows Server 2022).
2. No separador **Rede VPN**, confirme o nome do servidor e o **Sistema do servidor** (**Windows Server 2016 ou mais recente**, proposto pelo catálogo).
3. Escolha o **Perfil do agente**.
4. **Gerar o comando**. Vale uma hora e serve para um só servidor.

## 2. Correr no servidor

1. Abra o PowerShell como administrador.
2. Cole a linha e prima Enter.
3. O guião diz o que faz: a autoridade certificadora, o executável do agente, a entrada na rede privada, o pacote do Wazuh conferido, e por fim **agente Wazuh a correr, ligado ao gestor pela rede privada**.

## 3. Confirmar

- **Rede VPN** > **Máquinas**: o servidor aparece ligado, a reportar pela rede privada, com o agente ativo.
- **Wazuh Explorer**: o agente aparece com o nome do servidor, e o sistema do catálogo a que o SecVision o ligou sozinho.

## Limites

- Só um Windows Server 2016 ou mais recente corre o agente moderno.
- Na Rede VPN, a ligação do agente ao sistema do catálogo é automática (corre de dez em dez minutos, e nunca substitui uma ligação feita por uma pessoa); nos servidores antigos faz-se à mão.
