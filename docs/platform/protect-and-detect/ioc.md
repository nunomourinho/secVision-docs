# Indicadores de compromisso (IOC)

Os indicadores de compromisso (endereços IP, gamas e domínios maliciosos) que a organização bloqueia ou vigia, e os ficheiros que as firewalls e o SIEM vão buscar.

```{video} 356-indicadores-de-compromisso
```

## Onde fica no menu

**Menu:** Detetar › IOC & Intelligence › Indicadores de Compromisso

```{figure} /_static/capturas/ioc/menu.jpg
:alt: Menu lateral: Detetar › IOC & Intelligence › Indicadores de Compromisso

O caminho no menu lateral: Detetar › IOC & Intelligence › Indicadores de Compromisso.
```

1. No menu lateral, abra **Detetar**.
2. Dentro dele, abra **IOC & Intelligence**.
3. Clique em **Indicadores de Compromisso**: abre o ecrã desta página.


## Porquê

Os indicadores chegam de onde vierem: um boletim do CERT.PT, um relatório de incidente, o MISP. Serve o controlo 5.7 da ISO/IEC 27001, inteligência de ameaças. O que importa é que cheguem às firewalls e ao SIEM, com uma validade, e que nunca bloqueiem um sistema da própria organização.

## Os cinco separadores

```{figure} /_static/capturas/ioc/separadores-1.jpg
:alt: Os cinco separadores do ecrã, cada um uma tarefa diferente

Os cinco separadores do ecrã, cada um uma tarefa diferente.
```

1. **Importar**
2. **Gestão**
3. **Feeds**
4. **Whitelist**
5. **Configurações**
6. Clique em **Importar**.


## Importar

```{figure} /_static/capturas/ioc/importar-1.jpg
:alt: O separador Importar: os formatos, a descrição e os indicadores

O separador Importar: os formatos, a descrição e os indicadores.
```

1. **Os formatos aceites**
2. **Descrição (obrigatória)**
3. **Importar ficheiro**
4. **Os indicadores, colados**


Cole a lista ou carregue um ficheiro `.csv` ou `.txt`. São aceites o formato CSV (`valor,ação`), o formato relatório (as linhas com traço de um boletim) e a lista simples. Os valores podem vir em formato *defanged*, como `site[.]perigoso[.]pt`, que é como chegam nos boletins: a plataforma repõe os pontos. As ações válidas são `bloquear` e `monitorizar`; numa lista sem ação, a plataforma pergunta.

A **descrição** é obrigatória e diz de onde vieram os indicadores. A validade de cada importação vem do prazo padrão (em **Configurações**) e pode mudar-se no momento.

Reimportar não duplica: um indicador com a mesma ação é atualizado.

```{figure} /_static/capturas/ioc/emergencia-1.jpg
:alt: O Bloqueio de Emergência, mais abaixo no mesmo separador

O Bloqueio de Emergência, mais abaixo no mesmo separador.
```

1. **Bloqueio de Emergência**
2. **Os indicadores de emergência**


O **Bloqueio de Emergência** é para um incidente em curso, como um C2 confirmado: os indicadores entram como **permanentes**, sem validade, até alguém os desbloquear à mão.

## Gestão

```{figure} /_static/capturas/ioc/gestao-2.jpg
:alt: O separador Gestão: as contagens, os filtros e a lista

O separador Gestão: as contagens, os filtros e a lista.
```

1. **As contagens, por tipo e ação**
2. **Os filtros**
3. **Seleção em massa**
4. **Emergência, editar, apagar**


A lista viva, com a ação, a validade e a origem de cada indicador. As contagens de cima filtram a lista. Seleciona-se em massa para apagar ou mudar a data de expiração de vários de uma vez. Em cada linha, o escudo ativa a emergência, o lápis edita e o caixote apaga. A coluna da expiração mostra os dias que faltam, ou «há X dias» se já expirou: um indicador expirado sai dos feeds.

## Feeds

```{figure} /_static/capturas/ioc/feeds-2.jpg
:alt: O separador Feeds: o endereço base e um ficheiro por tipo e ação

O separador Feeds: o endereço base e um ficheiro por tipo e ação.
```

1. **O endereço base dos feeds**
2. **Um ficheiro de feed**
3. **Copiar o endereço**


O que sai para fora: oito ficheiros de texto, um valor por linha. São os IPs e os domínios a bloquear e a monitorizar, mais as versões resolvidas por DNS e as consolidadas. São gerados todos os dias às 2h, ou à mão, e publicados no porto **8081** para as firewalls, o EDR e o SIEM os irem buscar. Cada cartão tem o endereço do ficheiro e os botões **Abrir** e **Copiar URL**.

```{important}
**O porto 8081 não tem autenticação, de propósito:** um equipamento de rede que vai buscar uma lista não faz *login*. Quem tem de o alcançar são as firewalls e mais ninguém. Restrinja-o na rede.
```

## Whitelist

```{figure} /_static/capturas/ioc/whitelist-2.jpg
:alt: A whitelist automática, derivada do catálogo de segurança

A whitelist automática, derivada do catálogo de segurança.
```

1. **Do catálogo de segurança, automática**
2. **Resolver domínios**


O que nunca deve ser bloqueado, por muito que apareça num feed. A parte de cima é **automática**: os IPs e os domínios dos sistemas do catálogo de segurança, e os IPs resolvidos desses domínios. **Resolver domínios** volta a resolvê-los já.

```{figure} /_static/capturas/ioc/whitelist-manual-1.jpg
:alt: A whitelist manual, mais abaixo

A whitelist manual, mais abaixo.
```

1. **A whitelist manual**
2. **IP ou domínio**


A **whitelist manual** é para o resto: um parceiro, um serviço na nuvem. Escreva o IP ou o domínio e uma nota a dizer porquê. Quando um indicador importado coincide com a whitelist, a plataforma mostra um aviso no topo de todos os ecrãs até alguém decidir.

## Configurações

```{figure} /_static/capturas/ioc/configuracoes-2.jpg
:alt: O separador Configurações

O separador Configurações.
```

1. **Prazo de validade padrão**
2. **Validade dos IPs resolvidos por DNS**
3. **URL base dos feeds**


## Resumo

- Importa-se de qualquer origem, incluindo o formato *defanged* dos boletins.
- Os indicadores ativos saem em ficheiros de texto no porto 8081, para as firewalls e o SIEM.
- A whitelist protege os sistemas da própria organização de um bloqueio por engano.
- Ver também {doc}`detection-and-threats` e {doc}`/platform/administration/misp`.
