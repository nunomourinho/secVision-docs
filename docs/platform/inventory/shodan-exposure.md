# Exposição na Internet (Shodan)

Pesquisa no Shodan onde, nas gamas de endereços IP públicos da instituição, está exposta uma tecnologia: um produto, uma versão ou uma livraria web. Cada endereço encontrado é associado ao sistema do catálogo que o tem. Quando um endereço não pertence a nenhum sistema, aparece como **fora do catálogo**.

A mesma pesquisa existe em dois sítios: no **Catálogo de Segurança**, para filtrar a tabela pelos sistemas expostos, e nos **Relatórios de Recomendações**, onde fica guardada no relatório.

## Acesso

**Identificar** > **Inventário** > **Catálogo de Segurança** > **Exposição Shodan**

```{figure} /_static/capturas/exposicao-shodan/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Catálogo de Segurança

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

```{figure} /_static/capturas/exposicao-shodan/botao-1.jpg
:alt: O botão Exposição Shodan na barra de filtros do catálogo

O botão **Exposição Shodan**, na barra de filtros do catálogo.
```

1. Botão **Exposição Shodan:** Abre e fecha o painel de pesquisa.

## As gamas pesquisadas

As gamas não se escrevem no painel. A plataforma junta:

- as **gamas de endereços IP públicos** da ficha da organização (**Governar** > **Organização**), que são as mesmas que se comunicam ao regulador;
- as redes do **Inventário de Redes** cujo endereço é público.

A linha «N gamas públicas» mostra as gamas usadas e as que ficaram de fora, com o motivo: privadas, IPv6 ou contidas noutra gama. Se não houver nenhuma gama pública, o painel indica onde declará-las.

A plataforma acrescenta o filtro `net:` com estas gamas a todas as pesquisas. Uma query que traga o seu próprio `net:` é recusada, e os resultados que o Shodan devolva fora das gamas não são guardados.

## Pesquisar

```{figure} /_static/capturas/exposicao-shodan/painel-1.jpg
:alt: O painel Exposição Shodan no Catálogo de Segurança

O painel **Exposição Shodan**.
```

No painel, encontra os seguintes elementos:

1. **Gamas públicas:** O número de gamas usadas e de gamas ignoradas. Clique para ver a lista e o motivo de cada exclusão.
2. **Modelo:** A tecnologia a pesquisar, agrupada em aplicações web, livrarias web, servidores web, acesso remoto e perímetro, e bases de dados. A query de cada modelo aparece por baixo do campo. Sem modelo, o painel mostra os campos **Produto** (`product:`) e **Componente / livraria web** (`http.component:`).
3. **Versão:** Opcional. Uma versão exata (`2.4.49`) ou com operador (`< 2.4.50`, `>= 6.0`). Os modelos sem versão no Shodan, como o RDP, desativam o campo.
4. **Query do Shodan:** Opcional, para casos avançados (por exemplo `http.title:"Login" port:8443`). Não escreva o `net:`.
5. Botão **Estimar:** Indica quantos resultados existem e quantos créditos a pesquisa vai gastar, sem gastar nenhum.
6. Botão **Pesquisar (API):** Pesquisa com a API do Shodan. Requer a chave configurada em {doc}`/platform/administration/shodan`.
7. Botão **Correspondência local:** Cruza a tecnologia com os varrimentos InternetDB já feitos (**Verificar Shodan** nos sistemas e nas redes). Não gasta créditos.
8. Botão **Abrir no shodan.io:** Abre a mesma pesquisa no site do Shodan, com a sessão que tiver lá aberta.
9. Botão **Colar resultados:** Recebe o texto copiado da página de resultados do shodan.io.
10. Botão **Importar exportação:** Importa o ficheiro exportado do shodan.io.
11. Neste exemplo, clique em **Correspondência local**.

**Os três modos de pesquisar:**

- **Pesquisar (API)** é o modo completo: devolve banners, componentes web e versões. Com a filtragem por gamas, cada página de 100 resultados gasta 1 crédito de pesquisa e requer um plano pago do Shodan. Se o administrador tiver definido um teto mensal, uma pesquisa que o ultrapassaria é recusada antes de gastar créditos.
- **Correspondência local** é gratuita e imediata, mas vê menos: o InternetDB devolve apenas portas e CPE por endereço. Não identifica livrarias web, não traz banners e só conhece a versão quando ela vem no CPE. Os dados são os do último varrimento de cada endereço. O resultado indica esta limitação.
- **Abrir no shodan.io** não usa a chave da plataforma. Para guardar o que encontrar no site, copie a página de resultados e use **Colar resultados**, ou exporte os resultados («Download Results», formato JSON) e use **Importar exportação**.

## Resultado

```{figure} /_static/capturas/exposicao-shodan/resultado-1.jpg
:alt: O resultado de uma pesquisa de exposição

O resultado de uma pesquisa de exposição.
```

No resultado, encontra os seguintes elementos:

1. **A pesquisa guardada:** O modo, a query, a data, quem pesquisou e o número de resultados, com a ligação para repetir a pesquisa no shodan.io.
2. **Resultados:** Para cada serviço exposto, o endereço e a porta, a tecnologia e a versão, os CVE e o sistema do catálogo. Um CVE com o selo **KEV** consta do catálogo da CISA de vulnerabilidades exploradas ativamente. Cada CVE abre a página do NVD.
3. Botão **Filtrar o catálogo:** Mostra na tabela apenas os sistemas encontrados. Um selo por cima da tabela indica o filtro aplicado; o **×** do selo, ou **Limpar**, retira-o.

Quando o Shodan não indica a versão de um serviço, a linha mantém-se com a indicação «versão desconhecida»: não saber a versão não significa que o serviço não está exposto. As pesquisas anteriores ficam listadas por baixo do painel, para voltar a filtrar por elas.

## Guardar o que encontrou no shodan.io

Depois de clicar em **Abrir no shodan.io**, a pesquisa abre no site com as gamas da instituição já incluídas. Há duas formas de trazer os resultados para a plataforma.

**Colar os resultados da página:**

1. Na página de resultados do shodan.io, selecione tudo (Ctrl+A) e copie (Ctrl+C).
2. No painel, clique em **Colar resultados**, cole o texto e clique em **Pré-visualizar**.

Cada resultado da página começa pelo título, a data e o endereço IP, e a plataforma lê também os nomes, o cabeçalho `Server:` (produto e versão) e o `X-Powered-By:` (por exemplo, a versão do PHP). A página não mostra a porta nem os CVE: a porta é deduzida do banner (443 quando há certificado, 80 quando não há) e aparece sempre marcada como **(deduzida)**; os CVE ficam vazios.

**Importar a exportação:**

1. No site, exporte os resultados em **Download Results**, formato JSON.
2. No painel, clique em **Importar exportação** e escolha o ficheiro (`.json.gz` ou `.json`).

Nos dois casos, a pré-visualização mostra cada resultado. Os que estão fora das gamas e os repetidos não podem ser marcados; os que estão fora da versão pedida aparecem desmarcados. Clique em **Importar**: só nesse momento a pesquisa é gravada.

## Na ficha do sistema

Na ficha de cada sistema do catálogo, a secção **Exposição Shodan** mostra os serviços que as pesquisas encontraram nos endereços desse sistema, com a data e a pesquisa de origem. A secção só aparece quando há pelo menos um resultado.

## Nos relatórios de recomendações

**Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** > **Associar sistemas** > **Por exposição (Shodan)**

```{figure} /_static/capturas/relatorio-shodan/separador-1.jpg
:alt: O separador Por exposição (Shodan) em Associar sistemas

O separador **Por exposição (Shodan)**, em **Associar sistemas**.
```

1. Separador **Por exposição (Shodan):** A mesma pesquisa do catálogo, guardada neste relatório.

```{figure} /_static/capturas/relatorio-shodan/propostas-1.jpg
:alt: Os sistemas propostos a partir da pesquisa de exposição

Os resultados e os sistemas propostos.
```

1. **Resultados:** Os serviços expostos encontrados pela pesquisa.
2. **Sistemas propostos:** Os sistemas do catálogo que as pesquisas do relatório encontraram e que ainda não estão associados.
3. **Associar:** Associa um sistema ao relatório. Nas observações fica registado que foi encontrado exposto pelo Shodan, e em que pesquisas.
4. **Pesquisas guardadas:** As pesquisas feitas neste relatório, com a data, a query e os resultados.
5. Botão **Associar todos os propostos:** Associa todos os sistemas propostos de uma vez.

Nenhum sistema é associado automaticamente. Os endereços que não pertencem a nenhum sistema ficam nos resultados como **fora do catálogo**, e são muitas vezes o achado mais importante.

## Resumo

- Pesquisa a tecnologia em todas as gamas públicas da instituição, sem ter de as escrever, e associa cada endereço ao sistema do catálogo.
- O filtro `net:` é sempre o da plataforma. Uma query com outro `net:` é recusada, e os resultados fora das gamas não são guardados.
- Os endereços, os nomes e os banners ficam cifrados na base de dados.
- Pesquisar e importar requer o papel **operador**; consultar os resultados está disponível para todos os papéis.
- Na instalação de teste, a API do Shodan e o InternetDB são recusados: são serviços externos e não há um segundo para onde apontar a instância de teste.
- Ver também {doc}`/platform/administration/shodan` e {doc}`security-catalogue`.
