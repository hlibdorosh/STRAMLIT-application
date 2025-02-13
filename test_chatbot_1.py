import pytest
import openai


def test_api_key_setup(monkeypatch):
    # Mock the openai.api_key directly
    monkeypatch.setattr(openai, "api_key", "test-key")

    # Assert that the API key is set correctly
    assert openai.api_key == "test-key"


import pytest
import streamlit as st


def test_default_model_configuration():
    # Clear session state before test
    st.session_state.clear()

    # Run the code that sets up the default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Assert that the default model is set correctly
    assert st.session_state["openai_model"] == "gpt-3.5-turbo"


import pytest
import streamlit as st


def test_message_handling():
    # Clear session state before test
    st.session_state.clear()

    # Mock user input
    prompt = "Test message"

    # Initialize session state messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Simulate the user input handling
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Assert that the message is correctly stored
    assert len(st.session_state.messages) == 1
    assert st.session_state.messages[0]["role"] == "user"
    assert st.session_state.messages[0]["content"] == "Test message"

