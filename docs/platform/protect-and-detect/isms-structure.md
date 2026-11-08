# A árvore, os controlos, a cobertura e o arquivo do SGSI

Os restantes ecrãs do menu SGSI, para além das políticas, dos procedimentos e dos planos: a árvore de documentação, as fichas de controlo, as evidências, a cobertura por controlo e o arquivo.

```{video} 354-o-sgsi-por-inteiro
```

## Acesso

**Governar** > **SGSI** > **Árvore do SGSI**

```{figure} /_static/capturas/sgsi-estrutura/menu.jpg
:alt: Menu lateral: Governar > SGSI > Árvore do SGSI

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

Os ecrãs desta página pertencem ao mesmo módulo, **Governar** > **SGSI**, e utilizam o editor descrito em {doc}`isms-documents`.

## Árvore do SGSI

```{figure} /_static/capturas/sgsi-estrutura/arvore-1.jpg
:alt: A árvore de conformidade do SGSI

A árvore de conformidade do SGSI.
```

1. **Árvore de conformidade:** Vista hierárquica da documentação.

A árvore apresenta toda a documentação do SGSI numa vista hierárquica: as políticas no nível superior e, abaixo, os procedimentos, os planos, os controlos e as evidências que delas dependem. Permite localizar um documento e identificar o seu fundamento.

Um documento arquivado é apresentado esbatido e com a indicação **arquivado**. Não é ocultado, para preservar a hierarquia e evitar que os documentos que o citam fiquem sem referência.

## Controlos

**Governar** > **SGSI** > **Controlos**

```{figure} /_static/capturas/sgsi-estrutura/controlos-1.jpg
:alt: A categoria Controlos, com o botão para criar e o dos arquivados

A categoria Controlos, com os botões de criação e de arquivados.
```

No ecrã, encontra os seguintes elementos:

1. Botão **Novo documento:** Cria uma ficha de controlo.
2. Botão **Arquivados:** Apresenta as fichas arquivadas.

As fichas de controlo descrevem a implementação de cada controlo na organização e são criadas e editadas no mesmo editor dos restantes documentos.

Uma ficha de controlo descreve o controlo, mas **não o governa**. Por este motivo, nesta categoria, o bloco de ligação a controlos apresenta essa explicação em vez da opção de ligação. Um controlo é governado por uma política ou por um procedimento.

## Cobertura por controlo

**Governar** > **SGSI** > **Cobertura por controlo**

```{figure} /_static/capturas/sgsi-estrutura/cobertura-1.jpg
:alt: A cobertura documental, pelos dois lados

A cobertura documental, nas duas perspetivas.
```

No ecrã, encontra os seguintes elementos:

1. Opção **só os que estão a descoberto:** Apresenta apenas as lacunas.
2. **Controlos aplicáveis sem documento:** Controlos não governados por nenhum documento.
3. **Documentos sem controlo:** Documentos que não cobrem nenhum controlo.

Este ecrã responde às duas primeiras questões de um auditor:

- os controlos aplicáveis **sem nenhum documento** que os governe;
- os documentos que **não cobrem nenhum controlo**.

A associação apresentada neste ecrã é a mesma efetuada na página de cada documento, vista na perspetiva do controlo.

## Evidências

**Governar** > **SGSI** > **Evidências**

```{figure} /_static/capturas/sgsi-estrutura/evidencias-1.jpg
:alt: A categoria Evidências

A categoria Evidências.
```

1. Botão **Nova evidência:** Cria um documento de evidência.

Esta categoria contém os documentos que demonstram a aplicação de uma medida: relatórios, atas e registos. Uma evidência é **uma prova datada com prazo de validade**, pelo que não governa controlos, e o editor apresenta essa explicação em vez da opção de ligação. As evidências contabilizadas para a conformidade, recolhidas por controlo e com validade, são descritas em {doc}`/platform/monitoring/evidence`.

## Arquivo

**Governar** > **SGSI** > **Arquivo**

```{figure} /_static/capturas/sgsi-estrutura/arquivo-1.jpg
:alt: O arquivo, com os documentos de todas as categorias

O arquivo, com os documentos de todas as categorias.
```

No ecrã, encontra os seguintes elementos:

1. Botão **Restaurar:** Repõe o documento em vigor.
2. **Documento arquivado:** Cada linha corresponde a um documento arquivado, com os botões **Restaurar** e **Apagar definitivamente**.

O arquivo reúne os documentos arquivados das cinco categorias e permite identificar os documentos que deixaram de estar em vigor.

**O arquivo não elimina documentos.** Um documento arquivado deixa de constar das listas, do dossier do auditor e da cobertura documental e passa a modo de leitura; as versões, os anexos e as ligações a controlos são preservados e repostos com o documento. O arquivo é efetuado na página do documento, no botão **Arquivar**.

**A eliminação só é possível neste ecrã e apenas para documentos arquivados.** A eliminação exige duas confirmações: a primeira indica os elementos que serão perdidos (todas as versões, os anexos, incluindo as cópias assinadas, e as ligações aos controlos); a segunda exige a **introdução do título do documento**.

```{tip}
**Em caso de dúvida, mantenha o documento arquivado.** A eliminação justifica-se apenas para documentos criados por engano, como duplicados. Uma política que esteve em vigor faz parte do histórico do SGSI, e um auditor prefere consultá-la arquivada.
```

## Resumo

- A árvore apresenta toda a documentação do SGSI e as respetivas dependências.
- As fichas de controlo e as evidências não governam controlos; as políticas e os procedimentos governam.
- A cobertura por controlo identifica as lacunas, nas duas perspetivas.
- O arquivo preserva todos os dados; a eliminação só é possível no arquivo, com introdução do título.
