# Instalar em modo Docker

Instalação completa em modo Docker, num Ubuntu 24.04 recém-instalado: o instalador instala o Docker, o assistente configura a aplicação e o Docker Compose inicia todos os componentes em contentores.

```{video} 05-instalar-docker
```

Esta página descreve a instalação do SecVision em modo Docker, numa máquina Ubuntu 24.04 recém-instalada. É o modo proposto por omissão pelo instalador. O assistente de configuração é o mesmo do modo nativo, pelo que muitas perguntas são idênticas. A gravação foi feita numa máquina de laboratório; num servidor, os passos são os mesmos.

## Diferenças face ao modo nativo

No modo Docker, cada componente do SecVision é executado num contentor próprio: a base de dados, a aplicação, o servidor das páginas e o Presidio. Por este motivo, a MariaDB, o nginx e o PM2 não são instalados no sistema.

O Docker Compose gere os quatro componentes: inicia-os pela ordem correta e reinicia-os automaticamente após um reinício do servidor.

**Diferenças no modo Docker**

- Cada componente é executado num contentor próprio: base de dados, aplicação, páginas e Presidio.
- A MariaDB, o nginx e o PM2 não são instalados no sistema; estão incluídos nos contentores.
- O Docker Compose inicia os quatro componentes pela ordem correta e reinicia-os após um reinício do servidor.

## Obtenção do código

Comece por confirmar o ponto de partida: o comando de versão do Docker indica que o comando não existe. A máquina não tem Docker; o instalador irá instalá-lo.

Introduza:

```bash
docker --version
```

```{figure} /_static/img/05-instalar-docker/01.jpg
:alt: Uma máquina sem Docker

Máquina sem Docker.
```

Copie o código para o servidor com `git clone`, tal como no modo nativo, e entre na pasta **secvision**.

Introduza:

```bash
git clone <endereço-do-repositório> secvision
```

```{figure} /_static/img/05-instalar-docker/02.jpg
:alt: git clone

`git clone`.
```

## Instalador

Execute o instalador com `bash setup.sh`. É solicitada a palavra-passe do `sudo`, necessária para instalar programas no sistema. Introduza a palavra-passe do utilizador (não são apresentados caracteres) e prima Enter.

Introduza:

```bash
bash setup.sh
```

Respostas dadas às perguntas do instalador nesta instalação:

| Pergunta do instalador | Resposta |
|---|---|
| [sudo] password for secv | (a palavra-passe do utilizador) |
| Opção [1/2] | `1` |
| Password root do MySQL | (a palavra-passe root da base de dados escolhida) |
| Confirme a password root | (a palavra-passe root da base de dados escolhida) |
| Utilizador da aplicação | Enter (aceita o valor proposto) |
| Password da aplicação | (a palavra-passe da aplicação escolhida) |
| Confirme a password da aplicação | (a palavra-passe da aplicação escolhida) |
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

```{figure} /_static/img/05-instalar-docker/03.jpg
:alt: bash setup.sh

`bash setup.sh`.
```

No menu do modo de instalação, introduza **1** (Docker). Esta é também a opção selecionada ao premir apenas Enter.

O instalador deteta o ambiente WSL e indica que o modo nativo é uma alternativa. Num servidor Linux, esta nota não é apresentada.

```{figure} /_static/img/05-instalar-docker/04.jpg
:alt: Escolher o modo — 1, Docker

Escolha do modo: 1, Docker.
```

O instalador verifica o Docker e deteta que não está instalado. É apresentada a base aprovada (Docker 24 ou mais recente, com o plugin Compose, a partir do repositório oficial) e solicitada autorização para a instalar. Responda **s**.

Numa máquina com o Docker da distribuição, sem o Compose, o instalador substituí-lo-ia, mas apenas após uma cópia de segurança. Neste caso, não existem dados a copiar, e o instalador indica-o. No final, são verificadas novamente as versões do Docker e do Compose.

```{figure} /_static/img/05-instalar-docker/05.jpg
:alt: A base Docker aprovada

A base Docker aprovada.
```

## Assistente de configuração

Em seguida, o instalador instala o Node.js 22, necessário para o assistente de configuração, e inicia o assistente. São confirmados os pré-requisitos: Node.js, Docker, serviço do Docker em execução e Compose.

O aviso de porta 80 ocupada nesta máquina não é um erro: o assistente propõe outra porta mais adiante.

```{figure} /_static/img/05-instalar-docker/06.jpg
:alt: Node.js 22 e o assistente

Node.js 22 e o assistente.
```

**Base de dados:** Introduza a palavra-passe do administrador, duas vezes, e a da aplicação, também duas vezes, com pelo menos doze caracteres. Para o nome do utilizador da aplicação, prima Enter para aceitar o valor proposto.

```{figure} /_static/img/05-instalar-docker/07.jpg
:alt: Base de dados — duas palavras-passe

Base de dados: duas palavras-passe.
```

**Segredos de segurança:** São gerados aleatoriamente pelo assistente. Quando questionado sobre a sua apresentação no ecrã, responda **n**.

```{figure} /_static/img/05-instalar-docker/08.jpg
:alt: Os segredos — gerados sozinhos

Segredos gerados automaticamente.
```

**Aplicação:** Indique o nome da aplicação (**SecVision**) e o endereço de acesso no browser (**localhost**, nesta máquina de laboratório). Indique a porta **8080**, uma vez que a 80 está ocupada.

No modo Docker, o assistente regista esta porta também no ficheiro do Docker Compose, para que o contentor das páginas fique à escuta na porta correta.

```{figure} /_static/img/05-instalar-docker/09.jpg
:alt: Endereço e porta 8080

Endereço e porta 8080.
```

É apresentado o resumo da configuração. Após a confirmação, o ficheiro de configuração é criado.

```{figure} /_static/img/05-instalar-docker/10.jpg
:alt: Rever e gravar

Revisão e gravação.
```

## Construção e arranque

O Docker Compose constrói as imagens (o modelo de cada contentor) e transfere os componentes em falta: a base de dados, o Node.js e o modelo de língua portuguesa do Presidio. É a etapa mais demorada.

Em caso de falha do Docker Compose nesta etapa, o instalador termina de imediato e apresenta as últimas linhas do registo.

```{figure} /_static/img/05-instalar-docker/11.jpg
:alt: Construir as imagens

Construção das imagens.
```

Com os contentores iniciados, o instalador aguarda que a base de dados fique operacional e verifica a resposta da aplicação. Só depois cria a conta de administrador inicial.

```{figure} /_static/img/05-instalar-docker/12.jpg
:alt: A API responde, e a conta inicial

A API responde e é criada a conta inicial.
```

## Verificação

Com a instalação concluída, são apresentados o endereço (**localhost**, na porta 8080) e a conta inicial: **admin**, com a palavra-passe **ChangeMe123!**. São carregadas as mesmas vinte e quatro normas do modo nativo.

Os comandos úteis apresentados no final começam por `sudo`. O utilizador foi adicionado ao grupo do Docker, mas esta permissão só tem efeito a partir da sessão seguinte. Até lá, utilize `sudo`.

```{figure} /_static/img/05-instalar-docker/13.jpg
:alt: Instalação concluída

Instalação concluída.
```

O comando `sudo docker compose ps` apresenta quatro contentores em execução. A base de dados e o Presidio indicam o estado **healthy**, o que confirma a respetiva verificação de saúde.

Introduza:

```bash
sudo docker compose ps
```

```{figure} /_static/img/05-instalar-docker/14.jpg
:alt: sudo docker compose ps

`sudo docker compose ps`.
```

Por fim, consulte o estado da aplicação na porta 8080: a resposta **status ok**, em ambiente de produção, confirma que a instalação em modo Docker está concluída e verificada.

Introduza:

```bash
curl -s http://localhost:8080/api/health; echo
```

```{figure} /_static/img/05-instalar-docker/15.jpg
:alt: A plataforma responde

A plataforma responde.
```

## Resumo

Três comandos de referência, a executar na pasta do SecVision: `ps` apresenta os contentores em execução; `logs` apresenta as mensagens da aplicação e é o primeiro passo do diagnóstico quando uma página não abre; `down` e `up` param e reiniciam todos os componentes.

**Comandos de referência**

- sudo docker compose ps — contentores em execução
- sudo docker compose logs -f backend — mensagens da aplicação
- sudo docker compose down e up -d — parar e reiniciar todos os componentes
