import streamlit as st
import functions

# Load todos
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field after adding a todo


# Setting the page layout to wide
st.set_page_config(layout="wide")

# Displaying the logo and app title
col1, col2 = st.columns([1, 3])
with col1:
    # Replace 'path/to/logo.png' with the path or URL of your logo
    st.image("./img/logo.webp", width=100)
with col2:
    st.title("My Todo App")

# App description
st.markdown(
    """
## Welcome to My Todo App! 📝

This productivity app is designed to help you manage your daily tasks efficiently. With a simple and intuitive interface, you can easily add new tasks, view your pending tasks, and mark them as completed once done. Our goal is to help you stay organized and focused, boosting your productivity.

### Features:
- **Add New Tasks**: Easily add new tasks to your list.
- **Task Management**: View and manage your tasks with a simple click.
- **Progress Tracking**: Keep track of your completed tasks and stay motivated.

Let's get started and make your day more productive!
"""
)

# User input for new todo
st.text_input("Add a new todo...", on_change=add_todo, key="new_todo")

# Display todos
st.subheader("Your Tasks:")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=str(index))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[str(index)]
        st.experimental_rerun()
