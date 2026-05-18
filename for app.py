import streamlit as st

CIPHER_MAP = {
    'a': 'Anal', 'b': 'Butt', 'c': 'Cock', 'd': 'Dick',
    'e': 'EroMe', 'f': 'Fuck', 'g': 'GayPorn', 'h': 'Hentai',
    'i': 'InMyAss', 'j': 'JAV', 'k': 'Kut', 'l': 'LickMaBalls',
    'm': 'Moaning', 'n': 'NiggerSex', 'o': 'Oral', 'p': 'PornHub',
    'q': 'Quickie', 'r': 'Rape', 's': 'Sex', 't': 'Tits',
    'u': 'Urethra', 'v': 'Vagina', 'w': 'Wickle', 'x': 'Xvideos',
    'y': 'Yoon', 'z': '질', ' ': '-'
}
REVERSE_MAP = {v.lower(): k for k, v in CIPHER_MAP.items()}


def encrypt_sentence(sentence):
    return " ".join(CIPHER_MAP.get(char, char) for char in sentence.lower())


def decode_description(encoded_text):
    words = encoded_text.split()
    return "".join(REVERSE_MAP.get(word.lower(), word) for word in words)


st.set_page_config(page_title="Redian Translator", page_icon="🔐")

st.title("Redian Translator")
st.write("Translate Redian to English or English to Redian")

mode = st.sidebar.selectbox("Functions", ["English -> Redian", "Redian -> English"])

user_input = st.text_area("Input your text:", placeholder="input your text here")

if st.button("translate"):
    if user_input:
        if mode == "English -> Redian":
            result = encrypt_sentence(user_input)
            st.success("translated to Redian!")
        else:
            result = decode_description(user_input)
            st.success("translated to English!")

        st.code(result, language=None)
    else:
        st.warning("check ur input retard.")

st.divider()
st.caption("Wong wen xi Chinge - Long Osaka Vietnam Chinge - Hong Chinga Suck Chinga Nigga")
