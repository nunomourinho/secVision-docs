# Classificar alertas e ensaiar regras

Duas ferramentas para quem afina a deteção: a classificação de um alerta com IA — falso positivo ou alerta real, com confiança, impacto e prioridade, guardada — e o Wazuh Rule Studio, que importa as regras do gestor e as ensaia num Wazuh próprio, em Docker, sem tocar no de produção.

```{video} 508-classificar-e-studio
```

Este é o último página do módulo sobre o Wazuh. Duas ferramentas para quem afina a deteção: uma ajuda a decidir se um alerta é falso, a outra ensaia regras sem tocar no gestor.

## Classificar

**Menu:** Wazuh › Threat Hunting › Events

Começa-se no Wazuh, como nos falsos positivos: o alerta 5710 da base de dados 003, aberto, e o documento copiado.

```{figure} /_static/capturas/wazuh-clf-studio/wazuh-1.jpg
:alt: Wazuh › Threat Hunting › Events

O ecrã em Wazuh › Threat Hunting › Events (1 de 2).
```

1. Escreva «rule.id : 5710 and agent.name : "base-de-dados-003"» no campo **Start typing to search and filter the wazuh-discover-search-**.

```{figure} /_static/capturas/wazuh-clf-studio/wazuh-2.jpg
:alt: Wazuh › Threat Hunting › Events

O ecrã em Wazuh › Threat Hunting › Events (2 de 2).
```

**Menu:** Proteger › SOC › Falsos Positivos › Classificar

No SecVision, colado o alerta, Classificar FP ou Alerta Real prepara um pedido diferente: em vez de uma regra, pede uma opinião fundamentada, com evidências tiradas do próprio alerta. Sai anonimizado, como os outros.

O pedido diz à IA o critério: na dúvida, classificar como alerta real, com confiança baixa. É mais barato investigar um falso alarme do que ignorar um ataque.

```{figure} /_static/img/508-classificar-e-studio/02.jpg
:alt: Proteger › SOC › Falsos Positivos › Classificar

O ecrã em Proteger › SOC › Falsos Positivos › Classificar.
```

Copia-se o pedido e leva-se ao assistente de inteligência artificial. Cola-se e envia-se: o alerta vai com a máquina, a conta e o endereço trocados por etiquetas.

```{figure} /_static/img/508-classificar-e-studio/03.jpg
:alt: O pedido de classificação, pseudonimizado, colado no assistente de IA

O pedido, colado no assistente de IA. A janela é desenhada para o vídeo; o pedido e a resposta são reais, processados por um modelo de IA.
```

A resposta vem nos blocos pedidos. E repare na decisão: alerta real, com sessenta por cento de confiança. Um só evento, com uma conta que não existe, pode ser engano, mas também pode ser alguém a testar nomes. Na dúvida, investiga-se.

```{figure} /_static/img/508-classificar-e-studio/04.jpg
:alt: A resposta do assistente: alerta real, sessenta por cento de confiança

A resposta real do modelo: ALERTA_REAL, com 60 % de confiança, ainda com as etiquetas.
```

Colada a resposta, a plataforma repõe sozinha os valores reais e lê-a em quadro: a classificação, a confiança, as evidências, o impacto, a prioridade (investigar) e as sugestões, a começar por procurar outros eventos do mesmo endereço.

Guardada, a análise fica no histórico, com quem a fez. Se depois se criar a regra de falso positivo, há um registo de porquê, que é o que um auditor pergunta.

```{figure} /_static/img/508-classificar-e-studio/05.jpg
:alt: A análise lida em quadro, com os valores reais

A análise lida em quadro, com as etiquetas repostas.
```

## O Rule Studio

**Menu:** Wazuh › Server management › Rules

Agora o Rule Studio. Primeiro, o que está no gestor: no painel do Wazuh, nas regras personalizadas, o ficheiro das deteções que aplicámos na página anterior.

```{figure} /_static/img/508-classificar-e-studio/06.jpg
:alt: Wazuh › Server management › Rules

O ecrã em Wazuh › Server management › Rules.
```

**Menu:** Proteger › SOC › Wazuh Rule Studio

No Wazuh Rule Studio, Importar do servidor Wazuh lista os ficheiros de regras e de decoders do gestor. Escolhem-se os das deteções, e importam-se. Na vista de desenho, cada decoder e cada regra é um nó, ligado ao que o alimenta.

O Studio não mexe no gestor. As regras importadas ficam numa base própria, onde se podem mudar à vontade.

```{figure} /_static/img/508-classificar-e-studio/07.jpg
:alt: Proteger › SOC › Wazuh Rule Studio

O ecrã em Proteger › SOC › Wazuh Rule Studio.
```

## Ensaiar

**Menu:** Wazuh Rule Studio › Testes

Para ensaiar, o Studio levanta um Wazuh só dele, num contentor, na mesma versão do gestor.

```{figure} /_static/img/508-classificar-e-studio/08.jpg
:alt: Wazuh Rule Studio › Testes

O ecrã em Wazuh Rule Studio › Testes.
```

**Menu:** Wazuh Rule Studio › Testes

O contentor arranca, o analisador carrega as regras de origem, e o estado passa a pronto.

```{figure} /_static/img/508-classificar-e-studio/09.jpg
:alt: Wazuh Rule Studio › Testes

O ecrã em Wazuh Rule Studio › Testes.
```

**Menu:** Wazuh Rule Studio › Testes

Sincronizar envia as regras do Studio para esse Wazuh de ensaio. A linha da aplicação, testada, dispara a regra de deteção, tal como no gestor.

É aqui que se experimenta uma alteração antes de a aplicar: se a regra mudada deixar de disparar, ou disparar a mais, vê-se no ensaio, e o gestor nunca reinicia por causa de um erro.

```{figure} /_static/img/508-classificar-e-studio/10.jpg
:alt: Wazuh Rule Studio › Testes

O ecrã em Wazuh Rule Studio › Testes.
```

## Resumo

A classificação deixa registo do porquê, e o Studio deixa experimentar sem risco.

E a IA dá uma opinião, nunca uma decisão. Quem decide é quem responde pela segurança da organização.

**O que a plataforma faz — e o que não faz**

- Prepara o pedido de classificação anonimizado, lê a resposta e guarda a análise com quem a fez.
- O Rule Studio importa as regras do gestor e ensaia-as num Wazuh próprio, sem tocar no de produção.
- Não decide por ninguém: a IA dá uma opinião; quem responde pela segurança decide.
