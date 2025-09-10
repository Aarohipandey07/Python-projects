dict={}

#adding the contact
def add_contact(name,number):
    dict[name]=number
    print(f"add {name} with {number} successfully")

#updating the contact
def update_contact(name,number):
    if name in dict:
     dict[name]=number
     print(f"update {name} with {number} successfully")
    else:
         print(f"{name} not available")

#deleting the contact
def delete_contact(name,number):
    if name in dict:
     dict[name]=number
     print(f"delete {name} with {number} successfully")
    else:
     print(f"{name} not available")

#display the contact
def display_contact(name):
    if name in dict:

     print(f"display {name} with  successfully")
    else:
     print(f"{name} not available")

def main():
      while True:
           print("1.add")
           print("2.update")
           print("3.delete")
           print("4.display")
           print("5.exit")
           choice=int(input("enter your choice 1-5: "))
           if choice==1:
            name=input("enter name: ")
            number=int(input("enter number: "))
            add_contact(name, number)
           elif choice==2:
            name = input("enter name: ")
            number = int(input("enter number: "))
            update_contact(name,number)
           elif choice==3:
            name = input("enter name: ")
            number = int(input("enter number: "))
            delete_contact(name,number)
           elif choice==4:
            name = input("enter name: ")

            display_contact(name)
           elif choice==5:
               print("exit")

               break
           else:
             print("not available")

if __name__=="__main__":
    main()





