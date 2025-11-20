import streamlit as st
import gemini as gemini
import grok as grok


st.title("Hello Good SIR ")
selected_model=st.selectbox("Select Model ", ["ALL","OpenAI", "Gemini","Grok","Claude"])
#st.title(selected_model)
prompt=st.text_input("enter prompt")

if selected_model=="ALL" and prompt :
    st.title(prompt)
    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.header('OpenAI')
        st.text(grok.grokResp(prompt))
    
    with c2:
        st.header('Gemini')
        st.text(gemini.geminiResp(prompt))
        
    with c3:
        st.header('#Grok')
        st.text(gemini.geminiResp(prompt))
        
    with c4:
        st.header('#Claude')
        st.text(gemini.geminiResp(prompt))


elif selected_model=="OpenAI" and prompt:
    st.title(selected_model)
    st.text(grok.grokResp(prompt))
elif selected_model=="Gemini" and prompt:
    st.title(selected_model)
    st.text(gemini.geminiResp(prompt))


elif selected_model=="Grok" and prompt:
    st.title(selected_model)
    st.text("Model Not Available Due to API limitations By Parent Organisation")
elif selected_model=="Claude" and prompt:
    st.title(selected_model)
    st.text("Model Not Available Due to API limitations By Parent Organisation")
    