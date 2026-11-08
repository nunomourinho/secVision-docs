# Integração com diretório

Ligação a um Active Directory, ou a outro servidor LDAP, para a leitura de equipamentos e pessoas diretamente do diretório, sem recurso a ficheiros exportados manualmente.

```{video} 353-integracoes
```

O vídeo apresenta as quatro integrações: sistemas externos, MISP, feeds RSS e diretório.

## Acesso

**Governar** > **Administração do sistema** > **Integrações** > **Integração com diretório**

```{figure} /_static/capturas/adm-diretorio/menu.jpg
:alt: Menu lateral: Governar > Administração do sistema > Integrações > Integração com diretório

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Ligações

```{figure} /_static/capturas/adm-diretorio/ligacoes-1.jpg
:alt: As ligações configuradas e o botão Nova ligação

As ligações configuradas e o botão **Nova ligação**.
```

No ecrã, encontra os seguintes elementos:

1. **Ligação configurada:** Cada ligação existente é apresentada como um botão.
2. Botão **Nova ligação:** Permite configurar uma nova ligação.

**Como consultar ou alterar:** Clique na ligação pretendida para abrir a respetiva ficha.

## Configuração da ligação

```{figure} /_static/capturas/adm-diretorio/ficha-2.jpg
:alt: A ficha de uma ligação

A ficha de uma ligação.
```

No ecrã, encontra os seguintes elementos:

1. **Método:** **LDAPS** (porta 636) ou **LDAP com StartTLS** (porta 389). Ligações sem encriptação não são suportadas para garantir que as credenciais não circulam em texto limpo.
2. **Servidor e porta:** Endereço e porta do servidor de diretório.
3. **Base de procura** (*base DN*): Por exemplo, `DC=exemplo,DC=pt`.
4. **Sub-árvore dos computadores** (opcional).
5. **Sub-árvore das pessoas** (opcional). Sub-árvores mais restritas reduzem os dados pessoais lidos, em cumprimento do princípio da minimização.
6. **Conta de serviço:** Deve ter apenas permissões de leitura; a plataforma não escreve no diretório. Depois de guardada, a palavra-passe deixa de ser apresentada.

**Certificado:** Se o servidor utilizar uma autoridade certificadora própria, cole o certificado em formato PEM e mantenha a verificação ativa. A desativação da verificação fica registada na trilha de auditoria; a ligação continua encriptada, mas a identidade do servidor deixa de ser validada.

```{figure} /_static/capturas/adm-diretorio/testar-1.jpg
:alt: O botão Testar ligação, no fim da ficha

O botão **Testar ligação**, no fim da ficha.
```

1. Botão **Testar ligação:** Guarda a configuração e verifica a ligação.

**Testar a ligação:** O botão **Testar ligação** guarda a configuração e executa, por ordem, as seguintes verificações: resolução do nome, abertura da porta, validação do certificado, autenticação, leitura da base de procura e presença dos atributos obrigatórios. Cada verificação tem um resultado próprio, o que permite identificar o passo em que a ligação falha.

```{note}
O teste de ligação não está disponível no ambiente de testes. Esta restrição impede que uma instância de ensaio aceda a dados reais de colaboradores com credenciais de produção.
```

## Dados lidos

- **Computadores:** nome, sistema operativo, estado da conta (ativa ou inativa), datas e localização.
- **Pessoas:** nome, conta, correio eletrónico, cargo e unidade.

Não são lidos a fotografia, o telefone pessoal, a morada, o número mecanográfico, a chefia nem os grupos.

## Resumo

- A ligação é apenas de leitura e sempre encriptada.
- A conta de serviço necessita apenas de permissões de leitura.
- O teste de ligação indica o passo em que a ligação falha.
