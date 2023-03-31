import tkinter as tk
import time 

# 메인 컬러
mc = '#5e72d8'
dk = "#252525"


# 메인 창 생성
window = tk.Tk()
window.title("To-Do List")
window.geometry("500x800")
window.configure(bg='white')


today_date = time.localtime(time.time())
today = time.strftime("%A, %d %B", today_date)

# 날짜 생성
date_box = tk.Label(window, text=today, width=25)
date_box.pack(padx=10, pady=10)
date_box.configure(fg = dk, bg = 'white')
date_box.config(font=("Arial", 20, 'bold'))

#plus 아이콘
ps_icon = tk.PhotoImage(file="img/plus.png")
ps_icon = ps_icon.subsample(2, 2)

# plus 버튼
add_box = tk.Label(window, image=ps_icon)

# 리스트 박스 생성
tasks_listbox = tk.Listbox(window, width=50)
tasks_listbox.pack(padx=10, pady=10)

# 입력하는 박스 생성
task_entry = tk.Entry(window, width=50)
task_entry.pack(padx=10, pady=5)

# 일정 생성 함수
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# 일정 추가 박스 생성
add_button = tk.Button(window, text="Add Task", command=add_task, highlightbackground=mc)
add_button.configure(bg='white')

# 일정 삭제 함수
def remove_task():
    tasks_listbox.delete(tk.ACTIVE)

# 일정 삭제 박스 생성
remove_button = tk.Button(window, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5)

# create a function to clear all tasks from the listbox
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# create a button to clear all tasks
clear_button = tk.Button(window, text="Clear Tasks", command=clear_tasks)
clear_button.pack(padx=10, pady=5)

# run the main loop
window.mainloop()
