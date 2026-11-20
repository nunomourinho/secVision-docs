# Integração Shodan

Ligação à API do Shodan, para a pesquisa de exposição por tecnologia: onde, nas gamas públicas da instituição, está exposto um produto, uma versão ou uma livraria web. A pesquisa usa-se no Catálogo de Segurança e nos Relatórios de Recomendações (ver {doc}`/platform/inventory/shodan-exposure`).

## Acesso

**Governar** > **Administração do sistema** > **Integrações** > **Shodan**

```{figure} /_static/capturas/adm-shodan/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Integrações > Shodan

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Configuração do ecrã

```{figure} /_static/capturas/adm-shodan/chave-1.jpg
:alt: A configuração da integração Shodan

A configuração da chave de API e dos créditos.
```

No ecrã, encontra os seguintes elementos:

1. **Integração activa:** Quando desativada, **Pesquisar (API)** é recusado com indicação do motivo. **Abrir no shodan.io** e a **Correspondência local** continuam disponíveis, porque não usam a chave.
2. **Chave de API:** Obtém-se em account.shodan.io, em **API Key**. Depois de guardada, deixa de ser apresentada. Para a substituir, escreva a nova; o campo vazio mantém a chave guardada.
3. **Teto de créditos por mês:** O máximo de créditos de pesquisa que a plataforma pode gastar num mês. Vazio significa que só vale o limite do plano. Uma pesquisa que ultrapassaria o teto é recusada antes de gastar créditos. A ajuda do campo indica quantos créditos já foram gastos este mês.
4. **Máximo de páginas por pesquisa:** Cada página traz 100 resultados e gasta 1 crédito.
5. Botão **Guardar:** Regista a configuração.
6. Botão **Testar ligação:** Guarda a chave escrita e pergunta ao Shodan pelo plano e pelos créditos disponíveis, sem gastar créditos.

**Como configurar:** Escreva a chave de API, defina o teto de créditos, clique em **Guardar** e confirme a ligação com **Testar ligação**.

## O que sai do servidor, e o que custa

- Sai a query: a tecnologia pesquisada e as gamas públicas da instituição, que são as mesmas comunicadas ao regulador.
- Contar os resultados não gasta créditos. O ecrã de pesquisa usa essa contagem no botão **Estimar**, antes de pesquisar.
- Pesquisar com o filtro das gamas (`net:`) gasta 1 crédito de pesquisa por página de 100 resultados e requer um **plano pago** do Shodan. Com a chave gratuita, a pesquisa é recusada e a mensagem indica o motivo.

## Resumo

- A chave fica cifrada e não volta a ser apresentada depois de guardada.
- Sem chave, a pesquisa de exposição continua possível: abrir a pesquisa no shodan.io, com a sessão de quem a abre, e importar o ficheiro exportado; ou a correspondência local, sem custo.
- Na instalação de teste, a ligação é recusada: o Shodan é um serviço externo e não há um segundo para onde a apontar.
