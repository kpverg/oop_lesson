"""Δημιουργήστε κώδικα, ο οποίος κάνει το εξής : 
Δημιουργούμε δύο μεταβλητές που αντιστοιχούν σε δύο ακέραιους αριθμούς.
 Ο κώδικας μας θέλουμε να επιστρέφει το γινόμενο τους και αν αυτό το γινόμενο είναι 
 μεγαλύτερο από 1000, να επιστρέφει και το άθροισμά τους.(δημιουργία συνάρτησης)

"""

def calcBeforePrint(num1,num2):
    def mult(num1,num2):
        return num1*num2
    def summ(num1,num2):
        return num1+num2
    currentnum=mult(num1,num2)
    if currentnum>=1000:
        currentnum=summ(num1,num2)
    return currentnum



print(calcBeforePrint(50,10))