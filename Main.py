import random

possibleWorker = ["Panav Kotha" , "Abhi Sharma" , "Satvik Thati"]
personalInfo = []
customerInfo = {"Kana Zhao" : {"Phone Number" : "+18327679652" , "Email" : "kana@sadbuja.com"}  ,
                "Bhavik Thati" : {"Phone Number" : "+14256149884" , "Email" : "bhavikthati@gmail.com"} ,
                "Faiza Imran" : {"Phone Number" : "+914255536233" , "Email" : "faizaisawesome12@gmail.com"}}
i = 0
possibleWorkerIndex = 0

customerCareWorkerNumber = random.randrange(0 , len(possibleWorker) - 1)
customerCareWorker = None

while i < len(possibleWorker):
    if customerCareWorkerNumber == i:
        customerCareWorker = possibleWorker[possibleWorkerIndex]
    else:
        i += 1
        possibleWorkerIndex += 1

print("""Hi, this is {0} from Amazon's Customer Care.
         like to start off with getting your name, phone number and email before we can continue.""".format(customerCareWorker))
name = input("Name: ")
phoneNumber = input("Phone Number: ")
email = input("Email: ")

if name and phoneNumber and email in customerInfo and phoneNumber.startswith("+1"):
    input("""Thanks for waiting.
             Why have you called Amazon's Care today?""")
elif name and phoneNumber and email in customerInfo and not phoneNumber.startswith("+1"):
    print("""I believe you called the wrong Customer Care.
             Please check Amazon website to see what number to dial in depending on which country you live in.""")
else:
    print("""Please make sure your info is right.
             I do not see as a current customer at Amazon.
             Then enter your name, phone number and email which you believe is right down below.""")
    name = input("Name: ")
    phoneNumber = input("Phone Number: ")
    email = input("Email: ")
