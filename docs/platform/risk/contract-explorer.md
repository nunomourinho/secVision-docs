# Importar contratos públicos

O explorador de contratos públicos: carregar os ficheiros exportados do BASE.gov, escolher a própria entidade e importar os contratos que interessam.

## Onde fica no menu

**Menu:** Identificar › Fornecedores e Contratos › Importar contratos

```{figure} /_static/capturas/contratos-explorador/menu.jpg
:alt: Menu lateral: Identificar › Fornecedores e Contratos › Importar contratos

O caminho no menu lateral: Identificar › Fornecedores e Contratos › Importar contratos.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Fornecedores e Contratos**.
3. Clique em **Importar contratos**: abre o ecrã desta página.


**Faz-se antes do registo de fornecedores, não depois.** Quem tem contratos públicos começa por aqui e escreve menos meia lista à mão: os fornecedores podem depois ser propostos a partir dos contratos ({doc}`suppliers`).

## O que entra

Ficheiros JSON exportados do **BASE.gov**, o portal dos contratos públicos. São de dois tipos: um `entidades.json` com a lista de entidades adjudicantes, e um ou mais ficheiros de contratos, anúncios ou modificações.

```{note}
**A plataforma não vai ao BASE.gov buscar nada.** Não há nenhuma ligação para fora: os ficheiros são exportados de lá por quem os tem e carregados aqui. Não há botão «sincronizar».
```

## Os três passos

```{figure} /_static/capturas/contratos-explorador/entidades-1.jpg
:alt: O primeiro passo: carregar as entidades

O primeiro passo: carregar as entidades.
```

1. **Passo 1 — carregar as entidades**
2. **Importar entidades.json**


O ecrã anda pelos três passos sozinho.

1. **Carregar entidades:** o `entidades.json`.
2. **Selecionar as entidades alvo**, normalmente só a própria instituição e os organismos que dela dependem. É este passo que define o filtro: o cartão «arquivos processados» mostra sempre **lidos** e **extraídos**, e a diferença entre os dois é o que ficou de fora por não ser destas entidades.
3. **Carregar os dados e escolher:** filtrar por texto, adjudicatário, valor, data ou categoria técnica, marcar os que interessam e **importar para a base de dados**.

A etiqueta técnica é adivinhada da descrição e dos códigos CPV, e só tem dois valores: **Software** e **Hardware**. O que não cai em nenhum fica sem etiqueta: não é uma terceira categoria, é a ausência de palpite. A marca **Eco** vem do próprio registo.

## O que sai

Os registos escolhidos, gravados. **Só os escolhidos**: o que fica no *browser* não é gravado em lado nenhum, e «Recomeçar» deita fora tudo o que ainda não foi importado. Reimportar o mesmo ficheiro não duplica nada: a chave é a referência mais o tipo, e o ecrã diz quantos entraram e quantos foram ignorados por já lá estarem.

Os contratos gravados associam-se depois a sistemas do catálogo em **Governar › Contratos › Importados**. É essa associação que responde à pergunta que uma auditoria faz sempre: *este servidor está coberto por que contrato, e até quando?* Ver {doc}`suppliers`.

## Resumo

- Os ficheiros vêm do BASE.gov, exportados à mão; a plataforma não se liga a nada.
- Entidades primeiro, depois os contratos; só os escolhidos são gravados.
- Reimportar não duplica.
