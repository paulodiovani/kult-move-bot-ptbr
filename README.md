# 💀 KULT Bot 🤖

Bot para Discord escrito em Python para _Movimentos_ no PbtA **KULT: Divindade Perdida**.

Versão em Português do Brasil. 🇧🇷

Baseado no [rpgmik/KultMoveBot](https://github.com/rpgmik/KultMoveBot).

## Instalação

Instale em um servidor do Discord (você vai precisar de privilégios de admin) pelo link:

https://discordapp.com/api/oauth2/authorize?client_id=812513909198159904&permissions=0&scope=bot

### ⚠ Horas ativas ⏱

Devido à limitação de tempo para aplicativos gratuítos no Heroku, onde o Bot está hospedado,
atualmente ele fica ativo apenas **das 19:00 às 01:00**, todos os dias.

## Instruções de uso

Uma vez instalado, digite

`
!move ?
`

O Discord vai responder com a mensagem de uso abaixo.


```
!movimento ? - exibe esta mensagem
!movimento help - exibe esta mensagem
!movimento ajuda - exibe esta mensagem
!movimento info - exibe informações do Bot
!movimento xxx - realiza um movimento xxx
!movimento xxx -1 - realiza um movimento xxx com um modificador negativo de -1
!movimento xxx +2 - realiza um movimento xxx com um modificador positivo de +2
```

### Movimentos

```
Movimentos:
- Use o nome completo do movimento (em minúsculas, sem espaços) ao jogar.
  Por exemplo, para jogar 'Observar uma Situação' com um bônus de +2, use:
  !movimento observarumasituacao +2
- Atalhos estão disponíveis para os movimentos mais usados (veja abaixo).
  Por exemplo, para jogar 'Evitar Ferimento' com um bônus de +1, use:
  !movimento ef +1
```

### Atalhos de movimentos

```
- Evitar Dano (ed): jogue + Reflexos
- Suportar Ferimento (sf): jogue + Fortitude - Dano (+ Armadura)
- Manter o Sangue-frio (msf): jogue + Força de Vontade
- Agir Sob Pressão (asp): jogue + Sangue-frio
- Participar do Combate (pdc): jogue + Violência
- Influenciar um PdM (ipm): jogue + Carisma
- Influenciar um Pj (ipj): jogue + Carisma
- Ver Através da Ilusão (vai): jogue + Alma
- Ler uma Pessoa (lup): jogue + Intuição
- Observar uma Situação (oas): jogue + Percepção
- Investigar (inv): jogue + Razão
- Ajudar ou Atrapalhar (aoa): jogue + Atributo
- Movimento fora do padrão (mov): jogue + Modificador
```

## Servidores Brasileiros do KULT no Discord

- [KULT Brasil](https://discord.gg/H4wWwxmaHZ)

## Como colaborar

- [Abra pull requests][creating-a-pr] com traduções diretamente em `all_moves.yml`
- Reporte bugs ou problemas de tradução como [Issues][issues]
- Jogue KULT e divulgue o Bot

[creating-a-pr]: https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[issues]: https://github.com/paulodiovani/kult-move-bot-ptbr/issues

### Desenvolvimento Local

Você vai precisar de:

- python 3
- pipenv

Instruções:

1. Crie um app no Discord via https://discord.com/developers/applications
2. Clique em **Bot** no painel esquerdo e copie a **TOKEN** do seu Bot
3. Crie um arquivo `.env` (use o modelo `.env.sample`) e cole sua **TOKEN**
4. Instale as dependencias e inicie o bot
    ```bash
    pipenv install
    pipenv run bot
    ```
