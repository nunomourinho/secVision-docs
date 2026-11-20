# Integração VirusTotal

Ligação ao VirusTotal, para verificar o que os motores antivírus dizem dos instaladores do agente publicados no depósito da rede privada. A consulta é feita só pelo `sha256` de cada ficheiro; o ficheiro só sai do servidor quando um administrador decide enviá-lo.

## Acesso

**Governar** > **Administração do sistema** > **Integrações** > **VirusTotal**

```{figure} /_static/capturas/adm-virustotal/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Integrações > VirusTotal

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Configuração do ecrã

```{figure} /_static/capturas/adm-virustotal/chave-1.jpg
:alt: A configuração da chave de API do VirusTotal

A configuração da chave de API do VirusTotal.
```

No ecrã, encontra os seguintes elementos:

1. **Integração activa:** Quando desativada, a coluna **VirusTotal** do instalador do agente deixa de consultar o serviço.
2. **Chave de API:** Obtém-se no site do VirusTotal, no perfil do utilizador, em **API Key**. Depois de guardada, deixa de ser apresentada. Para a substituir, escreva a nova; o campo vazio mantém a chave guardada.
3. Botão **Guardar:** Regista a chave escrita.
4. Botão **Testar ligação:** Guarda a chave escrita e pergunta ao VirusTotal pelo ficheiro de teste EICAR, que todos os antivírus conhecem, confirmando a validade da chave.

**Como configurar:** Escreva a chave de API, clique em **Guardar** e confirme a ligação com **Testar ligação**.

## O que sai do servidor

- **Consultar** envia apenas o `sha256` do ficheiro. Nenhum ficheiro sai do servidor.
- **Enviar ficheiro** é um gesto separado, só para administradores, e pede confirmação: um ficheiro enviado ao VirusTotal fica disponível aos subscritores do serviço. É o caso habitual do executável `secvision-agente`, que é compilado na instalação e por isso o VirusTotal não conhece.
- Só se envia a cópia que o servidor do SecVision tem e cujo `sha256` coincide com o registado. Um ficheiro registado à mão, de que o servidor não tenha cópia, não se envia.

## Resumo

- A chave fica cifrada e não volta a ser apresentada depois de guardada.
- A chave gratuita aceita 4 pedidos por minuto e 500 por dia, e os termos do VirusTotal não a permitem em uso comercial. Quando a quota se esgota, a plataforma indica-o e para; não repete sozinha.
- Na instalação de teste a consulta é recusada: o VirusTotal é um serviço externo e não há um segundo para onde a apontar.
- Ver também {doc}`/wazuh/connect-a-server`, secção «Verificar os instaladores no VirusTotal».
