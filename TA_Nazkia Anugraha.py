import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage

# Daftar makanan Nusantara berdasarkan pulau
makanan_nusantara = {
    "Pulau Sumatra": [
        {
            "nama": "Rendang",
            "deskripsi": "Masakan daging dari Padang yang dimasak dengan rempah-rempah. Rasanya pedas dan gurih.",
            "resep": """
            Bahan-bahan:
            - 500 gram daging sapi, potong dadu
            - 400 ml santan kelapa
            - 2 batang serai, memarkan
            - 3 lembar daun jeruk
            - 1 lembar daun salam
            - 3 sdm minyak goreng
            - 1 sdt garam
            - 1 sdt gula merah
            - 2 sdt cabai merah (sesuai selera)

            Bumbu halus:
            - 8 butir bawang merah
            - 4 siung bawang putih
            - 2 cm jahe
            - 2 cm lengkuas
            - 1 buah cabai merah besar
            - 1 sdt ketumbar

            Cara memasak:
            1. Tumis bumbu halus, serai, daun jeruk, dan daun salam hingga harum.
            2. Masukkan daging sapi, aduk rata.
            3. Tuang santan, garam, gula merah, dan cabai. Masak hingga daging empuk dan kuah mengental.
            4. Sajikan rendang dengan nasi putih hangat.
            """
        }
    ],
    "Pulau Jawa": [
        {
            "nama": "Nasi Goreng Jawa",
            "deskripsi": "Nasi yang digoreng dengan bumbu khas Indonesia. Sering disajikan dengan telur, ayam, atau udang.",
            "resep": """
            Bahan-bahan:
            - 2 piring nasi putih
            - 2 siung bawang putih, cincang halus
            - 1 butir telur, kocok lepas
            - 2 sdm kecap manis
            - 1 sdm saus tiram
            - 1 sdm minyak goreng
            - 1/2 sdt garam
            - 1/2 sdt merica
            - 2 sdm daun bawang, iris halus
            - Ayam/udang/tempe (opsional)

            Cara memasak:
            1. Panaskan minyak dalam wajan, tumis bawang putih hingga harum.
            2. Masukkan telur, orak-arik hingga matang.
            3. Tambahkan nasi putih, aduk rata.
            4. Masukkan kecap manis, saus tiram, garam, dan merica. Aduk rata.
            5. Sajikan dengan tambahan ayam/udang dan taburan daun bawang.
            """
        }
    ],
    "Pulau Kalimantan": [
        {
            "nama": "Sate Payau",
            "deskripsi": "Sate khas Kalimantan yang menggunakan daging rusa atau daging satwa hutan lainnya yang dipanggang dengan bumbu rempah.",
            "resep": """
            Bahan-bahan:
            - 500 gram daging rusa (atau daging sapi) potong dadu
            - 10 tusuk sate bambu, rendam dalam air
            - 3 sdm kecap manis
            - 1 sdt air jeruk nipis
            - 1 sdm minyak goreng

            Bumbu kacang:
            - 100 gram kacang tanah, sangrai
            - 2 siung bawang putih
            - 1 sdt cabai merah (sesuai selera)
            - 1 sdm kecap manis
            - 1/2 sdt garam
            - 1/2 sdt gula merah

            Cara memasak:
            1. Marinasi daging dengan kecap manis, minyak goreng, dan air jeruk nipis selama 30 menit.
            2. Tusuk daging pada tusuk sate.
            3. Panggang sate di atas bara api hingga matang, olesi dengan sisa bumbu.
            4. Haluskan semua bahan bumbu kacang, beri air sedikit agar lebih cair.
            5. Sajikan sate dengan bumbu kacang.
            """
        }
    ],
    "Pulau Papua": [
        {
            "nama": "Papeda",
            "deskripsi": "Makanan khas Papua yang terbuat dari sagu dan disajikan dengan kuah ikan kunir.",
            "resep": """
            Bahan-bahan:
            - 200 gram tepung sagu
            - 800 ml air
            - 1 sdt garam

            Kuah Ikan:
            - 500 gram ikan tongkol atau ikan laut lainnya
            - 2 batang serai, memarkan
            - 3 lembar daun jeruk
            - 1 cm kunyit, haluskan
            - 3 siung bawang merah
            - 2 siung bawang putih
            - 1 sdt garam
            - 1 sdt gula merah

            Cara memasak:
            1. Masak air dalam panci, tambahkan garam.
            2. Tambahkan tepung sagu sedikit-sedikit, aduk hingga kental dan berbentuk gel.
            3. Untuk kuah, rebus ikan dengan daun jeruk, serai, dan bumbu lainnya hingga matang.
            4. Sajikan papeda dengan kuah ikan.
            """
        }
    ],
    "Pulau Sulawesi": [
        {
            "nama": "Coto Makassar",
            "deskripsi": "Sup daging khas Makassar yang kaya rempah dan gurih, biasanya disajikan dengan ketupat.",
            "resep": """
            Bahan-bahan:
            - 500 gram daging sapi (daging dan jeroan)
            - 2 batang serai, memarkan
            - 4 lembar daun salam
            - 3 siung bawang putih
            - 5 butir bawang merah
            - 2 cm jahe
            - 1 sdt ketumbar
            - 1 sdt jintan
            - 1 sdt merica
            - 1 liter air kaldu

            Cara memasak:
            1. Rebus daging dan jeroan dalam air kaldu hingga empuk.
            2. Haluskan bawang putih, bawang merah, jahe, ketumbar, jintan, dan merica.
            3. Tumis bumbu halus hingga harum, lalu masukkan ke dalam rebusan daging.
            4. Masak hingga kuah mendidih dan bumbu meresap.
            5. Sajikan coto dengan ketupat dan taburan bawang goreng.
            """
        }
    ]
}

class AppMakananNusantara:
    def __init__(self, root):
        self.root = root
        self.root.title("Taste of Indonesia")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        self.current_frame = None
        self.show_main_menu()

    def clear_window(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root, bg="#DEB887")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_main_menu(self):
        self.clear_window()

        canvas = tk.Canvas(self.current_frame, width=500, height=500)
        canvas.pack(fill=tk.BOTH, expand=True)

        try:
            bg_image = PhotoImage(file="indonesia.png")
            canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
            self.bg_image = bg_image
        except tk.TclError:
            print("Gambar tidak ditemukan!")

        header_label = tk.Label(self.current_frame, text="Flavour of Nusantara", 
                              font=("Helvetica", 16, "bold"), fg="#2F4F4F", bg="#f0f0f0")
        header_label.update_idletasks()
        header_width = header_label.winfo_reqwidth()
        window_width = self.root.winfo_width()
        header_label.place(x=(window_width - header_width) // 2, y=20)

        pulau_list = ["Pulau Sumatra", "Pulau Jawa", "Pulau Kalimantan", "Pulau Papua", "Pulau Sulawesi"]
        for i, pulau in enumerate(pulau_list):
            tombol = tk.Button(self.current_frame, text=pulau, width=25, height=2,
                             bg="#FDF5E6", fg="black",
                             command=lambda p=pulau: self.tampilkan_resep_pulau(p))
            tombol.place(x=(self.root.winfo_width() - tombol.winfo_reqwidth()) // 2,
                        y=100 + i * 50)

    def tampilkan_resep_pulau(self, pulau):
        self.clear_window()

        header_label = tk.Label(self.current_frame, text=f"Resep Makanan {pulau}",
                              font=("Helvetica", 16, "bold"), fg="white", bg="#DEB887")
        header_label.pack(pady=20)

        frame_resep = tk.Frame(self.current_frame, bg="#f0f0f0")
        frame_resep.pack(fill=tk.BOTH, expand=True, pady=20)

        if pulau in makanan_nusantara:
            for makanan in makanan_nusantara[pulau]:
                tombol = tk.Button(frame_resep, text=makanan["nama"], width=25, height=3,
                                 bg="#68C9A7", fg="black",
                                 command=lambda m=makanan: self.tampilkan_detail_makanan(m, pulau))
                tombol.pack(pady=15)

        tambah_button = tk.Button(frame_resep, text="Tambah Resep Baru", width=25, height=2,
                                bg="#FF9A8B", fg="black",
                                command=lambda: self.tambah_resep(pulau))
        tambah_button.pack(pady=10)

        back_button = tk.Button(self.current_frame, text="Kembali ke Menu Utama",
                              width=25, height=2, bg="#F7A6B8", fg="white",
                              command=self.show_main_menu)
        back_button.pack(pady=10)

    def tampilkan_detail_makanan(self, makanan, pulau):
        self.clear_window()

        header_label = tk.Label(self.current_frame, text=makanan["nama"],
                              font=("Helvetica", 16, "bold"), fg="#2F4F4F", bg="#68C9A7")
        header_label.pack(pady=20)

        desc_label = tk.Label(self.current_frame, text=makanan["deskripsi"],
                            wraplength=350, fg="#2F4F4F", bg="#FF9A8B")
        desc_label.pack(pady=20)

        text_frame = tk.Frame(self.current_frame, bg="#F7A6B8")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(text_frame, height=10, yscrollcommand=scrollbar.set,
                            wrap=tk.WORD, bg="#ffffff", fg="#2F4F4F")
        text_widget.insert(tk.END, makanan["resep"])
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_widget.config(state=tk.DISABLED)

        scrollbar.config(command=text_widget.yview)

        back_button = tk.Button(self.current_frame, text="Kembali ke Daftar Makanan",
                              bg="#F5FFFA", fg="black",
                              command=lambda: self.tampilkan_resep_pulau(pulau))
        back_button.pack(pady=20)

        delete_button = tk.Button(self.current_frame, text="Hapus Resep",
                                width=25, height=2, bg="#FFE4E1", fg="black",
                                command=lambda: self.hapus_resep(pulau, makanan))
        delete_button.pack(pady=10)

    def hapus_resep(self, pulau, makanan):
        confirm = messagebox.askyesno("Konfirmasi",
                                    f"Apakah Anda yakin ingin menghapus resep {makanan['nama']}?")
        if confirm:
            makanan_nusantara[pulau] = [m for m in makanan_nusantara[pulau]
                                       if m["nama"] != makanan["nama"]]
            messagebox.showinfo("Sukses", f"Resep {makanan['nama']} berhasil dihapus.")
            self.tampilkan_resep_pulau(pulau)

    def tambah_resep(self, pulau):
        
        tambah_window = tk.Toplevel(self.root)
        tambah_window.title("Tambah Resep Baru")
        tambah_window.geometry("400x600")
        tambah_window.configure(bg="#f0f0f0")

        tk.Label(tambah_window, text="Nama Makanan:", bg="#f0f0f0", font=("Helvetica", 10, "bold")).pack(pady=5)
        nama_entry = tk.Entry(tambah_window, width=40)
        nama_entry.pack(pady=5)

        tk.Label(tambah_window, text="Deskripsi Makanan:", bg="#f0f0f0", font=("Helvetica", 10, "bold")).pack(pady=5)
        deskripsi_entry = tk.Entry(tambah_window, width=40)
        deskripsi_entry.pack(pady=5)

        tk.Label(tambah_window, text="Resep Makanan:", bg="#f0f0f0", font=("Helvetica", 10, "bold")).pack(pady=5)
        resep_text = tk.Text(tambah_window, width=40, height=15)
        resep_text.pack(pady=10)

        def simpan_resep():
            nama = nama_entry.get()
            deskripsi = deskripsi_entry.get()
            resep = resep_text.get("1.0", tk.END).strip()

            if not nama or not deskripsi or not resep:
                messagebox.showerror("Error", "Semua kolom harus diisi!")
                return
                
            makanan_baru = {"nama": nama, "deskripsi": deskripsi, "resep": resep}
            makanan_nusantara[pulau].append(makanan_baru)

            messagebox.showinfo("Sukses", "Resep baru berhasil ditambahkan!")
            tambah_window.destroy()
            self.tampilkan_resep_pulau(pulau)

        submit_button = tk.Button(tambah_window, text="Simpan Resep", 
                                command=simpan_resep,
                                bg="#68C9A7", fg="black",
                                width=20, height=2)
        submit_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMakananNusantara(root)
    root.mainloop()