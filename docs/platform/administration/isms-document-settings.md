# Documentos do SGSI: tipos e modelos Word

Duas configurações do editor de documentos do SGSI: as listas de tipos de documento disponíveis e o modelo Word de cada categoria.

```{video} 351-administracao-da-plataforma
```

O vídeo apresenta os três ecrãs da administração: cobertura, documentos do SGSI e versão.

## Acesso

**Governar** > **Administração do sistema** > **Documentos SGSI**

```{figure} /_static/capturas/adm-documentos-sgsi/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Documentos SGSI

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Tipos de documento

```{figure} /_static/capturas/adm-documentos-sgsi/tipos-1.jpg
:alt: Os tipos de documento, categoria a categoria

Os tipos de documento, por categoria.
```

No ecrã, encontra os seguintes elementos:

1. **Tipos de documento:** Listas organizadas por categoria.
2. **Categoria:** Uma categoria e os respetivos tipos.

Cada categoria do SGSI (políticas, procedimentos, planos, controlos e evidências) tem uma lista de tipos, apresentada no editor ao criar um documento. As listas são guardadas no servidor e são **comuns a todos os administradores e a todos os postos de trabalho**. Junto a cada tipo é indicado o número de documentos que o utilizam, **incluindo os arquivados**.

- **Renomear:** O novo nome é aplicado a todos os documentos.
- **Desativar:** Retira o tipo das opções disponíveis, sem alterar os documentos que já o utilizam. O editor apresenta-o como «fora da lista» até o tipo ser alterado.
- **Apagar:** Disponível apenas para tipos sem documentos associados. Num tipo em uso, o botão fica bloqueado e indica o motivo. Para eliminar o tipo, altere primeiro o tipo desses documentos na página do SGSI.

## Modelos Word

```{figure} /_static/capturas/adm-documentos-sgsi/modelos-1.jpg
:alt: Os modelos Word, um por categoria

Os modelos Word, um por categoria.
```

No ecrã, encontra os seguintes elementos:

1. **Modelos Word:** Um modelo por categoria.
2. Botão **Descarregar o modelo de exemplo:** Obtém um modelo com todas as marcas já posicionadas.
3. Botão **Experimentar num documento:** Exporta um documento real com o modelo carregado.
4. Botão **Carregar o modelo da instituição:** Envia o ficheiro `.docx` da instituição.

Cada categoria utiliza um ficheiro `.docx` da instituição, com o logótipo e a capa próprios. Enquanto não for carregado nenhum modelo, os documentos são exportados com o modelo do sistema.

**Como configurar:**

1. Clique em **Descarregar o modelo de exemplo**.
2. Abra o ficheiro no Word e aplique o logótipo, os tipos de letra e a capa da instituição, mantendo as marcas nas posições onde cada campo deve aparecer.
3. Clique em **Carregar modelo** na categoria respetiva.
4. Clique em **Experimentar num documento** e verifique o resultado num documento exportado.

```{figure} /_static/capturas/adm-documentos-sgsi/marcas-1.jpg
:alt: A lista das marcas que o modelo pode usar

A lista das marcas disponíveis para o modelo.
```

1. **Marcas disponíveis:** Campos que o modelo pode utilizar.

As marcas (`{{titulo}}`, `{{corpo}}`, `{{historico_versoes}}`, `{{controlos}}` e as restantes da lista) funcionam também no cabeçalho e no rodapé, onde habitualmente se encontra o logótipo. Um ficheiro só é rejeitado se não for um `.docx` legível; marcas em falta ou desconhecidas geram apenas avisos.

## Resumo

- Os tipos de documento são comuns a todos os utilizadores. Um tipo em uso pode ser desativado, mas não eliminado.
- Cada categoria tem um modelo Word, criado a partir do modelo de exemplo.
- Ver também {doc}`/platform/protect-and-detect/isms-documents`.
