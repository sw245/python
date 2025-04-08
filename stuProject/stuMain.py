
from stuModule import *
from stuFunc import *





while True:
    choice = tmenu_print()
    
    if choice == 1:
        stu_input()
        
    elif choice == 2:
        stu_print()
      
    elif choice == 3:
        stu_modify()
        
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break






# print("-"*60)