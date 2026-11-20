# Feeds RSS

Fontes de notícias e alertas de cibersegurança lidas pela plataforma e respetiva frequência de atualização.

```{video} 353-integracoes
```

O vídeo apresenta as quatro integrações: sistemas externos, MISP, feeds RSS e diretório.

```{video} 363-os-tipos-dos-feeds
```

O segundo vídeo mostra os tipos de cada canal.

## Acesso

**Governar** > **Administração do sistema** > **Integrações** > **Feeds RSS**

```{figure} /_static/capturas/adm-rss/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Integrações > Feeds RSS

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Configuração do ecrã

```{figure} /_static/capturas/adm-rss/feeds-1.jpg
:alt: A frequência de atualização e a lista de feeds

A frequência de atualização e a lista de feeds.
```

A interface apresenta os seguintes elementos:

1. **Frequência de atualização:** Permite definir o intervalo (de 1 a 24 horas).
2. Botão **Guardar:** Regista as alterações efetuadas.
3. Botão **Atualizar agora:** Lê imediatamente todos os feeds configurados.
4. Botão **Adicionar um feed:** Permite configurar uma nova fonte.

**Como configurar:** Selecione a frequência de atualização pretendida e clique em **Guardar**.

## Tipos de cada canal

Cada canal tem um ou mais tipos: **Alertas**, **Notícias**, **Outbreak** ou **Informacionais**. Ao adicionar um feed, escolhem-se os tipos por baixo dos campos (por omissão, **Alertas**). Num canal que já existe, os botões de tipo por baixo do nome ligam e desligam cada tipo, e a alteração grava-se logo, na trilha de auditoria. Um canal tem sempre pelo menos um tipo.

Os canais que existiam antes desta funcionalidade ficaram como **Alertas**. Os tipos servem a escolha de cada pessoa em {doc}`/platform/protect-and-detect/security-feeds`, que por omissão só mostra os alertas.

Não é possível eliminar feeds que já tenham artigos associados. Para deixar de receber notícias dessa fonte sem perder o histórico, deve desativar o feed.

```{important}
**Seleção de fontes.** Uma recomendação de segurança não validada pode causar mais danos do que a ameaça que pretende mitigar, e a responsabilidade pela recomendação é de quem a introduz no sistema. Dê preferência a CSIRT e autoridades (CNCS, CERT.PT, CISA, ENISA, NCSC) e aos próprios fabricantes; verifique o historial e a data de atualização da fonte; evite agregadores sem curadoria e blogues anónimos. Em caso de dúvida, não adicione a fonte.
```

## Resumo

- Os feeds alimentam o ecrã {doc}`/platform/protect-and-detect/security-feeds`.
- Os feeds com artigos associados podem ser desativados, mas não eliminados.
