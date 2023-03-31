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

# 서브(일정 생성) 창 생성
sub = tk.Tk()
sub.title("To-Do List")
sub.geometry("500x800")
sub.configure(bg='white')


today_date = time.localtime(time.time())
today = time.strftime("%A, %d %B", today_date)

header_frame = tk.Frame(window, bg="white")
header_frame.pack(padx=10, pady=10, fill=tk.X)

# 날짜 생성
date_box = tk.Label(header_frame, text=today)
date_box.pack(padx=(10, 50), pady=10, side=tk.LEFT)
date_box.configure(fg = dk, bg = 'white')
date_box.config(font=("Arial", 24, 'normal', 'bold'))

#plus 아이콘 (상대 경로)
ps_icon = tk.PhotoImage(file="/Users/joosungjun/Documents/Dev/2023-python-class/ToDoList/img/plus.png")

def aaa () :
    print("test")
    
# plus 버튼
add_box = tk.Label(header_frame, image=ps_icon, bg="white")
add_box.pack(side=tk.RIGHT, padx=(10, 20), pady=10)
add_box.bind("<Button-1>", lambda event: aaa())
add_box.configure(cursor='hand2')




# 리스트 박스 생성
tasks_listbox = tk.Listbox(window, width=50, height=200)
tasks_listbox.pack(padx=10, pady=10)
tasks_listbox.configure(bg='white', fg='#252525', highlightthickness=0, font=('Arial', 22))

# 입력하는 박스 생성
task_entry = tk.Entry(sub, width=50)
task_entry.pack(padx=10, pady=5)
task_entry.configure(bg='white', fg='#252525')

# 일정 생성 함수
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# 일정 추가 박스 생성
add_button = tk.Button(sub, text="추가하기", command=add_task, highlightbackground='white', width=10, height=2)
add_button.pack(padx=10, pady=5)

# 일정 삭제 함수
def remove_task():
    tasks_listbox.delete(tk.ACTIVE)

# 일정 삭제 박스 생성
remove_button = tk.Button(sub, text="Remove Task", command=remove_task, highlightbackground='white', width=10, height=2)
remove_button.pack(padx=10, pady=5)

# 전체 일정 삭제
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# 전체 일정 삭제 버튼 생성
clear_button = tk.Button(sub, text="모두 지우기", command=clear_tasks, highlightbackground='white', width=10, height=2)
clear_button.pack(padx=10, pady=5)



# window 창 열기
window.mainloop()
