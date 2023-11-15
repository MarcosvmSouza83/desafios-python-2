import textwrap

def menu ():
  menu = """\n
================ *** Banco Santander *** ================

Ola Sr(a),Digite a opcao desejada...

[d]\tDepositar  
[s]\tsacar
[e]\tExtrato
[nc]\tnova_conta
[lc]\tlistar_contas
[nu]\tnovo_usuario
[px]\tpix
[0]\tSair
=> """
  return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato,/):
 if valor > 0:
    saldo += valor
    extrato +=  f"Deposito: R$ {valor:.2f}\n"
    print("\n=== Deposito realizado com sucesso!====")
 else:
    print("operacao falhou! o valor informado e invalido. ")
    return saldo,extrato
            

def sacar(*,saldo,valor,extrato,limite,numeros_saques,limites_saques,limites_pix):
 excedeu_saldo = valor > saldo
 excedeu_limite = valor > limite
 excedeu_saques = numero_saques = limites_saques

 if excedeu_saldo:
    print("Operação falhou! Você não tem saldo suficiente.")

 elif excedeu_limite:
    print("Operação falhou! O valor do saque excede o limite disponivel.")    

 elif excedeu_saques: 
    print("Operação falhou! Numero Máximo de saques excedido.")

  
 elif valor > 0:
      saldo -= valor
      extrato +=  f"Saque: R$ {valor:.2f}\n" 
      numero_saques += 1 
      print("\n=== Saque realizado com sucesso===! ")

 else:
     print("Operação falhou!  O valor informado é inválido.") 

     return saldo,extrato


def exibir_extrato(saldo, /, *,extrato):
   print("\n\n\n================ EXTRATO ================")
   print("Não foram realizadas movimentações." if not extrato else extrato)
   print(f"\n\nSaldo disponivel: R$ {saldo:.2f}")
   print("\n==============================================")
      
   print("\n================ SALDO ================")
   print("Sujeito alterações até o final do expediente.")
   print(f"\n\n\n\nSaldo disponivel: R$ {saldo:.2f}")
   print("\n=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario :
       print(" já existe usuário com esse CPF! ")
       return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = ("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro,nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    
    print("=== usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("Informa o CPF do usuário:")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("\n=== conta criada com sucesso! ===")
      return{"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
      
   print("\n=== usuario nao encontrado,fluxo de criação de conta encerrado!===")


def listar_contas(contas):
    for conta in contas:
        linha = '''\
        Agencia:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
     '''
    print ("a" * 100)
    print(textwrap.dedent(linha))


def main():
    LIMITES_SAQUES = 3  
    AGENCIA = "0001"
 
    saldo = 5000
    limite = 1500
    pix = 5000
    extrato = ""
    numero_saques = 0
    numero_pix = 0
    LIMITES_PIX = 3
    usuarios =[]
    contas = []

    while True:

     opcao = (menu)

     if opcao == "d":
         valor = float(input("informe o valor de depo´sito"))

         saldo,extrato = depositar(saldo,valor,extrato)
         
     elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo,extrato = sacar(
          saldo=saldo,
          valor=valor,
          extrato=extrato,
          limite=limite,
          numero_saques=numero_saques,
          LIMITES_SAQUES=LIMITES_SAQUES,
          LIMITES_PIX=LIMITES_PIX,
     )

     elif opcao == "e":
         exibir_extrato(saldo,extrato=extrato)

     elif opcao == "nu":   
         criar_usuario(usuarios)

     elif opcao == "nc":   
         numero_conta = len(contas)+1
         conta = criar_conta(AGENCIA,numero_conta,usuarios) 

         if conta:
             contas.append(conta)

     elif opcao == "lc":
         listar_contas(contas)    

     elif opcao == "px":
      valor = float(input("Informe o valor do Pix: "))

      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_pix = numero_pix >= LIMITES_PIX
    
     if excedeu_saldo:
          print("Operação falhou! Voce não tem saldo suficiente.")   

     elif excedeu_limite:
           print("Operação falhou! O valor do pix excede o limite disponivel.")    

     elif excedeu_pix: 
          print("Operação falhou! Numero Máximo de pix excedido.")

  
     elif valor > 0:
            saldo -= valor
            extrato +=  f"Pix: R$ {valor:.2f}\n" 
            numero_pix += 1
     elif opcao == "0":
           valor = float(input)("================= Santander agradece a sua preferência! Obrigado.=====================")

    else:
         print("Operação inválida,por favor selecione novamente a operação desejada, ")     