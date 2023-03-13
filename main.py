import tkinter as tk

root = tk.Tk()
root.geometry('800x500')
root.title('slixzy.center')
root.config(bg='#131313')

main_frame = tk.Frame(root, bg='#131313')

page_1 = tk.Frame(main_frame)
page_1_lb = tk.Label(page_1, text='Log in', bg='#131313', font=('Bold', 15), fg='white', bd=10)
page_1_lb.pack()
page_1_lb2 = tk.Label(page_1, text='Name:', bg='#131313', fg='white', font=('Bold', 15),)
page_1_lb2.pack()
page_1.pack(pady=50)


page_2 = tk.Frame(main_frame)
page_2_lb = tk.Label(page_2, text='Select what are you want optimized', bg='#131313', font=('Bold', 15), fg='white')
page_2_lb.pack()



main_frame.pack(fill = tk.BOTH, expand=True)

pages = [page_1, page_2]
count = 0

def move_next_page():
    global count

    if not count > len(pages) - 2:
        
        for p in pages:
            p.pack_forget()

        count += 1
        page = pages[count]
        page.pack(pady=100)

bottom_frame = tk.Frame(root)

next_btn = tk.Button(bottom_frame, text='Next', font=('Bold', 12),width=8, fg='white', bg='#1877f2', bd=0, command=move_next_page)
next_btn.pack(side=tk.LEFT, )



bottom_frame.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
