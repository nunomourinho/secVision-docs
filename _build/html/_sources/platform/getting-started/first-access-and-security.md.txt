# Primeiro acesso e segurança da plataforma

O primeiro acesso em três tempos — senha inicial, senha nova, segundo fator — e as três decisões sobre a segurança da própria plataforma que se tomam antes de escrever a primeira política.

```{video} 301-primeiro-acesso-e-seguranca
```

Começamos o módulo da plataforma pela porta de entrada: o primeiro acesso. E por uma pergunta que um auditor faz assim que percebe que o sistema de gestão vive aqui: e a segurança da própria ferramenta?

## Primeiro acesso

O primeiro acesso tem três tempos, e não se saltam. Entra-se com a senha inicial; a plataforma obriga a mudá-la, com regras de complexidade; e obriga a inscrever um segundo fator — uma aplicação autenticadora, ou uma chave física. Sem os dois passos, não se chega a página nenhuma.

Faça isto primeiro, antes de criar o que quer que seja: a senha inicial está escrita na documentação pública do produto. {doc}`/installation/first-access` mostra estes três tempos, ecrã a ecrã.

**O primeiro acesso, em três tempos**

1 — A senha inicial
: admin e a senha de instalação — a plataforma responde que tem de mudar

2 — Uma senha nova
: com política de complexidade, e sem repetir as três últimas

3 — O segundo fator
: uma aplicação autenticadora, ou uma chave física ou biometria

```{figure} /_static/img/301-primeiro-acesso-e-seguranca/01.jpg
:alt: O primeiro acesso, em três tempos

O primeiro acesso, em três tempos.
```

## A segurança da plataforma

Antes de alguém escrever a primeira política, decidem-se três coisas, fora da aplicação. Se a plataforma fica atrás de HTTPS: o instalador serve HTTP, e sem cifra no transporte as chaves físicas não funcionam. Quem alcança a máquina na rede. E onde ficam as cópias de segurança, que levam segredos.

O que a plataforma faz sozinha está descrito no guia do administrador: política de senhas, segundo fator obrigatório, bloqueio ao fim de cinco tentativas, trilha que não se apaga, e cifra das colunas sensíveis na base de dados.

**A segurança da própria plataforma — três decisões**

- HTTPS: o instalador serve HTTP; sem cifra no transporte não há cookies seguros, e as chaves físicas não funcionam.
- Quem alcança a máquina: o porto da aplicação, e o porto das listas de indicadores, que não pede autenticação.
- Onde ficam as cópias de segurança — que levam segredos lá dentro.

## Resumo

Peça à informática o certificado, as regras de acesso na rede e o destino das cópias. E registe a decisão: é a primeira coisa que um auditor pergunta, e não ter resposta é um mau começo.

**O que pedir a quem**

- À informática: o certificado HTTPS, as regras de firewall, e o destino das cópias de segurança.
- Ao responsável: registar a decisão sobre a segurança da plataforma — é a prova de que se pensou nela.
