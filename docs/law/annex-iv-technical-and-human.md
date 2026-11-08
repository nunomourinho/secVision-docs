# Anexo IV — as medidas tecnológicas e humanas

As dezasseis medidas tecnológicas e as três humanas do Anexo IV: requisito de cada uma, acréscimo para o Grupo A e evidência técnica esperada pelo auditor.

```{video} 210-anexo-iv-medidas-tecnologicas-e-humanas
```

As medidas tecnológicas dependem sobretudo da informática, e as humanas das pessoas. Esta página apresenta-as por tema: postos de trabalho e sistemas, acessos, proteção da infraestrutura, cópias e registos, e pessoas.

## Medidas tecnológicas

**Sistemas e postos de trabalho.** Os dois grupos aplicam controlos de segurança em todos os sistemas, antivírus em postos e servidores e atualizações de segurança atempadas, de acordo com as recomendações dos fabricantes.

O Grupo A acrescenta o controlo de acesso aos postos e a cópia da respetiva informação, as atualizações também no hardware, configurações endurecidas e, nos telemóveis, a informação da entidade num perfil de trabalho separado do perfil pessoal.

**Sistemas e postos de trabalho**

| Medida | Grupo B | Acréscimo para o Grupo A |
|---|---|---|
| T.GPT Sistemas e postos | controlos de segurança em sistemas, aplicações e postos | — |
| T.PPT Proteção de postos | antivírus em postos e servidores | controlo de acesso aos postos e cópias da respetiva informação |
| T.AS Atualizações | atualizações de segurança atempadas no software | também no hardware |
| T.SC Securização | — | configurações seguras do posto, do sistema e das aplicações |
| T.PPT-2 Dispositivos móveis | — | informação da entidade apenas num perfil de trabalho |

**Acessos.** Os dois grupos asseguram o acesso remoto através de um canal seguro e com segundo fator, contas distintas para utilização e para administração e uma política de complexidade das palavras-passe.

O Grupo A acrescenta a autenticação multifator nas aplicações críticas, a atribuição de privilégios segundo a necessidade de conhecer e o menor privilégio, e o armazenamento das palavras-passe de administração numa solução própria (cofre de palavras-passe).

**Acessos e autenticação**

| Medida | Grupo B | Acréscimo para o Grupo A |
|---|---|---|
| T.AR Acesso remoto | acesso seguro (VPN, VDI) e segundo fator | — |
| Perfil de administração segregado | contas distintas para utilização e administração | — |
| T.MA Autenticação | política de complexidade das palavras-passe | — |
| T.AM Autenticação multifator | — | nas aplicações críticas |
| T.PAD Privilégios | — | necessidade de conhecer e menor privilégio |
| T.GP Gestão de palavras-passe | — | palavras-passe privilegiadas num cofre |

**Infraestrutura.** Os dois grupos asseguram a proteção do perímetro lógico (por exemplo, uma firewall) e do perímetro físico (por exemplo, a sala dos servidores), boas práticas no correio eletrónico e nas páginas de Internet, cópias de segurança utilizáveis e a ativação dos registos dos sistemas.

O Grupo A guarda as cópias separadamente do ambiente que protegem, para que um ataque não as comprometa em simultâneo, e conserva os registos, para permitir a investigação de incidentes.

**Infraestrutura, cópias e registos**

| Medida | Grupo B | Acréscimo para o Grupo A |
|---|---|---|
| T.PPL Perímetro lógico | proteção perimetral da infraestrutura | — |
| T.PPF Perímetro físico | proteção física do centro de dados | — |
| T.PEW Correio e web | boas práticas de segurança no correio e nas páginas | o mesmo, no texto A |
| T.CS Cópias de segurança | realizar cópias e garantir a sua utilização | guardá-las separadamente do ambiente protegido |
| T.RAR Registos | ativar os registos por omissão | conservar os registos |

## Medidas humanas

As três medidas humanas são: sensibilização e formação (no Grupo A, com um plano); consulta regular de fontes de informação fidedignas sobre ameaças, como os alertas do CNCS; e, no Grupo A, exercícios periódicos de phishing, com o envio deliberado de mensagens simuladas para medir a taxa de adesão.

O critério de verificação dos exercícios exige os resultados, as conclusões e as ações tomadas. Um exercício sem seguimento não é considerado.

**Pessoas**

| Medida | Grupo B | Acréscimo para o Grupo A |
|---|---|---|
| Sensibilização e formação | ações de sensibilização ou formação | plano de formação, com processos |
| H.FIC Fontes de informação | consulta de fontes fidedignas sobre ameaças | — |
| H.EC Exercícios de phishing | — | exercícios periódicos, com resultados e conclusões |

Para estas medidas, o critério exige quase sempre «evidência técnica»: uma exportação datada da configuração, um relatório de cobertura, o registo de um restauro bem-sucedido ou os registos de presença na formação.

**Evidências solicitadas pelo auditor**

| Tipo de medida | Evidência típica |
|---|---|
| Configuração | captura de ecrã ou exportação da configuração, com data |
| Cobertura | relatório da ferramenta: postos com antivírus, sistemas atualizados |
| Teste | registo de um restauro de cópia de segurança bem-sucedido |
| Pessoas | presenças na formação; resultados dos exercícios |

Na plataforma, muitas destas evidências são recolhidas automaticamente a partir das ferramentas, a cobertura indica os sistemas protegidos por cada ferramenta e a formação tem um registo próprio. O módulo da plataforma descreve cada ecrã.

**Correspondência na plataforma**

- Recolha automática de evidências a partir das ferramentas ({doc}`/platform/monitoring/evidence`).
- Cobertura por ferramenta: sistemas protegidos por cada ferramenta ({doc}`/platform/compliance/mapping-and-tools`).
- Agentes Wazuh, deteção e registos ({doc}`/platform/protect-and-detect/agents-and-surface` e {doc}`/platform/protect-and-detect/detection-and-threats`).
- Formação e sensibilização ({doc}`/platform/protect-and-detect/training-and-awareness`).
