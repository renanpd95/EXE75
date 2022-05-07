import random,math

prod = 0
pvt = 0
pcv = 0
pct = 0
pcc = 0

for i in range(40):
  pc = random.randint (0,1000)
  pv = random.randint (0,1000)
 
  prod = prod + 1
  if(pc < pv):
    print(prod,"ºProduto:")
    print("Houve Lucro :D")
    print("pc R$",pc,"pv R$",pv)
    print("__________________\n")
    #media preço de venda
    pvt =  pvt + pv
    pcv = pcv + 1
    medpcv = pvt / pcv
    
  elif(pc > pv):
    print(prod,"ºProduto:")
    print("Houve Prejuizo :(")
    print("pc R$",pc,"pv R$",pv)
    print("__________________\n")
    #media preço de custo
    pct =  pct + pc
    pcc = pcc + 1
    medpcc = pct / pcc
    
  elif(pc == pv):
    print(prod,"ºProduto:")
    print("Houve Empate :S")
    print("pc R$",pc,"pv R$",pv)
    print("__________________\n")
else:
  
  print(f"Media Preço de Venda:{medpcv:.2f}")
  print(f"Media Preço de Custo:{medpcc:.2f}")
  