def verifica(listas, valor_a):
        print(listas)
        if valor_a in listas:
            valor_base_b = input("Digite qual base da lista numérica você deseja converter: ")
            #--Binário para Decimal--
            if valor_base_b in listas:
                if valor_a == "bin" and valor_base_b == "dec":
                    print()
                    num_a = input("Digite um valor: ")
                    converter_a = int(num_a, 2)
                    print("O número binário", num_a, "em decimal é", converter_a)
                #--Decimal para Binário--
                elif valor_a == "dec" and valor_base_b == "bin":
                    print()
                    num_b = int(input("Digite um valor: "))
                    converter_b = bin(num_b)
                    print("O número Decimal", num_b, "em Binário é", converter_b)
                #--Decimal para Octal--
                elif valor_a == "dec" and valor_base_b == "oct":
                    print()
                    num_d = int(input("Digite um valor: "))
                    converter_d = oct(num_d)
                    print("O número Decimal", num_d, "em Binário é", converter_d)
                #--Octal para Decimal--
                elif valor_a == "oct" and valor_base_b == "dec":
                    print()
                    num_e = input("Digite um valor: ")
                    converter_e = int(num_e, 8)
                    print("O número Octal", num_e, "em Decimal é", converter_e)
                #--Decimal para Hexadecimal--
                elif valor_a == "dec" and valor_base_b == "hex":
                    print()
                    num_f = int(input("Digite um valor: "))
                    converter_f = hex(num_f)
                    print("O número Decimal", num_f, "em Hexadecimal é", converter_f)
                #--Hexadecimal para Decimal--
                elif valor_a == "hex" and valor_base_b == "dec":
                    print()
                    num_g = input("Digite um valor: ")
                    converter_g = int(num_g, 16)
                    print("O número Hexadecimal", num_g, "em Decimal é", converter_g)
            else:
                print(f"'{valor_a}' não está na lista")
                
            
        else:
            print(f"'{valor_a}' não está na lista")
            