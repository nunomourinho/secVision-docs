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

1. **Pesquisar:** Pesquisa nos artigos.
2. **Filtrar por feed:** Apresenta apenas os artigos de uma fonte.
3. Opção **Mostrar arquivados:** Apresenta novamente os artigos arquivados.
4. Botão **Adicionar a um relatório de recomendações:** Associa o artigo a um relatório novo ou existente, onde são redigidas as recomendações de mitigação e associados os sistemas do catálogo afetados ({doc}`/wazuh/software-and-cve-search`).
5. Botão **Arquivar:** Retira o artigo da lista do utilizador; os restantes utilizadores continuam a visualizá-lo.

## Resumo

- Centraliza a leitura dos alertas de todas as fontes.
- Os artigos relevantes são encaminhados para um relatório de recomendações, associado aos sistemas afetados.
