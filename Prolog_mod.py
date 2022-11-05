from pyswip import Prolog
from os.path import exists

def createKb(path):
    if not exists(path):
        kb = open(path, "w")
        print("<+> Creating Knowledge Base... <+>")
        kb.write('movie("comedy",M,P,V):- M = (happy) , ((V > 89) ; (P=(cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.\n')
        kb.write('movie("action",M,P,V):- M = (happy) , ((V > 79 , V < 90) ; (P=(cecs) ; P=(necs))),!.\n')
        kb.write('movie("romance",M,P,V):- M = (happy) , ((V < 50) ; (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn))),!.\n')
        kb.write('movie("fantasy",M,P,V):- M = (happy) , ((V > 69 , V < 80) ; (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.\n')
        kb.write('movie("adventure",M,P,V):- M = (happy) , ((V > 59 , V < 70) ; (P= (ctecg) ; P=(cticg) ; P=(ctecs) ; P=(ctics ; P=(cins)))),!.\n')
        kb.write('movie("sci-fi",M,P,V):- M = (happy) , ((V > 49 , V < 60) ; (P= (cecs) ; P=(cics))),!.\n')
        kb.write('movie("horror",M,P,V):- M = (sad), ((V > 59 , V < 70) ; (P= (ctins) ; P=(cins))),!.\n')
        kb.write('movie("romance",M,P,V):- M = (sad) , ((V > 79 , V < 90) ; (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn))),!.\n')
        kb.write('movie("comedy-romance",M,P,V):- M = (sad) , ((V > 69 , V < 80) ; (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng))),!.\n')
        kb.write('movie("drama",M,P,V):- M = (sad) , ((V > 89) ; (P= (cics) ; P=(ctics) ; P=(cecs))),!.\n')
        kb.write('movie("thriller",M,P,V):- M = (sad) , ((V > 49 , V < 60) ; (P= (cteng) ; P=(cting) ; P=(ctens) ; P=(ctins))),!.\n')
        kb.write('movie("crime",M,P,V):- M = (sad) , ((V > 39 , V < 50) ; (P= (cecs) ; P=(cics))),!.\n')
        kb.write('movie("mystery",M,P,V):- M = (sad) , ((V < 40) ; (P= (ctens) ; P=(ctins))),!.\n')
        print("<+> Done <+>")
        kb.close()
    else:
        print("<+> Knowledge Base already created <+>")

def createKb_old(path):
    if not exists(path):
        kb = open(path, "w")
        print("<+> Creating Knowledge Base... <+>")
        kb.write('movie("comedy",M,P,V):- (M = (happy) , V > 89) , (P=(cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng)),!.\n')
        kb.write('movie("action",M,P,V):- (M = (happy) , (V > 79 , V < 90)) , (P= (cecs) ; P=(necs)),!.\n')
        kb.write('movie("romance",M,P,V):- (M = (happy) , V < 50) , (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn)),!.\n')
        kb.write('movie("fantasy",M,P,V):- (M = (happy) , (V > 69 , V < 80)) , (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng)),!.\n')
        kb.write('movie("adventure",M,P,V):- (M = (happy) , (V > 59 , V < 70)) , (P= (ctecg) ; P=(cticg) ; P=(ctecs) ; P=(ctics ; P=(cins))),!.\n')
        kb.write('movie("sci-fi",M,P,V):- (M = (happy) , (V > 49 , V < 60)) , (P= (cecs) ; P=(cics)),!.\n')
        kb.write('movie("horror",M,P,V):- (M = (sad), (V > 59 , V < 70)) , (P= (ctins) ; P=(cins)),!.\n')
        kb.write('movie("romance",M,P,V):- (M = (sad) , (V > 79 , V < 90)) , (P= (ctecg) ; P=(ctecs) ; P=(ctecn) ; P=(cticg) ; P=(ctics) ; P=(cticn)),!.\n')
        kb.write('movie("comedy-romance",M,P,V):- (M = (sad) , (V > 69 , V < 80)) , (P= (cecg) ; P=(ceng) ; P=(ctecg) ; P=(cteng)),!.\n')
        kb.write('movie("drama",M,P,V):- (M = (sad) , V > 89) , (P= (cics) ; P=(ctics) ; P=(cecs)),!.\n')
        kb.write('movie("thriller",M,P,V):- (M = (sad) , (V > 49 , V < 60)) , (P= (cteng) ; P=(cting) ; P=(ctens) ; P=(ctins)),!.\n')
        kb.write('movie("crime",M,P,V):- (M = (sad) , (V > 39 , V < 50)) , (P= (cecs) ; P=(cics)),!.\n')
        kb.write('movie("mystery",M,P,V):- (M = (sad) , (V < 40)) , (P= (ctens) ; P=(ctins)),!.\n')
        print("<+> Done <+>")
        kb.close()
    else:
        print("<+> Knowledge Base already created <+>")

def query_kb(kb_path, query):
    pl = Prolog()
    pl.consult(kb_path)
    return list(pl.query(query))