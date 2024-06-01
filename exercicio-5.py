import convercao

#--main--

print("Programa que converte bases numéricas")
print()

bases = ["bin", "dec", "oct", "hex"]

print(bases)
valor_base_a = input("Digite qual base da lista numérica que você deseja converter: ")
print()

convercao.verifica(bases, valor_base_a)