# Servidores Windows antigos

O agente moderno do SecVision não corre num Windows anterior ao Server 2016. O caminho é uma **ponte**.

## Acesso

**Proteger** > **Instalar agente Wazuh** > **Iniciar Integração**, e **Rede VPN** > **Convites** > **Avançado**

## Porque não usam o comando único

- O agente do SecVision precisa do Windows Server 2016 ou mais recente.
- O comando único pede o PowerShell moderno e o protocolo TLS 1.2, que estes sistemas não têm.
- O Wazuh ainda tem um agente para eles (versão 4.3), mas esse agente não sabe entrar na rede privada.

## A ponte

Uma **ponte** é uma máquina Linux da mesma rede, com o agente do SecVision em modo ponte. Recebe a ligação do servidor antigo e leva-a pela rede privada até ao gestor. Instala-se em **Rede VPN** > **Convites** > **Avançado** > **Instalar numa máquina**: nome da máquina, **Esta máquina é uma ponte**, o endereço dela na rede local e as **origens permitidas** (sem origens não arranca, porque deixava qualquer máquina da rede usá-la).

## Em cada servidor antigo

1. Em **Iniciar Integração**, o separador do agente Wazuh propõe o script certo para o sistema operativo do catálogo: **Windows Server 2008 R2 (.bat)** (serve também o 2012 R2) ou **Windows Server 2003 (.bat)**.
2. O endereço do gestor que o script leva é o **da ponte**; define-se no Agent Builder.
3. No servidor, o script e o pacote do agente antigo (`wazuh-agent.msi`, 4.3.10) ficam na mesma pasta: estes sistemas não descarregam nada.
4. Corre-se o script. Atualiza os certificados, instala o agente, aplica as limitações do perfil e inicia o serviço.

## Sistemas em que foi provado

| Sistema | Estado |
|---|---|
| Windows Server 2012 R2 | Provado pela ponte: o agente fica Active no gestor. |
| Windows Server 2008 R2 | Provado pela ponte: o agente fica Active no gestor. |
| Windows Server 2003 R2 | Ligado uma vez em laboratório; **uma segunda instalação de ensaio não ficou ligada** (o pacote deixou o endereço do gestor a `0.0.0.0`): por esclarecer. |

## Limites

- Ligar um servidor antigo ao Wazuh dá visibilidade, não o torna seguro: estes sistemas já não recebem correções do fabricante, e o melhor é substituí-los.
- A ligação do agente ao sistema do catálogo faz-se à mão: o SecVision só liga sozinho os servidores instalados pelo comando único.
- O Linux muito antigo vai também pela ponte, mas não foi testado.
