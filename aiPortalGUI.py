from tkinter import *
from tkinter import ttk

class MyFirstGUI:

	def __init__(self, master):
		self.master = master
		master.title("AI PORTAL")

		tab_control = ttk.Notebook(master)
		tabPatient = ttk.Frame(master)
		tabRadiology = ttk.Frame(master)
		tabPathology = ttk.Frame(master)
		tabGenetics = ttk.Frame(master)
		tabDICOM = ttk.Frame(master)

		tab_control.add(tabPatient, text='Patient Demographic Criteria')
		tab_control.add(tabRadiology, text='Radiology Diagnosis Criteria')
		tab_control.add(tabPathology, text='Pathology Criteria')
		tab_control.add(tabGenetics, text='Genetics Criteria')
		tab_control.add(tabDICOM, text='DICOM Header Criteria')
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