import streamlit as st
import pygame
import time

# Pygame ile müzik çalma
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("your_music_file.mp3")  # Müzik dosyasını seçin
    pygame.mixer.music.play(-1)  # Döngüde çal (-1)

# Streamlit arayüzü
def main():
    st.title("Spotify Wrapped Tarzında İş Özeti")
    
    # Müzik kontrolü
    st.sidebar.header("Müzik Kontrol")
    if st.sidebar.button("Müziği Başlat"):
        play_music()
    if st.sidebar.button("Müziği Durdur"):
        pygame.mixer.music.stop()

    # Kaydırmalı sayfalar
    page = st.selectbox("Sayfa Seçin", ["Genel Bakış", "En İyi Performans", "Trendler"])

    if page == "Genel Bakış":
        st.header("Genel Bakış")
        st.write("Burada genel iş verilerinizi özetleyin.")
        st.image("overview_chart.png")  # Bir grafik ekleyin
    elif page == "En İyi Performans":
        st.header("En İyi Performans")
        st.write("En iyi ekip üyeleri veya ürünler hakkında bilgi verin.")
        st.image("top_performance_chart.png")
    elif page == "Trendler":
        st.header("Trendler")
        st.write("Ay bazında büyüme ve diğer veriler.")
        st.line_chart([1, 2, 3, 4, 5])  # Örnek veri

    # Slayt geçişi
    st.sidebar.subheader("Slaytlar Arası Geçiş")
    st.sidebar.slider("Sayfa Geçişi", min_value=1, max_value=3, step=1, format="Sayfa %d")

if __name__ == "__main__":
    main()
