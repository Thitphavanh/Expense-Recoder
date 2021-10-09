# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime
# ttk is theme of Tk

GUI = Tk()
GUI.title('ໂປຣແກຣມບັນທຶກຄ່າໃຊ້ຈ່າຍ version.1.0 by Hery')
GUI.geometry('600x700+500+0')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) # .pack ຕິດປຸ່ມເຂົ້າກັບ GUI  ຫຼັກ

#--------------------MUNU--------------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='file',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')
# Help
def About():
	print(menu=menubar)
	messagebox.showinfo('About','ສະບາຍດີ ໂປຣແກຣມນີ້ແມ່ນໂປຣແກຣມບັນທຶກຂໍ້ມູນ\nສົນໃຈບໍລິຈາກເຮົາບໍ? ຂໍ 1 BTCພໍແລ້ວ\nBTC Address: abc')



helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_cascade(label='About',command=About)

# Donate
def Donate():
	messagebox.showinfo('Donate','BTC Address:')
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_cascade(label='Donate',command=Donate)



#----------------------------------------


Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1) # expand ເອົາໄວ້ຂະຫຍາຍ ໃຊ້ຄູ່ກັບ fill

icon_t1 = PhotoImage(file='t1_expense.png') # .subsample(2) = ຍໍ້ຮູບ
icon_t2 = PhotoImage(file='t2_expenselist.png')


Tab.add(T1,text=f'{"ເພີ່ມຄ່າໃຊ້ຈ່າຍ":^{30}}',image=icon_t1,compound='top')
Tab.add(T2,text=f'{"ຄ່າໃຊ້ຈ່າຍທັງໝົດ":^{30}}',image=icon_t2,compound='top')



F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'ຈັນ',
		'Tue':'ຄານ',
		'Wed':'ພຸດ',
		'Thu':'ພະຫັດ',
		'Fri':'ສຸກ',
		'Sat':'ເສົາ',
		'Sun':'ອາທິດ'}

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	quantity = v_quantity.get()

	if expense == '':
		print('No Data')
		messagebox.showerror('Error','ກະລຸນາໃສ່ຂໍ້ມູນຄ່າໃຊ້ຈ່າຍ')
		return
	elif price == '':
		messagebox.showerror('Error','ກະລຸນາໃສ່ລາຄາ')
		return
	elif quantity == '':
		messagebox.showerror('Error','ກະລຸນາໃສ່ຈຳນວນ')
		return


	total = float(price) * float(quantity)
	try:
		total = float(price) * float(quantity)
		# .get ດຶງຄ່າມາຈາກ v_expense = StringVar()
		print('ລາຍການ: {} ລາຄາ: {}'.format(expense,price))
		print('ຈຳນວນ: {} ລວມທັງໝົດ: {} ກີບ'.format(quantity,total)) 
		text = 'ລາຍການ: {} ລາຄາ: {}\n'.format(expense,price)
		text = text + 'ຈຳນວນ: {} ລວມທັງໝົດ: {} ກີບ'.format(quantity,total)
		v_result.set(text)
		# clear ຂໍ້ມູນເກົ່າ
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')

		# ບັນທຶກຂໍ້ມູນລົງ csv ຢ່າລືມ import csv ນຳ
		today = datetime.now().strftime('%a') # day['Mon'] = 'ຈັນ'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
			# with ແມ່ນສັ່ງເປີດ file ແລ້ວປິດອັດຕະໂນມັດ
			# 'a' ການບັນທຶກເລື່ອຍໆ ເພີ່ມຂໍ້ມູນຈາກຂໍ້ມູນເກົ່າ
			# newline='' ເຮັດໃຫ້ຂໍ້ມູນບໍ່ມີບັນທັດວ່າງ
			fw = csv.writer(f) # ສ້າງ function ສຳລັບຂຽນຂໍ້ມູນ
			data = [dt,expense,price,quantity,total]
			fw.writerow(data)
			  
		# ເຮັດໃຫ້ເຄີຣເຊີຣ໌ກັບໄປຕຳແໜ່ງບ່ອນໃສ່ E1
		E1.focus()
		update_table()
	except Exception as e:

		print('ERROR:',e)
		messagebox.showerror('Error','ກະລຸນາໃສ່ຂໍ້ມູນໃໝ່ ເຈົ້າໃສ່ຂໍ້ມູນຜິດ')
		v_expense.set('')
		v_price.set('')
		v_quantity.set('')
		#messagebox.showwarning('Error','ກະລຸນາໃສ່ຂໍ້ມູນໃໝ່ ເຈົ້າໃສ່ຂໍ້ມູນຜິດ')
		#messagebox.showinfo('Error','ກະລຸນາໃສ່ຂໍ້ມູນໃໝ່ ເຈົ້າໃສ່ຂໍ້ມູນຜິດ')


		  
#  ເຮັດໃຫ້ສາມາດກົດ enter ໄດ້ 
GUI.bind('<Return>',Save) # ຕ້ອງເພີ່ມໃນ def Save(event=None)

FONT1 = (None,20) # None ປ່ຽນເປັນ 'Phetsarath'

#-------------image----------------

main_icon = PhotoImage(file='icon_money.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()



#----------------text1-------------------
L = ttk.Label(F1,text='ລາຍການຄ່າໃຊ້ຈ່າຍ',font=FONT1).pack()
v_expense = StringVar()
# StringVar() ແມ່ນ ໂຕແປພິເສດສຳຫຼັບເກັບຂໍ້ມູນໃນ GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#----------------------------------------------

#----------------text2-------------------
L = ttk.Label(F1,text='ລາຄາ (ກີບ)',font=FONT1).pack()
v_price = StringVar()
# StringVar() ແມ່ນ ໂຕແປພິເສດສຳຫຼັບເກັບຂໍ້ມູນໃນ GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#----------------------------------------------

#----------------text3-------------------
L = ttk.Label(F1,text='ຈຳນວນ (ອັນ)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() ແມ່ນ ໂຕແປພິເສດສຳຫຼັບເກັບຂໍ້ມູນໃນ GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#----------------------------------------------

icon_b1 = PhotoImage(file='b_save.png')


B2 = ttk.Button(F1,text=f'{"Save": ^{10}}',image=icon_b1,compound='top',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('-------------ຜົນຮັບ-------------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='black')
result.pack(pady=20)

#-----------------TAB2------------------------

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data
		# print(data)
		# print('-----')
		# print(data[0][0])
		# for a,b,c,d,e in data:
		# 	print(e)

# table
L = ttk.Label(T2,text='ຕາຕະລາງສະແດງຜົນລັບທັງໝົດ',font=FONT1).pack(pady=20)

header = ['ວັນ-ເວລາ','ລາຍການ','ຄ່າໃຊ້ຈ່າຍ','ຈຳນວນ', 'ລວມ']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=15)
resulttable.pack()

# for i in range(len(header)):
# 	resulttable.heading(header[i],text=header[i])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [150,170,80,80,80]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w) 

# resulttable.insert('',0,value=['ຈັນ','ນ້ຳດື່ມ',5000,5,25000])
# resulttable.insert('','end',value=['ຄານ','ນ້ຳດື່ມ',5000,5,25000])


def update_table():
	resulttable.delete(*resulttable.get_children())
	# for c in resulttable.get_children():
	# 	resulttable.delete(c)
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_table()
print('GET CHILD:',resulttable.get_children())
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
