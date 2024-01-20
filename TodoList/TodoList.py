
class TodoList:
    
    def __init__(self):
        self.list=[]
        
    def add_item(self,item):
        self.list.append(item)
    
    def view_items(self):
        return self.list
    
    def remove_item(self, index):
        try:
            del self.list[index]
        except:
            print("index out of range")
        
if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item: ")
            todo_list.add_item(item)
        elif choice == "2":
            try:
                index = int(input("Enter the index to remove: "))
                todo_list.remove_item(index)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            except IndexError as e:
                print(e)
        elif choice == "3":
            print("Todo Items:", todo_list.view_items())
        elif choice == "4":
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        