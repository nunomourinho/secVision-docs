# Deteção e inteligência de ameaças

Ajuste das regras de deteção e supressão de falsos positivos, com registo do decisor; indicadores de compromisso, fontes de alertas de segurança e relatórios de recomendações, com a pesquisa dos sistemas que têm um determinado software ou CVE.

```{video} 334-detecao-e-ameacas
```

A monitorização exige o ajuste das regras de deteção e o conhecimento das ameaças a procurar. Esta página descreve as regras de deteção e a inteligência de ameaças.

## Acesso

**Proteger** > **SOC** > **Regras de Deteção**

```{figure} /_static/capturas/detecao-ameacas/menu.jpg
:alt: Menu lateral: Proteger > SOC > Regras de Deteção

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

O Anexo IV exige a consulta regular de fontes fidedignas sobre ameaças, e o Anexo III exige a monitorização das redes para deteção de incidentes. A ISO 27001 exige ambos: inteligência de ameaças e monitorização.

**Finalidade**

- O Anexo IV exige a consulta regular de fontes de informação fidedignas sobre ameaças (H.FIC).
- O Anexo III exige a monitorização das redes para deteção de incidentes (DE.MC-1).
- A ISO/IEC 27001 exige inteligência de ameaças (controlo 5.7) e monitorização (8.16).

## Regras de deteção

O ecrã organiza-se em três passos numerados.

```{figure} /_static/capturas/detecao-ameacas/abrir-1.jpg
:alt: Proteger > SOC > Regras de Deteção

Ecrã **Proteger** > **SOC** > **Regras de Deteção**.
```

No ecrã, encontra os seguintes elementos:

1. **Passo 1:** Colar um exemplo do registo a detetar e gerar o pedido pseudonimizado à inteligência artificial.
2. **Passo 2:** Colar a resposta e separar os componentes.
3. **Passo 3:** Aplicar ao gestor, com salvaguarda, validação e verificação.

O ecrã **Falsos Positivos** segue o processo inverso: a partir de um alerta indevido, é produzida a regra que o suprime. Cada regra regista o autor e o motivo, uma vez que a supressão de um alerta é uma decisão que tem de ser justificável. Os pedidos à inteligência artificial são sempre pseudonimizados.

## Ameaças

**Detetar** > **IOC & Intelligence**

Este ecrã apresenta os indicadores de compromisso: endereços e domínios maliciosos, importados de boletins como os do CERT.PT, com a ação (bloquear ou monitorizar), a validade e a origem. Os indicadores são publicados em listas consultadas pelas firewalls e pelo sistema de monitorização.

As fontes de segurança disponibilizam os alertas publicados, e os relatórios de recomendações relacionam cada aviso com os sistemas da organização afetados. Esta relação distingue a subscrição de alertas da inteligência de ameaças.

```{figure} /_static/capturas/detecao-ameacas/ioc-1.jpg
:alt: Detetar > IOC & Intelligence

Ecrã **Detetar** > **IOC & Intelligence** (1 de 2).
```

1. Separador **Gestão:** Apresenta a gestão dos indicadores.

```{figure} /_static/capturas/detecao-ameacas/ioc-2.jpg
:alt: Detetar > IOC & Intelligence

Ecrã **Detetar** > **IOC & Intelligence** (2 de 2).
```

## Sistemas afetados

**Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações**

A identificação dos sistemas afetados é automatizada. Num relatório, a opção **Associar sistemas** inclui o separador **Por software / CVE**: indique um pacote com operador e versão (neste exemplo, o openssl até à versão 3.0.13) ou um CVE, e a plataforma consulta todos os agentes Wazuh em simultâneo e devolve os sistemas do catálogo onde o pacote está instalado.

As versões são comparadas segundo as regras do Debian ou do RPM, e não como texto. Uma versão corrigida por backport é assinalada e só é excluída por decisão explícita. Cada ocorrência indica os CVE reportados pelo Wazuh. Os agentes sem sistema no catálogo são apresentados separadamente, para associação a um sistema existente ou criação de um novo.

Na instância de teste, a pesquisa é recusada, com indicação do motivo: não existe um segundo Wazuh para consulta. Na instância real, com o Indexer configurado, o resultado é a lista dos sistemas afetados, pronta a associar ao relatório.

```{figure} /_static/capturas/detecao-ameacas/relatorios-1.jpg
:alt: Detetar > IOC & Intelligence > Relatórios de Recomendações

Ecrã **Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** (1 de 5).
```

**Como pesquisar:**

1. Clique em **Novo Relatório**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-2.jpg
:alt: Detetar > IOC & Intelligence > Relatórios de Recomendações

Ecrã **Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** (2 de 5).
```

1. Clique em **Associar sistemas**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-3.jpg
:alt: Detetar > IOC & Intelligence > Relatórios de Recomendações

Ecrã **Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** (3 de 5).
```

1. Clique em **Por software / CVE**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-4.jpg
:alt: Detetar > IOC & Intelligence > Relatórios de Recomendações

Ecrã **Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** (4 de 5).
```

1. Introduza «openssl» no campo do pacote.
2. Introduza «3.0.13» no campo **versão (vazio = todas)**.
3. Opção **Pesquisar nos agentes Wazuh:** Define a origem da pesquisa.
4. Clique em **Pesquisar**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-5.jpg
:alt: Detetar > IOC & Intelligence > Relatórios de Recomendações

Ecrã **Detetar** > **IOC & Intelligence** > **Relatórios de Recomendações** (5 de 5).
```

No resultado, encontra os seguintes elementos:

1. Opção **Excluir versões com backport (só em software).**
2. **N1:** Sistemas afetados de nível N1.
3. **N2:** Sistemas afetados de nível N2.

## Resumo

As listas de indicadores são publicadas numa porta sem autenticação, uma vez que as firewalls não suportam início de sessão. Por este motivo, apenas as firewalls devem ter acesso a essa porta.

Os módulos Responder e Recuperar estão vazios nesta versão. A gestão de incidentes e a recuperação são demonstradas, nesta fase, com evidência carregada manualmente.

**Funcionalidades e limitações**

- Gera o pedido à IA e separa a resposta; a aplicação ao gestor inclui salvaguarda e validação.
- As listas de indicadores são publicadas numa porta sem autenticação, que deve estar acessível apenas às firewalls.
- A pesquisa por software ou CVE requer o Wazuh Indexer; sem este, é indicado o elemento em falta em vez de uma lista vazia.
- Os módulos Responder e Recuperar estão vazios nesta versão: incidentes e recuperação são demonstrados por evidência manual.
