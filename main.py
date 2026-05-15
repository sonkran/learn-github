import time

phone_number_all_user = ["0123456789", "0987654321", "0111111111"]
password_all_user = {"0123456789":"59731801", "0987654321":"35982439", "0111111111":"91232812"}


while True:
        user_choice = input("press r to register or press e to login: ").lower()
        if user_choice == "r" or user_choice == "e":
            break
        else:
            print("invalid input. Please try again.")


while user_choice == "r":
    user_register_phone_number = input("Enter your phone number for register: ")
    if not user_register_phone_number.startswith("0"):
            print("Phone number has to start with 0. Please try again.")
    elif len(user_register_phone_number) != 10:
            print("Phone number must be at least 10 character long. Please try again.")
    elif user_register_phone_number in phone_number_all_user:
        print("this phone number is already regised. Please try again")
    else:
        while True:
            user_register_password = input("Enter your password: ")
            if len(user_register_password) < 8:
                print("password must be at least 8 character long")
            else:
                print("you are registered.")
                phone_number_all_user.append(user_register_phone_number)
                password_all_user.update({user_register_phone_number:user_register_password})
                user_choice = "e"
                break
        break



while user_choice == "e":
    phone_number = input("Enter your phone number for login: ")
    if not phone_number.startswith("0"):
        print("Phone number has to start with 0. Please try again.")
        continue
    elif len(phone_number) != 10:
        print("Phone number must be 10 character long")
        continue
    elif phone_number not in phone_number_all_user:
        print("Phone number is not registered. Please try again.")
        continue
    else:
        while True:
            print(f"Phone number is {phone_number}")
            confirmation = input("press e to confirm or press q to quit: ").lower()
            if confirmation == "e":
                print("Phone number confirmed")
                break
            elif confirmation == "q":
                print("Exiting the program")
                break
            else:            
                print("Invalid input. Please try again.")
        break
limit = 0
locking_time = 60

while confirmation == "e":
    user_password = input("Enter your password: ")
    if user_password == password_all_user[phone_number]:
        print("Password is correct.")
        
        break
    else:        
        print("Incorrect password. Please try again.")
        limit += 1
        if limit == 3:
            print("too much failed attempts. locking the account.")
            for time_lock in range(locking_time, 0, -1):
                seconds = time_lock % 60
                minutes = (time_lock // 60) % 60
                hours = time_lock // 3600
                print(f"{hours:02}:{minutes:02}:{seconds:02}")
                time.sleep(1)
            user_answer_password_incorrect = input("press e to try again or press q to quit: ")
            if user_answer_password_incorrect == "e":
                print("you can try only one more times")
                limit = 2
                locking_time **= 2
                continue
            elif user_answer_password_incorrect == "q":
                print("Exiting program")
                break