# Wazuh Cheat Sheet

Referência rápida de comandos, ficheiros e configurações do Wazuh, para os casos em que uma regra gerada pela plataforma necessita de ajuste manual.

```{video} 358-wazuh-cheat-sheet
```

## Acesso

**Proteger** > **SOC** > **Wazuh Cheat Sheet**

```{figure} /_static/capturas/wazuh-cheatsheet/menu.jpg
:alt: Menu lateral: Proteger > SOC > Wazuh Cheat Sheet

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

Este ecrã não constitui um passo obrigatório do SGSI. Destina-se às intervenções diretas no Wazuh: teste de uma regra, consulta de um ficheiro de configuração ou reinício do gestor.

## Configuração do ecrã

```{figure} /_static/capturas/wazuh-cheatsheet/separadores-1.jpg
:alt: Os separadores da cheat sheet e o botão de copiar

Os separadores da cheat sheet e o botão de copiar.
```

No ecrã, encontra os seguintes elementos:

1. Separador **Comandos:** Gestor, agente, *indexer* e *dashboard*, reinício completo do *stack*, teste de regras com o `wazuh-logtest`, validação da configuração, *cluster*, FIM, *rootcheck* e estatísticas.
2. Separador **Ficheiros:** Localização de cada configuração.
3. Separador **Integrações:** API do Wazuh, teste da ligação e obtenção do *token*.
4. Separador **Regras & Decoders:** Fluxo de processamento, estrutura de decoders e regras e exemplos comentados.
5. Separador **Boas Práticas.**
6. Separador **Troubleshooting.**
7. Botão **Copiar:** Copia o comando correspondente; cada comando tem o seu botão.

## Regras e decoders

```{figure} /_static/capturas/wazuh-cheatsheet/regras-2.jpg
:alt: O separador Regras & Decoders

O separador **Regras & Decoders**.
```

Fluxo recomendado para uma nova regra:

1. Obter um *log* bruto real.
2. Criar o *decoder*, que extrai os campos do *log* (`srcip`, `username`, `action`…).
3. Testar com o `wazuh-logtest`.
4. Criar a regra, que avalia os campos e gera um alerta com um nível de severidade.
5. Testar novamente.
6. Validar o XML com o `xmllint`.
7. Reiniciar o gestor e confirmar os alertas.

O separador inclui também a tabela dos níveis de severidade, de 0 (ignorar, nunca gera alerta) a 12 ou superior (ataques confirmados).

```{important}
**Não edite `/var/ossec/ruleset/`:** estes ficheiros são substituídos nas atualizações. As regras e os decoders próprios devem ser guardados em `/var/ossec/etc/rules/` e `/var/ossec/etc/decoders/`.
```

## Resumo

- Referência dos comandos e ficheiros do Wazuh, com um botão para copiar cada comando.
- Para a edição de regras, ver também {doc}`/wazuh/detection-rules` e {doc}`/wazuh/ai-classification-and-studio`.
