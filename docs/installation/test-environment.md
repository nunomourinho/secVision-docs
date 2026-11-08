# O ambiente de testes

Criação, ao lado da produção, de uma segunda instalação com dados fictícios, para formação e experimentação sem afetar dados reais, e acesso a essa instalação.

```{video} 07-ambiente-de-testes
```

A plataforma está instalada e protegida, mas ainda não tem dados. Antes de introduzir dados reais, recomenda-se dispor de um ambiente para experimentação: o ambiente de testes.

## Descrição

O ambiente de testes é uma segunda instalação na mesma máquina, independente da produção. A produção mantém-se na porta 8080; os testes utilizam a porta 8090.

Os dois ambientes são totalmente separados: base de dados, serviço e pastas próprios. Os dados são fictícios: uma organização inventada, com sistemas, riscos e cinquenta mil pessoas. As operações que afetariam sistemas externos, como o servidor Wazuh, não estão disponíveis neste ambiente.

**Produção e testes**

- Produção: porta 8080, base de dados real, dados da organização.
- Testes: porta 8090, base de dados, serviço e pastas próprios, sem qualquer partilha.
- Os dados de teste são fictícios: uma organização inventada, com sistemas, riscos e 50 000 pessoas.
- As operações sobre sistemas externos, como o Wazuh, não estão disponíveis no ambiente de testes.

## Criar o ambiente

Na pasta da instalação, execute o comando seguinte. O comando requer `sudo` porque cria uma base de dados e configura o servidor web.

```bash
sudo bash bin/ambiente-teste.sh criar
```

```{figure} /_static/img/07-ambiente-de-testes/01.jpg
:alt: Um só comando

O comando de criação.
```

O script cria uma nova base de dados, com um utilizador com acesso exclusivo a essa base, e gera o ficheiro de configuração do ambiente de testes, com segredos próprios, distintos dos da produção. Em seguida, aplica as migrações, que criam as tabelas.

São aplicadas mais de cem migrações, pela mesma ordem de uma atualização. Por este motivo, o ambiente de testes permite também ensaiar uma atualização antes de a aplicar em produção.

```{figure} /_static/img/07-ambiente-de-testes/02.jpg
:alt: Uma base de dados só para os testes

Base de dados exclusiva do ambiente de testes.
```

## Dados de teste

O script cria a conta admin, como na produção, prepara pastas de ficheiros próprias, separadas das da produção, e inicia a geração dos dados.

```{figure} /_static/img/07-ambiente-de-testes/03.jpg
:alt: A conta inicial, as pastas e os dados

A conta inicial, as pastas e os dados.
```

Para permitir o ensaio da ligação ao Active Directory, o script cria um servidor Samba de ensaio num contentor, com cinquenta mil pessoas. Esta é a etapa mais demorada. Em seguida, o gerador preenche a organização fictícia: sistemas, ativos, riscos, documentos e auditorias.

```{figure} /_static/img/07-ambiente-de-testes/04.jpg
:alt: Um Active Directory de ensaio com 50 000 pessoas

Active Directory de ensaio com 50 000 pessoas.
```

## Credenciais de acesso

No final, o script indica as credenciais de acesso. A conta admin, com a palavra-passe inicial, segue os mesmos dois passos descritos na página anterior. Os utilizadores gerados estão prontos a utilizar: todos têm a palavra-passe Teste123! e o mesmo segredo de segundo fator.

Basta adicionar esse segredo uma vez à aplicação autenticadora para aceder com qualquer utilizador. Esta configuração só é aceitável porque os utilizadores são fictícios e o ambiente é de testes.

```{figure} /_static/img/07-ambiente-de-testes/05.jpg
:alt: Como entrar

Credenciais de acesso.
```

Por fim, o script inicia o serviço do ambiente de testes e configura o servidor web na porta 8090. A mensagem «ambiente de teste pronto» indica que a criação foi concluída.

```{figure} /_static/img/07-ambiente-de-testes/06.jpg
:alt: Arrancar o serviço e o servidor web

Arranque do serviço e do servidor web.
```

Para confirmar o estado, utilize a opção `estado` do mesmo script. São apresentados a base de dados, o número de registos de cada tabela e o estado do serviço e do servidor web.

Se alguma página do ambiente de testes não abrir, este comando é o primeiro passo do diagnóstico.

```{figure} /_static/img/07-ambiente-de-testes/07.jpg
:alt: Confirmar o que está de pé

Confirmação dos serviços em funcionamento.
```

## Acesso ao ambiente de testes

No browser, abra o mesmo endereço com a porta 8090. A faixa amarela no topo, **AMBIENTE DE TESTES**, e a moldura amarela em redor da página são apresentadas em todas as páginas, incluindo a de entrada, para distinguir este ambiente da produção.

Inicie sessão com um dos utilizadores gerados (por exemplo, um operador) e a palavra-passe partilhada.

```{figure} /_static/img/07-ambiente-de-testes/08.jpg
:alt: A porta 8090 e a faixa amarela

A porta 8090 e a faixa amarela.
```

É solicitado o código de segundo fator. Introduza o código apresentado pela aplicação para o segredo partilhado.

```{figure} /_static/img/07-ambiente-de-testes/09.jpg
:alt: O código partilhado

O código partilhado.
```

## Exploração

Ao contrário da produção, o painel já apresenta dados: sistemas por nível, cobertura e sistemas sem monitorização, tal como numa plataforma em utilização.

```{figure} /_static/img/07-ambiente-de-testes/10.jpg
:alt: Um painel cheio de dados

Painel com dados.
```

O catálogo de segurança apresenta os sistemas da organização fictícia. É possível editar, apagar e importar ficheiros sem qualquer efeito na produção.

```{figure} /_static/img/07-ambiente-de-testes/11.jpg
:alt: O catálogo de segurança

O catálogo de segurança.
```

A gestão de risco apresenta riscos já avaliados. O ambiente de testes é adequado para aprender cada módulo antes de o utilizar com dados reais.

```{figure} /_static/img/07-ambiente-de-testes/12.jpg
:alt: A gestão de risco

A gestão de risco.
```

## Resumo

Três comandos de referência: `estado`, para verificar os serviços em funcionamento; `recriar`, para eliminar o ambiente e criá-lo novamente com dados novos (útil após várias experiências); e `apagar`, para remover o ambiente de testes por completo. Nenhum dos três afeta a produção.

**Comandos de referência**

- sudo bash bin/ambiente-teste.sh estado — verifica os serviços em funcionamento
- sudo bash bin/ambiente-teste.sh recriar — elimina e cria novamente o ambiente, com dados novos
- sudo bash bin/ambiente-teste.sh apagar — remove o ambiente por completo; a produção não é afetada
