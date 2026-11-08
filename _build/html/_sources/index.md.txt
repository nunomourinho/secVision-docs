# SecVision

**Gestão da cibersegurança e da conformidade, do inventário à certificação.**

O SecVision é uma plataforma web que reúne num só sítio o que a lei portuguesa de cibersegurança
pede a uma organização: o inventário dos sistemas e da informação, o risco, as medidas e os
controlos, as provas, as auditorias e o dossier para a certificação. Lê o Active Directory, o DNS,
o DHCP e o Wazuh para saber o que existe e o que está protegido, e liga cada medida à norma e ao
artigo que a exige.

Este manual acompanha a **formação SecVision**, uma série de vídeos para quem **não tem formação em
cibersegurança nem em *compliance***. Cada página corresponde a um vídeo, que aparece no topo, e
descreve o mesmo conteúdo passo a passo, com o caminho dos menus e capturas de ecrã anotadas.

```{figure} /_static/capturas/registo-risco/menu.jpg
:alt: O SecVision aberto no Registo de risco, com o caminho do menu lateral numerado

O SecVision no ecrã do Registo de risco. Os números marcam o caminho no menu lateral: 1 Identificar,
2 Risco, 3 Registo de risco.
```

## Por onde começar

- **Vai instalar a plataforma?** Comece por {doc}`installation/index`.
- **É novo nestes temas?** Leia o {doc}`fundamentals/index` e depois {doc}`law/index`.
- **Vai usar a plataforma?** Siga o {doc}`platform/index`, pela ordem: é a ordem dos menus e a ordem em
  que o trabalho se faz.
- **Quer o caminho completo, do zero à certificação?** Veja {doc}`journey/first-year`.
- **Usa o Wazuh?** Veja o {doc}`wazuh/index`.

## A organização dos exemplos

Os exemplos usam sempre a mesma organização fictícia, a do ambiente de testes: o **Instituto
Politécnico de Vila Nova**, pessoa coletiva de direito público com 1240 trabalhadores, **entidade
pública relevante do Grupo A**. Todos os nomes, pessoas e dados são inventados.

```{note}
**A lei citada.** As referências legais são ao Decreto-Lei n.º 125/2025 (Regime Jurídico da
Cibersegurança, que transpõe a Diretiva NIS 2) e ao Regulamento n.º 756/2026. Este manual explica e
orienta; não substitui o texto legal nem o parecer de um jurista.
```

```{toctree}
:caption: Instalação
:maxdepth: 2

installation/index
```

```{toctree}
:caption: Formação
:maxdepth: 2

fundamentals/index
law/index
platform/index
journey/index
wazuh/index
```

```{toctree}
:caption: Projeto
:maxdepth: 1

project/limitations
```
