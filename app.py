
import sympy as sp  # biblioteca para algebra simbolica

# Configuração inicial da biblioteca

x, y, z, t = sp.symbols('x y z t')
# k, m, n = sp.symbols('k m n', integer=True)
# f, g, h = sp.symbols('f g h', cls=sp.Function)
# sp.init_printing(wrap_line=False)
# sp.init_session()
# sp.init_vprinting(use_unicode=True)


def getAntiderivada(funcao):
    antiderivada = sp.Integral(funcao, x)
    antiderivada = antiderivada.doit()
    antiderivadaSimplificada = sp.simplify(antiderivada)
    return antiderivadaSimplificada


def getIntegral(funcao, inf, sup):
    integral = sp.Integral(funcao, (x, inf, sup))
    sp.pprint(integral)
    integral = integral.doit()
    integralSimplificada = sp.simplify(integral)
    return integralSimplificada


def antiderivada():
    funcao = input('Insira a função a ser antiderivada: ')
    print('\n\nResultado:\n')
    print('\nA antiderivada de\n')
    sp.pprint(sp.Integral(funcao, x))
    print('\n = \n')
    result = getAntiderivada(funcao)
    sp.pprint(result)


def integralDefinida():
    funcao = input('Insira a função a ser integrada: ')
    inf = input('Insira o limite inferior: ')
    sup = input('Insira o limite superior: ')
    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')
    result = getIntegral(funcao, inf, sup)
    print('\n1° - Antiderivada = ')
    antiderivada = getAntiderivada(funcao)
    sp.pprint(antiderivada)
    print('\n2° - substituição dos limites:')
    funcSup = antiderivada.subs(x, sp.Symbol('{0}'.format(sup)))
    funcInf = antiderivada.subs(x, sp.Symbol('{0}'.format(inf)))
    sp.pprint(funcSup - funcInf)
    print('\n3° - Resultado = \n')
    sp.pprint(result)


def integralSubs():
    funcao = sp.sympify(
        input('Insira a função a ser integrada: '),
        evaluate=False)
    exp = sp.sympify(
        input('Insira a expressão a ser substituída: '),
        evaluate=False)
    integralOri = sp.Integral(funcao, x)
    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')
    sp.pprint(integralOri)
    print("\n1° Função escrita na nova variável:\n")

    print("=> Calculando o novo valor de dx\n")
    u = sp.Symbol('u')
    uExp = sp.Equality(u, exp)
    sp.pprint(uExp)
    print('\n')
    dx = sp.Symbol('dx')
    du = sp.Symbol('du')
    duDx = sp.sympify(du/dx)
    derivadaU = sp.diff(exp, x)
    sp.pprint(sp.Equality(duDx, derivadaU))
    print('\n')
    sp.pprint(sp.Equality(dx, ((derivadaU**-1)*du)))
    print('\n')

    print("=> Substituindo u na integral\n")
    srtU = str(funcao*(derivadaU**-1)).replace("{0}".format(exp), 'u')
    expU = sp.sympify(srtU, evaluate=False)
    integralU = sp.Integral(expU, u)
    sp.pprint(sp.Equality(integralOri, integralU))
    print('\n')

    print("=> Simplificando a integral em relação a u")
    integralFac = sp.Integral((sp.factor(expU)), u)
    print('\n')
    sp.pprint(integralFac)
    print('\n')

    print('2° - Integral indefinida da função na nova variável\n')
    resultU = sp.sympify(integralFac.doit() + sp.Symbol('C'))
    sp.pprint(sp.Equality(integralFac, resultU))
    print('\n')

    print('3° - Resultado da integral reescrito na variável antiga\n')
    resultX = resultU.subs(u, exp)
    sp.pprint(sp.Equality(integralOri, resultX))


def integralPartes():
    funcao = sp.sympify(
        input('Insira a função a ser integrada: '),
        evaluate=False)
    u = sp.sympify(
        input('Insira o elemento da substituição por u: '),
        evaluate=False)
    dv = sp.sympify(
        input('Insira o elemento da substituição por dv: '),
        evaluate=False)
    integralOri = sp.Integral(funcao, x)
    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')
    sp.pprint(integralOri)

    print('\n\n1° - Termos v e du:\n')

    print("=> Calculando o valor de du\n")
    dx = sp.Symbol('dx')
    du = sp.Symbol('du')
    duDx = sp.sympify(du/dx)
    derivadaU = sp.diff(u, x)
    sp.pprint(sp.Equality(duDx, derivadaU))
    print('\n')
    sp.pprint(sp.Equality(du, (derivadaU*dx)))
    print('\n')

    print("=> Calculando o valor de v\n")
    sp.pprint(sp.Equality(sp.Symbol('dv'), (dv*dx)))
    v = sp.Symbol('v')
    v = sp.Integral(dv, x).doit()
    print('\n')
    sp.pprint(sp.Equality(sp.Symbol('v'), v))

    print('\n\n2° - Integral reescrita por partes:\n')
    parte1 = u*v
    parte2 = sp.Integral(v*derivadaU, x)
    exp = sp.sympify(parte1 - parte2, evaluate=False)
    sp.pprint(sp.Equality(integralOri, exp))

    print('\n\n3° - Resultado da integral por partes:\n')
    result = exp.doit()
    sp.pprint(sp.Equality(integralOri, (result + sp.Symbol('C'))))


def main():
    print('\n\nCALCULADORA DE INTEGRAIS\n\n')
    option = -1
    validOptions = [1, 2, 3, 4]

    while option not in validOptions:
        print('ESCOLHA UMA OPÇÃO: ')
        print('[1] INTEGRAL INDEFINIDA')
        print('[2] INTEGRAL DEFINIDA')
        print('[3] INTEGRAL POR SUBSTITUIÇÃO')
        print('[4] INTEGRAL POR PARTES')
        print('[0] SAIR')
        print('\n> ', end='')
        option = int(input())

        if option not in validOptions:
            print('\nOpção inválida\n')

        match option:
            case 0:
                print('\n\nDESLIGANDO\n\n')
                break
            case 1:
                antiderivada()
                print('\n\n')
                continue
            case 2:
                integralDefinida()
                print('\n\n')
                continue
            case 3:
                integralSubs()
                print('\n\n')
                continue
            case 4:
                integralPartes()
                print('\n\n')
                continue
            case _:
                print('Opção inválida')
                print('\n\n')
                continue


main()

# fuc1 = (x+1)*sqrt(x**2+2*x)
# func2 = x*sin(x)
