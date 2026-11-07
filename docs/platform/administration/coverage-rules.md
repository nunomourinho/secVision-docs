# Cobertura: que níveis contam

Os níveis do catálogo de segurança que **não** entram nos indicadores de cobertura nem na fila de GAP.

Os sistemas do catálogo têm um nível, de N1 (crítico) a N4 (secundário). A taxa de cobertura e a lista de GAP, que são os sistemas sem monitorização, contam por omissão os três primeiros. Este ecrã decide quais ficam de fora. É só para administradores e não tem vídeo próprio.

## Onde fica no menu

**Menu:** Governar › Administração do sistema › Cobertura

```{figure} /_static/capturas/adm-cobertura/menu.jpg
:alt: Menu lateral: Governar › Administração do sistema › Cobertura

O caminho no menu lateral: Governar › Administração do sistema › Cobertura.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Administração do sistema**.
3. Clique em **Cobertura**: abre o ecrã desta página.


## Porquê

Um indicador de cobertura só diz alguma coisa se toda a gente souber o que conta. Os postos de trabalho e os equipamentos terminais (N4) são muitos e mudam todas as semanas: com eles, a taxa mediria a rotação do parque e não a proteção do que importa. Por isso o N4 está excluído por omissão.

## O ecrã

```{figure} /_static/capturas/adm-cobertura/niveis-1.jpg
:alt: Os quatro níveis, cada um com o seu interruptor

Os quatro níveis, cada um com o seu interruptor.
```

1. **N1 — Crítico**
2. **N2 — Estratégico**
3. **N3 — Operacional**
4. **N4 — Secundário, excluído por omissão**


| Nível | O que costuma ser |
|---|---|
| N1 — Crítico | servidores de produção, armazenamento crítico |
| N2 — Estratégico | firewalls, switches core, VOIP |
| N3 — Operacional | switches de acesso, infraestrutura Wi-Fi |
| N4 — Secundário | restantes sistemas, equipamentos terminais |

Marque os níveis que **não** devem contar. A taxa de cobertura do painel e a página GAP passam a filtrar sozinhas.

```{important}
Excluir N1 ou N2 esconde sistemas críticos da análise, e o ecrã avisa quando o faz. Se o fizer, tenha uma razão que possa explicar a um auditor.
```

## Resumo

- Escolhe que níveis ficam fora da taxa de cobertura e da fila de GAP.
- Por omissão, só o N4 fica de fora.
- Ver também {doc}`/platform/inventory/security-catalogue`.
