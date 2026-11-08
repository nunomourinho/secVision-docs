# Anexo IV — as medidas organizacionais

As doze medidas organizacionais do Anexo IV, uma a uma: requisito, entidades abrangidas e evidência esperada, começando pelas medidas dos dois grupos e terminando nas exclusivas do Grupo A.

```{video} 209-anexo-iv-medidas-organizacionais
```

As medidas organizacionais são as que menos dependem da informática: regras, responsabilidades e processos. O Anexo IV inclui doze. Esta página apresenta primeiro as medidas aplicáveis aos dois grupos e, em seguida, as exclusivas do Grupo A.

## Grupos A e B

Cinco medidas organizacionais aplicam-se aos dois grupos:

- **Ponto de contacto para incidentes:** Uma pessoa que responde a pedidos externos e, se necessário, fora do horário de expediente.
- **Gestão de acessos:** A atribuição, alteração e remoção de acessos exigem sempre pedido e aprovação.
- **Inventário:** No Grupo B, os ativos críticos e as respetivas dependências; no Grupo A, todos os ativos.
- **Equipamentos:** Registo da atribuição e da recolha de cada computador; no Grupo A, também a separação entre dispositivos pessoais e da entidade.
- **Fornecedores:** No Grupo B, identificação dos fornecedores com acesso aos sistemas e respetivos contactos para incidentes; no Grupo A, uma política de segurança de fornecedores, com avaliação do risco e critérios de aceitação.

**Medidas dos dois grupos**

| Medida | Requisito | Acréscimo para o Grupo A |
|---|---|---|
| O.CRI Ponto de contacto para incidentes | uma pessoa que responde a pedidos externos e, se necessário, fora do horário | — |
| O.GAP Gestão de acessos | pedido e aprovação para atribuir, alterar e remover acessos | — |
| O.IAC Inventário de ativos | ativos críticos e respetivas dependências, atualizados | todos os ativos, e não apenas os críticos |
| O.GEC Equipamentos | registo de atribuição e recolha dos equipamentos | separação entre dispositivos pessoais e da entidade |
| O.PSF Fornecedores | lista dos fornecedores com acesso aos sistemas, com contacto para incidentes | política de segurança de fornecedores, com avaliação do risco |

## Exclusivas do Grupo A

O Grupo A tem quatro políticas exclusivas: a Política de Cibersegurança, que formaliza o compromisso da entidade e é aprovada pela direção; a política de acessos e permissões; a política de utilização aceitável, que define as regras de utilização dos equipamentos e da informação por todo o pessoal; e a política de palavra-passe.

O critério de verificação segue um padrão: o documento não é suficiente. É exigida uma política aprovada e implementada ou, no caso da utilização aceitável, disponível a todo o pessoal.

**Medidas exclusivas do Grupo A: políticas**

| Medida | Requisito |
|---|---|
| O.PSI Política de Cibersegurança | compromisso da entidade com a cibersegurança, aprovado e implementado |
| O.PAP Política de acessos e permissões | definida e implementada |
| O.PUA Política de utilização aceitável | regras de utilização segura dos ativos, disponível a todo o pessoal |
| O.PP Política de palavra-passe | regras de gestão das palavras-passe |

O Grupo A tem ainda três processos exclusivos:

- **Classificação da informação:** Definição de níveis de sensibilidade, conforme descrito em {doc}`/fundamentals/information-and-assets`.
- **Gestão da mudança organizacional:** As contas e os acessos acompanham as entradas, as mudanças de funções e as saídas de pessoal, em articulação com os recursos humanos.
- **Identificação das funções críticas** e dos sistemas de que dependem. Esta medida relaciona a missão da organização com a informática; por exemplo, identifica a função crítica afetada por uma interrupção do sistema de matrículas.

**Medidas exclusivas do Grupo A: processos**

| Medida | Requisito |
|---|---|
| O.PCF Classificação da informação | critérios e níveis de sensibilidade dos dados |
| O.GMO Mudança organizacional | entradas, alterações e saídas de pessoal refletidas nas TIC, em articulação com os recursos humanos |
| O.ID Funções críticas | funções ou atividades críticas e respetivas dependências das TIC |

## Informação a solicitar

Estas medidas envolvem toda a organização. A direção aprova as políticas e identifica as funções críticas. Os recursos humanos comunicam as entradas e saídas. O serviço de compras identifica os fornecedores com acesso. O encarregado de proteção de dados contribui para a classificação da informação.

**Responsáveis**

| Responsável | Informação |
|---|---|
| Direção | aprovação das políticas; lista das funções críticas |
| Recursos humanos | aviso de entradas, mudanças e saídas, com data (O.GMO) |
| Serviço de compras | fornecedores com acesso aos sistemas e respetivos contactos (O.PSF) |
| Equipa de informática | inventário, registo de equipamentos, pedidos de acesso |
| Encarregado de proteção de dados | contributo para a classificação da informação (O.PCF) |

Na plataforma, as políticas são geridas no SGSI, com aprovação e versão assinada; o inventário e os ativos de informação registam as dependências; os fornecedores têm um registo próprio; e os processos críticos são associados aos ativos de que dependem.

**Correspondência na plataforma**

- Políticas no SGSI, com aprovação e versão assinada ({doc}`/platform/protect-and-detect/isms-documents`).
- Inventário e ativos de informação, com dependências ({doc}`/platform/inventory/import` a {doc}`/platform/inventory/information-assets`).
- Fornecedores, com acesso aos sistemas e contactos ({doc}`/platform/risk/suppliers`).
- Processos e serviços críticos ({doc}`/platform/inventory/processes-and-services`); papéis e pessoas ({doc}`/platform/organisation/roles-and-people`).
