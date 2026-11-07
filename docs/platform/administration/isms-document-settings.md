# Documentos do SGSI: tipos e modelos Word

Duas configurações do editor de documentos do SGSI: as listas de tipos que ele oferece e o modelo Word de cada categoria.

## Onde fica no menu

**Menu:** Governar › Administração do sistema › Documentos SGSI

```{figure} /_static/capturas/adm-documentos-sgsi/menu.jpg
:alt: Menu lateral: Governar › Administração do sistema › Documentos SGSI

O caminho no menu lateral: Governar › Administração do sistema › Documentos SGSI.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Administração do sistema**.
3. Clique em **Documentos SGSI**: abre o ecrã desta página.


## Os tipos de documento

```{figure} /_static/capturas/adm-documentos-sgsi/tipos-1.jpg
:alt: Os tipos de documento, categoria a categoria

Os tipos de documento, categoria a categoria.
```

1. **Os tipos de documento, por categoria**
2. **Uma categoria e os seus tipos**


Cada categoria do SGSI (políticas, procedimentos, planos, controlos e evidências) tem a sua lista de tipos, e é essa lista que o editor oferece ao criar um documento. As listas vivem no servidor e são **iguais para todos os administradores e todas as máquinas**. Ao lado de cada tipo está o número de documentos que o usam, **arquivados incluídos**.

- **Renomear** é seguro: o nome novo passa para todos os documentos.
- **Desativar** tira o tipo das escolhas sem tocar nos documentos que já o têm. O editor mostra-o como «fora da lista» até alguém o mudar.
- **Apagar** só é possível a um tipo que nenhum documento use. Num tipo em uso, o botão fica travado e diz porquê. Para o apagar mesmo, mude primeiro o tipo desses documentos, na página do SGSI.

## Os modelos Word

```{figure} /_static/capturas/adm-documentos-sgsi/modelos-1.jpg
:alt: Os modelos Word, um por categoria

Os modelos Word, um por categoria.
```

1. **Os modelos Word, um por categoria**
2. **Descarregar o modelo de exemplo**
3. **Experimentar num documento**
4. **Carregar o modelo da instituição**


Um ficheiro `.docx` por categoria, o da instituição, com o logótipo e a capa próprios. Enquanto não carregar nenhum, os documentos exportam-se com o modelo do sistema.

1. Clique em **Descarregar o modelo de exemplo**. Já traz todas as marcas nos sítios certos.
2. Abra-o no Word e ponha o logótipo, os tipos de letra e a capa da instituição, deixando as marcas onde quer que apareça cada campo.
3. Clique em **Carregar modelo** na categoria respetiva.
4. Clique em **Experimentar num documento**: a única prova que conta é exportar um documento a sério e olhar para ele.

```{figure} /_static/capturas/adm-documentos-sgsi/marcas-1.jpg
:alt: A lista das marcas que o modelo pode usar

A lista das marcas que o modelo pode usar.
```

1. **As marcas que o modelo pode usar**


As marcas (`{{titulo}}`, `{{corpo}}`, `{{historico_versoes}}`, `{{controlos}}` e as outras da lista) funcionam também no cabeçalho e no rodapé, que é onde costuma estar o logótipo. Nada é recusado além de «isto não é um `.docx` legível»: marcas em falta ou desconhecidas são avisos.

## Resumo

- Os tipos de documento são iguais para todos. Um tipo em uso desativa-se, não se apaga.
- Um modelo Word por categoria, a partir do modelo de exemplo.
- Ver também {doc}`/platform/protect-and-detect/isms-documents`.
