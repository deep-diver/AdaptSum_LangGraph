from string import Template
from state import State
from .llms import llm

def summarizer(state: State):
    summary_prompt_template = Template("""Below is the initial summary of our conversation. 
Based on the given summary and the last conversation between you (assistant) and me (user), I want to update the summary.

**Summary:** 
$previous_summary

**Last Conversation:**
$latest_conversation

Summary Guide:
* Instead of rewriting the entire summary each time, update only the specific portions necessary to reflect new information or changes.
* Only include information we have explicitly discussed in this session. Do not introduce any new information or topics, even if you have prior knowledge.
* Ensure the summary is factually accurate and reflects the nuances of our discussion.
* While being detailed, also aim for conciseness and clarity in the summary.
* Use markdown formatting to make the summary more readable
* Do not seprate sections for previous and updated summaries

""")

    last_conversation = f"""USER: {state["messages"][-2].content}\n\nASSISTANT: {state["messages"][-1].content}"""
    
    prev_summary = ""
    if "summary" in state:
        prev_summary = state['summary'][0]
    
    summary_prompt = summary_prompt_template.safe_substitute(
        previous_summary=prev_summary,
        latest_conversation=last_conversation
    )

    summary_msg = llm.invoke(summary_prompt).content
    return {"new_summary": [summary_msg]}
