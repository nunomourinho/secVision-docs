# Primeiro acesso e segurança da plataforma

O primeiro acesso em três passos (palavra-passe inicial, nova palavra-passe e segundo fator) e as três decisões sobre a segurança da própria plataforma, a tomar antes de redigir a primeira política.

```{video} 301-primeiro-acesso-e-seguranca
```

O módulo da plataforma começa pelo primeiro acesso e pela questão que um auditor coloca quando verifica que o sistema de gestão está suportado nesta ferramenta: qual é a segurança da própria ferramenta?

## Primeiro acesso

O primeiro acesso é composto por três passos obrigatórios:

1. Iniciar sessão com a palavra-passe inicial.
2. Definir uma nova palavra-passe, de acordo com as regras de complexidade.
3. Registar um segundo fator de autenticação (aplicação autenticadora ou chave de segurança física).

O acesso às restantes páginas só fica disponível após a conclusão dos passos 2 e 3.

Conclua o primeiro acesso antes de qualquer outra configuração: a palavra-passe inicial consta da documentação pública do produto. A página {doc}`/installation/first-access` apresenta estes três passos, ecrã a ecrã.

**O primeiro acesso em três passos**

1 — Palavra-passe inicial
: utilizador admin e palavra-passe de instalação; a plataforma solicita a alteração

2 — Nova palavra-passe
: sujeita à política de complexidade, sem repetir as três últimas

3 — Segundo fator
: aplicação autenticadora, chave física ou biometria

```{figure} /_static/img/301-primeiro-acesso-e-seguranca/01.jpg
:alt: O primeiro acesso em três passos

O primeiro acesso em três passos.
```

## Segurança da plataforma

Antes de redigir a primeira política, devem ser tomadas três decisões fora da aplicação:

- **HTTPS:** O instalador disponibiliza a plataforma em HTTP. Sem encriptação no transporte, as chaves de segurança físicas não funcionam.
- **Acesso de rede:** Definição dos equipamentos que podem aceder à máquina.
- **Cópias de segurança:** Local de armazenamento das cópias, que contêm segredos.

As proteções aplicadas automaticamente pela plataforma estão descritas no guia do administrador: política de palavras-passe, segundo fator obrigatório, bloqueio ao fim de cinco tentativas, trilha de auditoria não eliminável e encriptação das colunas sensíveis na base de dados.

**Segurança da própria plataforma: três decisões**

- HTTPS: o instalador disponibiliza a plataforma em HTTP; sem encriptação no transporte, os cookies seguros e as chaves físicas não funcionam.
- Acesso à máquina: a porta da aplicação e a porta das listas de indicadores, que não exige autenticação.
- Local das cópias de segurança, que contêm segredos.

## Resumo

Solicite à equipa de informática o certificado, as regras de acesso na rede e o destino das cópias de segurança, e registe a decisão tomada. Esta decisão é um dos primeiros elementos verificados numa auditoria.

**Responsáveis**

- Equipa de informática: certificado HTTPS, regras de firewall e destino das cópias de segurança.
- Responsável de segurança: registo da decisão sobre a segurança da plataforma, como evidência de que foi avaliada.
