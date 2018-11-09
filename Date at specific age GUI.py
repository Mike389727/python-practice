import datetime
from tkinter import *
from tkinter import ttk
"""Mike W - 
Program calculates what year it will be when you turn 100 """

class Tools(): 
     def __init__(self, current_age, future_age):
          self.current_age = current_age
          self.future_age = future_age
          self.year = 0

     def date_at_age_100(self):
          current_year = datetime.datetime.today().year
          difference_in_age = (int(self.future_age) - int(self.current_age))
          self.year = (current_year + difference_in_age)
          return self.year
     
     def __repr__(self):
          return 'error'
     
class AgeGui:
     def __init__(self, window):
          self.age_label = Label(window, text="My age is:")
          self.age_label.grid(row=0, column=0, padx=5, pady=5)
          
          self.name_label = Label(window, text="When I turn:")
          self.name_label.grid(row=1, column=0, padx=5, pady=5)  
          
          self.year_label = Label(window, text="The Year will be:")
          self.year_label.grid(row=2, column=0, padx=5, pady=5)   
          
          self.current_age_entry = Entry(window, width=12)
          self.current_age_entry.grid(row=0, column=1, padx=5)
          
          self.future_age = Entry(window, width=12)
          self.future_age.grid(row=1, column=1, padx=5) 
          
          self.button = Button(window, text='Submit', command=self.checkage)
          self.button.grid(row=0, column=2, padx=3)
          
          self.message_label = Label(window, text='')
          self.message_label.grid(row=5, column=0, columnspan=3, pady=10)
          
          window.mainloop()
     
     def checkage(self):
          future_age = self.future_age.get()
          current_age =  self.current_age_entry.get()
          data = Tools(current_age, future_age)
          data.date_at_age_100()
          self.message_label['text'] = data.year
                    
def main():
     window = Tk()
     gui = AgeGui(window)
     window.mainloop()
main()
     