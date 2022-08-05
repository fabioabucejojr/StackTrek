Eggs = int(input("How many eggs?: "))

price1 = 70

dozen = (Eggs // 12)
remainingeggs = (Eggs % 12) * 7
totalprice = ((price1 * dozen) + remainingeggs)

print(totalprice)
