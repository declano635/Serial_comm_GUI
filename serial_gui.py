import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import serial
import serial.tools.list_ports
import threading

# Default serial settings
SERIAL_PORT = "/dev/ttys022"  # Change if needed
BAUD_RATE = 9600

class SerialMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Serial Monitor")
        self.root.geometry("600x400")

        # Serial connection
        self.serial_port = None
        self.stop_thread = False

        # UI Elements
        self.port_label = ttk.Label(root, text="Port:")
        self.port_label.grid(row=0, column=0, padx=5, pady=5)
        self.port_combobox = ttk.Combobox(root, values=self.get_serial_ports())
        self.port_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.port_combobox.set(SERIAL_PORT)

        self.baud_label = ttk.Label(root, text="Baud Rate:")
        self.baud_label.grid(row=0, column=2, padx=5, pady=5)
        self.baud_combobox = ttk.Combobox(root, values=["9600", "115200", "57600", "38400"])
        self.baud_combobox.current(0)
        self.baud_combobox.grid(row=0, column=3, padx=5, pady=5)

        self.connect_button = ttk.Button(root, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=0, column=4, padx=5, pady=5)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
        self.text_area.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

        self.input_entry = ttk.Entry(root, width=50)
        self.input_entry.grid(row=2, column=0, columnspan=4, padx=5, pady=5)
        self.send_button = ttk.Button(root, text="Send", command=self.send_data)
        self.send_button.grid(row=2, column=4, padx=5, pady=5)

        self.save_button = ttk.Button(root, text="Save Log", command=self.save_log)
        self.save_button.grid(row=3, column=0, columnspan=5, pady=5)

    def get_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect_serial(self):
        if self.serial_port:
            self.stop_thread = True
            self.serial_port.close()
            self.serial_port = None
            self.connect_button.config(text="Connect")
            self.text_area.insert(tk.END, "Disconnected.\n")
            return

        port = self.port_combobox.get()
        baud = self.baud_combobox.get()
        if not port:
            messagebox.showerror("Error", "Please select a port.")
            return

        try:
            self.serial_port = serial.Serial(port, baudrate=int(baud), timeout=1)
            self.stop_thread = False
            self.connect_button.config(text="Disconnect")
            self.text_area.insert(tk.END, f"Connected to {port} at {baud} baud.\n")
            threading.Thread(target=self.read_serial, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def read_serial(self):
        while not self.stop_thread and self.serial_port:
            try:
                data = self.serial_port.readline().decode('utf-8').strip()
                if data:
                    self.text_area.insert(tk.END, f"RX: {data}\n")
                    self.text_area.see(tk.END)
            except:
                break

    def send_data(self):
        if self.serial_port:
            data = self.input_entry.get()
            if data:
                self.serial_port.write((data + '\n').encode('utf-8'))
                self.text_area.insert(tk.END, f"TX: {data}\n")
                self.input_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Not connected to any serial port.")

    def save_log(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Success", "Log saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialMonitor(root)
    root.mainloop()
