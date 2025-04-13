import streamlit as st
import openai

# Set your OpenAI key
openai.api_key = "your_openai_api_key_here"

# Iraqi personalities
characters = {
    "الحجيّة": "أنت الحجيّة، امرأة عراقية كبيرة بالعمر، حكيمة، درامية، ودمك خفيف...",
    "الحجي": "أنت الحجي، رجل عراقي كبير بالعمر، حكيم ومتدين...",
    "ابن المنطقة": "أنت ابن المنطقة، شاب عراقي عايش بالحارة...",
    "الفاشنيستا": "أنت بنوتة عراقية مودرن، تحبين الميكب، التيك توك...",
    "الشاعر": "أنت شاعر عراقي، تحب الحكي العميق والرومانسي...",
    "العسكري": "أنت عسكري عراقي، تتكلم بنبرة صارمة، تحب الانضباط...",
    "السياسي": "أنت سياسي عراقي محترف، تتكلم بلغة رسمية جداً..."
}

# Streamlit UI
st.set_page_config(page_title="Iraq AI", layout="centered")
st.title("🇮🇶 Iraq AI - دردش مع شخصية عراقية")

selected_character = st.selectbox("اختر شخصية: 🤖", list(characters.keys()))

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("اكتب سؤالك هنا 👇")

col1, col2 = st.columns(2)
with col1:
    send = st.button("💬 أرسل")
with col2:
    clear = st.button("🗑️ مسح المحادثة")

if clear:
    st.session_state.chat_history = []
    st.experimental_rerun()

if send and user_input:
    messages = [{"role": "system", "content": characters[selected_character]}]
    for msg in st.session_state.chat_history:
        messages.append(msg)
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]

    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"**أنت:** {msg['content']}")
    else:
        st.markdown(f"**{selected_character}:** {msg['content']}")
