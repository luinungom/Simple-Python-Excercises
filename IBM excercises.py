# Crea una función log que acepte cualquier número de argumentos y los imprima por pantalla en una misma línea.
# La línea debe empezar con el prefijo ‘LOG: ’.

def exercise1(*args):
    prefix = "LOG"
    for word in args:
        prefix += " " + word
    return prefix


print(exercise1("Hello", "World"))


# Modifica la función log para que usuario pueda especificar cualquier prefijo que desee.

def exercise2(prefix, *args):
    prefix = prefix
    for word in args:
        prefix += " " + word
    return prefix


print(exercise2("This is a prefix", "Hello", "World"))


# Modifica la función log para que el prefijo tenga el valor por defecto ‘LOG: ’.

def exercise3(text, prefix="LOG DEFAULT"):
    return prefix + " " + text


print(exercise3("Hello" " World"))
print(exercise3("Hello" " World", "LOG DIFFERENT MODIFIED"))


# Modifica la función log para que el usuario pueda establecer tanto prefijo como separador entre argumentos. Ambos
# deben pasarse sólo por los nombres (no por posición) ‘sep’ y ‘prefix’. No hace falta que estos tengan valor por defecto

def exercise4(sep, prefix, *args):
    prefix = prefix
    for word in args:
        prefix += sep + word
    return prefix


print(exercise4("-", "PREFIX", "Hello", "World"))


# Modifica la función log para que ahora ‘sep’ y ‘prefix’ tengan un valor por defecto.

def exercise5(sep="-", prefix="PREFIX", *args, ):
    prefix = prefix
    for word in args:
        prefix += sep + word
    return prefix


print(exercise5("/", "NEW_PREFIX", "Hello", "World", ))


def thing(param_1, param_2, *args, **kwargs):
    print(param_1, param_2, args, kwargs)


thing(param_2="a", param_1="b")

print("Esta frase" , "termina aquí.")
print("Esta frase " + "termina aquí.")

a = "uno"
c = a * 99
print(c)

s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())

miTupla = ("manzana", "banana", "cereza")
print(miTupla[-3])