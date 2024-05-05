import streamlit as st

def show_home_page():
    target_url = "https://www.google.com"
    image_url = "https://images.pexels.com/photos/8016901/pexels-photo-8016901.jpeg?auto=compress&cs=tinysrgb&w=1200"
    
    st.markdown(
        f"""
        <a href="{target_url}" target="_blank"><img src="{image_url}" alt="Homepage Image" width="100%"></a>
        
        <h2 class="title" id="homepage_hdr">Proje Hakkında</h2>
        
        <p class="text">       
        Bu kısımda proje hakkında bilgi vereceğiz. Kimler tarafından yapılıyor, ne yapılıyor, ne gibi teknolojiler kullanılıyor, proje yol haritası gibi bilgiler yer alıyor olacak.
        </p>
        
        <h2 class="title" id="homepage_hdr">Proje Hedefleri</h2>
        
        <p class="text">
        Bu kısımda projenin hedeflerini belirleyeceğiz. Örneğin projeyi yapma amacımızın ne olduğunu bununla neyi elde edebileceğimiz gibi bulguları belirleyecegiz.
        </p>
        
        <h2 class="title" id="homepage_hdr">Proje Özellikleri</h2>
        
        <p class="text">
        Bu kısımda projenin özellikleri yer alacak. Örneğin projede hangi aşamalar kaydedildi. Veriler nasıl toplandı, ne tür bir analiz sergilendi, ne tür bir görselleştirme yapıldı, tahmin aşaması nasıl yürütüldü ve web application nasıl yapıldı gibi bilgiler yer alabilir.
        </p>
        
        <hr>
        <br>
        <p align='right' class="text">
            <a href="https://github.com/f1rzen/IST491" target="_blank">View on GitHub</a>
            <br>
            <a href="https://www.google.com" target="_blank">See External Dashboard</a>
        </p>
        
        """,
        unsafe_allow_html=True
    )