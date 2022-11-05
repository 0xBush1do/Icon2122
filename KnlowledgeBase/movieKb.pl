movie("comedy",M,P,V):- M = (happy) , ((V > 89) ; (P=(cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.
movie("action",M,P,V):- M = (happy) , ((V > 79 , V < 90) ; (P=(cecs) ; P=(necs))),!.
movie("romance",M,P,V):- M = (happy) , ((V < 50) ; (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn))),!.
movie("fantasy",M,P,V):- M = (happy) , ((V > 69 , V < 80) ; (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.
movie("adventure",M,P,V):- M = (happy) , ((V > 59 , V < 70) ; (P= (ctecg) ; P=(cticg) ; P=(ctecs) ; P=(ctics ; P=(cins)))),!.
movie("sci-fi",M,P,V):- M = (happy) , ((V > 49 , V < 60) ; (P= (cecs) ; P=(cics))),!.
movie("horror",M,P,V):- M = (sad), ((V > 59 , V < 70) ; (P= (ctins) ; P=(cins))),!.
movie("romance",M,P,V):- M = (sad) , ((V > 79 , V < 90) ; (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn))),!.
movie("comedy-romance",M,P,V):- M = (sad) , ((V > 69 , V < 80) ; (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.
movie("drama",M,P,V):- M = (sad) , ((V > 89) ; (P= (cics) ; P=(ctics) ; P=(cecs))),!.
movie("thriller",M,P,V):- M = (sad) , ((V > 49 , V < 60) ; (P= (cteng) ; P=(cting) ; P=(ctens) ; P=(ctins))),!.
movie("crime",M,P,V):- M = (sad) , ((V > 39 , V < 50) ; (P= (cecs) ; P=(cics))),!.
movie("mystery",M,P,V):- M = (sad) , ((V < 40) ; (P= (ctens) ; P=(ctins))),!.
