def obtenerPremisa():
    simb1 = input("Ingresa el primer simbolo: ")
    operador = input("Ingresa el operador: ")
    simb2 = input("Ingresa el segundo simbolo: ")
    premisa = simb1 + " " + operador + " " + simb2
    return simb1, operador, simb2, premisa

def operacion(simb,value1,value2):
    if simb == '∧':
        return conjuncion(value1,value2)
    elif simb == '∨':
        return disyuncion(value1,value2)
    elif simb == "→":
        return condicional(value1,value2)
    elif simb == "↔":
        return bicondicional(value1,value2)

def obtainCriticRows(listValue):
    index = len(listValue)-1
    if listValue[index-2] == True and listValue[index-1] == True:
        return True
    else:
        return False

def compareConclution(listValue,value):
    index = len(listValue)-1
    if value == True and listValue[index] == True:
        return True
    else:
        return False

def compareCriticsValues(value1,value2,value3,value4):
    if value1 and value2 and value3 and value4 == True:
        return True
    else:
        return False

def verifyArgument(listValue1,listValue2,listValue3,listValue4):
    value1 = True
    value2 = True
    value3 = True
    value4 = True
    argumentValue = False
    if obtainCriticRows(listValue1) == True:
        value1 = compareConclution(listValue1, True)
    if obtainCriticRows(listValue2) == True:
        value2 = compareConclution(listValue2, True)
    if obtainCriticRows(listValue3) == True:
        value3 = compareConclution(listValue3, True)
    if obtainCriticRows(listValue4) == True:
        value4 = compareConclution(listValue4, True)
    if compareCriticsValues(value1, value2, value3, value4) == True:
        argumentValue = True
    return argumentValue
    

def conjuncion(valor1, valor2):
    value = valor1 and valor2
    return value
def disyuncion(valor1, valor2):
    value = valor1 or valor2
    return value
def condicional(valor1, valor2):
    value = True
    value = not(value) or valor1
    value = not(value) or valor2
    return value
def bicondicional(valor1,valor2):
    value = condicional(valor1,valor2) and condicional(valor2,valor1)
    return value
def negacion(valor):
    valor = not(valor)
    return valor

def setValues(listProp,prem1,opr,prem2,premisa,values1,values2,values3,values4):
    prop1_index = obtenerIndices(listProp, prem1)
    prop2_index = obtenerIndices(listProp, prem2)
    prem_index = obtenerIndices(listProp, premisa)
    values1[prem_index] = operacion(opr, values1[prop1_index], values1[prop2_index])
    values2[prem_index] = operacion(opr, values2[prop1_index], values2[prop2_index])
    values3[prem_index] = operacion(opr, values3[prop1_index], values3[prop2_index])
    values4[prem_index] = operacion(opr, values4[prop1_index], values4[prop2_index])
    return values1,values2,values3,values4
def obtenerIndices(listprop,prop1):
    x = 0
    i = 0
    for i in range(len(listprop)):
        if prop1 == listprop[i]:
            x = i
    return x
    
negindex1 = -1
negindex2 = -1
negprop1 = 0
negprop2 = 0
index = -1
listValues = []
listValues2 = []
listValues3 = []
listValues4 = []
listprop = []
cleanlistprop = []
i = 0
x = 0
prop1_index = 0
prop2_index = 0
prem_index = 0

print("Operadores\n====================\n")
print("1.-Negación ~\n")
print("2.-Conjuncion ∧\n")
print("3.-Disyunción ∨\n")
print("4.-Condicional →\n")
print("5.-Bicondicional ↔\n")
print("====================\n")
print("ADVERTENCIA: SOLO PUEDEN SER INGRESADAS 1 O 2 PROPOSICIONES")
input("PRESIONE ENTER PARA CONTINUAR")

print("Premisa 1")
p1prop1, p1opr, p1prop2, premisa1 = obtenerPremisa()
listprop.append(p1prop1)
listprop.append(p1prop2)
listValues.append(0)

print("\nPremisa 2")
p2prop1, p2opr, p2prop2, premisa2 = obtenerPremisa()
listprop.append(p2prop1)
listprop.append(p2prop2)
listValues.append(0)

print("\nConclusion")
concprop1, concopr, concprop2, conclusion = obtenerPremisa()
listprop.append(concprop1)
listprop.append(concprop2)
listValues.append(0)

print(f"\nLa primer premisa es: {premisa1}")
print(f"La segunda premisa es: {premisa2}")
print(f"La conclusion es: {conclusion}")

for i in listprop:
    if i not in cleanlistprop: cleanlistprop.append(i)
cleanlistprop.sort()
listprop = cleanlistprop.copy()
for i in cleanlistprop:
    listValues.append(0)
cleanlistprop.append(premisa1)
cleanlistprop.append(premisa2)
cleanlistprop.append(conclusion)
listValues2 = listValues.copy()
listValues3 = listValues.copy()
listValues4 = listValues.copy()
if len(listprop) < 2:
    listValues[0] = True
    listValues2[0] = False
else:
    for i in range(2):
        listValues[i] = True
        listValues2[i] = True
        listValues3[i] = False
        listValues4[i] = False
        if i == 1:
            listValues2[i] = False
            listValues3[i] = True
for i in listprop:
    index = index + 1
    if i.find("~") != -1: 
        x = x + 1
        if x == 1: 
            negindex1 = index
            negprop1 = i[1]
        if x > 1: 
            negindex2 = index
            negprop2 = i[1]
if negindex1 > -1:
    if negprop1 == cleanlistprop[0]:
        listValues[negindex1] = negacion(listValues[0])
        listValues2[negindex1] = negacion(listValues2[0])
        listValues3[negindex1] = negacion(listValues3[0])
        listValues4[negindex1] = negacion(listValues4[0])
    else:
        listValues[negindex1] = negacion(listValues[1])
        listValues2[negindex1] = negacion(listValues2[1])
        listValues3[negindex1] = negacion(listValues3[1])
        listValues4[negindex1] = negacion(listValues4[1])
        
if negindex2 >-1:
    if negprop2 == cleanlistprop[0]:
        listValues[negindex2] = negacion(listValues[0])
        listValues2[negindex2] = negacion(listValues2[0])
        listValues3[negindex2] = negacion(listValues3[0])
        listValues4[negindex2] = negacion(listValues4[0])
    else:
        listValues[negindex2] = negacion(listValues[1])
        listValues2[negindex2] = negacion(listValues2[1])
        listValues3[negindex2] = negacion(listValues3[1])
        listValues4[negindex2] = negacion(listValues4[1])

listValues, listValues2, listValues3, listValues4 = setValues(cleanlistprop, p1prop1, p1opr, p1prop2, premisa1, listValues, listValues2, listValues3, listValues4)
listValues, listValues2, listValues3, listValues4 = setValues(cleanlistprop, p2prop1, p2opr, p2prop2, premisa2, listValues, listValues2, listValues3, listValues4)
listValues, listValues2, listValues3, listValues4 = setValues(cleanlistprop, concprop1, concopr, concprop2, conclusion, listValues, listValues2, listValues3, listValues4)
    
for i in cleanlistprop:
    print(f'{i:<8}',end="")
print()
for i in listValues:
    i = str(i)
    print(f'{i:<8}',end="")
print()
for i in listValues2:
    i = str(i)
    print(f'{i:<8}',end="")
print()
if len(listprop) > 1:
    for i in listValues3:
        i = str(i)
        print(f'{i:<8}',end="")
    print()
    for i in listValues4:
        i = str(i)
        print(f'{i:<8}',end="")
    print()
if verifyArgument(listValues, listValues2, listValues3, listValues4) == True:
    print("El argumento es válido")
else:
    print("El argumento no es válido")