import tkinter as tk

root = tk.Tk()

# Create a Text widget with a scrollbar
text1 = tk.Text(root)
text2 = tk.Text(root)
text1.pack(side=tk.LEFT, fill=tk.BOTH)
text2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(root, command=text1.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text1.config(yscrollcommand=scrollbar.set)

for i in range(50):
    text1.insert(tk.END, f'This is line {i}\n')
for i in range(50):
    text2.insert(tk.END, f'This is line {i}\n')
root.mainloop()