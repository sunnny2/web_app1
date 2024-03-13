import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo) # add todo in end of list
    functions.write_todos(todos)# add todo in txt file
    print(todo)


todos = functions.get_todos()


st.title("my todo app")
st.subheader("this is my todo app")
st.write(" this appppppppppppppppppppppppppppppppp")

#this for will add new todo
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo ,key=todo)# create checkbox of item in todos.txt
    if checkbox:
        todos.pop(index)# delete todos element from index
        functions.write_todos(todos)#write new todos.txt
        del st.session_state[todo]# delete checkbox
        st.experimental_rerun()

st.text_input(label="pls write down ", placeholder="hint",
              on_change=add_todo, key="new_todo")#on_change call back function , add_tod is function

st.session_state


