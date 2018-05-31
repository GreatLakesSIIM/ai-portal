from tkinter import *
from tkinter import ttk

class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title("AI PORTAL")

		tab_control = ttk.Notebook(master)
		tab1 = ttk.Frame(master)
		tab2 = ttk.Frame(master)
		tab3 = ttk.Frame(master)
		tab4 = ttk.Frame(master)
		tab5 = ttk.Frame(master)

		tab_control.add(tab1, text='Patient Demographic Criteria')
		tab_control.add(tab2, text='Radiology Diagnosis Criteria')
		tab_control.add(tab3, text='Pathology Criteria')
		tab_control.add(tab4, text='Genetics Criteria')
		tab_control.add(tab5, text='DICOM Header Criteria')
		tab_control.pack(expand=1, fill='both')
		#window.mainloop()


		self.greet_button = Button(master, text="Greetings", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()