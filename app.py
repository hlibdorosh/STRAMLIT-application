# Unit 1: Import necessary libraries and set up the title
import streamlit as st
import openai
import toml
import os
# Set the title for the Streamlit app
st.title("Smartest API Student")

# Unit 2: Initialize OpenAI API key and session state variables

#secrets_path = r"C:\Users\doros\.streamlit\secrets.toml"

openai.api_key  = st.secrets["OPENAI_API_KEY"]


# Initialize the OpenAI model if not already set in the session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize the messages list if not already set in the session state
if "messages" not in st.session_state:
    st.session_state.messages = []


# Unit 3: Display chat messages stored in the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Unit 4: Handle new user input and generate responses using the OpenAI API
# Check if there is a new user input
if prompt := st.chat_input("Huh?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Call the OpenAI API using the correct parameters
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages,
            stream=True,
        )

        # Process the streamed response from the API
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta'].get('content', '')
            full_response += chunk_message
            message_placeholder.markdown(full_response + "...")

        # Finalize the assistant's message and store it in the session state
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
