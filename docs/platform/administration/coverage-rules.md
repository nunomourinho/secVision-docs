# Cobertura: níveis incluídos

Configuração dos níveis do catálogo de segurança que **não** entram nos indicadores de cobertura nem na lista de GAP.

```{video} 351-administracao-da-plataforma
```

O vídeo apresenta os três ecrãs da administração: cobertura, documentos do SGSI e versão.

Cada sistema do catálogo tem um nível, de N1 (crítico) a N4 (secundário). Por omissão, a taxa de cobertura e a lista de GAP (sistemas sem monitorização) consideram os três primeiros níveis. Este ecrã define os níveis excluídos e está disponível apenas para administradores.

## Acesso

**Governar** > **Administração do sistema** > **Cobertura**

```{figure} /_static/capturas/adm-cobertura/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Cobertura

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Critério de exclusão

Um indicador de cobertura só é útil se o seu âmbito for conhecido. Os postos de trabalho e os equipamentos terminais (N4) são numerosos e mudam com frequência; se fossem incluídos, a taxa refletiria a rotação do parque e não a proteção dos sistemas relevantes. Por este motivo, o N4 está excluído por omissão.

## Configuração do ecrã

```{figure} /_static/capturas/adm-cobertura/niveis-1.jpg
:alt: Os quatro níveis, cada um com o seu interruptor

Os quatro níveis, cada um com o seu interruptor.
```

No ecrã, encontra os seguintes elementos:

1. **N1 — Crítico:** Interruptor de exclusão do nível 1.
2. **N2 — Estratégico:** Interruptor de exclusão do nível 2.
3. **N3 — Operacional:** Interruptor de exclusão do nível 3.
4. **N4 — Secundário:** Interruptor de exclusão do nível 4, ativo por omissão.

| Nível | Exemplos habituais |
|---|---|
| N1 — Crítico | servidores de produção, armazenamento crítico |
| N2 — Estratégico | firewalls, switches core, VOIP |
| N3 — Operacional | switches de acesso, infraestrutura Wi-Fi |
| N4 — Secundário | restantes sistemas, equipamentos terminais |

**Como configurar:** Assinale os níveis que **não** devem ser contabilizados. A taxa de cobertura do painel e a página GAP passam a aplicar o filtro automaticamente.

```{important}
A exclusão de N1 ou N2 retira sistemas críticos da análise, e o ecrã apresenta um aviso nesse caso. Esta opção deve ser fundamentada e justificável perante um auditor.
```

## Resumo

- Define os níveis excluídos da taxa de cobertura e da lista de GAP.
- Por omissão, apenas o N4 é excluído.
- Ver também {doc}`/platform/inventory/security-catalogue`.
