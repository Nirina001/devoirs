'''(x*y)+(-x*z)+-(y*z)'''
def canonique(fonc):
    def binstr(n, length):
        binary = bin(n)[2:]
        return '0' * (length - len(binary)) + binary

    def dec_var(fonc):
        variables = set()
        for char in fonc:
            if char.isalpha():
                variables.add(char)
        return sorted(variables)

    def evaluation(fonc, assignment):
        for variable, value in assignment.items():
            fonc = fonc.replace(variable, str(value))
        return eval(fonc)

    def mintermes(fonc):
        minterms = []
        variables = dec_var(fonc)
        for i in range(2 ** len(variables)):
            binary_str = binstr(i, len(variables))
            assignment = {var: int(bit) for var, bit in zip(variables, binary_str)}
            if evaluation(fonc, assignment):
                minterms.append(assignment)
        return minterms

    def premform(fonc):
        minterms = mintermes(fonc)
        formcan = []
        for minterm in minterms:
            term = []
            for variable, value in minterm.items():
                if value == 0:
                    term.append(f"-{variable}")
                else:
                    term.append(variable)
            formcan.append(" * ".join(term))
        return " ) + ( ".join(formcan)

    def maxtermes(fonc):
        variables = dec_var(fonc)
        maxterms = []
        for i in range(2 ** len(variables)):
            binary_str = binstr(i, len(variables))
            assignment = {var: int(bit) for var, bit in zip(variables, binary_str)}
            if not evaluation(fonc, assignment):
                maxterms.append(assignment)
        return maxterms

    def secform(fonc):
        maxterms = maxtermes(fonc)
        can = []
        for max in maxterms:
            term = []
            for variable, value in max.items():
                if value == 0:
                    term.append(f"{variable}")
                else:
                    term.append(f"-{variable}")
            can.append(" + ".join(term))
        return " )*( ".join(can)

    # Exemple d'utilisation
    premiere = premform(fonc)
    print("Première forme canonique de la fonction :", "(", premiere, ")")
    sec = secform(fonc)
    print("Deuxième forme canonique de la fonction :","(", sec,")")


if __name__ == '__main__':
    print("Nom: ANDRIAHASIMANANA \n Prénoms: Onjanirina Heriniaina \n N° inscription: UA03279FS2024")
    print('la forme du fonction doit-être comme (x*y)+(-x*z)+-(y*z)')
    print("connecteurs: * = et, + = ou, - = non")
    prop = input("entrer une fonction logique : ")
    print(canonique(prop))


    # list splited by +
    pro = prop.split("+")
    # splited propo: proposition
    proposition = []
    # variable list from prop: propo
    propo = []
    # variable list: var
    var = []
    for i in pro:
        proposition.append(i.split())
    for i in range(len(pro)):
        propo = propo + proposition[i]

    def variables():
        global var, propo
        for b in range(len(propo)):
            for a in propo[b]:
                if a.isalpha():
                    var.append(a)
        return var


    def rm_double():
        global var
        tst = []
        for e in var:
            tst.append(var.count(e))
            while var.count(e) > 1:
                var.remove(e)
        return var


    variables()
    rm_double()
    rm_double()


    # print(var, rm_double())
    def et(*bla):
        all(bla)
        if all(bla) == True:
            return 1
        else:
            return 0


    def ou(*bla):
        any(bla)
        if any(bla) == True:
            return 1
        else:
            return 0


    def non(b):
        b = (b + 1) % 2
        return b

    # saval = [x, y, z] val
    saval = []
    # print("var", var)
    print("\t".join(str(va) for va in var))
    for i in range(2 ** len(var)):
        var_val = []
        saval.append(var_val)
        for j in range(len(var)):
            val = (i // (2 ** j)) % 2
            var_val.append(val)
        resultat = et(*var_val)
        azer = "\t".join(str(value) for value in var_val)
        print(azer, "\t")
    print("----------------------------------")
    # savno = [-x,-y,-z]
    savno = []
    print("\t".join(str(f"-{va}") for va in var))
    for i in range(len(saval)):
        var_var = []
        savno.append(var_var)
        for t in saval[i]:
            t = int(t)
            res = non(t)
            var_var.append(res)
        aze = "\t".join(str(value) for value in var_var)
        print(aze)

    # print("saval", saval)
    # print('savno', savno)
    # print("var",var)

    # a*b, b*c, c*a
    # print("proposition:", proposition)
    # print("propo", propo)
    propo_len = []
    for y in proposition:
        propo_len.append(len(y))

    prval = []
    for e in range(len(proposition)):
        prr = []
        prval.append(prr)
        # print("---------------------------------")
        # print("\t".join(proposition[e]))
        for r in range(2 ** len(var)):
            pr_val = []
            prr.append(pr_val)
            for t in range(propo_len[e]):
                vale = (r // (2 ** t)) % 2
                pr_val.append(vale)
            azet = "\t".join(str(value) for value in pr_val)
            result = et(*pr_val)
            # print("prval",prval)
            # print(azet,"\t",result)

    #     valeur ET (A*B)
    # variables du mions
    varno = []
    for r in var:
        varno.append("-" + r)

    # indx ['x', 'y', '-x', 'z', 'y', 'z']
    indx = []
    for i in range(len(proposition)):
        for a in range(len(proposition[i])):
            for r in proposition[i]:
                for e in proposition[i][a]:
                    if e.isalpha():
                        if r.count("-") == 0:
                            indx.append(e)
                        else:
                            if int(r.index('-') + 1) == int(r.index(e)):
                                indx.append(f'-{e}')
                            else:
                                indx.append(e)
    # print("indx", indx)
    # print("\t".join(indx))
    varet = []
    for i in range(0, len(proposition) * 2 - 1, 2):
        varet.append([indx[i], indx[i + 1]])
    # print("varet", varet)

    index = []
    variable = var + varno
    # print("variable", variable)
    for s in indx:
        for e in variable:
            if e == s:
                index.append(variable.index(e))
    # print("index", index)
    saveall = []

    for n in range(len(saval)):
        # for e in index:
        saveall = saveall + [saval[n] + savno[n]]

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    indexlst = []
    for i in range(0, len(proposition) * 2 - 1, 2):
        indexlst.append([index[i], index[i + 1]])

    saveet = []
    for z in range(len(saveall)):
        for x in indexlst:
            for y in propo:
                if y.count("-") == 0:
                    saveet.append(et(saveall[z][x[0]], saveall[z][x[1]]))
                    break
                elif not y.count("-") == 0:
                    if y.index('-') == 0:
                        saveet.append(non(et(saveall[z][x[0]], saveall[z][x[1]])))
                        break
                    else:
                        saveet.append(et(saveall[z][x[0]], saveall[z][x[1]]))
                        break

    #print("gduzhz", saaa(saveet))
    saaaa = []
    for a in range(0,len(saveet),len(pro)):
        saaaa.append(saveet[a:a+len(pro)])
    print("\t".join(propo),"\t",f"F({','.join(str(qs) for qs in var)})")

    saveou = []
    for b in saaaa:
        saveou.append(ou(*b))

    #print result +
    for b in range(2**len(var)):
        for k in saaaa:
            print(" \t\t".join(str(rer) for rer in saaaa[b]),"\t\t",str(saveou[b]))
            break
    canonique(prop)

