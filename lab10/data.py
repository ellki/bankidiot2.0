class Customer:
    #Klass som representerar en kund
    
    #Konstruktor:
    def __init__(self, customer_id: str, personal_nbr: str, name: str):
    #Skapar en kund med kundnummer customer_id, personnummer personal_nbr och namnet name
        self._customer_id = customer_id #(går att läsa men oföränderlig), Kundens unika kundnummer i banken
        self._personal_nbr = personal_nbr #(går att läsa men oföränderlig), Kundens personnummer
        self._name = name #(går att läsa och ändra), Kundens namn
        
    #Metoder:
    def __str__(self) -> str:
        #Returnerar en sträng för att användarvänligt beskriva denna kund
        return f'Kund: {self._customer_id} Namn (personnummer): {self._name} ({self._personal_nbr})'
    
    #Gör namn föränderligt, fattar dock ej när det skulle behövas.
    @property
    def name(self):
        return self._name

    @name.setter  #Gör namnet ändringsbart.
    def name(self, new_name):
        self._name = new_name

    @property
    def personal_nbr(self):
        return self._personal_nbr


class Account:
    #Klass som representerar ett bankkonto

    #Konstruktor:
    def __init__(self, customer_id: str, account_nbr: int):
    #Skapar ett konto för kunden med id customer_id och med kontonumret account_nbr
        self._customer_id = customer_id
        self._account_nbr = account_nbr
        self._balance: float = 0.0
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def account_nbr(self):
        return self._account_nbr

    #Methods:
    def deposit(self, amount: float) -> bool:
        #Sätter in beloppet amount på detta konto 
        #Returnerar True om insättningen lyckades och false annars (om beloppet är negativt)
        if amount > 0:
            self._balance += amount
            return True
        
        return False

    def withdraw(self, amount: float) -> bool:
        #Tar ut beloppet amount från detta konto.
        #Returnerar True om uttaget lyckades och False annars (om beloppet är felaktigt eller för stort)
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        
        return False

    def __str__(self) -> str:
        #Returnerar en strängrepresentation av detta konto på formen
        #’kontonummer: 1000, saldo: 0.0 (C10)’ Där C10 är exempel på kontoinnehavarens kundnummer
        return f'Kund: {self._customer_id}, Kontonummmer: {self._account_nbr}, Saldo: {self._balance}'

class Bank:
    '''Klass som representerar en bank och som ger möjlighet
    att lagra konton och kunder'''
    #Konstruktor:
    def __init__(self):
        self._customers = {} #Dictionary med Kundnummer:Kunder (Customer)
        self._personal_nbrs = []
        self._accounts = {} #Dictionary med Kontonnummer:Konto (Account)
        self._customer_nbr_counter = 9
        self._account_nbr_counter = 999

    #Metoder:
    def add_customer(self, name: str, personal_nbr: str) -> str: # or None:
        '''Skapar en ny kund och lägger till den till banken.
        Returnerar den nya kundens kundnummer eller None om personnumret
        redan fanns och kunden därför inte kunde skapas.'''
        if personal_nbr not in self._personal_nbrs:
            self._customer_nbr_counter += 1
            customer_id = 'C'+ str(self._customer_nbr_counter)
            self._customers[customer_id] = Customer(customer_id, personal_nbr, name)
            self._personal_nbrs.append(personal_nbr)
            return customer_id

        elif personal_nbr in self._personal_nbrs:
            return None

    def get_customer(self, customer_id: str) -> Customer:#or None:
        '''Returnerar kunden med kundnummer customer_id,
        returnerar None om ingen sådan kund existerar.'''
        if customer_id in self._customers:
            return self._customers[customer_id]
            

    def find_customer_by_part_of_name(self, name_part: str) -> list[Customer]:
        '''Returnerar en lista med de kundobjekt vars namn helt eller delvis
        innehåller strängen name_part'''
        pass

    def create_account(self, customer_id: str) -> int:
        '''Skapar ett nytt konto åt kunden med kundnummer customer_id.
        Returnerar det nya kontots kontonummer eller -1 om kunden inte existerar.'''
        # if customer_id in self._accounts:
        #     self._account_nbr_counter += 1
        #     account_nbr = self._account_nbr_counter
        #     self._accounts[customer_id] = [self._accounts[customer_id], Account(customer_id, account_nbr)]
        #     return account_nbr

        if customer_id in self._customers:
            self._account_nbr_counter += 1
            account_nbr = self._account_nbr_counter
            self._accounts[account_nbr] = Account(customer_id, account_nbr)
            return print(account_nbr) #print skall inte stå här
        
        else:
            return -1

    def get_account(self, account_nbr: int) -> Account: #or None:
        '''Returnerar det Account-objekt som har nummer account_nbr,
        returnerar None om ett sådant konto inte kan hittas.'''
        if account_nbr in self._accounts:
            return self._accounts[account_nbr]
        else:
            return None
    
    def remove_account(self, account_nbr: int) -> bool:
        '''Tar bort kontot med kontonummer account_nbr
        Returnerar True om kontot kunde tas bort, False annars
        (d.v.s. om kontot inte hittades eller saldot inte var noll).'''
        if account_nbr in self._accounts:
            del self._accounts[account_nbr]
            return True
        else:
            return False

    def transfer(self, from_acc_nbr: int, to_acc_nbr: int, amount: float) -> bool:
        '''För över summan amount från kontot med nummer from_acc_nbr
        till kontot med nummer to_acc_nbr.
        Returnerar True om båda kontona existerar och överföringen lyckas'''
        pass

    def all_accounts(self) -> list[Account]:
        '''Returnerar en lista med bankens samtliga bankkonton.'''
        pass

    def accounts_by_customer(self, customer_id: str) -> list[Account]: #or None:
        '''Returnerar en lista med samtliga konton som innehas av kunden
        med kundnummer customer_id.
        Returnerar None om ingen sådan kund existerar'''
        account_list=[]
        for account_nbr in self._accounts:
            account = self.get_account(account_nbr)
            if account.customer_id == customer_id: #account and
                account_list.append(account)

            return account_list



        

    # def all_customers_sorted_by_name(self) -> list[Customer]:
    #     '''Returnerar en lista med bankens samtliga kunder,
    #     listan som returneras ska vara sorterad stigande,
    #     i bokstavsordning, med avseende på kundernas namn'''
    #     for customer_id in self._customers:
    #         return f'{Bank.get_customer(self, customer_id),} \n\t {Bank.accounts_by_customer(self, customer_id)}' #FÅR JAG HA PRINT HÄR, HUR GÖR JAG ANNARS, RETURN BRYTER LOOPEN

    def all_customers_sorted_by_name(self) -> list[str]:
        for customer_id in self._customers:
            customer_info = f'{Bank.get_customer(self, customer_id)}'
            account_info = f' \t {Bank.accounts_by_customer(self, customer_id)}'
            
            return customer_info, account_info
            
        

            