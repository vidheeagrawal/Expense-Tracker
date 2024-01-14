from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import tkinter.messagebox
from datetime import datetime

class ExpenseTracker:

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x600+300+100")
        self.root.configure(background='lightgrey')

        Category = StringVar()
        Expense = StringVar()
        Date = StringVar()

        self.expense_data = []

        def Reset():
            Category.set("")
            Expense.set("")
            Date.set("")
            self.txtFrameDetail.delete("1.0", END)

        def Exit():
            Exit = tkinter.messagebox.askyesno("Expense Tracker", "Confirm Do You Want To Exit")
            if Exit > 0:
                root.destroy()
                return

        def DisplayData():
            self.expense_data.append({
                'Category': Category.get(),
                'Expense': Expense.get(),
                'Date': Date.get()
            })
            self.txtFrameDetail.insert(END, Category.get() + "\t\t" + Expense.get() +
                                       "\t\t" + Date.get() + "\n")

        def open_calendar():
            def get_date():
                selected_date = cal.selection_get()
                Date.set(selected_date.strftime("%Y-%m-%d"))
                top.destroy()

            top = Toplevel(self.root)
            cal = Calendar(top, font="Arial 14", selectmode="day", cursor="hand1")
            cal.pack(fill="both", expand=True)
            Button(top, text="Select Date", command=get_date).pack()

        def generate_summary():
            summary_window = Toplevel(self.root)
            summary_window.title("Expense Summary")
            summary_window.geometry("400x300+500+200")

            date_label = Label(summary_window, font=('Times New Roman', 14), text="Select Date:")
            date_label.pack(pady=10)

            date_var = StringVar()
            date_entry = Entry(summary_window, font=('Times New Roman', 14), textvariable=date_var)
            date_entry.pack(pady=10)

            def get_summary():
                selected_date = date_var.get()
                total_expense = sum(float(expense['Expense']) for expense in self.expense_data if expense['Date'] == selected_date)
                summary_label.config(text=f"Total Expense on {selected_date}: Rs. {total_expense}")

            date_button = Button(summary_window, text="Generate Summary", command=get_summary, bg="darkgreen", fg="white",
                                 font=('Times New Roman', 12, 'bold'))
            date_button.pack(pady=20)

            summary_label = Label(summary_window, font=('Times New Roman', 14), text="")
            summary_label.pack(pady=10)

        # Frame
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=800, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=39, font=('Times New Roman', 20, 'bold'),
                              text="\tExpense Tracker\t", bg="lightgrey", fg='darkgreen', padx=12)
        self.lblTitle.grid()

        DataFrame = Frame(MainFrame, bd=20, width=800, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=400, height=300, padx=20, relief=RIDGE,
                                  font=('Times New Roman', 12, 'bold'), text="Expense Details:", fg="darkgreen")
        DataFrameLEFT.pack(side=LEFT)

        # Widgets
        self.lblCategory = Label(DataFrameLEFT, font=('Times New Roman', 12), text="Category:", padx=2, pady=2)
        self.lblCategory.grid(row=0, column=0, sticky=W)

        self.cboCategory = ttk.Combobox(DataFrameLEFT, state='readonly', textvariable=Category,
                                       font=('Times New Roman', 12), width=23)
        self.cboCategory['value'] = ('--select--', 'Groceries', 'Utilities', 'Rent', 'Entertainment', 'Others')
        self.cboCategory.current(0)
        self.cboCategory.grid(row=0, column=1)

        self.lblExpense = Label(DataFrameLEFT, font=('Times New Roman', 12), text="Expense:", padx=2, pady=2)
        self.lblExpense.grid(row=0, column=2, sticky=W)
        self.lblExpense = Entry(DataFrameLEFT, font=('Times New Roman', 12), textvariable=Expense, width=25)
        self.lblExpense.grid(row=0, column=3)

        self.lblDate = Label(DataFrameLEFT, font=('Times New Roman', 12), text="Date:", padx=2, pady=2)
        self.lblDate.grid(row=1, column=0, sticky=W)
        self.lblDate = Entry(DataFrameLEFT, font=('Times New Roman', 12), textvariable=Date, width=25)
        self.lblDate.grid(row=1, column=1)
        Button(DataFrameLEFT, text="Select Date", command=open_calendar).grid(row=1, column=2)

        self.txtFrameDetail = Text(DataFrameLEFT, font=('Times New Roman', 15, 'bold'), width=40, height=13, padx=8,
                                   pady=20)
        self.txtFrameDetail.grid(row=3, column=0)

        # Buttons
        self.btnDisplayData = Button(DataFrameLEFT, text="ADD EXPENSE", fg="white", bg="darkgreen",
                                     font=('Times New Roman', 12, 'bold'), width=20, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=2, column=0, pady=10)

        self.btnReset = Button(DataFrameLEFT, text="RESET", fg="white", bg="darkgreen",
                               font=('Times New Roman', 12, 'bold'), width=20, bd=4, command=Reset)
        self.btnReset.grid(row=2, column=1, pady=10)

        self.btnExit = Button(DataFrameLEFT, text="EXIT", fg="white", bg="darkgreen",
                              font=('Times New Roman', 12, 'bold'), width=20, bd=4, command=Exit)
        self.btnExit.grid(row=2, column=2, pady=10)

        self.btnSummary = Button(DataFrameLEFT, text="VIEW SUMMARY", fg="white", bg="darkgreen",
                                 font=('Times New Roman', 12, 'bold'), width=20, bd=4, command=generate_summary)
        self.btnSummary.grid(row=2, column=3, pady=10)


# Main Menu
if __name__ == '__main__':
    root = Tk()
    application = ExpenseTracker(root)
    root.mainloop()
