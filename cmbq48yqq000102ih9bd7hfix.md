---
title: "How I Built a Simple To-Do App Using Python"
seoTitle: "Create a To-Do App with Python"
seoDescription: "Learn to build a basic to-do app using Python with key concepts and step-by-step code explanations. Perfect for beginners"
datePublished: Tue Jun 10 2025 06:04:33 GMT+0000 (Coordinated Universal Time)
cuid: cmbq48yqq000102ih9bd7hfix
slug: how-i-built-a-simple-to-do-app-using-python
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1749535089223/6e914832-ee33-4b37-975a-2b71a4aa4e88.png
ogImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749535391934/ff730ade-953d-44ae-b241-ac4b2a906b35.png
tags: programming, python, codenewbies, beginner-projects

---

### ⚙️ What You'll Learn:

* Creating a Python menu-based app
    
* Working with lists
    
* Saving data to a file
    
* Reading and updating tasks
    

---

### 🛠️ Tools Used:

* Python 3.x
    
* Any code editor (I used VS Code)
    
* Terminal / Command Prompt
    

---

### 🧩 Step-by-Step Code Explanation:

#### ✅ Step 1: Create the Main Menu

```plaintext
pythonCopyEditdef display_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
```

#### 📝 Step 2: Add & View Tasks

```plaintext
pythonCopyEdittasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
```

#### ❌ Step 3: Remove a Task

```plaintext
pythonCopyEditdef remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
```

#### 🔁 Step 4: Run the App

```plaintext
pythonCopyEditwhile True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice. Try again.")
```

---

### 💡 What I Learned:

* How to use functions to organize code
    
* How to work with lists and user input
    
* How loops and conditions help control program flow
    

---

### 🔚 Conclusion:

This was a fun and useful beginner project. If you're learning Python, try this out—it only takes 15–20 minutes, and you’ll understand so many key concepts in one go.

---

### 🔁 What’s Next?

I plan to upgrade this app by:

* Saving tasks to a file so they don't disappear
    
* Adding due dates or priorities
    
* Making a GUI using **Tkinter** or **PyQt**
    

---

### 🙌 Thanks for Reading!

If this helped you, follow me for more beginner-friendly Python tips and projects. Let’s learn and build together! 💻🐍