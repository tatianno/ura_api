# ura_api

Exemplo de como criar uma URA dinâmica, consumindo uma API externa com Asterisk e Python3.

## Exemplo de dialplan para chamar o SCPRIT AGI

```
....
same=>n,NoOp(Regra Custom - Inicio)
same=>n,Answer()
same=>n,NoOp(Definindo variaveis)
same=>n,Set(VENDAS_DST=C_3_INT,102,1)
same=>n,Set(URA_PRINCIPAL=C_3_INT,2000,1)
same=>n,Set(PROJ_FOLDER=/home/tatianno/ura_api)
same=>n,AGI(${PROJ_FOLDER}/ast_agi.py)
same=>n,NoOp(CPF ${CPF})
same=>n,NoOp(ANI ${ANI})
same=>n,NoOp(ECLIENTE: ${ECLIENTE})
same=>n,NoOp(INADIMPLENTE: ${INADIMPLENTE})
same=>n,NoOp(SINISTRO: ${SINISTRO})
same=>n,NoOp(Verificando se e cliente)
same=>n,ExecIf($[ "${ECLIENTE}" = "N" ]?Goto(vendas))
same=>n,NoOp(Verificando se tem sinistro ativo)
same=>n,ExecIf($[ "${SINISTRO}" = "S" ]?Goto(C_3_INT,102,1))
same=>n,NoOp(Verificando se o cliente está adimplente)
same=>n,ExecIf($[ "${INADIMPLENTE}" = "S" ]?Goto(inadimplente))
same=>n,Goto(${URA_PRINCIPAL})
;Logica de vendas
same=>n(vendas),Playback(${PROJ_FOLDER}/audios/vendas_conv)

....

same=>n,Hangup()
;Logica Sinistro
same=>n(sinistro),Playback(${PROJ_FOLDER}/audios/sinistro_conv)

...

same=>n,Hangup()
;Logica de Inadimplente
same=>n(vendas),Playback(${PROJ_FOLDER}/audios/inadimplente_conv)

...

same=>n,Hangup()
```
