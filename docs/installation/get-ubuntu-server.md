# Obter o Ubuntu Server

Descarregar o Ubuntu Server 24.04 LTS do site oficial, confirmar a imagem com o SHA256 e prepará-la para o servidor: uma pen de arranque, ou o ISO numa máquina virtual.

```{video} 02-obter-ubuntu-server
```

O SecVision instala-se num servidor com Linux — concretamente, com o Ubuntu Server. Antes de o instalar, temos de o obter. Nesta página descarregamos a imagem do site oficial, confirmamos que chegou intacta, e vemos como a levar até ao servidor.

## Porquê

Porquê um servidor? Porque o SecVision é partilhado: várias pessoas usam-no ao mesmo tempo, cada uma a partir do seu computador, pela rede. Precisa de uma máquina sempre ligada, com um endereço fixo que todos conheçam.

Pode ser um servidor físico ou uma máquina virtual — num Proxmox, num VMware ou num Hyper-V. Num PC com Windows também se consegue instalar, através do WSL, mas isso é para experimentar e demonstrar: quando o PC se desliga, a plataforma desliga-se com ele.

**Porquê um servidor**

- O SecVision é usado por várias pessoas ao mesmo tempo, a partir dos seus computadores, pela rede.
- Por isso vive num servidor dedicado — físico ou máquina virtual — sempre ligado e com endereço fixo.
- Num PC com Windows, o WSL serve para testes e demonstrações, não para a produção.

## Descarregar

A imagem obtém-se sempre no site oficial: ubuntu.com/download/server. Nunca de um sítio qualquer — é o sistema que vai guardar a informação de segurança da organização. Aceitamos os cookies para continuar.

```{figure} /_static/img/02-obter-ubuntu-server/01.jpg
:alt: ubuntu.com/download/server

Ubuntu.com/download/server.
```

A página propõe logo a versão mais recente, a 26.04. Mas não é essa que queremos.

O SecVision foi preparado e verificado sobre o Ubuntu 24.04 LTS. LTS quer dizer suporte prolongado: atualizações de segurança gratuitas até 2029. Num servidor de produção, usa-se a versão com que a aplicação foi testada.

```{figure} /_static/img/02-obter-ubuntu-server/02.jpg
:alt: A versão mais recente não é a nossa

A versão mais recente não é a nossa.
```

Descemos até às versões anteriores, ainda suportadas, e escolhemos Download 24.04.5 LTS. O 5 é a quinta revisão da 24.04: traz já as correções publicadas desde o lançamento.

```{figure} /_static/img/02-obter-ubuntu-server/03.jpg
:alt: Previous releases — 24.04.5 LTS

Previous releases — 24.04.5 LTS.
```

O download começa sozinho. É um ficheiro ISO com cerca de quatro gigabytes — uma imagem completa do disco de instalação. Pode demorar uns minutos.

Repare na ligação verify your download. É o passo que muita gente salta, e não devia.

```{figure} /_static/img/02-obter-ubuntu-server/04.jpg
:alt: O download começa

O download começa.
```

## Confirmar a imagem

No servidor de imagens do Ubuntu, ao lado de cada ISO, há um ficheiro chamado SHA256SUMS. Tem uma linha por imagem, com uma espécie de impressão digital do ficheiro: um código de 64 caracteres.

Se um único byte do ISO mudar — porque o download falhou a meio, ou porque alguém o adulterou — a impressão digital muda por completo. Por isso compara-se a do ficheiro descarregado com a oficial.

```{figure} /_static/img/02-obter-ubuntu-server/05.jpg
:alt: A lista oficial de SHA256

A lista oficial de SHA256.
```

No Windows, abrimos o PowerShell na pasta das transferências. O comando Get-FileHash calcula a impressão digital SHA256 do ISO. Demora uns segundos, porque lê o ficheiro inteiro.

```{figure} /_static/img/02-obter-ubuntu-server/06.jpg
:alt: Get-FileHash

Get-FileHash.
```

E vamos buscar a lista oficial, filtrada às imagens de servidor. A linha da 24.04.5 começa por 97f3d7ff e acaba em 0fd8 — exatamente como a nossa. A imagem está intacta.

Se fossem diferentes, não se usava: apagava-se o ficheiro e descarregava-se de novo.

```{figure} /_static/img/02-obter-ubuntu-server/07.jpg
:alt: As duas são iguais

As duas são iguais.
```

## Preparar o arranque

Falta levar a imagem até ao servidor. Num servidor físico, grava-se o ISO numa pen USB, com um programa como o Rufus ou o balenaEtcher, e arranca-se o servidor pela pen.

Numa máquina virtual é mais simples: carrega-se o ISO no Proxmox, no VMware ou no Hyper-V, e liga-se à drive de CD da máquina. Para começar, quatro processadores, oito gigabytes de memória e pelo menos quarenta de disco.

**Levar a imagem até ao servidor**

- Servidor físico: gravar o ISO numa pen USB de 8 GB ou mais, com o Rufus ou o balenaEtcher.
- Máquina virtual: carregar o ISO no Proxmox, VMware ou Hyper-V e ligá-lo à drive de CD da VM.
- Para começar: 4 processadores, 8 GB de memória e 40 GB de disco ou mais.
