from data import Customer
from data import Account
from data import Bank

alternativ=['1. Skapa en ny kund', '2. Skapa ett nytt konto', '3. Ta bort konto', '4. Sätta in pengar',
            '5. Ta ut pengar', '6. Överför pengar', '7. Skriv ut alla konton', '8. Sök på kund på del av namn', 
            '9. Skriv ut samtliga kunder (bokstavsordning) och dess konton', '10. Avsluta programmet']


def start_message():
    choice=0
    bank = Bank()
    while choice !=10:
        print('\n' 'Välj ett av följande alternativ:')
        for alt in alternativ:
            print(alt)
        choice = int(input())
        #Varje val ska printa detta meddelandet (via __str__ ? maybe?) och kalla på respektive funktion
        if choice == 1:
            print('Du har valt att skapa en ny kund')
            print(bank.add_customer(input('Ange kundens namn: ') , input('Ange kundens personnummer på formen ÅÅMMDD: ')))

        elif choice == 2:
            print('Du har valt att skapa ett nytt konto')
            bank.create_account(input('Ange kundnummer: '))
        elif choice == 3:
            print('Du har valt att ta bort ett konto')
            remove_account(int(input('Ange konto att ta bort: ')))
        elif choice == 4:
            print('Du har valt att sätta in pengar')
            a = Account('C10' , 1000 ) #Detta ska ske automatiskt på något vis, for-loop? if-sats? 
            a.deposit(int(input('Ange insättningsbelopp')))
        elif choice == 5:
            print('Du har valt att ta ut pengar')
            a = Account('C10' , 1000 )
            a.withdraw(int(input('Hur mycket vill du ta ut?')))
        elif choice == 6:
            print('Du har valt att överföra pengar')
            #funktion
        elif choice == 7:
            print('Du har valt att skriva ut alla konton')
            print(a) #bara test denna ska nog itne ligga här.
        elif choice == 8:
            print('Du har valt att söka på (del av) kundnamn')
            #funktion
        # elif choice == 9:
        #     print('Du har valt att skriva ut alla kunder tillsammans med deras konton')
        #     print(bank.all_customers_sorted_by_name())
        elif choice == 9:
            print('Du har valt att skriva ut alla kunder tillsammans med deras konton')
            for customer_info in bank.all_customers_sorted_by_name():
                print(customer_info)
        elif choice == 10:
            print('Du har valt att avsluta programmet, välkommen tillbaka!')

#####################################################################################################################1
            

bank = Bank()
start_message() 