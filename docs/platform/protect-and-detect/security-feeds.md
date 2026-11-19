# Feeds de segurança

Centralização das notícias e alertas de cibersegurança das fontes configuradas: leitura, arquivo dos artigos não relevantes e encaminhamento dos relevantes para um relatório de recomendações.

```{video} 357-feeds-de-seguranca
```

## Acesso

**Detetar** > **IOC & Intelligence** > **Feeds de Segurança**

```{figure} /_static/capturas/feeds-seguranca/menu.jpg
:alt: Menu lateral: Detetar > IOC & Intelligence > Feeds de Segurança

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Fontes

Os artigos provêm dos feeds RSS configurados pelo administrador em {doc}`/platform/administration/rss-feeds`, como o CERT.PT, a CISA, o SANS ISC e outras fontes adicionadas.

## Configuração do ecrã

```{figure} /_static/capturas/feeds-seguranca/artigos-1.jpg
:alt: Os artigos, com a pesquisa, o filtro por feed e as ações de cada artigo

Os artigos, com a pesquisa, o filtro por feed e as ações de cada artigo.
```

No ecrã, encontra os seguintes elementos:

1. **Pesquisar:** Pesquisa no título, no conteúdo e no nome da fonte de cada artigo.
2. **Filtrar por feed:** Apresenta apenas os artigos de uma fonte.
3. Opção **Mostrar arquivados:** Apresenta novamente os artigos arquivados, com a data e o motivo do arquivo.
4. Opção **Só com data suspeita:** Apresenta apenas os artigos com a data assinalada (ver abaixo).
5. **Caixa de seleção** de cada artigo: As ações seguintes aplicam-se a vários artigos de uma vez, na barra que aparece por cima da lista (**Adicionar a um relatório…**, **Arquivar…**, **Limpar seleção**).
6. Botão **Adicionar a um relatório de recomendações:** Associa o artigo (ou os selecionados) a um relatório novo ou existente, onde são redigidas as recomendações de mitigação e associados os sistemas do catálogo afetados ({doc}`/wazuh/software-and-cve-search`). Depois, o artigo mostra **Em relatório** (ou **Em N relatórios**), com a ligação.
7. Botão **Arquivar:** Retira o artigo da lista do utilizador; os restantes utilizadores continuam a visualizá-lo. O **motivo é obrigatório** e fica na trilha de auditoria.

## Datas suspeitas

Algumas fontes publicam avisos novos com uma data antiga. Numa lista ordenada por data, esses avisos ficam por baixo de outros já lidos. O ecrã assinala-os, sem mudar a ordem:

- **Data anterior ao mais recente:** o artigo foi recebido depois de outro do mesmo canal, mas tem uma data mais de 24 horas anterior à desse;
- **Data no futuro:** a data de publicação está mais de 24 horas à frente do momento em que foi recebido.

Quando há artigos assim nos últimos 30 dias, um aviso no topo diz quantos são, com o botão **Ver só esses**. Um canal que volte de uma avaria com artigos antigos legítimos também é assinalado: o destaque mostra a data de referência, para se perceber porquê.

## Arquivar com motivo

O motivo escolhe-se de uma lista:

- A tecnologia a que o feed se refere não está presente na organização.
- Assunto já tratado ou mitigado na organização.
- Duplicado de outro feed já analisado.
- Fora do âmbito do SGSI.
- Sem relevância para a segurança da organização.
- Outro motivo (descrever) — obriga a uma descrição.

Os outros motivos aceitam um complemento, por exemplo a tecnologia em causa. Os artigos arquivados antes desta funcionalidade aparecem com «sem motivo registado».

## No relatório

Um relatório pode reunir vários feeds. Dentro do relatório, a ordem dos feeds muda-se com as setas **Subir** e **Descer**, e a pesquisa de relatórios encontra também o texto dos feeds ligados.

## Resumo

- Centraliza a leitura dos alertas de todas as fontes, e assinala as datas suspeitas.
- Os artigos relevantes são encaminhados, um a um ou vários de uma vez, para um relatório de recomendações, associado aos sistemas afetados.
- O que não interessa arquiva-se, sempre com o motivo, registado na trilha de auditoria.
- Um pedido que falhe é dito como erro, com o código HTTP e **Tentar de novo**, e nunca como «Sem artigos».
