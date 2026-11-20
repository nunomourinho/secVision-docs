# Grupos, unidades e organograma

Organização da instituição: grupos de pessoas, bens e serviços, unidades orgânicas com governo central ou delegado, e o organograma que reúne unidades, papéis e pessoas.

```{video} 315-grupos-e-organograma
```

Uma instituição é composta por escolas, departamentos, laboratórios e serviços. Esta página descreve a organização da instituição na plataforma, em grupos e unidades, e o organograma que os reúne.

## Acesso

**Identificar** > **Inventário** > **Grupos de ativos**

```{figure} /_static/capturas/grupos-organograma/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Grupos de ativos

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Famílias de grupos

Os grupos dividem-se em quatro famílias: pessoas, bens, serviços e unidades orgânicas. Uma unidade orgânica tem, adicionalmente, uma posição na hierarquia (escola, departamento, laboratório) e um modelo de governo.

O governo central significa que o risco e os controlos são geridos pela organização. O governo delegado significa que a unidade os gere separadamente, com responsável próprio. A responsabilidade perante terceiros mantém-se, em ambos os casos, na instituição.

**As quatro famílias de grupos**

| Família | Exemplos |
|---|---|
| Pessoas | «Direção Financeira», «Docentes» |
| Bens | «Centro de dados», «Postos de trabalho» |
| Serviços | «Serviços expostos à Internet» |
| Unidade orgânica | parte da instituição com governo próprio, central ou delegado |

## Grupos

Os grupos são apresentados por família. Os membros de cada grupo são ativos de informação e pessoas do registo de pessoal.

Os grupos têm três finalidades: detalhar a Declaração de Aplicabilidade por grupo, delimitar o âmbito de uma evidência e constituir o objeto de uma auditoria. Uma evidência sem grupo aplica-se a toda a organização.

```{figure} /_static/capturas/grupos-organograma/abrir-1.jpg
:alt: Identificar > Inventário > Grupos de ativos

Ecrã **Identificar** > **Inventário** > **Grupos de ativos** (1 de 2).
```

1. **Unidades orgânicas:** Grupos da família de unidades orgânicas.

```{figure} /_static/capturas/grupos-organograma/abrir-2.jpg
:alt: Identificar > Inventário > Grupos de ativos

Ecrã **Identificar** > **Inventário** > **Grupos de ativos** (2 de 2).
```

## Organograma

**Governar** > **Organização** > **Organograma**

O Organograma reúne três elementos já existentes: a árvore de unidades, os papéis atribuídos em cada unidade e as pessoas. A estrutura é também alterada neste ecrã: criação de uma unidade subordinada, designação de uma pessoa para um papel numa unidade ou encerramento de um mandato.

O organograma identifica as unidades com governo próprio sem responsável designado e as unidades sem posição na árvore. Pode ser exportado para os programas de diagramas habituais, sem dados pessoais por omissão.

```{figure} /_static/capturas/grupos-organograma/organograma-1.jpg
:alt: Governar > Organização > Organograma

Ecrã **Governar** > **Organização** > **Organograma** (1 de 2).
```

No ecrã, encontra os seguintes elementos:

1. **Edição da estrutura:** Criação de unidades, designações e encerramento de mandatos.
2. Opção **Com nomes:** Inclui os dados pessoais na exportação.

```{figure} /_static/capturas/grupos-organograma/organograma-2.jpg
:alt: Governar > Organização > Organograma

Ecrã **Governar** > **Organização** > **Organograma** (2 de 2).
```

### A estrutura em JSON, sem pessoas

O botão **Estrutura (.json)** descarrega as unidades (nome, espécie, governo central ou delegado, descrição, se estão ativas e de quem dependem) e nada mais: nem responsáveis, nem papéis, nem pessoas. Por isso, qualquer papel o pode descarregar. Serve para trabalhar a estrutura fora da plataforma e voltar a trazê-la.

**Importar estrutura…** (papel operador) lê o ficheiro e mostra o que muda antes de gravar: o que é novo, o que altera e o que já está igual. Uma unidade identificada pelo `id` mas que na plataforma tem outro nome vem desmarcada, com os dois nomes lado a lado, porque sobrepor tem de ser deliberado. Para criar uma unidade no ficheiro, dê-lhe um `ref` à sua escolha e, em `pai`, o `ref` da unidade de que depende (que pode ser outra unidade nova). **Nada se apaga**: para retirar uma unidade, ponha `"ativo": false`.

## Resumo

Solicite à secretaria-geral a estrutura orgânica, aos recursos humanos a composição de cada unidade e à direção a identificação das unidades com governo próprio.

A exportação do organograma com nomes fica registada na trilha de auditoria, e o nome do ficheiro inclui o respetivo aviso.

**Informação a solicitar e funcionalidades**

- Secretaria-geral e recursos humanos: estrutura orgânica e composição de cada unidade.
- Direção: unidades com governo próprio e respetivos responsáveis.
- A exportação com dados pessoais fica registada na trilha de auditoria, e o nome do ficheiro inclui o aviso.
