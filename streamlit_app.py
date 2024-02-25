import urllib.parse
import streamlit as st

# URL 인코딩 함수
def encode_url(url):
    return urllib.parse.quote(url)

# URL 디코딩 함수
def decode_url(encoded_url):
    return urllib.parse.unquote(encoded_url)

def app():
    st.set_page_config(
        page_title="URL Encoder & Decoder",
        page_icon="https://www.techspot.com/images2/downloads/topdownload/2015/12/lock.png"
    )
    # Featured image
    st.image(
        "https://static.thenounproject.com/png/4673503-200.png",
        width=150
    )
    # Main title and description
    st.title("URL Encoder $ Decoder")
    st.markdown("Input URL to encode or decode.")

    url_type = st.radio(
        "Select URL type",
        ["Encode", "Decode"],
        index=None,
    )

    st.write("You selected: ", url_type)
    if url_type == "Encode":
        url = st.text_input("Input URL to encode")
        if st.button("Encode"):
            st.write("Encoded URL:\n")
            code = encode_url(url)
            st.code(code)        
            # st.text("Encoded URL:\n", encode_url(url))
    elif url_type == "Decode":
        url = st.text_input("Input URL to decode")
        if st.button("Decode"):
            st.write("Decoded URL:\n")
            code = decode_url(url)
            st.code(code)        
            # st.text(decode_url(url))

# 사용 예시
if __name__ == "__main__":
    app()
