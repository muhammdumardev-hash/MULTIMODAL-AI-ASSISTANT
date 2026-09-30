import streamlit as st
from groq import Groq
from multimodal.vision import analyze_image

st.set_page_config(page_title="AI Image & Document Assistant", page_icon="🖼️", layout="centered")

st.title("🖼️ AI Image & Document Assistant")
st.write("Upload an image and ask a question. The multimodal AI will analyze the visible content.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])

question = st.text_area(
    "Ask a question about the image",
    placeholder="Example: What product is shown in this image?"
)

with st.expander("💡 Prompt examples"):
    st.write("• Product: What product is shown in this image?")
    st.write("• Document: Extract the title, date, and important information.")
    st.write("• Diagram: Explain this diagram in simple words.")
    st.write("• Verification: Is a phone number visible in the image?")

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded image", use_container_width=True)

if st.button("🔍 Analyze Image", type="primary"):
    if not uploaded_file:
        st.warning("Please upload an image first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            model = st.secrets["GROQ_MODEL"]

            with st.spinner("Analyzing image..."):
                answer = analyze_image(
                    client=client,
                    model=model,
                    image_bytes=uploaded_file.getvalue(),
                    mime_type=uploaded_file.type,
                    question=question.strip(),
                )

            st.subheader("AI Response")
            st.write(answer)

        except KeyError:
            st.error("Missing GROQ_API_KEY or GROQ_MODEL in Streamlit Secrets.")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
