# A árvore, os controlos, a cobertura e o arquivo do SGSI

Os outros ecrãs do menu SGSI, além das políticas, dos procedimentos e dos planos: a árvore que liga tudo, as fichas de controlo, as evidências, a cobertura por controlo e o arquivo.

```{video} 354-o-sgsi-por-inteiro
```

## Onde fica no menu

**Menu:** Governar › SGSI › Árvore do SGSI

```{figure} /_static/capturas/sgsi-estrutura/menu.jpg
:alt: Menu lateral: Governar › SGSI › Árvore do SGSI

O caminho no menu lateral: Governar › SGSI › Árvore do SGSI.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **SGSI**.
3. Clique em **Árvore do SGSI**: abre o ecrã desta página.


Os ecrãs desta página estão todos no mesmo módulo, **Governar › SGSI**, e partilham o editor descrito em {doc}`isms-documents`.

## A árvore do SGSI

**Menu:** Governar › SGSI › Árvore do SGSI

```{figure} /_static/capturas/sgsi-estrutura/arvore-1.jpg
:alt: A árvore de conformidade do SGSI

A árvore de conformidade do SGSI.
```

1. **A árvore de conformidade**


Toda a documentação do SGSI numa só vista hierárquica: as políticas em cima, e por baixo os procedimentos, os planos, os controlos e as evidências que delas dependem. É o índice que se usa a toda a hora para saber onde está um documento e o que o justifica.

Um documento arquivado aparece esbatido e com o selo **arquivado**. Não é escondido de propósito: se desaparecesse, a hierarquia partia-se por baixo dele e os documentos que o citam ficavam órfãos no ecrã.

## Os controlos

**Menu:** Governar › SGSI › Controlos

```{figure} /_static/capturas/sgsi-estrutura/controlos-1.jpg
:alt: A categoria Controlos, com o botão para criar e o dos arquivados

A categoria Controlos, com o botão para criar e o dos arquivados.
```

1. **Novo documento**
2. **Arquivados**


As fichas de controlo descrevem como cada controlo está implementado na organização. Criam-se e editam-se como os outros documentos, no mesmo editor.

Uma ficha de controlo **não governa** o controlo, descreve-o. Por isso, nesta categoria, o bloco de ligação a controlos explica porque não se liga, em vez de oferecer a ligação. Quem governa um controlo é uma política ou um procedimento.

## A cobertura por controlo

**Menu:** Governar › SGSI › Cobertura por controlo

```{figure} /_static/capturas/sgsi-estrutura/cobertura-1.jpg
:alt: A cobertura documental, pelos dois lados

A cobertura documental, pelos dois lados.
```

1. **Só os que estão a descoberto**
2. **Controlos aplicáveis sem documento**
3. **Documentos que não cobrem controlo nenhum**


As duas perguntas que um auditor faz logo:

- que controlos aplicáveis **não têm documento nenhum** que os governe;
- que documentos **não cobrem controlo nenhum**.

A caixa **só os que estão a descoberto** deixa só o que falta. A ligação que esta página mostra é a mesma que se faz na página de cada documento: o mesmo facto, visto pelo lado do controlo.

## As evidências

**Menu:** Governar › SGSI › Evidências

```{figure} /_static/capturas/sgsi-estrutura/evidencias-1.jpg
:alt: A categoria Evidências

A categoria Evidências.
```

1. **Nova evidência**


Os documentos que provam que uma medida está aplicada: um relatório, uma ata, um registo. Uma evidência é **prova datada que caduca**, por isso não governa controlos, e o editor diz porquê em vez de oferecer a ligação. As provas que contam para a conformidade, recolhidas por controlo e com validade, estão em {doc}`/platform/monitoring/evidence`.

## O arquivo

**Menu:** Governar › SGSI › Arquivo

```{figure} /_static/capturas/sgsi-estrutura/arquivo-1.jpg
:alt: O arquivo, com os documentos de todas as categorias

O arquivo, com os documentos de todas as categorias.
```

1. **Restaurar**
2. **Um documento arquivado**


Tudo o que foi arquivado, nas cinco categorias, com **Restaurar** e **Apagar definitivamente** em cada linha. É o sítio para a pergunta «o que é que já não está em vigor?».

**Arquivar não é apagar.** Um documento arquivado sai das listas, do dossier do auditor e da cobertura documental, e passa a só-leitura; as versões, os anexos e as ligações a controlos ficam intactos e voltam com ele. Arquiva-se na página do próprio documento, no botão **Arquivar**.

**Apagar só se faz aqui, e só ao que já está arquivado.** A eliminação pede duas confirmações. A primeira diz o que se perde: todas as versões, os anexos (cópias assinadas incluídas) e as ligações aos controlos. A segunda obriga a **escrever o título do documento**.

```{tip}
**Na dúvida, deixe-o arquivado.** Um documento arquivado não estorva. Apagar só se justifica para o que nunca devia ter sido criado, como um duplicado ou um engano: uma política que esteve em vigor é história do SGSI, e um auditor vai preferir vê-la arquivada.
```

## Resumo

- A árvore mostra toda a documentação do SGSI e o que depende de quê.
- Fichas de controlo e evidências não governam controlos; políticas e procedimentos governam.
- A cobertura por controlo mostra o que está a descoberto, pelos dois lados.
- Arquivar guarda tudo; apagar só no arquivo, com o título escrito.
