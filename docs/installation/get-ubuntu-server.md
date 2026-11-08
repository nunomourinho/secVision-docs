# Obter o Ubuntu Server

Transferência do Ubuntu Server 24.04 LTS a partir do site oficial, verificação da imagem com o SHA256 e preparação para o servidor: pen de arranque ou ISO numa máquina virtual.

```{video} 02-obter-ubuntu-server
```

O SecVision é instalado num servidor com o Ubuntu Server. Esta página descreve a transferência da imagem a partir do site oficial, a verificação da sua integridade e a preparação do arranque no servidor.

## Requisito de servidor dedicado

O SecVision é uma plataforma partilhada: várias pessoas utilizam-na em simultâneo, a partir dos seus computadores, através da rede. Por este motivo, requer uma máquina sempre ligada e com um endereço fixo.

O servidor pode ser físico ou virtual (Proxmox, VMware ou Hyper-V). A instalação num PC com Windows, através do WSL, destina-se apenas a testes e demonstrações, uma vez que a plataforma fica indisponível sempre que o PC é desligado.

**Requisitos do servidor**

- O SecVision é utilizado por várias pessoas em simultâneo, a partir dos seus computadores, através da rede.
- Requer um servidor dedicado, físico ou virtual, sempre ligado e com endereço fixo.
- Num PC com Windows, o WSL destina-se a testes e demonstrações, não à produção.

## Transferência

Obtenha a imagem apenas no site oficial: ubuntu.com/download/server. Esta máquina vai guardar a informação de segurança da organização, pelo que não devem ser utilizadas outras fontes. Aceite os cookies para continuar.

```{figure} /_static/img/02-obter-ubuntu-server/01.jpg
:alt: ubuntu.com/download/server

ubuntu.com/download/server.
```

A página propõe a versão mais recente, a 26.04, que não é a versão suportada.

O SecVision foi preparado e verificado sobre o Ubuntu 24.04 LTS. LTS significa suporte prolongado, com atualizações de segurança gratuitas até 2029. Num servidor de produção, deve ser utilizada a versão com a qual a aplicação foi testada.

```{figure} /_static/img/02-obter-ubuntu-server/02.jpg
:alt: A versão mais recente não é a nossa

A versão mais recente não é a versão suportada.
```

Na secção das versões anteriores ainda suportadas, selecione **Download 24.04.5 LTS**. O número 5 corresponde à quinta revisão da 24.04, que inclui as correções publicadas desde o lançamento.

```{figure} /_static/img/02-obter-ubuntu-server/03.jpg
:alt: Previous releases — 24.04.5 LTS

Previous releases — 24.04.5 LTS.
```

A transferência inicia automaticamente. O ficheiro ISO tem cerca de quatro gigabytes (uma imagem completa do disco de instalação) e pode demorar alguns minutos.

A ligação **verify your download** dá acesso ao passo de verificação, descrito a seguir, que não deve ser omitido.

```{figure} /_static/img/02-obter-ubuntu-server/04.jpg
:alt: O download começa

Início da transferência.
```

## Verificação da imagem

No servidor de imagens do Ubuntu, junto a cada ISO, existe um ficheiro SHA256SUMS. Este ficheiro contém uma linha por imagem com o respetivo resumo criptográfico: um código de 64 caracteres.

A alteração de um único byte do ISO, devido a uma transferência incompleta ou a uma adulteração, altera completamente o resumo. Por este motivo, o resumo do ficheiro transferido deve ser comparado com o resumo oficial.

```{figure} /_static/img/02-obter-ubuntu-server/05.jpg
:alt: A lista oficial de SHA256

A lista oficial de SHA256.
```

No Windows, abra o PowerShell na pasta das transferências. O comando `Get-FileHash` calcula o resumo SHA256 do ISO. A operação demora alguns segundos, porque o ficheiro é lido na íntegra.

```{figure} /_static/img/02-obter-ubuntu-server/06.jpg
:alt: Get-FileHash

Get-FileHash.
```

Obtenha a lista oficial, filtrada para as imagens de servidor. A linha da 24.04.5 começa por 97f3d7ff e termina em 0fd8, tal como o resumo calculado. A imagem está íntegra.

Se os resumos forem diferentes, a imagem não deve ser utilizada: elimine o ficheiro e transfira-o novamente.

```{figure} /_static/img/02-obter-ubuntu-server/07.jpg
:alt: As duas são iguais

Os dois resumos coincidem.
```

## Preparação do arranque

Num servidor físico, grave o ISO numa pen USB com um programa como o Rufus ou o balenaEtcher e arranque o servidor a partir da pen.

Numa máquina virtual, carregue o ISO no Proxmox, no VMware ou no Hyper-V e associe-o à unidade de CD da máquina. Configuração inicial: quatro processadores, oito gigabytes de memória e pelo menos quarenta gigabytes de disco.

**Preparação do arranque**

- Servidor físico: gravar o ISO numa pen USB de 8 GB ou mais, com o Rufus ou o balenaEtcher.
- Máquina virtual: carregar o ISO no Proxmox, VMware ou Hyper-V e associá-lo à unidade de CD da VM.
- Configuração inicial: 4 processadores, 8 GB de memória e 40 GB ou mais de disco.
