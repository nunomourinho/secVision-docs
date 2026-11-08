# O registo de risco

Registo de cada risco sobre um ativo de informação: ameaça, vulnerabilidade, probabilidade, impacto por critério, tratamento, controlos e eixo de atuação, risco inerente e residual.

```{video} 325-registo-de-risco
```

Com os critérios aprovados, os riscos são registados. Cada risco incide sobre um ativo de informação e identifica a ameaça, a vulnerabilidade explorada, a probabilidade e o impacto.

## Acesso

**Identificar** > **Risco** > **Registo de risco**

```{figure} /_static/capturas/registo-risco/menu.jpg
:alt: Menu lateral: Identificar > Risco > Registo de risco

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Campos

Cada risco regista o ativo, a ameaça e a vulnerabilidade, a probabilidade e o impacto em cada um dos três critérios. O impacto considerado é o maior dos critérios aplicáveis; por exemplo, um risco de divulgação não afeta a disponibilidade.

Os controlos associados indicam o eixo em que atuam. Uma cópia de segurança não reduz a probabilidade de um incêndio, mas reduz a perda; o controlo de acessos reduz a probabilidade de um apagamento acidental. O risco residual é reduzido no eixo correspondente.

**Campos de um risco**

| Campo | Descrição |
|---|---|
| Ativo | informação sobre a qual o risco incide |
| Ameaça e vulnerabilidade | selecionadas do catálogo ou introduzidas manualmente |
| Probabilidade | na escala dos critérios |
| Impacto por critério | confidencialidade, integridade, disponibilidade; o impacto considerado é o maior dos aplicáveis |
| Tratamento | mitigar, aceitar, transferir ou evitar |
| Controlos e eixo | controlos que reduzem o risco, pela probabilidade ou pela perda |
| Dono | responsável pelo risco |

## Configuração do ecrã

A matriz apresenta a distribuição dos riscos, e a lista apresenta cada risco com o código, o risco inerente, o risco residual e a banda (se os critérios estiverem aprovados).

```{figure} /_static/capturas/registo-risco/abrir-1.jpg
:alt: Identificar > Risco > Registo de risco

Ecrã **Identificar** > **Risco** > **Registo de risco**.
```

No ecrã, encontra os seguintes elementos:

1. **Matriz:** Distribuição dos riscos por probabilidade e impacto.
2. Botão **Assistente:** Apoia o registo de novos riscos.

O método mais rápido de registo é o botão **Apreciar riscos** na ficha do ativo, que propõe os modelos do catálogo aplicáveis ao tipo de ativo. As propostas só são gravadas após confirmação.

## Ficha do risco

Para além da apreciação, a ficha de cada risco inclui os blocos descritos nas páginas seguintes: plano de tratamento e respetiva aprovação, revisão periódica, retenção e comunicação e consulta.

A ficha inclui também o risco herdado do local: por exemplo, se o edifício tiver risco de inundação, os servidores nele instalados podem herdá-lo através da árvore de contenção. A plataforma propõe a herança, mas não a propaga automaticamente; um servidor com proteção própria pode ser excluído, e a não confirmação constitui igualmente uma decisão.

```{figure} /_static/capturas/registo-risco/risco-1.jpg
:alt: Um risco, aberto

Ficha de um risco (1 de 2).
```

1. Botão **Editar:** Ativa a edição do risco.

```{figure} /_static/capturas/registo-risco/risco-2.jpg
:alt: Um risco, aberto

Ficha de um risco (2 de 2).
```

No ecrã, encontra os seguintes campos:

1. **Título.**
2. **Ativo.**
3. **Dono do risco.**
4. **Ameaça do catálogo.**
5. **Vulnerabilidade do catálogo.**
6. **Ameaça:** Descrição livre.
7. **Vulnerabilidade:** Descrição livre.
8. **Probabilidade.**
9. **Impacto.**

## Resumo

A apreciação é realizada com o dono de cada ativo e com a equipa de informática, para as vulnerabilidades e os controlos existentes. A plataforma calcula o risco inerente e o residual; o tratamento é decidido pelo dono do risco.

**Informação a solicitar e funcionalidades**

- Dono de cada ativo: probabilidade e impacto, na terminologia da organização.
- Equipa de informática: vulnerabilidades conhecidas e controlos existentes.
- A plataforma calcula o risco inerente e o residual; o tratamento é decidido pelo dono do risco.
