# Segurança do software e da configuração

Inventário das dependências e respetivas vulnerabilidades, análise estática do código com registo de aceitações e conformidade da configuração dos sistemas com perfis CIS ou STIG.

```{video} 336-seguranca-do-software
```

A fase de implementação termina com três ferramentas técnicas: o inventário das dependências do software, a análise do código e a conformidade da configuração dos sistemas.

## Acesso

**Proteger** > **Segurança do Software** > **Análise SAST**

```{figure} /_static/capturas/software/menu.jpg
:alt: Menu lateral: Proteger > Segurança do Software > Análise SAST

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Ferramentas

O relatório SBOM enumera as dependências do software e as vulnerabilidades conhecidas de cada uma. A análise SAST analisa diariamente o código à procura de falhas. A conformidade do sistema operativo compara a configuração com perfis de referência, como os do CIS.

No Anexo IV, estas ferramentas respondem às medidas de atualizações de segurança, de controlos nos sistemas e, no Grupo A, de securização das configurações.

**Três ferramentas**

| Ferramenta | Função | Anexo IV |
|---|---|---|
| Relatório SBOM | inventário das dependências e respetivas vulnerabilidades conhecidas | T.AS — atualizações |
| Análise SAST | análise estática diária do código e dos scripts | T.GPT — controlos nos sistemas |
| Conformidade do sistema operativo (SCAP) | comparação da configuração com perfis CIS ou STIG | T.SC — securização |

## Configuração do ecrã

**Proteger** > **Segurança do Software**

A análise SAST é executada diariamente; neste exemplo, não foram encontradas falhas. Uma falha que se decida não corrigir é aceite explicitamente, com registo do responsável pela aceitação, e não é ocultada.

```{figure} /_static/capturas/software/abrir-1.jpg
:alt: Proteger > Segurança do Software

Ecrã **Proteger** > **Segurança do Software**.
```

Na conformidade do sistema operativo, este ambiente de testes não tem o leitor SCAP instalado, e o ecrã indica o procedimento de instalação. Com o leitor instalado, os resultados das regras são classificados como passou, falhou, não aplicável e não verificado, e as regras aceites são contabilizadas separadamente.

O ecrã apresenta o seguinte aviso: a remediação automática não é reversível. A aplicação de um perfil completo numa máquina que executa a base de dados pode eliminá-la. Aplique a remediação regra a regra e nunca em produção sem salvaguarda prévia.

```{figure} /_static/capturas/software/scap-1.jpg
:alt: OS Compliance (SCAP)

OS Compliance (SCAP).
```

## Resumo

Para além do efeito técnico, estas ferramentas produzem evidência automática, que alimenta os recolectores da fase seguinte sem intervenção manual. Desta forma, a conformidade é demonstrada de forma contínua e não apenas antes da auditoria.

**Funcionalidades**

- Estas ferramentas alimentam a evidência automática da fase seguinte, sem intervenção manual.
- A conformidade é demonstrada de forma contínua, e não apenas antes da auditoria.
