funA_is_destructive = True
funA_description = 'Argumentet/listen \"a\" blir endret av funksjonen og dermed betyr at den er destruktiv' 

funB_is_destructive = False
funB_description = 'Funksjonens argument "a" blir kun brukt for å sjekke opp verdier, men blir ikke selv mutert, dermed er ikke funksjonen destruktiv.'

funC_is_destructive = True
funC_description = 'Funksjonen har en liste/streng argument \"a\" som blir brukt og i tilegg mutert. Destruktiv.'

funD_is_destructive = False
funD_description = 'Funksjonens argument "a" blir brukt kun for å finne ut lengden til listen/strengen, men blir selv aldri mutert. Ikke destruktiv.'

funE_is_destructive = True
funE_description = 'Argumentet "a" blir mutert på at elementene blir "poppet" og dermed fjernet, det er destruktivt.'

funF_is_destructive = False
funF_description = 'Leser kun av elementer i argumentet "a" men ikke muterer den. Ikke destruktiv.'
