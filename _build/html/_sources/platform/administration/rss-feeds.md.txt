# Feeds RSS

As fontes de notícias e alertas de cibersegurança que a plataforma lê, e de quanto em quanto tempo.

```{video} 353-integracoes
```

O vídeo mostra as quatro integrações: os sistemas externos, o MISP, os feeds RSS e o diretório.

## Onde fica no menu

**Menu:** Governar › Administração do sistema › Integrações › Feeds RSS

```{figure} /_static/capturas/adm-rss/menu.jpg
:alt: Menu lateral: Governar › Administração do sistema › Integrações › Feeds RSS

O caminho no menu lateral: Governar › Administração do sistema › Integrações › Feeds RSS.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Administração do sistema**.
3. Dentro dele, abra **Integrações**.
4. Clique em **Feeds RSS**: abre o ecrã desta página.


## O ecrã

```{figure} /_static/capturas/adm-rss/feeds-1.jpg
:alt: A frequência de atualização e a lista de feeds

A frequência de atualização e a lista de feeds.
```

1. **A frequência de atualização**
2. **Guardar**
3. **Atualizar agora**
4. **Adicionar um feed**


Escolha a frequência de atualização (de 1 a 24 horas) e clique em **Guardar**. **Atualizar agora** lê todos os feeds de imediato. **Adicionar** acrescenta uma fonte nova.

Um feed com artigos **não se apaga**: desativa-se. Apagar levaria o arquivo de artigos com ele.

```{important}
**Escolha as fontes com critério.** Uma recomendação de segurança não validada pode causar mais danos do que a ameaça que pretende mitigar, e a responsabilidade por essa recomendação é de quem a insere no sistema. Prefira CSIRTs e autoridades (CNCS, CERT.PT, CISA, ENISA, NCSC) e os próprios fabricantes; verifique o historial e a data de atualização da fonte; desconfie de agregadores sem curadoria e de blogues anónimos. Na dúvida, deixe de fora.
```

## Resumo

- Os feeds alimentam o ecrã {doc}`/platform/protect-and-detect/security-feeds`.
- Um feed com artigos desativa-se, não se apaga.
