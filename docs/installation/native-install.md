# Instalar em modo nativo

Instalação completa em modo nativo, num Ubuntu 24.04 recém-instalado: obtenção do código, execução do instalador, respostas às perguntas, conclusão e verificação do funcionamento da plataforma.

```{video} 04-instalar-nativo
```

Esta página descreve a instalação do SecVision em modo nativo, numa máquina Ubuntu 24.04 recém-instalada e sem outro software, com todas as etapas apresentadas tal como ocorrem.

A gravação foi feita numa máquina de laboratório, um Ubuntu no WSL. Num servidor, os comandos e as perguntas são os mesmos; apenas o endereço de acesso à plataforma é diferente.

## Verificação da máquina

Abra o terminal no servidor e confirme a máquina de destino. O comando `whoami` indica o utilizador com sessão iniciada: **secv**, um utilizador normal com permissão de `sudo`.

O comando `lsb_release` indica o sistema: Ubuntu 24.04, a versão de suporte prolongado. Esta verificação evita a instalação na máquina errada.

Introduza:

```bash
whoami
lsb_release -d
```

```{figure} /_static/img/04-instalar-nativo/01.jpg
:alt: Onde estamos

Verificação da máquina.
```

## Obtenção do código

Copie o código do SecVision para o servidor com o comando `git clone`. O git é a ferramenta que guarda o código e o histórico de todas as versões.

O endereço depende do local onde o repositório está alojado. Neste exemplo, é utilizado o endereço do laboratório; numa instalação real, utilize o endereço indicado pela organização. A cópia é criada numa pasta chamada **secvision**.

Introduza:

```bash
git clone <endereço-do-repositório> secvision
```

```{figure} /_static/img/04-instalar-nativo/02.jpg
:alt: git clone

`git clone`.
```

Entre na pasta com `cd` e liste o conteúdo com `ls`. As pastas **backend** e **frontend** são as duas partes da aplicação, a pasta **documentacao** contém o manual e o ficheiro **setup.sh** é o instalador.

Introduza:

```bash
cd secvision
ls
```

```{figure} /_static/img/04-instalar-nativo/03.jpg
:alt: A pasta do SecVision

A pasta do SecVision.
```

## Instalador

Execute o instalador com `bash setup.sh`. O instalador começa por pedir permissões de administrador, pelo que é solicitada a palavra-passe do `sudo`. Introduza a palavra-passe do utilizador (não são apresentados caracteres) e prima Enter.

Introduza:

```bash
bash setup.sh
```

Respostas dadas às perguntas do instalador nesta instalação:

| Pergunta do instalador | Resposta |
|---|---|
| [sudo] password for secv | (a palavra-passe do utilizador) |
| Opção [1/2] | `2` |
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

```{figure} /_static/img/04-instalar-nativo/04.jpg
:alt: bash setup.sh

`bash setup.sh`.
```

A primeira pergunta é o modo de instalação. Introduza **2**, para o modo nativo. O instalador deteta o ambiente WSL e recomenda o modo nativo; num servidor Ubuntu, esta nota não é apresentada.

Premir Enter sem introduzir nenhum valor seleciona o modo Docker, descrito na página seguinte.

```{figure} /_static/img/04-instalar-nativo/05.jpg
:alt: Escolher o modo — 2, nativo

Escolha do modo: 2, nativo.
```

## Pré-requisitos

O instalador verifica o software existente na máquina e, para cada programa em falta, solicita autorização antes de o instalar. Primeiro, a base de dados MariaDB, onde é guardada toda a informação. Responda **s** (sim).

Em seguida, o nginx, o servidor web que disponibiliza as páginas ao browser. Responda também **s**. Cada resposta inicia a instalação do programa a partir dos repositórios oficiais do Ubuntu.

```{figure} /_static/img/04-instalar-nativo/06.jpg
:alt: Instalar o que falta — MariaDB e nginx

Instalação dos programas em falta: MariaDB e nginx.
```

Segue-se o Docker. Mesmo no modo nativo, o Docker é necessário para o Presidio, que protege os dados pessoais antes do envio de qualquer texto para um serviço de inteligência artificial. O instalador instala a versão aprovada, a partir do repositório oficial do Docker.

Em seguida, o Node.js 22, que executa a aplicação. O instalador obtém-no do repositório NodeSource e, no final, confirma a versão instalada.

```{figure} /_static/img/04-instalar-nativo/07.jpg
:alt: Docker e Node.js 22

Docker e Node.js 22.
```

Por último, o PM2, que mantém a aplicação em execução e a reinicia após um reinício do servidor. Em seguida, o instalador acrescenta, sem solicitar confirmação, as ferramentas de análise utilizadas pela plataforma, como o nmap e o semgrep.

```{figure} /_static/img/04-instalar-nativo/08.jpg
:alt: PM2 e ferramentas de análise

PM2 e ferramentas de análise.
```

A etapa mais demorada é a preparação do Presidio, com o modelo de língua portuguesa. São transferidos cerca de dois gigabytes, apenas na primeira instalação.

No final, o instalador verifica o funcionamento do Presidio com a análise de uma frase de teste. A instalação só é dada como concluída quando o serviço devolve uma resposta válida.

```{figure} /_static/img/04-instalar-nativo/09.jpg
:alt: Presidio — o guardião dos dados pessoais

Presidio: proteção dos dados pessoais.
```

## Assistente de configuração

Com os programas instalados, é iniciado o assistente de configuração, que coloca cinco perguntas e cria o ficheiro de configuração da plataforma. O assistente começa por confirmar os pré-requisitos.

```{figure} /_static/img/04-instalar-nativo/10.jpg
:alt: O assistente de configuração

O assistente de configuração.
```

**Base de dados:** Introduza a palavra-passe do administrador da base de dados, duas vezes. Em seguida, prima Enter para aceitar o nome proposto para o utilizador da aplicação e introduza a respetiva palavra-passe, com pelo menos doze caracteres, também duas vezes.

As palavras-passe não são apresentadas no ecrã, conforme indicado pelo assistente. Se as duas entradas não coincidirem, a pergunta é repetida.

```{figure} /_static/img/04-instalar-nativo/11.jpg
:alt: Base de dados — duas palavras-passe

Base de dados: duas palavras-passe.
```

**Segredos de segurança:** São as chaves que protegem as sessões dos utilizadores da plataforma. O assistente gera-os aleatoriamente e pergunta apenas se devem ser apresentados no ecrã. Responda **n**.

```{figure} /_static/img/04-instalar-nativo/12.jpg
:alt: Os segredos — gerados sozinhos

Segredos gerados automaticamente.
```

**Aplicação:** Indique o nome apresentado nas aplicações autenticadoras (**SecVision**) e o endereço de acesso à plataforma no browser. Nesta máquina de laboratório, o endereço é **localhost**; num servidor da rede, utilize o nome do servidor.

A porta é a **8080**. Por não ser a porta habitual, o assistente propõe corrigir o endereço completo; responda **s**. O limite de tamanho dos ficheiros enviados mantém-se nos cinquenta megabytes propostos.

```{figure} /_static/img/04-instalar-nativo/13.jpg
:alt: Endereço e porta

Endereço e porta.
```

O assistente apresenta o resumo da configuração. Após a confirmação, é criado o ficheiro de configuração, legível apenas pelo utilizador.

```{figure} /_static/img/04-instalar-nativo/14.jpg
:alt: Rever e gravar

Revisão e gravação.
```

## Construção e arranque

O instalador constrói a aplicação: transfere as bibliotecas necessárias e prepara as páginas apresentadas no browser. Esta etapa também é demorada.

```{figure} /_static/img/04-instalar-nativo/15.jpg
:alt: Construir a aplicação

Construção da aplicação.
```

A última fase coloca a plataforma em funcionamento. São criadas a base de dados e as respetivas tabelas (cada linha com um visto corresponde a uma parte da estrutura aplicada), configurado o nginx, iniciada a aplicação com o PM2 e registadas as tarefas executadas automaticamente todas as noites.

No final, o instalador aguarda a resposta da aplicação, cria a conta de administrador inicial e confirma a configuração da proteção dos dados pessoais.

```{figure} /_static/img/04-instalar-nativo/16.jpg
:alt: Base de dados, nginx, PM2 e tarefas agendadas

Base de dados, nginx, PM2 e tarefas agendadas.
```

## Resumo

Com a instalação concluída, o resumo apresenta o endereço da plataforma e a conta inicial: **admin**, com a palavra-passe **ChangeMe123!**. Anote estes dados, necessários para o primeiro acesso.

A indicação «normas carregadas: vinte e quatro» corresponde ao número esperado: as normas e a legislação incluídas na plataforma. As normas ISO são adquiridas separadamente e instaladas posteriormente.

```{figure} /_static/img/04-instalar-nativo/17.jpg
:alt: Instalação concluída

Instalação concluída.
```

## Verificação do funcionamento

O comando `pm2 status` apresenta a aplicação **secinventory-api** no estado **online**. Os estados **errored**, ou um número de reinícios em crescimento constante, indicam um problema.

Introduza:

```bash
pm2 status
```

```{figure} /_static/img/04-instalar-nativo/18.jpg
:alt: pm2 status

`pm2 status`.
```

Por fim, consulte o estado da aplicação: a resposta **status ok**, em ambiente de produção, confirma o funcionamento. O nginx, na porta 8080, responde com o código 200, o que indica que a página está a ser disponibilizada.

A instalação está concluída e verificada. Em caso de falha num dos passos, o registo completo encontra-se no ficheiro **setup-install.log**, na pasta do SecVision.

Introduza:

```bash
curl -s http://localhost:4000/api/health; echo
curl -sI http://localhost:8080 | head -1
```

```{figure} /_static/img/04-instalar-nativo/19.jpg
:alt: A plataforma responde

A plataforma responde.
```
