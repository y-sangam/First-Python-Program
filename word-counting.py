print("THIS IS A PROGRAM TO COUNT THE NUMBERS IN THE PARAGRAPH")
paragraph = input("Enter your paragraph: ")
lenthOfWord= len(paragraph)
print("Your paragraph has ",lenthOfWord," number")
user_gives_a_number= int(input("Please Enter the number of word that you  wanna print: "))
attempt = 0
while user_gives_a_number>lenthOfWord:
    attempt += 1
    if attempt==3:
        print("OH! Maximum attempt exeeded :(")
        exit()
    else:
        print("the number you gave is out of range pleasee chose beetween 1 to ", lenthOfWord,":(  ")
        user_gives_a_number=int(input("Please enter the correct number: "))
print("The letter on number ", user_gives_a_number," is ",paragraph[user_gives_a_number-1])
print("It Took You ",attempt," attempts. :)")
while True:
    print("THIS IS A PROGRAM TO COUNT THE NUMBERS IN THE PARAGRAPH")
    paragraph = input("If you wanna countiniue the game type your para/word or type Exit:  ")
    if paragraph =="exit":
        print("Thanks For Playing. BYE :)")
        exit()
    if paragraph=="EXIT":
        print("Thanks For Playing. BYE :)")
        exit()
    if paragraph=="Exit":
        print("Thanks For Playing. BYE :)")
        exit()
    else:
        lenthOfWord= len(paragraph)
        print("Your paragraph has ",lenthOfWord," number")
        user_gives_a_number= int(input("Please Enter the number of word that you  wanna print: "))
        attempt = 0
        while user_gives_a_number>lenthOfWord:
            attempt += 1
            if attempt==3:
                print("OH! Maximum attempt exeeded :(")
                exit()
            else:
                print("the number you gave is out of range pleasee chose beetween 1 to ", lenthOfWord,":(  ")
                user_gives_a_number=int(input("Please enter the correct number: "))
        print("The letter on number ", user_gives_a_number," is ",paragraph[user_gives_a_number-1])
        print("It Took You ",attempt," attempts. :)")