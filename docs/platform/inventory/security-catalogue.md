# O catálogo de segurança e a cobertura

Os sistemas operados pela instituição, com o nível de criticidade (N1 a N4), a inclusão no âmbito e o estado de monitorização, e a taxa de cobertura resultante, apresentada no ponto de situação.

```{video} 313-catalogo-de-seguranca
```

```{video} 362-o-catalogo-e-os-agentes
```

O segundo vídeo mostra os agentes fora do catálogo e o filtro **Software / CVE**.

O inventário identifica os equipamentos existentes. O catálogo de segurança identifica os sistemas operados pela instituição, o respetivo nível de criticidade e o estado da monitorização de segurança, a partir dos quais é calculada a cobertura.

## Acesso

**Identificar** > **Inventário** > **Catálogo de Segurança**

```{figure} /_static/capturas/catalogo/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Catálogo de Segurança

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Níveis

Cada sistema tem um nível: N1 crítico, N2 estratégico, N3 operacional e N4 secundário. A cobertura considera os três primeiros níveis; o N4 está excluído por omissão.

Cada sistema está monitorizado ou em GAP (incluído no âmbito, mas sem monitorização de segurança ativa). Os dias em GAP são calculados desde a transição, no momento da consulta, e não são gravados.

**Os quatro níveis**

| Nível | Significado | Incluído na cobertura |
|---|---|---|
| N1 | crítico: a sua falha interrompe a missão | sim |
| N2 | estratégico | sim |
| N3 | operacional | sim |
| N4 | secundário | não, por omissão |

```{tip}
A exclusão do N4 é configurada em **Administração** > **Cobertura**. Um sistema em GAP é um sistema incluído no âmbito sem monitorização ativa.
```

## Catálogo

```{figure} /_static/capturas/catalogo/abrir-1.jpg
:alt: Identificar > Inventário > Catálogo de Segurança

Ecrã **Identificar** > **Inventário** > **Catálogo de Segurança**.
```

No ecrã, encontra os seguintes filtros, a par do filtro por rede:

1. **Nível:** De N1 a N4.
2. **Estado:** Monitorizado ou GAP.
3. **Ativo de informação:** Sistemas com ou sem ativo de informação associado.

O botão **Software / CVE** pergunta aos agentes Wazuh que sistemas têm um programa numa dada versão (com um operador: `<=`, `<`, `=`, `>=` ou `>`; sem versão, conta qualquer versão) ou um CVE. Só entram sistemas com agente Wazuh ligado. A resposta mostra, por termo, quantos sistemas e quantas ocorrências, e por baixo de cada sistema os pacotes e os CVE que o Wazuh reporta. As versões comparam-se pelas regras do Debian e do RPM; um pacote com **backport** (a distribuição aplicou a correção sem mudar o número da versão) vem marcado, e a opção **Excluir versões com backport** deixa-os de fora. Marcados os sistemas, **Filtrar o catálogo por estes N sistemas** reduz a tabela a esses, com o que foi encontrado por baixo de cada nome, e as ações em massa (nível, varreduras, mapear a ativos) aplicam-se a eles. A mesma pesquisa existe nos relatórios de recomendações, para associar os sistemas afetados ({doc}`/wazuh/software-and-cve-search`).

Ao lado dos filtros, o botão **Exposição Shodan** pesquisa no Shodan onde, nas gamas públicas da instituição, está exposta uma tecnologia, e filtra a tabela pelos sistemas que a expõem (ver {doc}`shodan-exposure`).

O botão **Agentes fora do catálogo** lista os agentes do Wazuh que não estão associados a nenhum sistema e permite associá-los ou criar o sistema a partir deles (ver {doc}`/wazuh/systems-and-agents`).

## Responsáveis

```{video} 364-os-responsaveis-de-cada-sistema
```

**Identificar** > **Inventário** > **Catálogo de Segurança** > **Editar sistema** > **Responsáveis**

Cada sistema liga-se a quem responde por ele, em três campos, cada um ao seu registo:

1. **Proprietário:** Uma pessoa do registo de pessoal ({doc}`/platform/organisation/roles-and-people`), procurada pelo nome ou pelo e-mail. O e-mail é o do registo, que a sincronização com o Active Directory mantém. É a pessoa a quem se escreve quando o sistema tem um problema que ela resolve ou decide.
2. **Fornecedor que o mantém:** Um fornecedor do registo de fornecedores. Uma empresa alojada ou uma entidade parceira não entra, porque não mantém sistemas.
3. **Grupo ou unidade:** Um grupo ativo. Um grupo desativado não recebe sistemas novos.

O campo **Ou descrever em texto** mantém-se para o que não é pessoa do registo, como um órgão ou um consultor externo. Uma pessoa que já saiu da organização não pode ser escolhida para uma ligação nova; a que já estava ligada continua, com a indicação **saiu**, até ser escolhida a pessoa que a substituiu.

```{figure} /_static/img/364-os-responsaveis-de-cada-sistema/02.jpg
:alt: Editar sistema > Responsáveis

O bloco **Responsáveis** na edição do sistema.
```

Na tabela, a coluna **Proprietário** apresenta a pessoa e o e-mail. Um nome registado apenas em texto aparece em itálico, com a indicação «(não ligado)».

Na ficha do sistema, **Escrever a…** abre uma janela onde se escreve o **assunto** da mensagem. O assunto vem preenchido com o nome do sistema, que pode ser apagado, e a mensagem não identifica nenhuma ferramenta. O botão **Abrir o correio** abre o programa de correio com o destinatário e esse assunto, e a mensagem é escrita aí. O mesmo está disponível para o fornecedor, quando o contacto registado inclui um e-mail.

```{figure} /_static/img/364-os-responsaveis-de-cada-sistema/03.jpg
:alt: Ficha do sistema > Escrever a

A janela **Escrever a…**, com o assunto escolhido por quem escreve.
```

Os filtros **Proprietário**, **Fornecedor** e **Grupo** apresentam os sistemas de cada um. **Sem proprietário ligado** apresenta os sistemas que ainda não têm pessoa associada; um nome registado só em texto conta como sem proprietário, porque não permite o contacto. Com vários sistemas selecionados, **Definir responsáveis…** altera os três campos de uma vez, apenas nos que forem marcados.

**Ligar proprietários escritos à mão…** compara cada nome do campo de texto com o registo de pessoal e não grava nada sem confirmação. Os nomes iguais vêm propostos; os parecidos e os que correspondem a duas pessoas com o mesmo nome ficam por escolher; uma pessoa que já saiu não é proposta. **Ligar os confirmados** grava apenas esses, e o texto mantém-se.

```{figure} /_static/img/364-os-responsaveis-de-cada-sistema/04.jpg
:alt: Ligar proprietários escritos à mão

A ligação dos nomes escritos à mão às pessoas do registo.
```

Um fornecedor ou um grupo que ainda é responsável por sistemas não pode ser apagado: a plataforma indica quantos são. Apagar uma pessoa do registo retira-a dos sistemas, e o nome em texto, se existir, mantém-se.

Um sistema sem ativo de informação associado é apresentado a âmbar. Esta indicação não significa risco nulo, mas sim que o risco da informação que suporta ainda não foi apreciado. Este tema é descrito na página seguinte.

## Ponto de situação

**Identificar** > **Inventário** > **Visão Geral**

A Visão Geral apresenta o resumo desta fase em quatro indicadores: sistemas no âmbito, sistemas monitorizados, sistemas em GAP e taxa de cobertura global. São também apresentadas a cobertura por camada (N1 a N4) e os sistemas em GAP por sistema operativo e por tipo.

Esta informação permite, por exemplo, identificar que os sistemas em GAP são servidores do mesmo tipo, que podem ser corrigidos da mesma forma. Enquanto existirem sistemas em GAP, é apresentado um aviso com ligação ao ecrã de instalação do agente de monitorização.

```{figure} /_static/capturas/catalogo/dashboard-1.jpg
:alt: Identificar > Inventário > Visão Geral

Ecrã **Identificar** > **Inventário** > **Visão Geral** (1 de 2).
```

1. **Aviso de sistemas em GAP:** Ligação direta ao instalador do agente.

```{figure} /_static/capturas/catalogo/dashboard-2.jpg
:alt: Identificar > Inventário > Visão Geral

Ecrã **Identificar** > **Inventário** > **Visão Geral** (2 de 2).
```

## Resumo

O nível de cada sistema é uma decisão de negócio e não técnica, pelo que deve ser definido com a direção e os donos dos serviços. A identificação dos sistemas monitorizados deve ser solicitada à equipa de informática.

A taxa de cobertura indica sempre, em rodapé, os níveis excluídos, uma vez que uma taxa sem o denominador visível não é adequada para apresentação.

**Informação a solicitar e funcionalidades**

- Direção e donos dos serviços: nível de cada sistema, uma decisão de negócio e não técnica.
- Equipa de informática: sistemas com monitorização de segurança ativa.
- A taxa indica sempre os níveis excluídos: uma taxa sem o denominador visível não é adequada para apresentação.
- Cada sistema liga-se ao proprietário (uma pessoa do registo, com o e-mail), ao fornecedor que o mantém e ao grupo a que pertence; a plataforma prepara o destinatário e o assunto, e a mensagem é escrita por quem a envia.
