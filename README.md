# 💀 KULT Bot 🤖

Bot para Discord escrito em Python para _Movimentos_ no PbtA **KULT: Divindade Perdida**.

Versão em Português do Brasil. 🇧🇷

Baseado no [rpgmik/KultMoveBot](https://github.com/rpgmik/KultMoveBot.

- Veja abaixo instruções de uso

## Traduçao para Português do Brasil (em progresso)

- [ ] Movimentos Básicos
- [ ] Vantagens
- [ ] Desvantagens
- [x] Instruções
  + [ ] Instruções de como rodar localmente
- [ ] Ajuda e exemplos

### Como colaborar

- [Abra pull requests][creating-a-pr] com traduções diretamente em `all_moves.yml`
- Reporte bugs ou problemas de tradução como [Issues][issues]
- Jogue KULT e divulgue o Bot

[creating-a-pr]: https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[issues]: https://github.com/paulodiovani/kult-move-bot-ptbr/issues

### Agradecimentos

- Admins do Discord de KULT BR
- Buró Editora, que trouxe este excelente RPG para o Brasil

## Servidores Brasileiros do KULT no Discord

- KULT Brasil
 
## Instalação

Instale em um servidor do Discord (você vai precisar de privilégios de admin) pelo link:

https://discordapp.com/api/oauth2/authorize?client_id=812513909198159904&permissions=0&scope=bot

## Instruções de uso

Uma vez instalado, digite

`
!move ?
`

O Discord vai responder com a mensagem de uso abaixo.


```
!move ? - displays this message
!move help - displays this message
!move info - displays bot code info
!move xxx - roll to perform Move xxx
!move xxx -1 - roll to perform Move xxx with negative modifier -1
!move xxx +2 - roll to perform Move xxx with positive modifier +2
```

### Movimentos

```
- Use the full move name (lower-case, no spaces) when rolling.
  For example, to roll for 'Artistic Talent' with a +2 bonus use:
  !move artistictalent +2
- Shortcuts are available for commonly used moves (see below).
  For example, to roll for 'Avoid Harm' with a +1 bonus use:
  !move ah +1
```

### Atalhos de movimentos

```
- Avoid Harm (ah): roll + Reflexes
- Endure Injury (ei): roll + Fortitude - Harm (+ Armour)
- Keep It Together (kit): roll + Willpower
- Act Under Pressure (aup): roll + Coolness
- Engage In Combat (eic): roll + Violence
- Influence Other - NPC (ion): roll + Charisma
- Influence Other - PC (iop): roll + Charisma
- See Through the Illusion (sti): roll + Soul
- Read A Person (rap): roll + Intuition
- Observe A Situation (oas): roll + Perception
- Investigate (inv): roll + Reason
- Help Or Hinder (hoh): roll + Attribute
- Non-standard move (non): roll + Modifier
```

### Anomalies (full move name):

```
- Influence Other - NPC: !move influenceothernpc
- Influence Other - PC: !move influenceotherpc
```
