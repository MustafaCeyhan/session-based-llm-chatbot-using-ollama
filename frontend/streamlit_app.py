import streamlit as st
import requests
import uuid  # For generating unique session IDs

# Initialize session state for storing conversation history and session ID
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())  # Generate a new session ID for each conversation

# Set page config at the very beginning
st.set_page_config(page_title="AI Personal Assistant", page_icon="🤖")
# Title
st.title("AI Personal Assistant")

# Optional: Button to reset the conversation in the sidebar
if st.sidebar.button("Start New Conversation"):
    st.session_state['messages'] = []
    st.session_state['session_id'] = str(uuid.uuid4())  # Generate a new session ID

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if user_input := st.chat_input("You:"):
    # Add user input to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare the state for the backend invocation
    state = {
        "question": user_input,
        #"language": language,
        "history": st.session_state['messages'],  # Pass current conversation history
        "session_id": st.session_state['session_id']  # Include the session ID
    }
    # Call the backend API
    try:
        #response = requests.post("http://backend:8000/llm", json=state)  # Adjust the URL as 
        response = requests.post("http://localhost:8000/llm", json=state)  # Adjust the URL as needed
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(result['response'])
        st.session_state.messages.append({"role": "assistant", "content": result['response']})

    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")