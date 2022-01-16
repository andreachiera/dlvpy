import json

from dlvpy.program.program import Program
from dlvpy.program.options import Options

dlv_path = "C:\\dlvpy\\bin\\windows\\dlv.mingw-odbc.exe"

def readJson(folder):
    file = open(folder, 'r', encoding="utf-8")
    data = json.load(file)
    file.close()
    return data


def fileOffertaFormativa():
    return readJson('./offerta_formativa/offerta_formativa_2021.json')


def configOffertaFormativa():
    return readJson('./offerta_formativa/config.json')


def fileDictDocenti():
    return readJson('./docenti/dict/docenti.json')


def noConfig():
    return None


def config1DictDocenti():
    return readJson('./docenti/dict/config1.json')


def config2DictDocenti():
    return readJson('./docenti/dict/config2.json')


def config3DictDocenti():
    return readJson('./docenti/dict/config3.json')


def fileListDocenti():
    return readJson('./docenti/list/docenti.json')


def config1ListDocenti():
    return readJson('./docenti/list/config.json')


def fileDonut():
    return readJson('./donut/donuts.json')


def configDonut():
    return readJson('./donut/config.json')


def exampleOffertaFormativa():
    at_least_700_students = """
        atLeast700Students(K, S) :- unical(K, _, _, _, _, _, _, _, _, S, _), S > 700.
        atLeast2(K, S):- atLeast700Students(K, S).
        % schema(atLeast700Students(key(autoincrement), "codice", "studenti"))
        % schema(atLeast2(key(["codice", "studenti"], "-"), "codice", "studenti"))
    """
    # -atLeast700Students(K, S) :- atLeast700StudentsFirst(K, S), S < 860.
    # atLeast700Students(K, S) :- atLeast700StudentsFirst(K, S), S >= 860.

    program = Program()
    idx = program.add_input((fileOffertaFormativa(), configOffertaFormativa()))
    program.add_logic_rules(at_least_700_students)
    options: Options = Options(dlv_path)
    options.add_option("-nofacts")
    program.execute(options)
    print(program.get_last_result())


def exampleDictDocenti():
    #insegnamenti_nel_primo_semestre_primo_anno = "firstSemesterInsegnamenti(Kdoc, KIns, Y, S) :- docenti__insegnamenti(Kdoc, KIns, _, _, _, Y, S, _), Y = 1, S = 1."
    docenti_con_almeno_2_insegnamenti = "atLeastTwoInsegnamenti(D1) :- docenti__insegnamenti(D1, I1, _, _, _, _, _, _, _), docenti__insegnamenti(D2, I2, _, _, _, _, _, _, _), D1 = D2, I1 != I2."

    program = Program()
    idx = program.add_input((fileDictDocenti(), config1DictDocenti()))
    # idx = print(program.readFactsOf(program.add_input((fileDictDocenti(), config2DictDocenti()))))
    # idx = print(program.readFactsOf(program.add_input((fileDictDocenti(), config3DictDocenti()))))
    # idx = print(program.readFactsOf(program.add_input(fileDictDocenti())))
    # idx = program.add_input(fileDictDocenti())
    print(program.readFactsOf(idx))
    #program.add_logic_rules("%schema(schema(key, \"nome\", \"cognome\", \"nascita\", \"collaboratori\"))")
    program.add_logic_rules(docenti_con_almeno_2_insegnamenti)
    options: Options = Options(dlv_path)
    program.execute(options)
    print(program.get_last_result())

def exampleListDocenti():
    program = Program()
    idx = program.add_input((fileListDocenti(), config1ListDocenti()))
    print(program.readFactsOf(idx))
    program.add_logic_rules("""
        insegnamenti(A,B,C,D,E,F,G) :- docenti__insegnamenti(A,B,C,D,E,F,G).
        esami(A,B,C,D,E,F,G) :- docenti__insegnamenti__esami(A,B,C,D,E,F,G).
        % schema(docenti(key,"nome","cognome"))
        % schema(insegnamenti(ancestor_key(docenti),key,"nome","materiale","anno","semestre","cfu"))
        % schema(esami(ancestor_key(docenti),ancestor_key(insegnamenti),key,"data","tipo","ore","domande"))
    """)
    options: Options = Options(dlv_path)
    options.add_option("-pfilter=docenti,insegnamenti,esami")
    program.execute(options)
    results = program.get_last_result()
    print(results)


def exampleDonut():
    program = Program()
    program.add_input((fileDonut(), configDonut()))
    idx = program.add_logic_rules("""donutKey(DKey) :- donuts__topping(DKey, _, \"Sugar\").
        % schema(donutKey(key))
        % schema(donuts(key,"type","name","ppu"))
        %schema(donuts__batters(ancestor_key(donuts),key,"chiave","type"))
        %schema(donuts__topping(ancestor_key(donuts),key,"type"))
        %schema(donuts__fillings(ancestor_key(donuts),key,"name","addcost"))
    """)
    print(program.readSchemaOf(idx))
    print(program.readFactsOf(idx))
    idResult, error = program.execute(dlv_path)
    print(program.get_last_result())

def exampleQuery1():
    program = Program()
    program.add_logic_rules("""
        a v b.
        a ?
    """)
    # not a ?
    # not -a ?
    option = Options(dlv_path)
    option.add_options(["-cautious", "--witness"])
    #option.add_options(["-brave", "--witness"])
    program.execute(option)
    print(program.get_last_result())

def exampleQuery2():
    program = Program()
    program.add_logic_rules("""
        borders(technocratia,absurdistan).
        borders(technocratia,schilda).
        borders(technocratia,shangri_la).
        borders(schilda,absurdistan).
        borders(schilda,shangri_la).
        country(C) :- borders(C,_).
        country(C) :- borders(_,C).
        colored(C,red) v colored(C,blue) v colored(C,yellow) :- country(C).
        colored(shangri_la,blue).
        :- colored(C1,Col), colored(C2,Col), borders(C1,C2).
        colored(C,Col)?
    """)
    options = Options(dlv_path)
    options.add_option("-silent")
    options.add_option("-brave")
    program.execute(options)
    print(program.get_last_result())

def exampleModelWithCost():
    program = Program()
    program.add_logic_rules("""
        root(a).
        node(a). node(b). node(c). node(d). node(e).
        edge(a,b,4). edge(a,c,3). edge(c,b,2). edge(c,d,3). edge(b,e,4). edge(d,e,5).

        in_tree(X,Y,C) v out_tree(X,Y) :- edge(X,Y,C), reached(X).
        :- root(X), in_tree(_,X,C).
        :- in_tree(X,Y,C), in_tree(Z,Y,C), X != Z.

        reached(X):- root(X).
        reached(Y):- reached(X), in_tree(X,Y,C).
        :- node(X), not reached(X).

        :~ in_tree(X,Y,C). [C:1]
        
    """)
    options = Options(dlv_path)
    options.add_options(["-silent", "-nofacts"])
    program.execute(options)
    print(program.get_last_result())

    program.remove_all_logic_rules()
    program.add_logic_rules("""
        employee("a"). employee("b"). employee("c"). employee("d"). employee("e").
        know("a","b"). know("b","c"). know("c","d"). know("d","e"). know("a", "c").

        same_skill("a","b").
        married("c","d").

        member(X,p1) v member(X,p2) :- employee(X).
        :~ member(X,P), member(Y,P), X != Y, not know(X,Y). [1:1]
        :~ member(X,P), member(Y,P), X != Y, married(X,Y). [1:2]
        :~ member(X,P), member(Y,P), X != Y, same_skill(X,Y). [1:2]
        
        %     schema( employee ( key ) )
        % schema(know(key(["p1", "p2"], "_"),"p1","p2"))
    """)
    program.execute(dlv_path)
    print(program.get_last_result())

def exampleNoAnswerSets():
    program = Program()
    program.add_logic_rules("")
    program.execute(dlv_path)
    print(program.get_last_result())

def example3Col():
    program = Program()
    program.add_logic_rules("""
        node(X) :- arc(X,_).
        node(Y) :- arc(_,Y).
        % schema(node(key(autoincrement), "name"))
        color(X,red) v color(X,green) v color(X,blue) :- node(X).
        badGraph :- arc(X,Y), color(X,Z), color(Y,Z).
        p :- badGraph, not p.
        not badGraph?
        % schema(color(key, "color"))
    """)
    program.add_logic_rules("""
        arc(a,b).
        arc(a,c).
        arc(b,c).
    """)
    options: Options = Options(dlv_path)
    options.add_option("-pfilter=color,node")
    program.execute(options)
    print(program.get_last_result())

def exampleRandom():
    program = Program()
    program.add_logic_rules("""
        p([a,[1,2]]).
        p(X) :- p([X | T]).
        % schema(p(key(["lista"]), "lista")))
    """)
    program.execute(dlv_path)
    print(program.get_last_result())

def exampleFibonacci():
    program = Program()
    program.add_logic_rules("""
        fibonacci(0,0).
        fibonacci(1,1).
        fibonacci(2,1).
        fibonacci(N,F) :- #succ(N2,N1), #succ(N1,N), fibonacci(N1,F1), fibonacci(N2,F2), +(F1,F2,F).
        %schema(fibonacci(key(autoincrement), "n", "value"))
    """)
    options: Options = Options(dlv_path)
    options.add_options(["-N=999"])
    program.execute(options)
    print(program.get_last_result())

exampleNoAnswerSets()
example3Col()
exampleFibonacci()
exampleOffertaFormativa()
exampleQuery1()
exampleQuery2()
exampleModelWithCost()
exampleDictDocenti()
exampleListDocenti()
exampleDonut()
exampleRandom()