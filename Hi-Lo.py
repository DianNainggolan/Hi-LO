import tkinter as tk
from tkinter import messagebox

# Konversi nilai kartu
def convert_card(card):
    card_value = {
        "A": 14, "a": 14, "ACE": 14, "Ace": 14, "ace": 14, 
        "J": 11, "j": 11, "JACK": 11, "Jack": 11, "jack": 11,
        "Q": 12, "q": 12, "QUEEN": 12, "Queen": 12, "queen": 12,
        "K": 13, "k": 13, "KING": 13, "King": 13, "king": 13
    }
    if card.isdigit():
        card = int(card)
        if card == 1:  
            return 14  # Jika input 1, ubah menjadi 14 (Ace)
        return card if 2 <= card <= 14 else None 
    return card_value.get(card, None)

# Hitung probabilitas Hi-Lo
def calculate_probability(card, deck):
    card_ = int(card)
    remaining_deck = deck[:]
    remaining_deck.remove(card_)

    higher = len([c for c in remaining_deck if c > card_]) / 51 * 100
    lower = len([c for c in remaining_deck if c < card_]) / 51 * 100
    same = len([c for c in remaining_deck if c == card_]) / 51 * 100
    
    return [higher, lower, same]

# Fungsi untuk menampilkan hasil
def calculate():
    card = entry_card.get().strip()
    card = convert_card(card)

    if card is None:
        messagebox.showerror("Error", "Invalid input! Enter a valid card (2-10, J, Q, K, A).")
        return

    probability = calculate_probability(card, deck)

    label_result.config(text=f"Probabilitas:\nLebih tinggi: {probability[0]:.2f}%\nLebih rendah: {probability[1]:.2f}%\nSama: {probability[2]:.2f}%")

# Data deck kartu
deck = [x for x in range(2, 15)] * 4

# Setup GUI
root = tk.Tk()
root.title("Hi-Lo Probability Calculator")
root.geometry("350x250")

label_instruction = tk.Label(root, text="Selamat datang di perhitungan probabilitas permainan Hi-Lo")
label_instruction.pack(pady=5)

label_instruction = tk.Label(root, text="Masukkan kartu: ")
label_instruction.pack(pady=5)

entry_card = tk.Entry(root)
entry_card.pack(pady=5)

button_calculate = tk.Button(root, text="Hitung Probabilitas", command=calculate)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="Probabilitas akan muncul di sini")
label_result.pack(pady=10)


# Jalankan aplikasi
root.mainloop()
