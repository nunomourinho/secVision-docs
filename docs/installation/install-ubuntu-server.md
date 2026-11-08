# Instalar o Ubuntu Server

O instalador do Ubuntu Server 24.04 do início ao fim: idioma e teclado, rede, discos com LVM (com todo o espaço atribuído ao sistema), utilizador, servidor SSH, instalação, primeiro arranque e primeiras tarefas num servidor novo.

```{video} 03-instalar-ubuntu-server
```

Com a imagem do Ubuntu Server verificada, o servidor é arrancado a partir dela para instalar o sistema. Este exemplo utiliza uma máquina virtual, mas os ecrãs são os mesmos de um servidor físico arrancado a partir de uma pen.

## Primeiros ecrãs

Depois do arranque, é carregado o instalador. A navegação é feita com o teclado: as setas para selecionar e o Enter para confirmar.

O primeiro ecrã define o idioma do instalador. Recomenda-se manter o inglês, utilizado na generalidade dos guias e nas mensagens de erro pesquisadas na internet. O idioma não altera o funcionamento do servidor.

```{figure} /_static/img/03-instalar-ubuntu-server/01.jpg
:alt: Idioma — English

Idioma: English.
```

O teclado deve corresponder ao teclado utilizado: abra a lista, selecione **Portuguese** e confirme.

Com o teclado incorreto, os símbolos das palavras-passe são introduzidos de forma errada, o que impede o início de sessão posterior.

```{figure} /_static/img/03-instalar-ubuntu-server/02.jpg
:alt: Teclado — Portuguese

Teclado: Portuguese.
```

No tipo de instalação, mantenha a opção **Ubuntu Server**, selecionada por omissão. A versão mínima destina-se a sistemas sem acesso interativo.

```{figure} /_static/img/03-instalar-ubuntu-server/03.jpg
:alt: Ubuntu Server

Ubuntu Server.
```

## Rede

O instalador deteta a placa de rede e obtém um endereço automaticamente, por DHCP.

Num servidor de produção, recomenda-se um endereço fixo, para que os utilizadores acedam sempre ao mesmo endereço. Este endereço pode ser configurado neste ecrã, na placa de rede, ou através de uma reserva no DHCP, pedida à equipa de informática. No laboratório, a configuração mantém-se.

```{figure} /_static/img/03-instalar-ubuntu-server/04.jpg
:alt: Rede

Rede.
```

Se a rede da organização exigir um proxy para aceder à internet, indique-o neste ecrã. Neste exemplo, não é utilizado.

```{figure} /_static/img/03-instalar-ubuntu-server/05.jpg
:alt: Proxy e mirror

Proxy e mirror.
```

O *mirror* é o servidor de onde são obtidos os pacotes e as atualizações. O instalador seleciona o *mirror* português e testa-o; a indicação **passed tests** confirma que o teste foi concluído com sucesso.

```{figure} /_static/img/03-instalar-ubuntu-server/06.jpg
:alt: O mirror português

O *mirror* português.
```

## Discos

Utilize o disco inteiro, organizado com LVM, uma camada que permite aumentar o espaço posteriormente sem reinstalar. Esta opção está selecionada por omissão.

```{figure} /_static/img/03-instalar-ubuntu-server/07.jpg
:alt: Disco inteiro, com LVM

Disco inteiro, com LVM.
```

No resumo, o sistema (`/`) fica apenas com dezanove gigabytes, e os restantes dezanove ficam livres. Esta é a configuração por omissão do Ubuntu.

O SecVision necessita de todo o espaço disponível para as imagens dos contentores, as evidências e as cópias de segurança. Para isso, edite o volume **ubuntu-lv**.

```{figure} /_static/img/03-instalar-ubuntu-server/08.jpg
:alt: O / só com metade do disco

O `/` apenas com metade do disco.
```

No campo do tamanho, apague o valor e introduza o máximo indicado entre parênteses. Clique em **Save** para guardar.

```{figure} /_static/img/03-instalar-ubuntu-server/09.jpg
:alt: Alargar o volume ao máximo

Expansão do volume ao máximo.
```

O sistema passa a dispor de todo o espaço. Selecione **Done**; o instalador avisa que o conteúdo do disco será apagado. Confirme com **Continue**.

```{figure} /_static/img/03-instalar-ubuntu-server/10.jpg
:alt: Confirmar — o disco vai ser apagado

Confirmação: o disco será apagado.
```

## Utilizador e acesso

No perfil, indique o nome, o nome do servidor (**secvision**, o nome com que a máquina se identifica na rede), o nome do utilizador (**secv**) e a palavra-passe, duas vezes.

Este utilizador terá permissão de `sudo`. Escolha uma palavra-passe forte e guarde-a num cofre de palavras-passe, uma vez que dá acesso ao servidor.

```{figure} /_static/img/03-instalar-ubuntu-server/11.jpg
:alt: O servidor e o utilizador

O servidor e o utilizador.
```

O Ubuntu Pro é uma subscrição opcional da Canonical. Selecione **Skip for now**; a subscrição pode ser ativada mais tarde.

```{figure} /_static/img/03-instalar-ubuntu-server/12.jpg
:alt: Ubuntu Pro — Skip for now

Ubuntu Pro: Skip for now.
```

Assinale **Install OpenSSH server** com a barra de espaços. Esta opção permite administrar o servidor remotamente, a partir de outro computador.

```{figure} /_static/img/03-instalar-ubuntu-server/13.jpg
:alt: Install OpenSSH server

Install OpenSSH server.
```

Não assinale nenhum *snap* da lista.

Em particular, não instale o Docker neste ecrã: o instalador do SecVision instala a versão aprovada, a partir do repositório oficial, e uma segunda instalação causaria conflitos.

```{figure} /_static/img/03-instalar-ubuntu-server/14.jpg
:alt: Nenhum snap

Nenhum *snap*.
```

## Instalação

O instalador prepara os discos, copia o sistema, instala o arranque e o servidor SSH e transfere as atualizações de segurança já publicadas.

```{figure} /_static/img/03-instalar-ubuntu-server/15.jpg
:alt: A instalar o sistema

Instalação do sistema.
```

Quando surgir **Installation complete**, selecione **Reboot Now** para reiniciar no sistema instalado.

```{figure} /_static/img/03-instalar-ubuntu-server/16.jpg
:alt: Installation complete — Reboot Now

Installation complete: Reboot Now.
```

O instalador pede para retirar o suporte de instalação (a pen ou o ISO da máquina virtual) e premir Enter.

As linhas a vermelho com **FAILED** são normais neste momento: o sistema tenta desmontar a imagem que está a ser retirada.

```{figure} /_static/img/03-instalar-ubuntu-server/17.jpg
:alt: Retirar o suporte

Remoção do suporte de instalação.
```

## Primeiro arranque

O servidor arranca pela primeira vez a partir do disco e apresenta o pedido de início de sessão: **secvision login**.

```{figure} /_static/img/03-instalar-ubuntu-server/18.jpg
:alt: O primeiro arranque

O primeiro arranque.
```

Inicie sessão com o utilizador **secv** e a respetiva palavra-passe. Tal como no terminal do Windows, a palavra-passe não é apresentada durante a introdução.

```{figure} /_static/img/03-instalar-ubuntu-server/19.jpg
:alt: Primeiro login

Primeiro início de sessão.
```

Efetue três verificações:

- `ip`: apresenta o endereço do servidor na rede, utilizado para lhe aceder.
- `df`: confirma que o sistema (`/`) dispõe dos trinta e oito gigabytes atribuídos.
- Fuso horário: o servidor é instalado em UTC. Altere-o para Lisboa com o `timedatectl`, para que as datas e horas do SecVision correspondam à hora local.

```{figure} /_static/img/03-instalar-ubuntu-server/20.jpg
:alt: Endereço, disco e fuso horário

Endereço, disco e fuso horário.
```

Por fim, atualize o sistema: `sudo apt update`, para obter a lista de atualizações, e `full-upgrade`, para as instalar. Esta prática é recomendada antes de instalar qualquer aplicação num servidor novo.

```{figure} /_static/img/03-instalar-ubuntu-server/21.jpg
:alt: Atualizar o sistema

Atualização do sistema.
```

O servidor está instalado, atualizado e acessível por SSH.

```{figure} /_static/img/03-instalar-ubuntu-server/22.jpg
:alt: Servidor pronto

Servidor pronto.
```

## Resumo

A partir deste ponto, não é necessário aceder fisicamente ao servidor. No Windows, abra o PowerShell e introduza `ssh`, seguido do utilizador, de uma arroba e do endereço do servidor. Os comandos das páginas seguintes são introduzidos nessa sessão.

**Acesso por SSH**

- No Windows, abra o PowerShell e introduza: ssh secv@ seguido do endereço do servidor.
- Os comandos das páginas seguintes são introduzidos nessa sessão, com o mesmo efeito do que no próprio servidor.
- Guarde o endereço, o utilizador e a palavra-passe, necessários para qualquer intervenção no servidor.
