print("Codificador de palavras")
chave =input("Digite a palavra para sem encriptada! ")

#CODIFICADOR#

senha = " "
for letra in chave:
    if letra in "Aa":
        senha = senha + ";"
    elif letra in "Bb":senha = senha + "!"
    elif letra in "Cc":senha = senha + "}"
    elif letra in "Dd":senha = senha + "{"
    elif letra in "Ee":senha = senha + "<"
    elif letra in "Ff":senha = senha + ">"
    elif letra in "Gg":senha = senha + "?"
    elif letra in "Hh":senha = senha + "v"
    elif letra in "Ii":senha = senha + "u"
    elif letra in "Jj":senha = senha + "."
    elif letra in "Kk":senha = senha + ","
    elif letra in "Ll":senha = senha + "7"
    elif letra in "Mm":senha = senha + "#"
    elif letra in "Nn":senha = senha + "+"
    elif letra in "Oo":senha = senha + "c"
    elif letra in "Pp":senha = senha + "-"
    elif letra in "Qq":senha = senha + "3"
    elif letra in "Rr":senha = senha + ")"
    elif letra in "Ss":senha = senha + "_"
    elif letra in "Tt":senha = senha + "4"
    elif letra in "Uu":senha = senha + "$"
    elif letra in "Vv":senha = senha + "¨"
    elif letra in "Ww":senha = senha + "6"
    elif letra in "Xx":senha = senha + "*"
    elif letra in "Yy":senha = senha + "f"
    elif letra in "Zz":senha = senha + "a"
    elif letra in " " :senha = senha + " "

#PALAVRA CODIFICADA#   
 
print("FRASE ENCRIPTADA")
print(" ")
print(senha)
print("")