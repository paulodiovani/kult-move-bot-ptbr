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
- Read A Person (rap): jogue + Intuição
- Observar uma Situação (oas): jogue + Percepção
- Investigar (inv): jogue + Razão
- Ajudar ou Atrapalhar (aoa): jogue + Atributo
- Movimento fora do padrão (mov): jogue + Modificador
```
