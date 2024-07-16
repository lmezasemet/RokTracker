import tkinter
from tkinter import filedialog
import tkinter.messagebox
import customtkinter

    
class MyFileBrowserFrame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.file_path1 = None
        self.file_path2 = None

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.file_path_label1 = customtkinter.CTkLabel(self, text="No file selected", fg_color="gray30")
        self.file_path_label1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.browse_button = customtkinter.CTkButton(self, text="Browse", command=self.browse_button_callback1)
        self.browse_button.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")
        
        self.file_path_label2 = customtkinter.CTkLabel(self, text="No file selected", fg_color="gray30")
        self.file_path_label2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.browse_button = customtkinter.CTkButton(self, text="Browse", command=self.browse_button_callback2)
        self.browse_button.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="ew")

    def browse_button_callback1(self):
        self.file_path1 = filedialog.askopenfilename()
        self.file_path_label1.configure(text=self.file_path1)
        self.file_path_label1.update_idletasks()
    
    def browse_button_callback2(self):
        self.file_path2 = filedialog.askopenfilename()
        self.file_path_label2.configure(text=self.file_path2)
        self.file_path_label2.update_idletasks()
        
    def get(self):
        if(self.file_path1 == None):
            tkinter.messagebox.showinfo("Error", "Please select the first file")
            return None
        elif(self.file_path2 == None):
            tkinter.messagebox.showinfo("Error", "Please select the second file")
            return None
        else:
            return self.file_path1, self.file_path2
        
class MyCustomDKPFormula(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        
        self.t4 = 3
        self.t5 = 6
        self.t4deads = 18
        self.t5deads = 32
        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        # Create 4 inputs for the DKP formula (T4, T5, T4 Deads, T5 Deads)
        
        self.t4_label = customtkinter.CTkLabel(self, text="T4")
        self.t4_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.t4_input = customtkinter.CTkEntry(self, textvariable=tkinter.StringVar(value=str(self.t4)))
        self.t4_input.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew")
        
        self.t5_label = customtkinter.CTkLabel(self, text="T5")
        self.t5_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.t5_input = customtkinter.CTkEntry(self, textvariable=tkinter.StringVar(value=str(self.t5)))
        self.t5_input.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="ew")
        
        self.t4deads_label = customtkinter.CTkLabel(self, text="T4 Deads")
        self.t4deads_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.t4deads_input = customtkinter.CTkEntry(self, textvariable=tkinter.StringVar(value=str(self.t4deads)))
        self.t4deads_input.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="ew")
        
        self.t5deads_label = customtkinter.CTkLabel(self, text="T5 Deads")
        self.t5deads_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.t5deads_input = customtkinter.CTkEntry(self, textvariable=tkinter.StringVar(value=str(self.t5deads)))
        self.t5deads_input.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="ew")
        
        
    def get(self):
        t4 = self.t4_input.get()
        t5 = self.t5_input.get()
        t4deads = self.t4deads_input.get()
        t5deads = self.t5deads_input.get()
        
        if(t4 == "" or t5 == "" or t4deads == "" or t5deads == ""):
            tkinter.messagebox.showinfo("Error", "Please fill all the fields")
            return (), (), (), ()
        else:
            return t4, t5, t4deads, t5deads
        
class MyCustomDKPFileName(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        self.dkfile_name = customtkinter.CTkEntry(self, textvariable=tkinter.StringVar(value="DKP"))
        self.dkfile_name.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        
    def get(self):
        return self.dkfile_name.get()
        
    

    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=3)
        
        self.file_browser_frame = MyFileBrowserFrame(self, "Files")
        self.file_browser_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        self.dkp_formula_frame = MyCustomDKPFormula(self, "DKP Formula")
        self.dkp_formula_frame.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        self.dkfile_name = MyCustomDKPFileName(self, "DKP File Name")
        self.dkfile_name.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="nsew")
        

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=9, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
    def button_callback(self):
        file_paths = self.file_browser_frame.get()
        t4, t5, t4deads, t5deads = self.dkp_formula_frame.get()
        if(file_paths == None or t4 == () or t5 == () or t4deads == () or t5deads == ()):
            print("Error")
            return
        else:
            print(file_paths)
            print(t4)
            print(t5)
            print(t4deads)
            print(t5deads)
            
        
        
            return
    
    def save_button_callback(self):
        #save the DKP file
        self.dkfile_name.get()
        print(self.dkfile_name.get())
        
   


app = App()
app.mainloop()

