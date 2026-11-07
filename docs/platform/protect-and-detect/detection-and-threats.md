# Deteção e inteligência de ameaças

Afinar as regras de deteção e silenciar falsos positivos com registo de quem decidiu; e os indicadores de compromisso, as fontes de alertas de segurança e os relatórios de recomendações — com a pesquisa de que sistemas têm um software ou um CVE.

```{video} 334-detecao-e-ameacas
```

Monitorizar não chega: é preciso afinar o que se deteta, e saber o que procurar. Nesta página vemos as regras de deteção, e a inteligência de ameaças.

## Onde fica no menu

**Menu:** Proteger › Soc › Regras de Deteção

```{figure} /_static/capturas/detecao-ameacas/menu.jpg
:alt: Menu lateral: Proteger › Soc › Regras de Deteção

O caminho no menu lateral: Proteger › Soc › Regras de Deteção.
```

1. No menu lateral, abra **Proteger**.
2. Dentro dele, abra **Soc**.
3. Clique em **Regras de Deteção**: abre o ecrã desta página.

## Porquê

O Anexo IV pede a consulta regular de fontes fidedignas sobre ameaças. O Anexo III pede a monitorização das redes para detetar incidentes. E a ISO 27001 pede as duas coisas: inteligência de ameaças e monitorização.

**Para que serve**

- O Anexo IV pede consulta regular de fontes de informação fidedignas sobre ameaças (H.FIC).
- O Anexo III pede monitorização das redes para detetar incidentes (DE.MC-1).
- A ISO/IEC 27001 pede inteligência de ameaças (controlo 5.7) e monitorização (8.16).

## A deteção

**Menu:** Proteger › SOC › Regras de Deteção

No menu Proteger, SOC, Regras de Deteção, três passos numerados: colar um exemplo do registo a detetar e gerar o pedido à inteligência artificial; colar a resposta e separar os componentes; aplicar ao gestor, com salvaguarda, validação e verificação.

Os Falsos Positivos fazem o caminho contrário: partindo de um alerta que não devia ter disparado, produz-se a regra que o silencia. Cada regra guarda quem a gravou e porquê: calar um alerta é uma decisão que alguém tem de poder explicar. E os pedidos à inteligência artificial saem sempre pseudonimizados.

```{figure} /_static/capturas/detecao-ameacas/abrir-1.jpg
:alt: Proteger › SOC › Regras de Deteção

O ecrã em Proteger › SOC › Regras de Deteção.
```

1. **Passo 1 — o pedido à IA, pseudonimizado**
2. **Passo 2 — separar a resposta**
3. **Passo 3 — aplicar, com salvaguarda**

## As ameaças

**Menu:** Detetar › IOC & Intelligence

No menu Detetar, os indicadores de compromisso: endereços e domínios maliciosos, importados de boletins como os do CERT.PT, com a ação — bloquear ou monitorizar —, a validade e a origem. Saem em listas que as firewalls e o sistema de monitorização vão buscar.

As fontes de segurança trazem os alertas publicados, e os relatórios de recomendações fazem a ponte entre «saiu um aviso» e «isto afeta estes três sistemas nossos». É essa ponte que distingue subscrever alertas de fazer inteligência de ameaças.

```{figure} /_static/capturas/detecao-ameacas/ioc-1.jpg
:alt: Detetar › IOC & Intelligence

O ecrã em Detetar › IOC & Intelligence (1 de 2).
```

1. Clique em **Gestão**.

```{figure} /_static/capturas/detecao-ameacas/ioc-2.jpg
:alt: Detetar › IOC & Intelligence

O ecrã em Detetar › IOC & Intelligence (2 de 2).
```

## Que sistemas são afetados

**Menu:** Detetar › IOC & Intelligence › Relatórios de Recomendações

E a ponte já não se faz de memória. Num relatório, Associar sistemas tem um separador Por software ou CVE: escreve-se um pacote com um operador e uma versão — aqui, o openssl até à 3.0.13 — ou um CVE, e a plataforma pergunta a todos os agentes Wazuh de uma vez e devolve os sistemas do catálogo onde ele está.

As versões comparam-se pelas regras do Debian ou do RPM, não como texto. Uma versão corrigida por backport vem marcada, e só fica de fora se alguém o decidir. Cada ocorrência traz os CVE que o Wazuh reporta para ela. E os agentes sem sistema no catálogo aparecem à parte, para se associarem a um sistema ou criarem um.

Aqui, a instância de teste recusa, e diz porquê: não há um segundo Wazuh para consultar. Na instância real, com o Indexer configurado, a resposta é a lista dos sistemas afetados, pronta a associar ao relatório.

```{figure} /_static/capturas/detecao-ameacas/relatorios-1.jpg
:alt: Detetar › IOC & Intelligence › Relatórios de Recomendações

O ecrã em Detetar › IOC & Intelligence › Relatórios de Recomendações (1 de 5).
```

1. Clique em **Novo Relatório**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-2.jpg
:alt: Detetar › IOC & Intelligence › Relatórios de Recomendações

O ecrã em Detetar › IOC & Intelligence › Relatórios de Recomendações (2 de 5).
```

1. Clique em **Associar sistemas**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-3.jpg
:alt: Detetar › IOC & Intelligence › Relatórios de Recomendações

O ecrã em Detetar › IOC & Intelligence › Relatórios de Recomendações (3 de 5).
```

1. Clique em **Por software / CVE**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-4.jpg
:alt: Detetar › IOC & Intelligence › Relatórios de Recomendações

O ecrã em Detetar › IOC & Intelligence › Relatórios de Recomendações (4 de 5).
```

1. Escreva «openssl» no campo **openssl**.
2. Escreva «3.0.13» no campo **versão (vazio = todas)**.
3. **Pesquisar nos agentes Wazuh**
4. Clique em **Pesquisar**.

```{figure} /_static/capturas/detecao-ameacas/relatorios-5.jpg
:alt: Detetar › IOC & Intelligence › Relatórios de Recomendações

O ecrã em Detetar › IOC & Intelligence › Relatórios de Recomendações (5 de 5).
```

1. **Excluir versões com backport (só em software)**
2. **N1**
3. **N2**

## Resumo

As listas de indicadores publicam-se num porto sem autenticação, de propósito: uma firewall não faz login. Por isso só as firewalls o devem alcançar.

E, com honestidade: os módulos Responder e Recuperar estão vazios nesta versão. A gestão de incidentes e a recuperação provam-se, por agora, com evidência carregada à mão.

**O que a plataforma faz — e o que não faz**

- Gera o pedido à IA e separa a resposta; aplicar ao gestor faz salvaguarda e validação.
- As listas de indicadores publicam-se num porto sem autenticação — só as firewalls o devem alcançar.
- A pesquisa por software ou CVE precisa do Wazuh Indexer; sem ele, diz o que falta em vez de uma lista vazia.
- Os módulos Responder e Recuperar estão vazios nesta versão: incidentes e recuperação provam-se por evidência manual.
