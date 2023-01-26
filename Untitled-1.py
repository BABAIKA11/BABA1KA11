KolvoOperacii = int(input(f"Введите количество операций: "))
i = 0
MainNumber = 0
Number1 = int(input(f"Введите цифру: "))
Operator = input(f"Введите действие: ")
Number2 = int(input(f"Введите цифру: "))
if Operator == "+" or Operator == "Сложение":
    print(Number1,"+", Number2, " = ",Number1 + Number2)
    MainNumber = Number1 + Number2
elif Operator == "-" or Operator == "Вычетание": 
    print(Number1,"-", Number2," = ",Number1 - Number2)
    MainNumber = Number1 - Number2
elif Operator == "*" or Operator == "Умножение": 
    print(Number1,"*", Number2," = ",Number1 * Number2)
    MainNumber = Number1 * Number2
elif (Operator == "/" or Operator == "Деление") and Number2 != 0: 
    print(Number1,"/", Number2," = ",Number1 / Number2)
    MainNumber = Number1 / Number2
else:
    print("Совсем дурачок чтоли введите то что просят!(А также на 0 делить нельзя!!!!)")
while i < KolvoOperacii-1:
   i+=1
   Operator = input(f"Введите действие: ")
   Number = int(input(f"Введите цифру: "))
   if Operator == "+" or Operator == "Сложение":
       print(MainNumber,"+", Number, " = ",MainNumber + Number)
       MainNumber = MainNumber + Number
   elif Operator == "-" or Operator == "Вычетание": 
       print(MainNumber,"-", Number," = ",MainNumber - Number)
       MainNumber = MainNumber - Number
   elif Operator == "*" or Operator == "Умножение": 
       print(MainNumber,"*", Number," = ",MainNumber * Number)
       MainNumber = MainNumber * Number
   elif Operator == "/" or Operator == "Деление" and Number2 != 0: 
       print(MainNumber,"/", Number," = ",MainNumber / Number)
       MainNumber = MainNumber / Number
   else:
       print("Совсем дурачок чтоли введите то что просят!(А также на 0 делить нельзя!!!!)")