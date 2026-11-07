# Integração com diretório

Um Active Directory, ou outro servidor LDAP, de onde a plataforma **lê** equipamentos e pessoas, em vez de depender de ficheiros exportados à mão.

```{video} 353-integracoes
```

O vídeo mostra as quatro integrações: os sistemas externos, o MISP, os feeds RSS e o diretório.

## Onde fica no menu

**Menu:** Governar › Administração do sistema › Integrações › Integração com diretório

```{figure} /_static/capturas/adm-diretorio/menu.jpg
:alt: Menu lateral: Governar › Administração do sistema › Integrações › Integração com diretório

O caminho no menu lateral: Governar › Administração do sistema › Integrações › Integração com diretório.
```

1. No menu lateral, abra **Governar**.
2. Dentro dele, abra **Administração do sistema**.
3. Dentro dele, abra **Integrações**.
4. Clique em **Integração com diretório**: abre o ecrã desta página.


## As ligações

```{figure} /_static/capturas/adm-diretorio/ligacoes-1.jpg
:alt: As ligações declaradas e o botão para uma nova

As ligações declaradas e o botão para uma nova.
```

1. **Uma ligação declarada**
2. **Nova ligação**


Cada ligação declarada aparece como um botão. Clique numa para a ver ou alterar, ou em **Nova ligação**.

## Uma ligação

```{figure} /_static/capturas/adm-diretorio/ficha-2.jpg
:alt: A ficha de uma ligação

A ficha de uma ligação.
```


O que cada número pede:

1. **O método.** `LDAPS` (porta 636) ou `LDAP com StartTLS` (porta 389). Não há opção sem cifra, e é deliberado: sem ela, a palavra-passe da conta de serviço viajaria legível na rede.
2. **O servidor e a porta.**
3. **A base de procura** (*base DN*), por exemplo `DC=exemplo,DC=pt`.
4. **A sub-árvore dos computadores**, opcional.
5. **A sub-árvore das pessoas**, opcional. Quanto mais estreitas as sub-árvores, menos dados se leem, que é o que a lei pede.
6. **A conta de serviço.** Dê-lhe **apenas permissões de consulta**: a plataforma nunca escreve no diretório. A palavra-passe, uma vez guardada, deixa de ser mostrada.

Se o servidor usa uma autoridade certificadora própria, cole o certificado dela em PEM e **deixe a verificação ligada**. Desligá-la é possível e fica registado na trilha: a ligação continua cifrada, mas deixa de provar com quem está a falar.

```{figure} /_static/capturas/adm-diretorio/testar-1.jpg
:alt: O botão Testar ligação, no fim da ficha

O botão Testar ligação, no fim da ficha.
```

1. **Testar ligação**


**Testar ligação** grava primeiro e depois experimenta, verificação a verificação: o nome resolve, a porta abre, o certificado valida, as credenciais servem, a base lê-se, há objetos e trazem os atributos essenciais. Cada linha falha por sua conta, porque cada uma tem uma cura diferente.

```{note}
**No ambiente de testes, a ligação recusa-se a funcionar, e é de propósito.** Não há um segundo servidor de domínio para onde apontar: a instância de teste leria o pessoal verdadeiro com credenciais verdadeiras.
```

## O que se lê

Dos computadores: nome, sistema operativo, se a conta está ativa, datas e localização. Das pessoas: nome, conta, correio eletrónico, cargo e unidade. **Não** se lê fotografia, telefone pessoal, morada, número mecanográfico, chefia nem grupos.

## Resumo

- Só leitura, sempre cifrada.
- A conta de serviço precisa apenas de permissões de consulta.
- O teste diz em que passo a ligação falha.
