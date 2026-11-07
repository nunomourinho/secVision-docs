# Instalar em modo nativo

A instalação completa em modo nativo, num Ubuntu 24.04 acabado de instalar: obter o código, correr o instalador, responder às perguntas, esperar pelo fim e confirmar que a plataforma está a funcionar.

```{video} 04-instalar-nativo
```

Nesta página instalamos o SecVision em modo nativo, numa máquina Ubuntu 24.04 acabada de instalar, sem nada lá dentro. Vai ver tudo o que acontece, tal como acontece.

A gravação foi feita numa máquina de laboratório, um Ubuntu no WSL. No seu servidor, os comandos e as perguntas são exatamente os mesmos; muda só o endereço com que se chega à plataforma.

## Confirmar a máquina

Abrimos o terminal no servidor. Antes de mais, confirmamos onde estamos. O comando whoami diz-nos com que utilizador entrámos: secv, um utilizador normal, com permissão de sudo.

E o lsb_release mostra o sistema: Ubuntu 24.04, a versão de suporte prolongado. É boa prática começar sempre assim — evita instalar na máquina errada.

Escreva:

```bash
whoami
lsb_release -d
```

```{figure} /_static/img/04-instalar-nativo/01.jpg
:alt: Onde estamos

Onde estamos.
```

## Obter o código

Agora trazemos o código do SecVision para o servidor, com o comando git clone. O git é a ferramenta que guarda o código e o histórico de todas as versões.

O endereço depende de onde o repositório está alojado. Aqui é o do nosso laboratório; no seu caso, será o endereço que a sua organização lhe indicar. A cópia fica numa pasta chamada secvision.

Escreva:

```bash
git clone <endereço-do-repositório> secvision
```

```{figure} /_static/img/04-instalar-nativo/02.jpg
:alt: git clone

Git clone.
```

Entramos na pasta com cd, e listamos o que lá está com ls. Não é preciso conhecer tudo: o backend e o frontend são as duas partes da aplicação, a pasta documentacao é o manual, e o setup.sh é o instalador. É ele que vamos correr.

Escreva:

```bash
cd secvision
ls
```

```{figure} /_static/img/04-instalar-nativo/03.jpg
:alt: A pasta do SecVision

A pasta do SecVision.
```

## O instalador

Corremos o instalador com bash setup.sh. A primeira coisa que ele faz é pedir permissões de administrador — por isso aparece o pedido de palavra-passe do sudo. Escrevemos a palavra-passe do nosso utilizador; repare que não aparece nada enquanto escrevemos. Enter, e seguimos.

Escreva:

```bash
bash setup.sh
```

O que se respondeu a cada pergunta do instalador nesta instalação:

| Pergunta do instalador | Resposta |
|---|---|
| [sudo] password for secv | (a palavra-passe do seu utilizador) |
| Opção [1/2] | `2` |
| Password root do MySQL | (a palavra-passe root da base de dados que escolher) |
| Confirme a password root | (a palavra-passe root da base de dados que escolher) |
| Utilizador da aplicação | Enter (aceita o valor proposto) |
| Password da aplicação | (a palavra-passe da aplicação que escolher) |
| Confirme a password da aplicação | (a palavra-passe da aplicação que escolher) |
| Mostrar segredos | `n` |
| WebAuthn RP Name | `SecVision` |
| Domínio / RP ID | `localhost` |
| Origin URL completo | Enter (aceita o valor proposto) |
| Porto de acesso à aplicação | `8080` |
| Corrigir Origin | `s` |
| Tamanho máximo de upload | Enter (aceita o valor proposto) |
| Confirmar substituição do .env | `s` |
| Gravar .env e continuar | `s` |
| Prima Enter | Enter (aceita o valor proposto) |
| (S/n) | `s` |
| (s/N) | `n` |
| Modo de instalação | `menu-modo` |
| Passo 1/5 — Detecção do sistema | `deteccao` |
| Instalar MariaDB automaticamente | `pergunta-mariadb` |
| Instalar nginx automaticamente | `pergunta-nginx` |
| Instalar a base Docker aprovada | `pergunta-docker` |
| Instalar Node.js 22 | `pergunta-node` |
| Instalar PM2 automaticamente | `pergunta-pm2` |
| A instalar semgrep | `ferramentas` |
| A construir a imagem do Presidio | `presidio` |
| Presidio a responder | `presidio-ok` |
| Configuração segura da aplicação | `assistente` |
| Configuração da Base de Dados | `assistente-bd` |
| Segredos de Segurança | `assistente-segredos` |
| Configuração da Aplicação | `assistente-aplicacao` |
| Revisão e Confirmação | `assistente-revisao` |
| Construção da aplicação | `construcao` |
| Configuração de serviços e lançamento | `servicos` |
| Instalação concluída | `concluida` |

```{figure} /_static/img/04-instalar-nativo/04.jpg
:alt: bash setup.sh

Bash setup.sh.
```

Surge a primeira pergunta: o modo de instalação. Escrevemos dois, para o modo nativo. Repare na nota do instalador: deteta que está num ambiente WSL e recomenda o modo nativo. Num servidor Ubuntu, essa nota não aparece.

Se carregasse só em Enter, sem escrever nada, ficaria o modo Docker — é esse o que vemos na página seguinte.

```{figure} /_static/img/04-instalar-nativo/05.jpg
:alt: Escolher o modo — 2, nativo

Escolher o modo — 2, nativo.
```

## Pré-requisitos

O instalador verifica o que já existe na máquina e, para cada programa que falta, pede autorização antes de o instalar. Primeiro, a base de dados MariaDB, onde fica guardada toda a informação. Respondemos s, de sim.

Depois, o nginx: o servidor web, que entrega as páginas ao browser. Também sim. Cada resposta lança a instalação desse programa a partir dos repositórios oficiais do Ubuntu.

```{figure} /_static/img/04-instalar-nativo/06.jpg
:alt: Instalar o que falta — MariaDB e nginx

Instalar o que falta — MariaDB e nginx.
```

A seguir, o Docker. Mesmo no modo nativo, é preciso para uma peça: o Presidio, que protege os dados pessoais antes de qualquer texto seguir para uma inteligência artificial. O instalador põe a versão aprovada, a partir do repositório oficial do Docker.

E o Node.js, na versão 22: é o motor que corre a aplicação. O instalador obtém-no do repositório NodeSource e, no fim, confirma a versão que ficou instalada.

```{figure} /_static/img/04-instalar-nativo/07.jpg
:alt: Docker e Node.js 22

Docker e Node.js 22.
```

Por último, o PM2: é ele que mantém a aplicação sempre a correr, e a volta a arrancar se o servidor reiniciar. Depois, sem perguntar, o instalador acrescenta as ferramentas de análise que a plataforma usa — como o nmap e o semgrep.

```{figure} /_static/img/04-instalar-nativo/08.jpg
:alt: PM2 e ferramentas de análise

PM2 e ferramentas de análise.
```

Agora vem a etapa mais demorada: preparar o Presidio, com o modelo de língua portuguesa. São perto de dois gigabytes a descarregar, e só acontece da primeira vez.

Quando termina, o instalador não se fica pelo «arrancou»: pede-lhe que analise uma frase de ensaio, e só diz que está pronto quando o Presidio responde a sério.

```{figure} /_static/img/04-instalar-nativo/09.jpg
:alt: Presidio — o guardião dos dados pessoais

Presidio — o guardião dos dados pessoais.
```

## O assistente

Os programas estão instalados. Entra agora o assistente de configuração, que faz cinco perguntas e escreve o ficheiro de configuração da plataforma. Primeiro, confirma os pré-requisitos.

```{figure} /_static/img/04-instalar-nativo/10.jpg
:alt: O assistente de configuração

O assistente de configuração.
```

A base de dados. Pede a palavra-passe do administrador da base, duas vezes, para confirmar. Depois o nome do utilizador da aplicação — carregamos em Enter para aceitar o que propõe — e a palavra-passe dele, com pelo menos doze caracteres, também duas vezes.

Nenhuma palavra-passe aparece no ecrã, e o assistente avisa disso antes de começar. Se as duas não coincidirem, volta a perguntar.

```{figure} /_static/img/04-instalar-nativo/11.jpg
:alt: Base de dados — duas palavras-passe

Base de dados — duas palavras-passe.
```

Os segredos de segurança são as chaves que protegem as sessões de quem entra na plataforma. Não precisamos de inventar nenhum: o assistente gera-os ao acaso. Só pergunta se os queremos ver no ecrã — respondemos que não.

```{figure} /_static/img/04-instalar-nativo/12.jpg
:alt: Os segredos — gerados sozinhos

Os segredos — gerados sozinhos.
```

Agora, a aplicação. Um nome, que aparece nas aplicações autenticadoras: SecVision. Depois o endereço pelo qual o browser vai chegar à plataforma. Aqui, nesta máquina de laboratório, é localhost; num servidor da sua rede, será o nome desse servidor.

A porta fica em 8080. Como não é a porta habitual, o assistente propõe-se a acertar o endereço completo — respondemos que sim. O limite de tamanho dos ficheiros enviados fica nos cinquenta megabytes propostos.

```{figure} /_static/img/04-instalar-nativo/13.jpg
:alt: Endereço e porta

Endereço e porta.
```

O assistente mostra o resumo do que vai gravar. Confirmamos, e ele escreve o ficheiro de configuração, só legível pelo nosso utilizador.

```{figure} /_static/img/04-instalar-nativo/14.jpg
:alt: Rever e gravar

Rever e gravar.
```

## Construção e arranque

O instalador constrói a aplicação: descarrega as bibliotecas de que ela depende e prepara as páginas que o browser vai mostrar. É outra espera.

```{figure} /_static/img/04-instalar-nativo/15.jpg
:alt: Construir a aplicação

Construir a aplicação.
```

A última fase põe tudo a funcionar. Cria a base de dados e as suas tabelas — cada linha com um visto é uma parte da estrutura aplicada. Configura o nginx, arranca a aplicação com o PM2 e regista as tarefas que correm sozinhas todas as noites.

No fim, espera que a aplicação responda, cria a conta de administrador inicial e confirma que a proteção dos dados pessoais ficou configurada.

```{figure} /_static/img/04-instalar-nativo/16.jpg
:alt: Base de dados, nginx, PM2 e tarefas agendadas

Base de dados, nginx, PM2 e tarefas agendadas.
```

## Resumo

Instalação concluída. O resumo mostra o endereço da plataforma e a conta inicial: admin, com a palavra-passe ChangeMe123!. Anote-as — vamos usá-las já na página do primeiro acesso.

E «normas carregadas: vinte e quatro» é o número certo: são as normas e a legislação que vêm com a plataforma. As normas ISO compram-se à parte, e quem as tiver instala-as depois.

```{figure} /_static/img/04-instalar-nativo/17.jpg
:alt: Instalação concluída

Instalação concluída.
```

## Confirmar que funciona

Vamos confirmar com os nossos olhos. O pm2 status mostra a aplicação, secinventory-api, no estado online. Se aparecesse errored, ou a coluna dos reinícios estivesse sempre a subir, era sinal de problema.

Escreva:

```bash
pm2 status
```

```{figure} /_static/img/04-instalar-nativo/18.jpg
:alt: pm2 status

Pm2 status.
```

Por fim, perguntamos à própria aplicação se está bem: responde status ok, em ambiente de produção. E o nginx, na porta 8080, responde com o código 200 — quer dizer que a página está a ser servida.

A instalação está feita e confirmada. Se algum passo tivesse falhado, o registo completo está no ficheiro setup-install.log, dentro da pasta do SecVision.

Escreva:

```bash
curl -s http://localhost:4000/api/health; echo
curl -sI http://localhost:8080 | head -1
```

```{figure} /_static/img/04-instalar-nativo/19.jpg
:alt: A plataforma responde

A plataforma responde.
```
