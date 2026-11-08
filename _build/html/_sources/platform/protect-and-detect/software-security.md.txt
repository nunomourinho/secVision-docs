# Segurança do software e da configuração

O inventário de dependências e as suas vulnerabilidades, a análise estática do código com aceitações registadas, e a conformidade da configuração dos sistemas com perfis CIS ou STIG.

```{video} 336-seguranca-do-software
```

Três ferramentas técnicas fecham a fase de implementar: o inventário das dependências do software, a análise do código, e a conformidade da configuração dos sistemas.

## Onde fica no menu

**Menu:** Proteger › Segurança do software › Análise SAST

```{figure} /_static/capturas/software/menu.jpg
:alt: Menu lateral: Proteger › Segurança do software › Análise SAST

O caminho no menu lateral: Proteger › Segurança do software › Análise SAST.
```

1. No menu lateral, abra **Proteger**.
2. Dentro dele, abra **Segurança do software**.
3. Clique em **Análise SAST**: abre o ecrã desta página.

## As ferramentas

O relatório SBOM lista as dependências do software e as vulnerabilidades conhecidas de cada uma. A análise SAST lê o código à procura de falhas, todos os dias. E a conformidade do sistema operativo compara a configuração com perfis de referência, como os do CIS.

No Anexo IV, servem as atualizações de segurança, os controlos nos sistemas, e — no Grupo A — a securização das configurações.

**Três ferramentas**

| Ferramenta | O que faz | Anexo IV |
|---|---|---|
| Relatório SBOM | inventário das dependências e as suas vulnerabilidades conhecidas | T.AS — atualizações |
| Análise SAST | análise estática do código e dos scripts, todos os dias | T.GPT — controlos nos sistemas |
| Conformidade do sistema operativo (SCAP) | configuração comparada com perfis CIS ou STIG | T.SC — securização |

## O ecrã

**Menu:** Proteger › Segurança do Software

No menu Proteger, Segurança do Software. A análise SAST corre todos os dias; aqui não encontrou falhas. Quando encontra, uma falha que se decida não corrigir aceita-se explicitamente, com quem aceitou registado; não desaparece por se ignorar.

```{figure} /_static/capturas/software/abrir-1.jpg
:alt: Proteger › Segurança do Software

O ecrã em Proteger › Segurança do Software.
```

Na conformidade do sistema operativo, este ambiente de testes não tem o leitor SCAP instalado, e o ecrã diz como o instalar. Com ele, as regras saem em passou, falhou, não aplicável e não verificado, e as aceites contam à parte.

Um aviso que o próprio ecrã dá: a remediação automática não é reversível. Aplicar um perfil completo numa máquina que corre a base de dados pode apagá-la. Remedeie regra a regra, e nunca em produção sem salvaguarda feita.

```{figure} /_static/capturas/software/scap-1.jpg
:alt: OS Compliance (SCAP)

OS Compliance (SCAP).
```

## Resumo

Além do efeito técnico, estas ferramentas dão prova automática: alimentam os recolectores da fase seguinte sem ninguém escrever nada. É a diferença entre um sistema que se prova todos os dias, e um que se prova na véspera da auditoria.

**O que a plataforma faz**

- Estas ferramentas alimentam a prova automática da fase seguinte, sem ninguém escrever nada.
- É a diferença entre um sistema que se prova todos os dias e um que se prova na véspera da auditoria.
