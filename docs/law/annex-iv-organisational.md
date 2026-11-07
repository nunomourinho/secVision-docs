# Anexo IV — as medidas organizacionais

As doze medidas organizacionais do Anexo IV, uma a uma: o que pede cada uma, a quem, e que prova se espera — primeiro as do Grupo B, depois as que só o Grupo A cumpre.

```{video} 209-anexo-iv-medidas-organizacionais
```

As medidas organizacionais são as que menos dependem da informática: regras, responsabilidades e processos. São doze no Anexo IV. Começamos pelas que cabem aos dois grupos, e acabamos nas que só o Grupo A cumpre.

## Grupos A e B

Cinco medidas organizacionais cabem aos dois grupos. O ponto de contacto para incidentes: uma pessoa que responde a pedidos externos e, se for preciso, fora de horas. A gestão de acessos: dar, alterar e retirar um acesso sempre com pedido e aprovação.

O inventário: no Grupo B, os ativos críticos e as dependências entre eles; no Grupo A, todos os ativos. Os equipamentos: registar a quem se entregou cada computador e quando foi recolhido — e, no Grupo A, separar os dispositivos pessoais dos da entidade.

E os fornecedores: no Grupo B, saber quais têm acesso aos sistemas, e como contactá-los num incidente. No Grupo A, ter uma política de segurança de fornecedores, com avaliação do risco e critérios de aceitação.

**As dos dois grupos**

| Medida | O que pede | Grupo A acrescenta |
|---|---|---|
| O.CRI Ponto de contacto para incidentes | uma pessoa que responde a pedidos externos e, se preciso, fora de horas | — |
| O.GAP Gestão de acessos | pedido e aprovação para dar, alterar e retirar acessos | — |
| O.IAC Inventário de ativos | ativos críticos e as dependências, atualizados | todos os ativos, não só os críticos |
| O.GEC Equipamentos | registo de atribuição e recolha dos equipamentos | separar dispositivos pessoais dos da entidade |
| O.PSF Fornecedores | lista dos fornecedores com acesso aos sistemas, com contacto para incidentes | uma política de segurança de fornecedores, com avaliação do risco |

## Só Grupo A

Só no Grupo A, quatro políticas. A Política de Cibersegurança, que é o compromisso da entidade e é aprovada pela direção. A política de acessos e permissões. A política de utilização aceitável, que diz a todo o pessoal como usar os equipamentos e a informação. E a política de palavra-passe.

Note o padrão do critério de verificação: não basta o documento. Pede-se política aprovada e implementada — ou, na utilização aceitável, disponível a todo o pessoal.

**As que só o Grupo A cumpre — as políticas**

| Medida | O que pede |
|---|---|
| O.PSI Política de Cibersegurança | o compromisso da entidade com a cibersegurança — aprovada e implementada |
| O.PAP Política de acessos e permissões | definida e implementada |
| O.PUA Política de utilização aceitável | regras de uso seguro dos ativos, disponível a todo o pessoal |
| O.PP Política de palavra-passe | como se gerem as palavras-passe |

E três processos. A classificação da informação: decidir níveis de sensibilidade, como vimos em {doc}`/fundamentals/information-and-assets`. A gestão da mudança organizacional: quando alguém entra, muda de funções ou sai, as contas e os acessos acompanham — combinado com os recursos humanos.

E a identificação das funções críticas, e de que sistemas dependem. É esta medida que liga a missão da organização à informática: se o sistema de matrículas parar, que função crítica para?

**As que só o Grupo A cumpre — os processos**

| Medida | O que pede |
|---|---|
| O.PCF Classificação da informação | critérios e níveis de sensibilidade dos dados |
| O.GMO Mudança organizacional | entradas, alterações e saídas de pessoal refletidas nas TIC, em sintonia com os recursos humanos |
| O.ID Funções críticas | as funções ou atividades críticas, e as suas dependências das TIC |

## Na sua organização

Estas medidas atravessam a organização. A direção aprova as políticas e diz quais são as funções críticas. Os recursos humanos avisam das entradas e saídas. As compras sabem que fornecedores têm acesso. E o encarregado de proteção de dados ajuda a classificar a informação.

**O que pedir a quem**

| A quem | O quê |
|---|---|
| Direção | aprovação das políticas; a lista das funções críticas |
| Recursos humanos | aviso de entradas, mudanças e saídas, com data (O.GMO) |
| Compras | fornecedores com acesso aos sistemas e os seus contactos (O.PSF) |
| Informática | inventário, registo de equipamentos, pedidos de acesso |
| Encarregado de proteção de dados | contributo para a classificação da informação (O.PCF) |

Na plataforma, as políticas vivem no SGSI, com aprovação e versão assinada; o inventário e os ativos de informação guardam as dependências; os fornecedores têm registo próprio; e os processos críticos ligam-se aos ativos de que dependem.

**Onde isto entra na plataforma**

- Políticas no SGSI, com aprovação e versão assinada ({doc}`/platform/protect-and-detect/isms-documents`).
- Inventário e ativos de informação, com dependências ({doc}`/platform/inventory/import` a {doc}`/platform/inventory/information-assets`).
- Fornecedores, com acesso aos sistemas e contactos ({doc}`/platform/risk/suppliers`).
- Processos e serviços críticos ({doc}`/platform/inventory/processes-and-services`); papéis e pessoas ({doc}`/platform/organisation/roles-and-people`).
