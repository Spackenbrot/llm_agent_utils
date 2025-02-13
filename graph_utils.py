from langgraph.graph import MessagesState

def get_recent_tool_calls(state: MessagesState):
    recent_tool_messages = []
    for message in reversed(state["messages"]):
        if message.type == "tool":
            recent_tool_messages.append(message)
        else:
            break
    return recent_tool_messages[::-1]