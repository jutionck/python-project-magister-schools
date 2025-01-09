import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class IMDbDashboard:
    def __init__(self):
        self.df = pd.read_csv('imdb.csv')
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_box(self, text, width=40):
        """Fungsi untuk membuat box dengan border"""
        print("+" + "-" * (width-2) + "+")
        for line in text.split('\n'):
            print("|" + line.ljust(width-2) + "|")
        print("+" + "-" * (width-2) + "+")

    def print_menu_box(self):
        """Fungsi untuk menampilkan menu dalam box"""
        menu_text = (
            "Hello,\n"
            "Selamat Datang di Dashboard IMDB\n"
            "\n"
            "> NIM  : 2311601633\n"
            "> Nama : Jution Candra Kirana\n"
            "\n"
            "M E N U\n"
            "\n"
            "[1] Genre\n"
            "[2] Color\n"
            "[3] Bahasa\n"
            "[4] Negara\n"
            "[5] Total Film\n"
            "[6] Bar Chart Rating\n"
            "[7] Resume Gross dan Duration\n"
            "[8] Query (Language dan Genre)\n"
            "\n"
            "[0] Exit"
        )
        self.print_box(menu_text, 40)

    def main_menu(self):
        while True:
            self.print_menu_box()
            choice = input("\nInput Pilihan: ")
            
            if choice == '1':
                self.show_genres()
            elif choice == '2':
                self.show_colors()
            elif choice == '3':
                self.show_languages()
            elif choice == '4':
                self.show_countries()
            elif choice == '5':
                self.show_total_movies()
            elif choice == '6':
                self.show_rating_chart()
            elif choice == '7':
                self.show_gross_duration_resume()
            elif choice == '8':
                self.query_language_genre()
            elif choice == '0':
                self.print_box("Terima kasih telah menggunakan IMDb Dashboard!")
                break
            else:
                self.print_box("Pilihan tidak valid!")
            
            input("\nTekan Enter untuk melanjutkan...")
            os.system('cls' if os.name == 'nt' else 'clear')

    def show_genres(self):
        genres = set()
        for genre_list in self.df['Genre'].str.split(','):
            if isinstance(genre_list, list):
                genres.update([g.strip() for g in genre_list])
        
        output_text = "=== Daftar Genre ===\n\n"
        for i, genre in enumerate(sorted(genres), 1):
            output_text += f"{i:2d}. {genre}\n"
        output_text += f"\nTotal Genre: {len(genres)}"
        self.print_box(output_text)

    def show_colors(self):
        colors = self.df['Color/B&W'].value_counts()
        output_text = "=== Daftar Color ===\n\n"
        for i, (color, count) in enumerate(colors.items(), 1):
            output_text += f"{i}. {color}: {count} film\n"
        output_text += f"\nTotal Jenis Color: {len(colors)}"
        self.print_box(output_text)

    def show_languages(self):
        languages = set()
        for lang_list in self.df['Language'].str.split(','):
            if isinstance(lang_list, list):
                languages.update([l.strip() for l in lang_list])
        
        output_text = "=== Daftar Bahasa ===\n\n"
        for i, lang in enumerate(sorted(languages), 1):
            output_text += f"{i:2d}. {lang}\n"
        output_text += f"\nTotal Bahasa: {len(languages)}"
        self.print_box(output_text)

    def show_countries(self):
        countries = set()
        for country_list in self.df['Country'].str.split(','):
            if isinstance(country_list, list):
                countries.update([c.strip() for c in country_list])
        
        output_text = "=== Daftar Negara ===\n\n"
        for i, country in enumerate(sorted(countries), 1):
            output_text += f"{i:2d}. {country}\n"
        output_text += f"\nTotal Negara: {len(countries)}"
        self.print_box(output_text)

    def show_total_movies(self):
        output_text = "=== Total Film ===\n\n"
        output_text += f"Jumlah Film: {len(self.df)}"
        self.print_box(output_text)

    def show_rating_chart(self):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=self.df, x='Rating', bins=20)
        plt.title('Distribusi Rating Film')
        plt.xlabel('Rating')
        plt.ylabel('Jumlah Film')
        plt.show()

    def show_gross_duration_resume(self):
        output_text = "=== Resume Gross Revenue ===\n"
        output_text += f"Total: ${self.df['Gross Revenue'].sum():,.2f}\n"
        output_text += f"Rata-rata: ${self.df['Gross Revenue'].mean():,.2f}\n"
        output_text += f"Terendah: ${self.df['Gross Revenue'].min():,.2f}\n"
        output_text += f"Tertinggi: ${self.df['Gross Revenue'].max():,.2f}\n"
        
        output_text += "\n=== Resume Duration ===\n"
        output_text += f"Total: {self.df['Duration (min)'].sum():,} menit\n"
        output_text += f"Rata-rata: {self.df['Duration (min)'].mean():.2f} menit\n"
        output_text += f"Terendah: {self.df['Duration (min)'].min()} menit\n"
        output_text += f"Tertinggi: {self.df['Duration (min)'].max()} menit"
        
        self.print_box(output_text)

    def query_language_genre(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            language = input("Masukkan bahasa (spasi untuk keluar): ")
            if language.strip() == "":
                break
                
            genre = input("Masukkan genre: ")
            
            # Filter berdasarkan bahasa dan genre
            filtered_df = self.df[
                self.df['Language'].str.contains(language, case=False, na=False) &
                self.df['Genre'].str.contains(genre, case=False, na=False)
            ]
            
            if len(filtered_df) == 0:
                self.print_box("Tidak ada film yang sesuai dengan kriteria!")
                continue
            
            output_text = "=== Hasil Query ===\n\n"
            output_text += "5 Film Teratas:\n"
            # Menampilkan top 5 berdasarkan urutan di dataset
            top_5 = filtered_df.head(5)[['Title', 'Rating', 'Lead Actor']]
            for _, row in top_5.iterrows():
                output_text += f"- {row['Title']} ({row['Rating']}, Actor: {row['Lead Actor']})\n"
        
            output_text += f"\nTotal Film: {len(filtered_df)}\n"
            
            output_text += "\n=== Durasi ===\n"
            output_text += f"Total: {filtered_df['Duration (min)'].sum():,} menit\n"
            output_text += f"Rata-rata: {filtered_df['Duration (min)'].mean():.2f} menit\n"
            min_duration = filtered_df.loc[filtered_df['Duration (min)'].idxmin()]
            max_duration = filtered_df.loc[filtered_df['Duration (min)'].idxmax()]
            output_text += f"Terendah: {min_duration['Duration (min)']} menit ({min_duration['Lead Actor']})\n"
            output_text += f"Tertinggi: {max_duration['Duration (min)']} menit ({max_duration['Lead Actor']})\n"
            
            output_text += "\n=== Gross Revenue ===\n"
            output_text += f"Total: ${filtered_df['Gross Revenue'].sum():,.2f}\n"
            output_text += f"Rata-rata: ${filtered_df['Gross Revenue'].mean():,.2f}\n"
            min_gross = filtered_df.loc[filtered_df['Gross Revenue'].idxmin()]
            max_gross = filtered_df.loc[filtered_df['Gross Revenue'].idxmax()]
            output_text += f"Terendah: ${min_gross['Gross Revenue']:,.2f} ({min_gross['Lead Actor']})\n"
            output_text += f"Tertinggi: ${max_gross['Gross Revenue']:,.2f} ({max_gross['Lead Actor']})"
            
            self.print_box(output_text)
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    dashboard = IMDbDashboard()
    dashboard.main_menu()