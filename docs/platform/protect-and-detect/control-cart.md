# O carrinho de controlos e os documentos com IA

Uma política ou um procedimento destina-se a cumprir controlos, ou seja, os requisitos da norma ou da lei. O carrinho reúne esses controlos para a redação do documento com apoio de inteligência artificial, sem envio dos dados da organização. No final, os controlos ficam associados ao documento e a cobertura é atualizada.

```{video} 359-carrinho-e-documentos-com-ia
```

## Acesso

O carrinho não tem entrada própria no menu: está disponível no cabeçalho de todas as páginas (ícone do carrinho, com o número de itens). É preenchido nos ecrãs onde os controlos são apresentados; o exemplo desta página começa na Declaração de Aplicabilidade.

**Governar** > **GRC — Conformidade** > **Declaração de Aplicabilidade**, seguido da seleção da norma.

```{figure} /_static/capturas/carrinho/menu.jpg
:alt: Menu lateral: Governar > GRC — Conformidade > Declaração de Aplicabilidade

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Funcionamento

- O carrinho guarda os controlos e os documentos a utilizar, à semelhança de um site de compras.
- É preenchido nos ecrãs onde os controlos são apresentados: Declaração de Aplicabilidade, controlos ativos, cobertura por controlo e lista de documentos do SGSI.
- É utilizado na redação de um documento ou numa pergunta à IA.
- No pedido, o texto das normas é enviado em claro, por ser público e necessário à IA. Os dados da organização (nome, unidades, pessoas) são enviados como etiquetas.

## Preenchimento do carrinho

```{figure} /_static/capturas/carrinho/soa-1.jpg
:alt: A Declaração de Aplicabilidade, filtrada por «acesso», com o botão do carrinho

A Declaração de Aplicabilidade, filtrada por «acesso».
```

**Como preencher:**

1. Introduza «acesso» no campo **Pesquisar por código, título ou justificação**; são apresentados quatro controlos.
2. Botão do carrinho, em cada controlo: adiciona apenas esse controlo.
3. Clique em **Juntar ao carrinho (4)** para adicionar todos os controlos apresentados.

## Carrinho

```{figure} /_static/capturas/carrinho/carrinho-1.jpg
:alt: O carrinho, no cabeçalho

O carrinho, no cabeçalho de qualquer página.
```

1. Clique em **Carrinho de conhecimento**, no cabeçalho.

```{figure} /_static/capturas/carrinho/carrinho-2.jpg
:alt: O carrinho aberto: os quatro controlos e as duas saídas

O carrinho aberto: os quatro controlos e as duas opções de utilização.
```

No ecrã, encontra os seguintes elementos:

1. **Conteúdo do carrinho:** Os quatro controlos, cada um com a norma de origem.
2. **Ficha da organização:** Incluída sempre, com o nome e o setor em etiquetas; o NIF, a morada e o telefone não são incluídos.
3. Botão **Perguntar à IA:** Por exemplo, para verificar se três procedimentos cobrem um controlo.
4. Botão **Escrever um documento:** Inicia a redação, descrita a seguir.

## Documento

**Governar** > **SGSI** > **Procedimentos**

```{figure} /_static/capturas/carrinho/documento-2.jpg
:alt: Um procedimento novo, com o título e o botão Escrever com IA

Um procedimento novo, com o título e o botão **Escrever com IA**.
```

**Como criar:**

1. Clique em **NOVO** e introduza o título: «Procedimento de gestão de acessos».
2. Clique em **Escrever com IA**, por cima do corpo. Com o corpo vazio, o pedido destina-se a redigir de raiz; com texto existente, destina-se a rever.

Os controlos do carrinho só podem ser associados a políticas, procedimentos e planos, as três categorias de documentos que governam controlos.

## Documentação incluída no pedido

```{figure} /_static/capturas/carrinho/escolher-2.jpg
:alt: O ecrã que escolhe que documentos do SGSI vão com o pedido

Seleção dos documentos do SGSI incluídos no pedido.
```

1. **Política de referência:** A política de que o procedimento depende.
2. Assinale **Política de Controlo de Acessos** e clique em **Continuar**.

O conteúdo destes documentos é incluído no pedido para que a IA não repita nem contradiga o texto existente e utilize o mesmo vocabulário. Todo o conteúdo é pseudonimizado.

## Pedido

```{figure} /_static/capturas/carrinho/pedido-2.jpg
:alt: O pedido, pseudonimizado, pronto a copiar

O pedido, pseudonimizado, pronto a copiar.
```

No ecrã, encontra os seguintes elementos:

1. **Pedido pseudonimizado:** Leia-o antes de o copiar; é o único conteúdo enviado para fora da plataforma.
2. Botão **Copiar.**
3. Botão **Já tenho a resposta:** Utilizado após a resposta do assistente.

No campo «O que quer pedir por palavras suas», descreva o pedido (neste exemplo, «um procedimento de gestão de acessos — pedido, aprovação, revisão periódica e revogação») e clique em **Refazer o prompt**. O texto dos quatro controlos é enviado em claro; a organização, as unidades e o responsável da política são enviados como etiquetas (`[ORG_1]`, `[PESSOA_1]`).

## Serviço de IA

O pedido é colado no serviço de IA utilizado pela organização. No vídeo, a janela do assistente foi criada para efeitos de demonstração; o pedido e a resposta são reais, processados por um modelo de IA.

```{figure} /_static/img/359-carrinho-e-documentos-com-ia/07.jpg
:alt: A resposta do assistente: o procedimento inteiro, ainda com as etiquetas

A resposta real do modelo: o procedimento completo, em secções, ainda com as etiquetas.
```

A resposta contém o procedimento completo, em secções. Na ausência de informação sobre a organização, a IA não a inventa: insere um marcador entre parênteses retos, como «[indicar a periodicidade]», para decisão posterior.

## Importação da resposta

```{figure} /_static/capturas/carrinho/resposta-3.jpg
:alt: A resposta lida, com os valores reais, e as opções

A resposta importada, com os valores reais repostos.
```

No ecrã, encontra os seguintes elementos:

1. Opção **Ligar também os controlos do carrinho:** Selecionada por omissão. Associa ao documento os controlos do carrinho ainda não associados, com a nota «Coberto por texto escrito com apoio de IA».
2. Botão **Substituir o corpo.**
3. Botão **Inserir no fim** (ou no cursor).
4. Botão **Descartar.**

**Como importar:** Cole a resposta e clique em **Ler a resposta**. As etiquetas são substituídas pelos valores reais; por exemplo, «[ORG_1]» é substituído pelo nome da organização. As alterações só são gravadas ao clicar em **Guardar**.

## Gravação

```{figure} /_static/capturas/carrinho/guardar-4.jpg
:alt: O procedimento guardado, com os quatro controlos que governa

O procedimento guardado. Em baixo, «Controlos que este documento governa»: os quatro controlos do carrinho.
```

Após a gravação, o documento fica com o texto e com os controlos que governa associados (O.GAP, O.PAP, T.AR, T.PAD). Os marcadores entre parênteses retos indicam os elementos a decidir antes da aprovação.

## Cobertura

**Governar** > **SGSI** > **Cobertura por controlo**

```{figure} /_static/img/359-carrinho-e-documentos-com-ia/10.jpg
:alt: A cobertura por controlo, depois do procedimento

A cobertura por controlo, na norma do QNRCS para entidades públicas relevantes.
```

A cobertura por controlo reflete a alteração: estes controlos deixaram de estar a descoberto, uma vez que existe um documento que os governa.

## Resumo

- Reúne controlos e documentos num carrinho e inclui-os no pedido à IA.
- Pseudonimiza os dados da organização e repõe os valores na resposta.
- Associa os controlos ao documento, e a cobertura é atualizada.
- Não aprova o documento: o texto é uma proposta, a rever pelo respetivo responsável.
