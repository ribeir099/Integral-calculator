
import sympy as sp  # biblioteca para algebra simbolica

# Configuração inicial da biblioteca

x, y, z, t = sp.symbols('x y z t')
# k, m, n = sp.symbols('k m n', integer=True)
# f, g, h = sp.symbols('f g h', cls=sp.Function)
# sp.init_printing(wrap_line=False)
# sp.init_session()
# sp.init_vprinting(use_unicode=True)


def getAntiderivada(funcao):
    # Cria uma integral indefinida da função em relação a x
    antiderivada = sp.Integral(funcao, x)

    # Calcula a antiderivada
    antiderivada = antiderivada.doit()

    # Simplifica a antiderivada
    antiderivadaSimplificada = sp.simplify(antiderivada)

    return antiderivadaSimplificada


def getIntegral(funcao, inf, sup):
    # Cria uma integral definida da função em relação a x no intervalo
    integral = sp.Integral(funcao, (x, inf, sup))

    # Imprime a integral de forma bonita (formato matemático)
    sp.pprint(integral)

    # Calcula a integral
    integral = integral.doit()

    # Simplifica a integral
    integralSimplificada = sp.simplify(integral)

    return integralSimplificada


def antiderivada():
    # Solicita ao usuário a função a ser antiderivada
    funcao = input('Insira a função a ser antiderivada: ')

    print('\n\nResultado:\n')
    print('\nA antiderivada de\n')

    # Imprime a integral indefinida da função
    sp.pprint(sp.Integral(funcao, x))
    print('\n = \n')

    # Calcula a antiderivada
    result = getAntiderivada(funcao)

    # Imprime o resultado da antiderivada
    sp.pprint(result)


def integralDefinida():
    # Solicita ao usuário a função a ser integrada
    funcao = input('Insira a função a ser integrada: ')

    # Solicita ao usuário o limite inferior
    inf = input('Insira o limite inferior: ')

    # Solicita ao usuário o limite superior
    sup = input('Insira o limite superior: ')

    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')

    # Calcula a integral definida
    result = getIntegral(funcao, inf, sup)

    print('\n1° - Antiderivada = ')

    # Calcula a antiderivada
    antiderivada = getAntiderivada(funcao)

    # Imprime a antiderivada
    sp.pprint(antiderivada)

    print('\n2° - substituição dos limites:')

    # Substitui x pelo limite superior na antiderivada
    funcSup = antiderivada.subs(x, sp.Symbol('{0}'.format(sup)))

    # Substitui x pelo limite inferior na antiderivada
    funcInf = antiderivada.subs(x, sp.Symbol('{0}'.format(inf)))

    # Imprime o resultado da substituição dos limites
    sp.pprint(funcSup - funcInf)

    print('\n3° - Resultado = \n')

    # Imprime o resultado da integral definida
    sp.pprint(result)


def integralSubs():
    # Solicita ao usuário a função a ser integrada
    funcao = sp.sympify(
        input('Insira a função a ser integrada: '),
        evaluate=False)

    # Solicita ao usuário a expressão a ser substituída
    exp = sp.sympify(
        input('Insira a expressão a ser substituída: '),
        evaluate=False)

    # Cria uma integral indefinida da função em relação a x
    integralOri = sp.Integral(funcao, x)

    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')

    # Imprime a integral indefinida original
    sp.pprint(integralOri)

    print("\n1° Função escrita na nova variável:\n")
    print("=> Calculando o novo valor de dx\n")

    # Define o símbolo u
    u = sp.Symbol('u')

    # Define a igualdade u = exp
    uExp = sp.Equality(u, exp)

    # Imprime a igualdade
    sp.pprint(uExp)

    print('\n')

    # Define o símbolo dx
    dx = sp.Symbol('dx')

    # Define o símbolo du
    du = sp.Symbol('du')

    # Calcula a razão du/dx
    duDx = sp.sympify(du/dx)

    # Calcula a derivada de exp em relação a x
    derivadaU = sp.diff(exp, x)

    # Imprime a igualdade du/dx = derivadaU
    sp.pprint(sp.Equality(duDx, derivadaU))

    print('\n')

    # Imprime a igualdade dx = (derivadaU^-1)*du
    sp.pprint(sp.Equality(dx, ((derivadaU**-1)*du)))

    print('\n')
    print("=> Substituindo u na integral\n")

    # Substitui exp por u na expressão da integral
    srtU = str(funcao*(derivadaU**-1)).replace("{0}".format(exp), 'u')

    # Converte a expressão para uma expressão simbólica
    expU = sp.sympify(srtU, evaluate=False)

    # Cria uma integral indefinida da expressão em relação a u
    integralU = sp.Integral(expU, u)

    # Imprime a igualdade entre a integral original e a integral em u
    sp.pprint(sp.Equality(integralOri, integralU))

    print('\n')
    print("=> Simplificando a integral em relação a u")

    # Simplifica a integral em relação a u
    integralFac = sp.Integral((sp.factor(expU)), u)

    print('\n')

    # Imprime a integral simplificada em relação a u
    sp.pprint(integralFac)

    print('\n')
    print('2° - Integral indefinida da função na nova variável\n')

    # Calcula a integral indefinida em u e adiciona a constante de integração
    resultU = sp.sympify(integralFac.doit() + sp.Symbol('C'))

    # Imprime a igualdade entre a integral em u e o resultado em u
    sp.pprint(sp.Equality(integralFac, resultU))

    print('\n')
    print('3° - Resultado da integral reescrito na variável antiga\n')

    # Substitui u por exp no resultado em u
    resultX = resultU.subs(u, exp)

    # Imprime a igualdade entre a integral original e o resultado em x
    sp.pprint(sp.Equality(integralOri, resultX))


def integralPartes():
    # Solicita ao usuário a função a ser integrada
    funcao = sp.sympify(
        input('Insira a função a ser integrada: '),
        evaluate=False)

    # Solicita ao usuário o elemento da substituição por u
    u = sp.sympify(
        input('Insira o elemento da substituição por u: '),
        evaluate=False)

    # Solicita ao usuário o dv
    dv = sp.sympify(
        input('Insira o elemento da substituição por dv: '),
        evaluate=False)

    # Cria uma integral indefinida da função em relação a x
    integralOri = sp.Integral(funcao, x)

    print('\n\nResultado:\n')
    print('\nCalculando a integral:\n')

    # Imprime a integral indefinida original
    sp.pprint(integralOri)

    print('\n\n1° - Termos v e du:\n')
    print("=> Calculando o valor de du\n")

    # Define o símbolo dx
    dx = sp.Symbol('dx')

    # Define o símbolo du
    du = sp.Symbol('du')

    # Calcula a razão du/dx
    duDx = sp.sympify(du/dx)

    # Calcula a derivada de u em relação a x
    derivadaU = sp.diff(u, x)

    # Imprime a igualdade du/dx = derivadaU
    sp.pprint(sp.Equality(duDx, derivadaU))

    print('\n')

    # Imprime a igualdade du = derivadaU*dx
    sp.pprint(sp.Equality(du, (derivadaU*dx)))

    print('\n')
    print("=> Calculando o valor de v\n")

    # Imprime a igualdade du = derivadaU*dx
    sp.pprint(sp.Equality(sp.Symbol('dv'), (dv*dx)))

    # Define o símbolo v
    v = sp.Symbol('v')

    # Calcula a integral de dv em relação a x
    v = sp.Integral(dv, x).doit()

    print('\n')

    # Imprime a igualdade v = valor da integral de dv
    sp.pprint(sp.Equality(sp.Symbol('v'), v))

    print('\n\n2° - Integral reescrita por partes:\n')

    # Calcula a primeira parte da integral reescrita por partes
    parte1 = u*v

    # Calcula a segunda parte da integral reescrita por partes
    parte2 = sp.Integral(v*derivadaU, x)

    # Cria a expressão da integral reescrita por partes
    exp = sp.sympify(parte1 - parte2, evaluate=False)

    # Imprime a igualdade entre a
    # integral original e a expressão reescrita por partes
    sp.pprint(sp.Equality(integralOri, exp))

    print('\n\n3° - Resultado da integral por partes:\n')

    # Avalia a expressão da integral por partes
    result = exp.doit()

    # Imprime o resultado final da integral por partes
    sp.pprint(sp.Equality(integralOri, (result + sp.Symbol('C'))))


def main():
    print('\n\nCALCULADORA DE INTEGRAIS\n\n')

    while True:
        print('ESCOLHA UMA OPÇÃO: ')
        print('[1] INTEGRAL INDEFINIDA')
        print('[2] INTEGRAL DEFINIDA')
        print('[3] INTEGRAL POR SUBSTITUIÇÃO')
        print('[4] INTEGRAL POR PARTES')
        print('[0] SAIR')
        print('\n> ', end='')
        option = int(input())

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
