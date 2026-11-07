# Anexo IV — as medidas tecnológicas e humanas

As dezasseis medidas tecnológicas e as três humanas do Anexo IV: o que pede cada uma, o que o Grupo A acrescenta, e que prova técnica um auditor espera.

```{video} 210-anexo-iv-medidas-tecnologicas-e-humanas
```

As medidas tecnológicas são as que mais dependem da informática, e as humanas, das pessoas. Vamos percorrê-las por temas: postos de trabalho e sistemas, acessos, proteção da infraestrutura, cópias e registos, e por fim as pessoas.

## Tecnológicas

Nos sistemas e postos de trabalho: controlos de segurança em todos; antivírus em postos e servidores; e atualizações de segurança aplicadas a tempo, conforme as recomendações dos fabricantes.

O Grupo A acrescenta: controlo de acesso aos postos e cópia da sua informação; atualizações também no hardware; configurações endurecidas; e, nos telemóveis, a informação da entidade só num perfil de trabalho, separado do pessoal.

**Sistemas e postos de trabalho**

| Medida | Grupo B | Grupo A acrescenta |
|---|---|---|
| T.GPT Sistemas e postos | controlos de segurança em sistemas, aplicações e postos | — |
| T.PPT Proteção de postos | antivírus em postos e servidores | controlo de acesso aos postos e cópias da sua informação |
| T.AS Atualizações | atualizações de segurança atempadas no software | também no hardware |
| T.SC Securização | — | configurações seguras do posto, do sistema e das aplicações |
| T.PPT-2 Dispositivos móveis | — | informação da entidade só num perfil de trabalho |

Nos acessos: o acesso remoto sempre por um canal seguro e com segundo fator; contas diferentes para usar e para administrar; e uma política de complexidade das palavras-passe.

O Grupo A acrescenta autenticação multifator nas aplicações críticas, privilégios dados pela necessidade de conhecer e pelo menor privilégio, e as palavras-passe de administração guardadas numa solução própria, uma espécie de cofre.

**Acessos e autenticação**

| Medida | Grupo B | Grupo A acrescenta |
|---|---|---|
| T.AR Acesso remoto | acesso seguro (VPN, VDI) e segundo fator | — |
| Perfil de administração segregado | contas diferentes para usar e para administrar | — |
| T.MA Autenticação | política de complexidade das palavras-passe | — |
| T.AM Autenticação multifator | — | nas aplicações críticas |
| T.PAD Privilégios | — | necessidade de conhecer e menor privilégio |
| T.GP Gestão de palavras-passe | — | palavras-passe privilegiadas num cofre |

Na infraestrutura: proteção do perímetro lógico, como uma firewall, e do perímetro físico, como a sala dos servidores. Boas práticas no correio eletrónico e nas páginas de Internet. Cópias de segurança que se conseguem usar. E os registos dos sistemas ativados.

O Grupo A guarda as cópias separadas do ambiente que protegem — para um ataque não levar as duas coisas — e guarda os registos, para que haja com que investigar um incidente.

**Infraestrutura, cópias e registos**

| Medida | Grupo B | Grupo A acrescenta |
|---|---|---|
| T.PPL Perímetro lógico | proteção perimetral da infraestrutura | — |
| T.PPF Perímetro físico | proteção física do centro de dados | — |
| T.PEW Correio e web | boas práticas de segurança no correio e nas páginas | o mesmo, no texto A |
| T.CS Cópias de segurança | fazer cópias e garantir que se usam | guardá-las separadas do ambiente protegido |
| T.RAR Registos | ativar os registos por omissão | guardar os registos |

## Humanas

As três medidas humanas. Sensibilização e formação — no Grupo A, com um plano. Consulta regular de fontes de informação fidedignas sobre ameaças, como os alertas do CNCS. E, no Grupo A, exercícios periódicos de phishing — mensagens falsas, enviadas de propósito, para medir quem cai.

O critério de verificação dos exercícios pede os resultados, as conclusões e o que se fez com eles. Um exercício sem seguimento não conta.

**As pessoas**

| Medida | Grupo B | Grupo A acrescenta |
|---|---|---|
| Sensibilização e formação | ações de sensibilização ou formação | um plano de formação, com processos |
| H.FIC Fontes de informação | consultar fontes fidedignas sobre ameaças | — |
| H.EC Exercícios de phishing | — | exercícios periódicos, com resultados e conclusões |

Para estas medidas, o critério pede quase sempre «evidência técnica». Na prática: uma exportação da configuração com data, um relatório de cobertura, o registo de um restauro que funcionou, e as presenças na formação.

**Que prova o auditor pede**

| Tipo de medida | Prova típica |
|---|---|
| Configuração | captura do ecrã ou exportação da configuração, com data |
| Cobertura | relatório da ferramenta: que postos têm antivírus, que sistemas estão atualizados |
| Teste | registo de um restauro de cópia de segurança que funcionou |
| Pessoas | presenças na formação; resultados dos exercícios |

Na plataforma, muitas destas provas recolhem-se automaticamente das ferramentas; a cobertura mostra que sistemas cada ferramenta protege; e a formação tem o seu registo. Vamos ver cada ecrã no módulo da plataforma.

**Onde isto entra na plataforma**

- Recolha automática de evidências a partir das ferramentas ({doc}`/platform/monitoring/evidence`).
- Cobertura por ferramenta: que sistemas cada ferramenta protege ({doc}`/platform/compliance/mapping-and-tools`).
- Agentes Wazuh, deteção e registos ({doc}`/platform/protect-and-detect/agents-and-surface` e {doc}`/platform/protect-and-detect/detection-and-threats`).
- Formação e sensibilização ({doc}`/platform/protect-and-detect/training-and-awareness`).
