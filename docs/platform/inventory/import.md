# Importar o parque

Primeiro passo do inventário: importação das exportações do Active Directory, do DNS e do DHCP e respetiva correlação num inventário único do parque técnico.

```{video} 311-importar-o-parque
```

A segunda fase do trabalho consiste em conhecer os ativos existentes. Não existe sistema de gestão sem inventário, uma vez que não é possível proteger ativos desconhecidos. O primeiro passo é a importação do parque técnico para a plataforma.

## Acesso

**Identificar** > **Inventário** > **Importar Dados**

```{figure} /_static/capturas/importar/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Importar Dados

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Finalidade

A ISO 27001 exige um inventário dos ativos. O Anexo IV do Regulamento exige-o igualmente: no Grupo B, os ativos críticos e as respetivas dependências; no Grupo A, todos os ativos. O Regulamento exige ainda, separadamente, a lista dos ativos acessíveis pela Internet.

**Finalidade**

- A ISO/IEC 27001 exige um inventário da informação e dos ativos associados (controlo 5.9).
- O Anexo IV exige o inventário dos ativos críticos, com as dependências, e, no Grupo A, de todos os ativos (O.IAC).
- O Regulamento exige ainda a lista dos ativos acessíveis pela Internet (art. 32.º).

## Informação a solicitar

Solicite à equipa de informática três exportações em CSV: os computadores do Active Directory, os registos do DNS e as concessões do DHCP. Cada fonte abrange uma parte do parque; em conjunto, abrangem a quase totalidade.

**Responsáveis**

| Exportação | Responsável | Conteúdo |
|---|---|---|
| Active Directory — computadores | equipa de informática (administração de sistemas) | computadores do domínio |
| DNS — registos de nome | equipa de informática (redes) | nomes e endereços |
| DHCP — concessões | equipa de informática (redes) | equipamentos que solicitaram endereço |

```{tip}
Em formato CSV. O leitor deteta automaticamente o separador e reconstitui os caminhos LDAP divididos pelas vírgulas.
```

## Configuração do ecrã

O leitor deteta automaticamente o separador (ponto e vírgula ou vírgula), trata os campos entre aspas e reconstitui os caminhos do diretório divididos pelas vírgulas.

```{figure} /_static/capturas/importar/abrir-1.jpg
:alt: Identificar > Inventário > Importar Dados

Ecrã **Identificar** > **Inventário** > **Importar Dados**.
```

1. **Ficheiros:** Campos para carregar as três exportações.

```{figure} /_static/capturas/importar/carregar-1.jpg
:alt: Processar e correlacionar

Processar e correlacionar.
```

No ecrã, encontra os seguintes elementos:

1. Botão **Processar e Correlacionar:** Associa as três fontes pelo nome do equipamento. Uma concessão do DHCP sem nome utilizável é associada pelo endereço IP.
2. Opção **Substituir dados existentes:** Elimina as importações anteriores. Para acrescentar dados, mantenha a opção desmarcada.

**Como importar:** Carregue os três ficheiros e clique em **Processar e Correlacionar**.

O resultado corresponde ao parque técnico e não ao inventário final. Os ativos de informação, objeto da apreciação de risco, são criados numa fase posterior.

## Resumo

A plataforma correlaciona as fontes e, existindo uma ligação ao diretório, pode atualizar os computadores diariamente. O inventário reflete as fontes: os dados incorretos são corrigidos na origem e importados novamente.

**Funcionalidades e limitações**

- Correlaciona as três fontes num inventário único, pelo nome ou, na sua falta, pelo endereço.
- Pode sincronizar diariamente os computadores com o diretório, se existir uma ligação configurada.
- Não acrescenta dados inexistentes nas fontes: o inventário reflete a origem, onde as correções devem ser feitas.
