# Integração MISP

A ligação ao MISP, a plataforma de partilha de informação sobre ameaças, para enriquecer os indicadores de compromisso com eventos, nível de ameaça e etiquetas.

```{video} 353-integracoes
```

O vídeo mostra as quatro integrações: os sistemas externos, o MISP, os feeds RSS e o diretório.

## Onde fica no menu

**Menu:** Governar › Administração do sistema › Integrações › Integração MISP

```{figure} /_static/capturas/adm-misp/menu.jpg
:alt: Menu lateral: Governar › Administração do sistema › Integrações › Integração MISP

O caminho no menu lateral: Governar › Administração do sistema › Integrações › Integração MISP.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Administração do sistema**.
3. Dentro dele, abra **Integrações**.
4. Clique em **Integração MISP**: abre o ecrã desta página.


## O ecrã

```{figure} /_static/capturas/adm-misp/ligacao-1.jpg
:alt: A configuração da ligação ao MISP

A configuração da ligação ao MISP.
```


O que cada número faz:

1. **Módulo MISP activo.** Desligado, tudo o que é MISP desaparece da aplicação.
2. **URL do MISP:** o endereço da instância.
3. **Chave de API.** Uma vez guardada, deixa de ser mostrada; para a trocar, apague o campo e escreva a nova.
4. **Verificar certificado SSL.** Desligue **apenas** em ambientes de ensaio com certificados auto-assinados.
5. **Enriquecimento automático diário**, e a hora a que corre (5h por omissão).
6. **Guardar configuração.**
7. **Testar ligação** grava primeiro e depois pergunta a versão ao MISP. É o botão que diz se a chave está boa.
8. **Enriquecer todos os IoCs** consulta já o MISP para todos os indicadores ativos e guarda o número de eventos, o nível de ameaça e as etiquetas de cada um.

## Resumo

- O MISP enriquece os IPs e domínios dos indicadores de compromisso.
- A chave não volta a ser mostrada depois de guardada.
- Ver também {doc}`/platform/protect-and-detect/ioc`.
