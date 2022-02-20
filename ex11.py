"""
i.Να δημιουργήσετε μία συνάρτηση η οποία εκτυπώνει τον μέσο όρο δύο τιμών. 
(π.χ. Μέσος όρος των μεταβλητών x και y είναι :  )
ii.Να δημιουργήσετε μία συνάρτηση η οποία θα παίρνει ως input 3 μεταβλητές και θα επιστρέφει 
την μεγαλύτερη από αυτές τις 3. Να το κάνετε χωρίς να χρησιμοποιήσετε την συνάρτηση max().

"""

def findAverage(num1,num2):
    print(f"Ο μέσος όρος των τιμών {num1} και {num2} είναι:", (num1+num2)/2)

def findMaxNum(num1,num2,num3):
    #maxnum=number[0]
    numlst=[num1,num2,num3]
    maxnum=-500000
    for number in numlst:
        if number>maxnum:
            maxnum=number
        elif number==maxnum :
            print (f" Ο αριθμός {number} δόθηκε δύο φορές")
        elif number<maxnum :
            pass
        else:
            print(f"Παρουσιάστηκε πρόβλημα στην επεξεργασία")
            return-1
    return maxnum
       

findAverage(12,99)
maxNum=findMaxNum(22,22,44)
if not maxNum ==-1 :
    print("Ο μέγιστος αριθμός είναι:",maxNum)