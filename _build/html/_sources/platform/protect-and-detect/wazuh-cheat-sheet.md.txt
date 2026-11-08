# Wazuh Cheat Sheet

A referência rápida de comandos, ficheiros e configurações do Wazuh, para quando uma regra gerada pela plataforma precisa de ser mexida à mão.

```{video} 358-wazuh-cheat-sheet
```

## Onde fica no menu

**Menu:** Proteger › SOC › Wazuh Cheat Sheet

```{figure} /_static/capturas/wazuh-cheatsheet/menu.jpg
:alt: Menu lateral: Proteger › SOC › Wazuh Cheat Sheet

O caminho no menu lateral: Proteger › SOC › Wazuh Cheat Sheet.
```

1. No menu lateral, abra **Proteger**.
2. Dentro dele, abra **SOC**.
3. Clique em **Wazuh Cheat Sheet**: abre o ecrã desta página.


Não é um passo obrigatório do SGSI. Está aqui porque é onde se trabalha quando é preciso ir ao próprio Wazuh: testar uma regra, ver um ficheiro de configuração, reiniciar o gestor.

## O ecrã

```{figure} /_static/capturas/wazuh-cheatsheet/separadores-1.jpg
:alt: Os separadores da cheat sheet e o botão de copiar

Os separadores da cheat sheet e o botão de copiar.
```

1. **Comandos**
2. **Ficheiros**
3. **Integrações**
4. **Regras & Decoders**
5. **Boas Práticas**
6. **Troubleshooting**
7. **Copiar o comando**


Cada separador agrupa um tema:

- **Comandos:** gestor, agente, *indexer* e *dashboard*, o reinício completo do *stack*, testar regras com o `wazuh-logtest`, validar a configuração, *cluster*, FIM, *rootcheck* e estatísticas;
- **Ficheiros:** onde está cada configuração;
- **Integrações:** a API do Wazuh, como testar a ligação e obter o *token*;
- **Regras & Decoders:** o fluxo de processamento, a estrutura de decoders e regras, e exemplos comentados;
- **Boas Práticas** e **Troubleshooting**.

Cada comando tem o seu botão **Copiar**.

## Regras e decoders

```{figure} /_static/capturas/wazuh-cheatsheet/regras-2.jpg
:alt: O separador Regras & Decoders

O separador Regras & Decoders.
```


O fluxo recomendado para uma regra nova:

1. Obter um *log* bruto real.
2. Criar o *decoder*, que extrai os campos do *log* (`srcip`, `username`, `action`…).
3. Testar com o `wazuh-logtest`.
4. Criar a regra, que avalia os campos e gera um alerta com um nível de severidade.
5. Testar novamente.
6. Validar o XML com o `xmllint`.
7. Reiniciar o gestor e confirmar os alertas.

Ao lado está a tabela dos níveis de severidade, de 0 (ignorar, nunca gera alerta) a 12 ou mais (ataques confirmados).

```{important}
**Nunca edite `/var/ossec/ruleset/`:** esses ficheiros são substituídos nas atualizações. As regras e os decoders próprios vão sempre para `/var/ossec/etc/rules/` e `/var/ossec/etc/decoders/`.
```

## Resumo

- A referência dos comandos e ficheiros do Wazuh, com um botão para copiar cada um.
- Para mexer em regras, ver também {doc}`/wazuh/detection-rules` e {doc}`/wazuh/ai-classification-and-studio`.
