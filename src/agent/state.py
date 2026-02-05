from typing import TypedDict, List

class AgentState(TypedDict):
    user_input: str
    plan: List[str]
    current_step: int
    tool_result: str
    history: List[str]
    final_answer: str

def planner_node(state):
    prompt = f"""
    Break this request into ordered logical steps.
    Return a Python list.
    Request: {state['user_input']}
    """

    steps = llm(prompt)   # your model call
    state["plan"] = eval(steps)
    state["current_step"] = 0
    return state