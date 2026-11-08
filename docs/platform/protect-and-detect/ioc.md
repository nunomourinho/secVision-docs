# Indicadores de compromisso (IOC)

Os indicadores de compromisso (endereços IP, gamas e domínios maliciosos) bloqueados ou monitorizados pela organização e os ficheiros consultados pelas firewalls e pelo SIEM.

```{video} 356-indicadores-de-compromisso
```

## Acesso

**Detetar** > **IOC & Intelligence** > **Indicadores de Compromisso**

```{figure} /_static/capturas/ioc/menu.jpg
:alt: Menu lateral: Detetar > IOC & Intelligence > Indicadores de Compromisso

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

Os indicadores podem ter diversas origens: um boletim do CERT.PT, um relatório de incidente ou o MISP. Este ecrã responde ao controlo 5.7 da ISO/IEC 27001 (inteligência de ameaças). Os indicadores devem chegar às firewalls e ao SIEM, com validade definida, e nunca devem bloquear um sistema da própria organização.

## Separadores

```{figure} /_static/capturas/ioc/separadores-1.jpg
:alt: Os cinco separadores do ecrã, cada um uma tarefa diferente

Os cinco separadores do ecrã, cada um com uma função distinta.
```

No ecrã, encontra os seguintes separadores:

1. **Importar:** Introdução de indicadores.
2. **Gestão:** Lista dos indicadores ativos.
3. **Feeds:** Ficheiros publicados para as firewalls e o SIEM.
4. **Whitelist:** Endereços e domínios que nunca devem ser bloqueados.
5. **Configurações:** Prazos e endereço base.

## Importar

```{figure} /_static/capturas/ioc/importar-1.jpg
:alt: O separador Importar: os formatos, a descrição e os indicadores

O separador **Importar**: formatos, descrição e indicadores.
```

No ecrã, encontra os seguintes elementos:

1. **Formatos aceites:** CSV (`valor,ação`), formato de relatório (linhas com traço de um boletim) e lista simples.
2. **Descrição:** Campo obrigatório que identifica a origem dos indicadores.
3. Botão **Importar ficheiro:** Carrega um ficheiro `.csv` ou `.txt`.
4. **Indicadores:** Campo para colar a lista.

**Como importar:** Cole a lista ou carregue um ficheiro, preencha a descrição e confirme. Os valores podem estar em formato *defanged*, como `site[.]perigoso[.]pt`, habitual nos boletins; a plataforma repõe os pontos. As ações válidas são `bloquear` e `monitorizar`; numa lista sem ação, a plataforma solicita a sua indicação.

A validade de cada importação corresponde ao prazo padrão (definido em **Configurações**) e pode ser alterada no momento da importação. A reimportação não gera duplicados: um indicador com a mesma ação é atualizado.

```{figure} /_static/capturas/ioc/emergencia-1.jpg
:alt: O Bloqueio de Emergência, mais abaixo no mesmo separador

O **Bloqueio de Emergência**, no mesmo separador.
```

1. **Bloqueio de Emergência:** Destinado a incidentes em curso, como um C2 confirmado.
2. **Indicadores de emergência:** Registados como **permanentes**, sem validade, até ao desbloqueio manual.

## Gestão

```{figure} /_static/capturas/ioc/gestao-2.jpg
:alt: O separador Gestão: as contagens, os filtros e a lista

O separador **Gestão**: contagens, filtros e lista.
```

No ecrã, encontra os seguintes elementos:

1. **Contagens:** Por tipo e ação; filtram a lista quando selecionadas.
2. **Filtros.**
3. **Seleção em massa:** Permite apagar ou alterar a data de expiração de vários indicadores em simultâneo.
4. **Ações por linha:** O escudo ativa a emergência, o lápis edita e o caixote apaga.

A lista apresenta a ação, a validade e a origem de cada indicador. A coluna da expiração indica os dias restantes ou, se o indicador já tiver expirado, «há X dias». Os indicadores expirados deixam de constar dos feeds.

## Feeds

```{figure} /_static/capturas/ioc/feeds-2.jpg
:alt: O separador Feeds: o endereço base e um ficheiro por tipo e ação

O separador **Feeds**: endereço base e um ficheiro por tipo e ação.
```

No ecrã, encontra os seguintes elementos:

1. **Endereço base dos feeds.**
2. **Ficheiro de feed:** Cada cartão corresponde a um ficheiro, com os botões **Abrir** e **Copiar URL**.
3. Botão **Copiar URL:** Copia o endereço do ficheiro.

São publicados oito ficheiros de texto, com um valor por linha: os IP e os domínios a bloquear e a monitorizar, as versões resolvidas por DNS e as versões consolidadas. Os ficheiros são gerados diariamente às 2h, ou manualmente, e publicados na porta **8081**, para consulta pelas firewalls, pelo EDR e pelo SIEM.

```{important}
**A porta 8081 não exige autenticação:** um equipamento de rede que obtém uma lista não suporta início de sessão. Apenas as firewalls devem ter acesso a esta porta; restrinja o acesso na rede.
```

## Whitelist

```{figure} /_static/capturas/ioc/whitelist-2.jpg
:alt: A whitelist automática, derivada do catálogo de segurança

A whitelist automática, derivada do catálogo de segurança.
```

No ecrã, encontra os seguintes elementos:

1. **Whitelist automática:** IP e domínios dos sistemas do catálogo de segurança e IP resolvidos desses domínios.
2. Botão **Resolver domínios:** Repete de imediato a resolução dos domínios.

A whitelist contém os endereços que nunca devem ser bloqueados, mesmo que constem de um feed.

```{figure} /_static/capturas/ioc/whitelist-manual-1.jpg
:alt: A whitelist manual, mais abaixo

A whitelist manual.
```

1. **Whitelist manual:** Para os restantes casos, como um parceiro ou um serviço na nuvem.
2. **IP ou domínio:** Campo de introdução, acompanhado de uma nota com o motivo.

Quando um indicador importado coincide com a whitelist, a plataforma apresenta um aviso no topo de todos os ecrãs até à decisão.

## Configurações

```{figure} /_static/capturas/ioc/configuracoes-2.jpg
:alt: O separador Configurações

O separador **Configurações**.
```

No ecrã, encontra os seguintes elementos:

1. **Prazo de validade padrão.**
2. **Validade dos IP resolvidos por DNS.**
3. **URL base dos feeds.**

## Resumo

- A importação aceita qualquer origem, incluindo o formato *defanged* dos boletins.
- Os indicadores ativos são publicados em ficheiros de texto na porta 8081, para as firewalls e o SIEM.
- A whitelist impede o bloqueio indevido dos sistemas da própria organização.
- Ver também {doc}`detection-and-threats` e {doc}`/platform/administration/misp`.
