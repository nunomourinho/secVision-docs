# Anonimização de IA

Registo de todos os pedidos enviados da plataforma para serviços de IA e bancada de ensaio para verificar, com um texto real, o conteúdo que seria enviado.

```{video} 352-anonimizacao-de-ia
```

## Acesso

**Governar** > **Administração do sistema** > **Anonimização de IA**

```{figure} /_static/capturas/adm-anonimizador/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Anonimização de IA

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Funcionamento

Os assistentes de IA da plataforma (falsos positivos, regras de deteção, conformidade, documentos) geram um *prompt* que o utilizador cola no serviço de IA que utiliza. Antes do envio, endereços, nomes e identificadores são substituídos por etiquetas (`[IP_1]`, `[PESSOA_1]`), que são repostas na resposta. **A anonimização não pode ser desativada** e nenhum caminho da API devolve o texto original. Este ecrã permite verificar o funcionamento da anonimização.

## Registo de saídas

```{figure} /_static/capturas/adm-anonimizador/registo-1.jpg
:alt: O registo de saídas para IA, com os filtros e as contagens

O registo de saídas para IA, com os filtros e as contagens.
```

No ecrã, encontra os seguintes elementos:

1. **Registo de saídas:** Lista dos *prompts* enviados.
2. **Período:** Filtro por intervalo de datas.
3. **Fluxo de IA:** Filtro por assistente de origem.
4. Botão **Exportar:** Exporta o registo em CSV, XLSX ou DOCX.
5. **Categorias:** Contagem dos valores substituídos, por categoria.

Cada linha corresponde a um *prompt* enviado e indica a data, o utilizador, o fluxo e o número de valores substituídos por categoria. A exportação em CSV, XLSX ou DOCX serve de evidência para auditoria.

## Bancada de ensaio

```{figure} /_static/capturas/adm-anonimizador/bancada-2.jpg
:alt: A bancada de ensaio: o estado das camadas e o texto a experimentar

A bancada de ensaio: o estado das camadas e o texto a ensaiar.
```

No ecrã, encontra os seguintes elementos:

1. **Camadas:** Estado das quatro camadas de anonimização.
2. Botão **Verificar camadas:** Verifica a disponibilidade de cada camada.
3. **Texto a ensaiar:** Campo para colar o texto de teste.
4. Botão **Mascarar:** Apresenta o texto que seria enviado.
5. **As minhas listas de termos:** Termos que o utilizador define como sempre visíveis ou sempre mascarados.

**Como ensaiar:** Cole um alerta real ou um excerto de um documento e clique em **Mascarar**. A bancada apresenta o texto que seria enviado, a tabela de conversão (por exemplo, a que endereço corresponde `[IP_1]`), os valores mantidos em claro e o respetivo motivo, e a camada que detetou cada valor. As listas de termos aplicam-se apenas aos *prompts* do próprio utilizador.

**Diagnóstico:** O painel das camadas indica se as quatro camadas estão disponíveis ou identifica a camada em falta. Se faltar uma camada obrigatória, **nenhum *prompt* é gerado** em toda a plataforma; é essa a causa de um erro 503 nos assistentes de IA.

## Exemplo completo de um pedido

O vídeo apresenta o ciclo completo de um pedido, processado por um modelo de IA real.

```{figure} /_static/img/352-anonimizacao-de-ia/05.jpg
:alt: Copiar o que sairia da plataforma

Cópia do texto que seria enviado, já pseudonimizado.
```

O texto é colado num assistente de IA. Máquinas, pessoa, telefones, endereço e número de contribuinte seguem como etiquetas. Apenas o correio eletrónico da pessoa segue em claro, por pertencer a um domínio de documentação configurado como exceção, conforme indicado previamente pela bancada.

```{figure} /_static/img/352-anonimizacao-de-ia/06.jpg
:alt: O pedido pseudonimizado, colado no assistente de IA

O pedido colado no assistente de IA. A janela foi criada para o vídeo; o pedido e a resposta são reais, processados por um modelo de IA.
```

A resposta analisa o alerta e propõe passos, referindo-se sempre às etiquetas (`[IP_1]`, `[PESSOA_1]`). A resposta identifica também o correio eletrónico enviado em claro e recomenda mascará-lo. A resposta é então copiada.

```{figure} /_static/img/352-anonimizacao-de-ia/07.jpg
:alt: A resposta do assistente, com as etiquetas

A resposta real do modelo, ainda com as etiquetas.
```

Na bancada, cole a resposta no campo de **reversão** e clique em **Reverter**. A resposta é apresentada com os valores reais repostos: endereço, máquinas, pessoa e telefone. Os assistentes da plataforma (falsos positivos, regras de deteção, classificação de alertas, documentos do SGSI) executam este passo automaticamente quando a resposta é colada.

```{figure} /_static/img/352-anonimizacao-de-ia/08.jpg
:alt: A reversão da resposta, com os valores reais

A reversão: a resposta com os valores reais repostos.
```

```{note}
**Prazos de conservação.** O mapa que permite repor os valores originais expira ao fim de 30 dias. A linha do registo é conservada durante um ano, uma vez que a contagem (por exemplo, «4 endereços IP») e a data constituem evidência de auditoria sem dados pessoais.
```

## Resumo

- O registo de saídas documenta os pedidos enviados para serviços de IA.
- A bancada apresenta o texto que seria enviado e repõe os valores reais numa resposta.
- Sem as camadas obrigatórias, nenhum *prompt* é gerado.
