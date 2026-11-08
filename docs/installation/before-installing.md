# Antes de instalar

Ponto de partida do manual: o que é o SecVision, os conceitos básicos de terminal necessários para acompanhar o manual, os dois modos de instalação e o critério de escolha, os requisitos da máquina e as perguntas do instalador.

```{video} 01-antes-de-instalar
```

Este manual descreve a instalação do SecVision de raiz, passo a passo. Não é necessária experiência prévia com Linux nem com cibersegurança: cada etapa indica a operação a realizar, o respetivo objetivo e o resultado esperado no ecrã.

Esta primeira parte descreve a preparação. As duas páginas seguintes tratam do servidor: obter e instalar o Ubuntu Server. Seguem-se os dois modos de instalação do SecVision, o primeiro acesso à plataforma e o ambiente de testes.

## O SecVision

O SecVision é uma plataforma web que reúne o inventário dos sistemas da organização e identifica os sistemas monitorizados pelas ferramentas de segurança e os que não têm monitorização.

A plataforma apoia também a gestão da segurança da informação: normas aplicáveis, riscos, controlos e auditorias. É instalada uma única vez num servidor e utilizada através do browser, como qualquer site.

**O que é o SecVision**

- Uma plataforma web que reúne o inventário dos sistemas, a partir do Active Directory, do DNS e do DHCP.
- Identifica os sistemas protegidos e os sistemas sem proteção, por nível de criticidade (N1 a N4).
- Apoia a gestão da segurança da informação: normas, riscos, controlos, evidências e auditorias.
- É instalada uma vez num servidor; os utilizadores acedem pelo browser, sem instalar software no seu computador.

## Conceitos básicos de terminal

O terminal é uma janela onde se introduzem comandos por escrito. Cada comando é executado com a tecla Enter. A linha terminada em cifrão indica o utilizador, a máquina e que o terminal está pronto para o comando seguinte.

Algumas tarefas exigem permissões de administrador, obtidas com o comando `sudo`, que solicita a palavra-passe do próprio utilizador. Durante a introdução da palavra-passe, não é apresentado nenhum caráter no ecrã; trata-se do comportamento normal. Introduza a palavra-passe e prima Enter.

**O terminal, em resumo**

- O terminal é uma janela onde se introduzem comandos por escrito: um comando, seguido da tecla Enter.
- A linha «secv@secvision:~$» indica o utilizador (secv), a máquina (secvision) e que o terminal aguarda um comando.
- «sudo» antes de um comando pede permissões de administrador. O sistema solicita a palavra-passe do próprio utilizador.
- Durante a introdução de uma palavra-passe no terminal, não são apresentados caracteres nem asteriscos. Introduza a palavra-passe e prima Enter.

## Modos de instalação

O instalador disponibiliza dois modos de instalação, escolhidos na primeira pergunta. No modo Docker, cada componente do SecVision é executado num contentor próprio: um ambiente isolado que inclui tudo o que o componente necessita. É o modo proposto por omissão.

No modo nativo, os componentes são instalados diretamente no sistema: a base de dados MariaDB, o Node.js que executa a aplicação, o nginx que disponibiliza as páginas ao browser e o PM2, que mantém a aplicação em execução. Para o utilizador, o resultado é o mesmo.

**Dois modos de instalação**

Modo Docker
: Cada componente é executado num contentor próprio, isolado e com tudo o que necessita

Modo nativo
: Os componentes são instalados no próprio sistema: base de dados, Node.js, nginx e PM2

```{figure} /_static/img/01-antes-de-instalar/01.jpg
:alt: Duas maneiras de instalar

Dois modos de instalação.
```

O modo Docker é a opção por omissão e mantém os componentes organizados em contentores. O modo nativo é indicado para um PC com Windows, através do WSL, sem Docker Desktop, ou quando se pretende ter cada componente instalado diretamente no sistema.

Em ambos os modos, o instalador instala também o Docker, porque o Presidio é sempre executado num contentor. O Presidio deteta e oculta os dados pessoais antes do envio de qualquer texto para um serviço de inteligência artificial. Sem o Presidio, estas funcionalidades ficam desativadas.

**Critérios de escolha**

- Docker: opção por omissão. Os componentes ficam organizados em contentores e a atualização é feita com um comando do Docker.
- Nativo: indicado para um PC com Windows (WSL2) sem Docker Desktop, ou quando se pretende ter os componentes instalados diretamente no sistema.
- Em ambos os casos, o instalador instala o Docker, porque o Presidio é sempre executado num contentor.
- O Presidio protege os dados pessoais antes do envio de qualquer texto para um serviço de inteligência artificial.

```{tip}
Em caso de dúvida, utilize o modo que a equipa de sistemas já adota noutros servidores.
```

## Requisitos da máquina

É necessário um servidor dedicado, físico ou virtual, com o Ubuntu Server 24.04. O SecVision é utilizado por várias pessoas em simultâneo, através da rede, pelo que a máquina deve estar sempre ligada e ter um endereço fixo. Para testes num PC com Windows, é possível instalar através do WSL (algumas destas gravações foram feitas numa máquina de laboratório deste tipo), mas esta opção não é adequada para produção.

É necessário um utilizador com permissão de `sudo`. Não é necessário nem recomendado trabalhar como root (o administrador total do sistema). A máquina deve ter acesso à internet durante a instalação. Como configuração inicial, são suficientes quatro processadores, oito gigabytes de memória e cerca de quarenta gigabytes livres em disco.

**Requisitos**

- Um servidor dedicado, físico ou virtual, com Ubuntu Server 24.04 LTS, sempre ligado e com endereço fixo.
- Para testes ou demonstrações, é possível utilizar um PC com Windows, através do WSL2; esta opção não é adequada para produção.
- Um utilizador com permissão de `sudo`. Não é necessário nem recomendado trabalhar como root.
- Acesso à internet durante a instalação: o instalador descarrega programas, bibliotecas e contentores.
- Configuração inicial: 4 processadores, 8 GB de memória e cerca de 40 GB livres em disco.

```{tip}
Estes valores correspondem à máquina de laboratório destas páginas. Em produção, preveja mais espaço em disco para as evidências e as cópias de segurança.
```

## Perguntas do instalador

Recomenda-se preparar as respostas antes da instalação. O instalador solicita duas palavras-passe para a base de dados (a do administrador e a da aplicação), com pelo menos doze caracteres. Guarde-as num cofre de palavras-passe.

O instalador solicita também o endereço de acesso à plataforma. Este endereço é relevante para as chaves de segurança físicas, como a YubiKey, que só funcionam no endereço configurado. É ainda solicitada a porta: a 80, ou a 8080 se a 80 estiver ocupada. No final, é apresentada a conta inicial: admin.

**Perguntas do instalador**

- Duas palavras-passe para a base de dados: a do administrador (root) e a da aplicação, com 12 ou mais caracteres.
- O endereço de acesso à plataforma; por exemplo, o nome do servidor na rede.
- A porta: o instalador propõe a 80, ou a 8080 se a 80 estiver ocupada.
- No final, são apresentados o endereço e a conta inicial: admin, com a palavra-passe ChangeMe123!.

```{tip}
Guarde as palavras-passe num cofre de palavras-passe antes de começar. Nenhuma é apresentada no ecrã durante a introdução.
```

## Antes do primeiro acesso

No primeiro acesso, a plataforma exige a alteração da palavra-passe inicial e a ativação do segundo fator de autenticação. Tenha disponível um telemóvel com uma aplicação autenticadora ou uma chave de segurança.

Este passo é obrigatório, uma vez que o SecVision guarda informação sensível sobre a segurança da organização e uma palavra-passe, por si só, não oferece proteção suficiente.

```{important}
- O primeiro acesso exige a alteração da palavra-passe inicial e a ativação do segundo fator de autenticação.
- Tenha disponível um telemóvel com uma aplicação autenticadora (por exemplo, Google ou Microsoft Authenticator) ou uma chave FIDO2.
- Sem o segundo fator, não é possível aceder à plataforma.
```
