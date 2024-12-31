import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import heapq

class SortingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Sorting Algorithms Visualizer")
        self.root.geometry("700x600")
        self.root.configure(bg="#f7f7f7")

        self.array = []
        self.sorted_array = []
        
        # Title Label
        title = tk.Label(root, text="SORTING ALGORITHMS VISUALIZER", font=("Helvetica", 18, "bold"), bg="#0078D7", fg="white", pady=10)
        title.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.LabelFrame(root, text="Input Array Configuration", font=("Helvetica", 12), bg="#f7f7f7", bd=2)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        tk.Label(input_frame, text="Array Size:", font=("Arial", 10), bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=5)
        self.size_entry = ttk.Entry(input_frame, width=15)
        self.size_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Minimum Value:", font=("Arial", 10), bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=5)
        self.min_entry = ttk.Entry(input_frame, width=15)
        self.min_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Maximum Value:", font=("Arial", 10), bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=5)
        self.max_entry = ttk.Entry(input_frame, width=15)
        self.max_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons for Input
        ttk.Button(input_frame, text="Generate Array", command=self.generate_array).grid(row=0, column=3, padx=20)
        ttk.Button(input_frame, text="Show Array", command=self.show_array).grid(row=1, column=3, padx=20)

        # Sorting Frame
        sorting_frame = tk.LabelFrame(root, text="Sorting Algorithms", font=("Helvetica", 12), bg="#f7f7f7", bd=2)
        sorting_frame.pack(pady=20, padx=10, fill=tk.BOTH)

        # Buttons for Sorting
        ttk.Button(sorting_frame, text="Insertion Sort", command=self.insertion_sort).grid(row=0, column=0, padx=20, pady=10)
        self.insertion_time = tk.Label(sorting_frame, text="", font=("Arial", 10), bg="#f7f7f7")
        self.insertion_time.grid(row=0, column=1, padx=20)

        ttk.Button(sorting_frame, text="Heap Sort", command=self.heap_sort).grid(row=1, column=0, padx=20, pady=10)
        self.heap_time = tk.Label(sorting_frame, text="", font=("Arial", 10), bg="#f7f7f7")
        self.heap_time.grid(row=1, column=1, padx=20)

        ttk.Button(sorting_frame, text="Quick Sort", command=self.quick_sort).grid(row=2, column=0, padx=20, pady=10)
        self.quick_time = tk.Label(sorting_frame, text="", font=("Arial", 10), bg="#f7f7f7")
        self.quick_time.grid(row=2, column=1, padx=20)

        ttk.Button(sorting_frame, text="Counting Sort", command=self.counting_sort).grid(row=3, column=0, padx=20, pady=10)
        self.counting_time = tk.Label(sorting_frame, text="", font=("Arial", 10), bg="#f7f7f7")
        self.counting_time.grid(row=3, column=1, padx=20)

        # Show Sorted Array Button
        ttk.Button(root, text="Show Sorted Array", command=self.show_sorted_array).pack(pady=10)

    def generate_array(self):
        try:
            size = int(self.size_entry.get())
            min_val = int(self.min_entry.get())
            max_val = int(self.max_entry.get())
            if min_val > max_val:
                raise ValueError("Minimum value cannot be greater than Maximum value.")
            self.array = [random.randint(min_val, max_val) for _ in range(size)]
            messagebox.showinfo("Success", "Array Generated Successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def show_array(self):
        if self.array:
            messagebox.showinfo("Generated Array", f"Array: {self.array}")
        else:
            messagebox.showerror("Error", "Generate an array first!")

    def insertion_sort(self):
        arr = self.array[:]
        start_time = time.time()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        end_time = time.time()
        self.sorted_array = arr
        self.insertion_time.config(text=f"{end_time - start_time:.6f} sec")

    def heap_sort(self):
        arr = self.array[:]
        start_time = time.time()
        heapq.heapify(arr)
        self.sorted_array = [heapq.heappop(arr) for _ in range(len(arr))]
        end_time = time.time()
        self.heap_time.config(text=f"{end_time - start_time:.6f} sec")

    def quick_sort(self):
        arr = self.array[:]
        start_time = time.time()
        self.sorted_array = self.quick_sort_recursive(arr)
        end_time = time.time()
        self.quick_time.config(text=f"{end_time - start_time:.6f} sec")

    def quick_sort_recursive(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort_recursive(left) + middle + self.quick_sort_recursive(right)

    def counting_sort(self):
        arr = self.array[:]
        start_time = time.time()
        max_val = max(arr)
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        self.sorted_array = [i for i, c in enumerate(count) for _ in range(c)]
        end_time = time.time()
        self.counting_time.config(text=f"{end_time - start_time:.6f} sec")

    def show_sorted_array(self):
        if self.sorted_array:
            messagebox.showinfo("Sorted Array", f"Sorted Array: {self.sorted_array}")
        else:
            messagebox.showerror("Error", "Sort the array first!")

if __name__ == "_main_":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()