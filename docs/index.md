# SecVision

**Gestão da cibersegurança e da conformidade, do inventário à certificação.**

O SecVision é uma plataforma web que reúne os requisitos da lei portuguesa de cibersegurança para
uma organização: inventário dos sistemas e da informação, risco, medidas e controlos, evidências,
auditorias e dossier de certificação. A plataforma lê o Active Directory, o DNS, o DHCP e o Wazuh
para identificar os sistemas existentes e os sistemas protegidos, e associa cada medida à norma e
ao artigo que a exige.

Este manual acompanha a **formação SecVision**, uma série de vídeos destinada a profissionais **sem
formação em cibersegurança nem em *compliance***. Cada página corresponde a um vídeo, apresentado
no topo, e descreve o mesmo conteúdo passo a passo, com o caminho dos menus e capturas de ecrã
anotadas.

```{figure} /_static/capturas/registo-risco/menu.jpg
:alt: O SecVision aberto no Registo de risco, com o caminho do menu lateral numerado

O SecVision no ecrã do Registo de risco. Os números indicam o caminho no menu lateral: 1 Identificar,
2 Risco, 3 Registo de risco.
```

## Por onde começar

- **Instalação da plataforma:** comece por {doc}`installation/index`.
- **Primeiro contacto com estes temas:** leia {doc}`fundamentals/index` e, em seguida, {doc}`law/index`.
- **Utilização da plataforma:** siga {doc}`platform/index` pela ordem indicada, que corresponde à ordem
  dos menus e à ordem de execução do trabalho.
- **Percurso completo, do início à certificação:** consulte {doc}`journey/first-year`.
- **Integração com o Wazuh:** consulte {doc}`wazuh/index`.

## A organização dos exemplos

Os exemplos utilizam sempre a mesma organização fictícia, a do ambiente de testes: o **Instituto
Politécnico de Vila Nova**, pessoa coletiva de direito público com 1240 trabalhadores, **entidade
pública relevante do Grupo A**. Todos os nomes, pessoas e dados são fictícios.

```{note}
**A lei citada.** As referências legais são ao Decreto-Lei n.º 125/2025 (Regime Jurídico da
Cibersegurança, que transpõe a Diretiva NIS 2) e ao Regulamento n.º 756/2026. Este manual tem
caráter explicativo e orientador e não substitui o texto legal nem o parecer de um jurista.
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
