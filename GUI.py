import tkinter as tk
from tkinter import filedialog

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DP Project GUI")
        self.geometry("600x400")
        self.configure(bg='black')

        # Create a button to select a file
        self.select_file_button = tk.Button(self, text="Select File", command=self.select_file)
        self.select_file_button.pack()

    def select_file(self):
        # Open a file dialog
        file_path = filedialog.askopenfilename()

        # Create a new page to display the results
        results_window = ResultsWindow(file_path)
        results_window.mainloop()

class ResultsWindow(tk.Toplevel):
    def __init__(self, file_path):
        super().__init__()
        self.title("Results")
        self.geometry("600x400")
        self.configure(bg='black')

        # Display the file path (for testing)
        self.file_path_label = tk.Label(self, text=file_path, bg='black', fg='white')
        self.file_path_label.pack()

        # TODO: Read the file and calculate the results
        # TODO: Display the results in the GUI

if __name__ == "__main__":
    app = GUI()
    app.mainloop()