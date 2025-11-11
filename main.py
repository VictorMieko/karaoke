import streamlit as st

# Importa a view principal da aplicação
from views.listas_musicas_karaoke import main as render_karaoke_page


# Configuração da página
st.set_page_config(
    page_title="Karaoke Music Application",
    page_icon="🎤",
    layout="wide",
)


def main():
    st.title("Karaoke Music Application")
    st.caption("Navegue pelo catálogo completo e encontre a próxima música para soltar a voz.")
    render_karaoke_page()


if __name__ == "__main__":
    main()



"""
import streamlit as st

from views.listas_musicas_karaoke import view_listas_musicas_karaoke

st.title("Conexão Tech RO 2025 - SAPIENS")

st.set_page_config(
    page_title="Listas de Músicas Karaoke",
    page_icon=":🐱‍👤",
    layout="wide"
)

def main():
    st.title("🎉 Listas de Músicas para Karaokê")
    view_listas_musicas_karaoke()

if __name__ == "__main__":
    main()
"""