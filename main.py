from Prolog_mod import *
from KNN_recommenderSystem import *
from Utility import *
import pandas as pd
from SearchGraph import *

def menu():
    print("""
> Posso consigliarti un film a partire dal tuo umore e dalla tua personalità <
> LEGGENDA CARATTERISTICHE: <
    (Calmo -> c, Caotico -> ct) (Estroverso -> e, Introverso -> i) (Coscienzioso -> c, Nevrotico -> n) (Giocoso -> g, Serio -> s)
> La scelta della personalità consiste nello scrivere la prima lettera di ogni Tripla o Coppia di valori: <
> Esempio: Calmo, Estroverso, Coscienzioso, Giocoso => cecg <
> La scelta dell'umore consiste in: 'happy' oppure 'sad' <
> Successivamente ti verrà richiesto il livello di "happiness" o "sadness" (1-100) <
> Digita X per far terminare il programma <\n""")
    p = input("<> Inserisci la tua personalità: ").lower()
    if p == "x":
        return 0, 0
    m = input("<> Inserisci il tuo umore: ").lower()
    while len(p) <= 0 and (m != "happy" or m != "sad"):
        p = input("<-> Qualcosa è andato storto <->\nRiprova inserendo la tua personalità:").lower()
        m = input("<-> Inserisci nuovamente il tuo umore: ").lower()
    if m == "happy":
        v = int(input("<> Livello felicità (1-100): "))
        while not(v > 0 and v <= 100):
            v = int(input("<-> Qualcosa è andato storto <->\nRiprova inserendo il livello di felicità (1-100): "))
    elif m == "sad":
        v = int(input("<> Livello tristezza (1-100): "))
        while not (v > 0 and v <= 100):
            v = int(input("<-> Qualcosa è andato storto <->\nRiprova inserendo il livello di tristezza (1-100): "))
    return m, p, str(v)

def menu_consegne():
    print("""
> Il nostro servizio di delivery intelligente può spedire i film consigliati direttamente a casa tua <
> Se decidi di continuare, visualizzerai il percorso più breve che il nostro robot di consegne può - <
> - percorrere per raggiungere la tua abitazione <""")

    s = input("> Premi 'c' per continuare, 'x' per non richiedere il ritiro. <\n> ").lower()
    while s != 'c' and s != 'x':
        s = input("> Comando non valido, riprova premendo 'c' per continuare, 'x' per non richiedere il ritiro. <\n> ").lower()
    if s == 'c':
        return 1
    else:
        return 0


if __name__ == "__main__":
    kb_filePath = "KnlowledgeBase/movieKb.pl"
    dataset_movie_path = "Dataset/movies.csv"
    dataset_rating_path = "Dataset/ratings.csv"
    createKb(kb_filePath)
    while True:
        m, p, v = menu()
        if m == 0:
            print("> Arrivederci <")
            break
        else:
            category = str(query_kb(kb_filePath, 'movie(Movie, '+m+', '+p+', '+v+')')[0].get('Movie'))
            print("<+> Categoria selezionata: "+category+" <+>")
            movies_df = pd.read_csv(dataset_movie_path)
            ratings_df = pd.read_csv(dataset_rating_path, usecols=['userId', 'movieId', 'rating'])
            movies_df_filtered = filter_by_category(movies_df, category)
            ratings_df_filtered = filter_ratings(ratings_df, movies_df_filtered)
            indices, distances, movies_f = recommendMovie(movies_df_filtered, ratings_df_filtered, 6)
            if len(indices) < 0:
                print(f"<-> Spiacente, per la categoria {category} non ci sono film popolari <->")
                print("<+> FINE SERVIZIO <+>")
                input("Premi un pulsante per continuare...")
                break
            #print("<+> Valutazione del modello KNN <+>")
            #showMetricsAndBM(ratings_df_filtered)
            print("<+> FILM CONSIGLIATO PER TE <+>")
            showResults(indices, distances, movies_f)
            if (menu_consegne() == 1):
                print("<+> Importo la piantina del tuo quartiere <+>")
                g = createGraph()
                #showGraph()
                dom = input("<+> Il nostro punto vendita si trova in 'A', indica il punto di ritiro che preferisci (da 'B' a 'J') <+>\n> ").upper()
                while dom < 'B' and dom > 'J':
                    dom = input("<-> Punto non valido o inesistente, riprova: <->\n> ")
                aStarAlgo('A', dom, g)
                print("<+> FINE SERVIZIO <+>")
            else:
                print("<+> FINE SERVIZIO <+>")
            input("Premi un pulsante per continuare...")