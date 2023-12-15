import streamlit as st
import openai
import langchain

# from langchain import PromptTemplate, LLMChain
# from langchain.llms import OpenAI

# # Set your OpenAI API key
# openai_api_key = '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'

# # Create a sidebar for language selection
# st.sidebar.title('Translation App')
# input_language = st.sidebar.selectbox('Input Language', ['English', 'Spanish', 'French', 'German'])
# output_language = st.sidebar.selectbox('Output Language', ['English', 'Spanish', 'French', 'German'])

# # Create a text area for user input
# user_input = st.text_area("Enter text here", "")

# # Define your prompt template
# template = "Translate the following text from {input_language} to {output_language}: {text}"
# prompt_template = PromptTemplate(
#     template=template,
#     input_variables=["input_language", "output_language", "text"]
# )

# # Define your language model
# llm = OpenAI(api_key=openai_api_key, temperature=0)

# # Define your LLMChain
# llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# # Translate the text when the 'Translate' button is clicked
# if st.button('Translate'):
#     # Use LangChain for translation
#     translation = llm_chain.run({
#         "input_language": input_language,
#         "output_language": output_language,
#         "text": user_input
#     })
    
#     # Display the translation
#     st.write(f'Translation: {translation}')


# from langchain import PromptTemplate, LLMChain
# from langchain.llms import OpenAI
# import os

# # Create a sidebar for language selection
# st.sidebar.title('Translation App')
# input_language = st.sidebar.selectbox('Input Language', ['English', 'Spanish', 'French', 'German'])
# output_language = st.sidebar.selectbox('Output Language', ['English', 'Spanish', 'French', 'German'])

# # Create a text input for the user to enter their OpenAI API key
# openai_api_key = st.sidebar.text_input("Enter your OpenAI API key here", "")

# # Set the OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = openai_api_key

# # Create a text area for user input
# user_input = st.text_area("Enter text here", "")

# # Define your prompt template
# template = "Translate the following text from {input_language} to {output_language}: {text}"
# prompt_template = PromptTemplate(
#    template=template,
#    input_variables=["input_language", "output_language", "text"]
# )

# # Define your language model
# llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"], temperature=0)

# # Define your LLMChain
# llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# # Translate the text when the 'Translate' button is clicked
# if st.button('Translate'):
#    # Use LangChain for translation
#    translation = llm_chain.run({
#        "input_language": input_language,
#        "output_language": output_language,
#        "text": user_input
#    })
   
#    # Display the translation
#    st.write(f'Translation: {translation}')

from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
import os

# Create a sidebar for language selection
st.sidebar.title('Translation App')
languages = ['English', 'Spanish', 'French', 'German', 'Other']
input_language = st.sidebar.selectbox('Input Language', languages)
output_language = st.sidebar.selectbox('Output Language', languages)

# If 'Other' is selected, display a text input field
if input_language == 'Other':
    input_language = st.sidebar.text_input("Enter your input language", "")
if output_language == 'Other':
    output_language = st.sidebar.text_input("Enter your output language", "")

# Create a text input for the user to enter their OpenAI API key

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = openai_api_key

# Create a text area for user input
user_input = st.text_area("Enter text here", "", max_chars=600)

if openai_api_key and input_language and output_language and user_input:
    # Define your prompt template
    template = "Translate the following text from {input_language} to {output_language}: {text}"
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["input_language", "output_language", "text"]
    )

    # Define your language model
    llm = OpenAI(api_key=os.environ["OPENAI_API_KEY"], temperature=0)

    # Define your LLMChain
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    # Translate the text when the 'Translate' button is clicked
    if st.button('Translate'):
        # Use LangChain for translation
        translation = llm_chain.run({
            "input_language": input_language,
            "output_language": output_language,
            "text": user_input
        })
        
        # Display the translation
        st.write(f'Translation: {translation}')
else:
    st.write("Please enter all required information.")
