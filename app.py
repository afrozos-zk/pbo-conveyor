import streamlit as st
from sorter import ConveyorSystem
import uuid
import base64

st.set_page_config(page_title="Sortir Warna", layout="centered")

st.title("🚦 Simulasi Konveyor Sortir Warna")
st.caption("Hanya kotak warna hijau yang boleh lewat.")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return encoded
    
# Inisialisasi sistem jika belum ada di session_state
if "system" not in st.session_state:
    st.session_state.system = ConveyorSystem()

if st.button("🔄 Simulasi"):
    box = st.session_state.system.generate_box()
    result = st.session_state.system.check_box()

    color = box.color
    unique_id = str(uuid.uuid4()).replace("-", "")[:8]
    anim_name = f"anim_{unique_id}"
    box_class = f"box-{unique_id}"

    # Tentukan animasi berdasarkan hasil sortir
    if result == "pass":
        keyframes = f"""
        @keyframes {anim_name} {{
            0% {{ left: 0px; opacity: 1; }}
            70% {{ left: 650px; opacity: 1; }}
            100% {{ left: 650px; opacity: 0; }}
        }}
        """
    else:
        keyframes = f"""
        @keyframes {anim_name} {{
            0% {{ left: 0px; opacity: 1; }}
            70% {{ left: 325px; opacity: 1; }}
            100% {{ left: 325px; opacity: 0; }}
        }}
        """

    # HTML + CSS animasi + sensor visual
    animation_html = f"""
    <style>
    .conveyor-wrapper {{
        position: relative;
        height: 60px;
        width: 700px;
        background-color: #f0f0f0;
        border: 2px solid #ccc;
        margin-bottom: 20px;
    }}

    .sensor {{
        position: absolute;
        left: 325px;
        top: 0;
        width: 5px;
        height: 100%;
        background-color: red;
        opacity: 0.7;
    }}

    .{box_class} {{
        width: 50px;
        height: 50px;
        position: absolute;
        background-color: {color};
        animation: {anim_name} 5s linear forwards;
        top: 5px;
    }}

    {keyframes}
    </style>

    <div class="conveyor-wrapper">
        <div class="sensor"></div>
        <div class="{box_class}"></div>
    </div>
    """

    st.markdown(animation_html, unsafe_allow_html=True)
    st.success(f"Warna kotak: {color.upper()} - {'Lolos ✅' if result == 'pass' else 'Disortir ❌'}")

# footnote
logo_base64 = get_base64_image("logoafr.png")  # Pastikan file ada di folder sama dengan app.py

footer_html = f"""
<div style="display: flex; align-items: center; justify-content: center; margin-top: 40px;">
    <p style="margin-right: 10px; font-size: 16px; color: gray;">Created by</p>
    <a href="https://instagram.com/afrozos" target="_blank">
        <img src="data:image/png;base64,{logo_base64}" width="30" style="border-radius: 50%;">
    </a>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
