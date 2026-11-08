# Importar o parque

O primeiro passo do inventário: trazer as exportações do Active Directory, do DNS e do DHCP, e deixar a plataforma correlacioná-las num inventário único do parque técnico.

```{video} 311-importar-o-parque
```

Começa a segunda fase: saber o que se tem. Não há sistema de gestão sem inventário — não se protege o que não se sabe que existe. O primeiro passo é trazer o parque técnico para a plataforma.

## Onde fica no menu

**Menu:** Identificar › Inventário › Importar Dados

```{figure} /_static/capturas/importar/menu.jpg
:alt: Menu lateral: Identificar › Inventário › Importar Dados

O caminho no menu lateral: Identificar › Inventário › Importar Dados.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Inventário**.
3. Clique em **Importar Dados**: abre o ecrã desta página.

## Porquê

A norma ISO 27001 pede um inventário dos ativos. O Anexo IV do Regulamento pede-o também: no Grupo B, os ativos críticos e as dependências; no Grupo A, todos os ativos. E o Regulamento pede, à parte, a lista dos ativos acessíveis pela Internet.

**Para que serve**

- A ISO/IEC 27001 pede um inventário da informação e dos ativos associados (controlo 5.9).
- O Anexo IV pede o inventário dos ativos críticos, com as dependências — e no Grupo A, de todos os ativos (O.IAC).
- O Regulamento pede ainda a lista dos ativos acessíveis pela Internet (art. 32.º).

## Antes de abrir o ecrã

Peça à informática três exportações em CSV: os computadores do Active Directory, os registos do DNS e as concessões do DHCP. Cada fonte vê uma parte do parque; juntas, veem quase tudo.

**O que pedir a quem**

| Exportação | Quem a faz | O que traz |
|---|---|---|
| Active Directory — computadores | informática (administração de sistemas) | os computadores do domínio |
| DNS — registos de nome | informática (redes) | nomes e endereços |
| DHCP — concessões | informática (redes) | os equipamentos que pediram endereço |

```{tip}
Em CSV. O leitor deteta sozinho o separador e repara os caminhos LDAP partidos pelas vírgulas.
```

## O ecrã

**Menu:** Identificar › Inventário › Importar Dados

No menu Identificar, Inventário, Importar Dados. Carregam-se os três ficheiros. O leitor deteta sozinho se o separador é ponto e vírgula ou vírgula, lida com campos entre aspas, e volta a juntar os caminhos do diretório que as vírgulas partiram ao meio.

```{figure} /_static/capturas/importar/abrir-1.jpg
:alt: Identificar › Inventário › Importar Dados

O ecrã em Identificar › Inventário › Importar Dados.
```

1. **Os três ficheiros**

Processar e Correlacionar junta as três fontes pelo nome do equipamento. Uma concessão do DHCP sem nome aproveitável entra pelo endereço IP, em vez de se perder.

Atenção à caixa Substituir dados existentes: apaga as importações anteriores. Para acrescentar, deixe-a desmarcada. E lembre-se: o que sai daqui é o parque técnico, não o inventário final. Os ativos de informação, que são o que o risco aprecia, criam-se mais à frente.

```{figure} /_static/capturas/importar/carregar-1.jpg
:alt: Processar e correlacionar

Processar e correlacionar.
```

1. **Processar e correlacionar**
2. **Apaga as importações anteriores**

## Resumo

A plataforma correlaciona as fontes e, havendo uma ligação ao diretório, pode atualizar os computadores todas as noites. O que não faz é inventar: o inventário é um espelho das fontes, e o que estiver errado corrige-se na origem e reimporta-se.

**O que a plataforma faz — e o que não faz**

- Correlaciona as três fontes num inventário único, pelo nome e, à falta dele, pelo endereço.
- Pode sincronizar os computadores com o diretório todas as noites, havendo ligação declarada.
- Não inventa o que não vem nas fontes: o inventário é um espelho, corrige-se na origem.
