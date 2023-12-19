print("***********Experiments***********")
tst_number=int(input("Enter the number of test cases: "))
i,rabt,rat,frg=1,0,0,0
anm_numbers=0
while i<=tst_number:
    anm_ch=str(input(f"Test:{i}\nEnter the type of animal: "))
    print("")
    anm_number=int(input(f"Enter the amount of {anm_ch}: "))
    if anm_number>=1 and anm_number<=15:
        if anm_ch=="rabt":
            rabt+=anm_number
        elif anm_ch=="rat":
            rat+=anm_number
        elif anm_ch=="frg":
            frg+=anm_number
    i+=1
    anm_numbers+=anm_number
print("***********Results***********")
print("Total tests: ",tst_number)
print("Total animals: ",anm_numbers)
print("Total Rabbit: ",rabt)
print("Total Rat: ",rat)
print("Total Frog: ",frg)
prcnt_rabt=(rabt/anm_numbers)*100
prcnt_rat=(rat/anm_numbers)*100
prcnt_frg=(frg/anm_numbers)*100
print(f"Percenatge of Rabbit: {prcnt_rabt:.2f}%")
print(f"Percenatge of Rat: {prcnt_rat:.2f}%")
print(f"Percenatge of Frog: {prcnt_frg:.2f}%")
print("***********End of Results***********")
