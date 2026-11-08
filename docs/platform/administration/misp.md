# Integração MISP

Ligação ao MISP, a plataforma de partilha de informação sobre ameaças, para enriquecer os indicadores de compromisso com eventos, nível de ameaça e etiquetas.

```{video} 353-integracoes
```

O vídeo apresenta as quatro integrações: sistemas externos, MISP, feeds RSS e diretório.

## Acesso

**Governar** > **Administração do sistema** > **Integrações** > **Integração MISP**

```{figure} /_static/capturas/adm-misp/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Integrações > Integração MISP

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Configuração do ecrã

```{figure} /_static/capturas/adm-misp/ligacao-1.jpg
:alt: A configuração da ligação ao MISP

A configuração da ligação ao MISP.
```

No ecrã, encontra os seguintes elementos:

1. **Módulo MISP activo:** Quando desativado, todas as funcionalidades MISP deixam de ser apresentadas na aplicação.
2. **URL do MISP:** Endereço da instância.
3. **Chave de API:** Depois de guardada, deixa de ser apresentada. Para a substituir, apague o campo e introduza a nova chave.
4. **Verificar certificado SSL:** Deve ser desativado **apenas** em ambientes de ensaio com certificados autoassinados.
5. **Enriquecimento automático diário:** Ativa a execução diária e define a hora (5h por omissão).
6. Botão **Guardar configuração:** Regista as alterações efetuadas.
7. Botão **Testar ligação:** Guarda a configuração e pede a versão ao MISP, confirmando a validade da chave.
8. Botão **Enriquecer todos os IoCs:** Consulta imediatamente o MISP para todos os indicadores ativos e regista, para cada um, o número de eventos, o nível de ameaça e as etiquetas.

**Como configurar:** Ative o módulo, indique o endereço e a chave de API, clique em **Guardar configuração** e confirme a ligação com **Testar ligação**.

## Resumo

- O MISP enriquece os endereços IP e os domínios dos indicadores de compromisso.
- A chave não volta a ser apresentada depois de guardada.
- Ver também {doc}`/platform/protect-and-detect/ioc`.
