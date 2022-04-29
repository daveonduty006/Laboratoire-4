## **Python Project #4**
### 'The ATM Simulator Program' ###
***
*working with  dictionaries, rudimentary encryption and data manipulation (prelude to OOP introduction)*
***

### Description ###
    This fourth project is the classic ATM simulator program without any outside modules. The program was first initialized with a unencrypted database of bank accounts-like data (account number, account password, chequing balance, saving balance, investment balance, interest rate).
    An encryption algorithm was then implemented in order to save the data in memory into a new, encrypted database, allowing the deletion of the old database.
    Using the reversed logic for the decryption algorithm, the program was then ready for further implementations such as a user login menu, a menu of account selection (chequing, saving, investment), a menu simulating day-to-day bank operations such as deposits, removals, reviewing investment returns on a 5 year period relative to the account interest rate and a way to change account without having to exit the program.
    When the exit option is selected, the user-modified data is always re-encrypted before being rewritten into the database.
    Finally, an administrator menu (inaccessible to normal users) was implemented to allow special admin-like operations such as account removal, creation, modification of the interest rate, etc.

### Steps of the Project ###

    ** Step 1 **
    Create a database ('unencrypted_db.txt') with the following data:
    (see data.png)
    
    ** Step 2 **
    Create a way for a user to log into his account with his account number and password. As long as one information is wrong, access into the account is denied. (hint: use dictionary)
    Once login is successful, the user should be presented an account selection menu (chequing, saving, investment).
    Once the type of account is selected, a menu of operations is presented to the user with the following options: 
        1. Make a deposit
        2. Make a withdrawal
        3. Change account
        4. Exit
    ALWAYS DISPLAY THE ACCOUNT BALANCE AFTER SELECTING IT FROM THE ACCOUNT SELECTION MENU.

    ** Step 3 **
    Create a simple algorithm for encrypting and decrypting (reversed logic) the data within the unencrypted database. 
    ALGORITHM USED:
    a -> b / z -> a
    0 -> 1 / 9 -> 0
    No outside modules can be used for the encryption.
    The encrypted data should then be written within a new database ('db.txt') and the old one deleted.

    ** Step 4 **
    Create the functions that will simulate the operations of the user operations menu EXCEPT the returns on investment. 
    For withdrawals, do not allow them if there is insufficient funds.
    MAKE SURE TO DISPLAY THE SELECTED ACCOUNT BALANCE FIRST WITHIN EACH OPERATION FUNCTIONS.

    ** Step 5 **
    Create an alternate user operations menu if the user select his investment account on the account selection menu.
    This menu should have the following options: 
        1. Make a deposit
        2. Make a withdrawal
        3. View investment returns
        4. Change account
        5. Exit
    MAKE SURE TO ONLY DISPLAY THIS ALTERNATE MENU ONLY IF THE USER SELECT HIS INVESTMENT ACCOUNT. 

    ** Step 6 **
    Create a way to have the projected returns on investment for the next 5 years displayed on the screen if the user select the investment returns option on the alternate user operations menu. 
    Hint: look for the formula to calculate compound interest.

    ** Step 7 ** 
    Create a special administrator menu that can only be accessed if the account number '0000' and the password 'admin' is entered at the login menu. 
    This menu should present the following options:
        1. Add new account
        2. Remove account
        3. Change interest rate
        4. Exit
    Hint: Use of a dictionary make the implemention of these operations relatively easy. 

### Project Author ###
    David Normandin

### State of the Project ###
    Finished