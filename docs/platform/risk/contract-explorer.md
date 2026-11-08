# Importar contratos públicos

O explorador de contratos públicos: carregamento dos ficheiros exportados do BASE.gov, seleção da própria entidade e importação dos contratos relevantes.

```{video} 355-importar-contratos-publicos
```

## Acesso

**Identificar** > **Fornecedores e Contratos** > **Importar contratos**

```{figure} /_static/capturas/contratos-explorador/menu.jpg
:alt: Menu lateral: Identificar > Fornecedores e Contratos > Importar contratos

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

**Esta importação deve preceder o registo de fornecedores.** As entidades com contratos públicos devem começar por este ecrã, reduzindo o registo manual: os fornecedores podem depois ser propostos a partir dos contratos ({doc}`suppliers`).

## Ficheiros de entrada

São importados ficheiros JSON exportados do **BASE.gov**, o portal dos contratos públicos, de dois tipos: um ficheiro `entidades.json` com a lista de entidades adjudicantes e um ou mais ficheiros de contratos, anúncios ou modificações.

```{note}
**A plataforma não estabelece ligação ao BASE.gov.** Não existe ligação externa: os ficheiros são exportados do portal e carregados manualmente. Não existe opção de sincronização.
```

## Procedimento

```{figure} /_static/capturas/contratos-explorador/entidades-1.jpg
:alt: O primeiro passo: carregar as entidades

Primeiro passo: carregamento das entidades.
```

No ecrã, encontra os seguintes elementos:

1. **Passo 1:** Carregamento das entidades.
2. Botão **Importar entidades.json:** Carrega o ficheiro de entidades.

O ecrã avança automaticamente pelos três passos:

1. **Carregar entidades:** Carregue o ficheiro `entidades.json`.
2. **Selecionar as entidades alvo:** Normalmente, apenas a própria instituição e os organismos dela dependentes. Este passo define o filtro: o cartão «arquivos processados» indica sempre os registos **lidos** e **extraídos**, e a diferença corresponde aos registos excluídos por não pertencerem às entidades selecionadas.
3. **Carregar os dados e selecionar:** Filtre por texto, adjudicatário, valor, data ou categoria técnica, assinale os registos pretendidos e clique em **importar para a base de dados**.

A categoria técnica é inferida da descrição e dos códigos CPV e tem apenas dois valores: **Software** e **Hardware**. Os registos que não correspondem a nenhum ficam sem categoria; esta ausência não constitui uma terceira categoria. A indicação **Eco** provém do próprio registo.

## Resultado

São gravados **apenas os registos selecionados**: os dados carregados no browser não são guardados, e a opção **Recomeçar** descarta todos os dados ainda não importados. A reimportação do mesmo ficheiro não gera duplicados: a chave é a referência e o tipo, e o ecrã indica o número de registos importados e ignorados por já existirem.

Os contratos gravados são posteriormente associados a sistemas do catálogo em **Governar** > **Contratos** > **Importados**. Esta associação responde a uma questão habitual nas auditorias: *qual o contrato que cobre este servidor, e até quando?* Ver {doc}`suppliers`.

## Resumo

- Os ficheiros são exportados manualmente do BASE.gov; a plataforma não estabelece ligações externas.
- As entidades são carregadas primeiro, seguidas dos contratos; apenas os registos selecionados são gravados.
- A reimportação não gera duplicados.
