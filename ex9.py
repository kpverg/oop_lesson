"""
Δημιουργήστε κώδικα, ο οποίος κάνει το εξής : Παίρνετε ως εύρος αριθμών από 
το 1 εώς το 10. Ο κώδικας μας θα γίνει με την βοήθεια επαναλήψεων, σε κάθε επανάληψη 
θέλουμε να φαίνεται ο τρέχων αριθμός, ο προηγούμενος και το άθροισμα του τρέχοντος και 
του προηγούμενου αριθμού.
"""

preNum=0
for num in range(1,11):

    print(f"Ο τρέχων αριθμός είναι :{num}")
    print(f"Ο προηγούμενος αριθμός είναι :{preNum}")

    print(f"Το άθροισμα των δύο είναι :{num+preNum}")
    preNum=num;


