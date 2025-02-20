from langchain_core.prompts import ChatPromptTemplate
from .llms import structured_llm_grader

system = """You are a grader assessing if a new summary is properly updated compared to the previous summary based on the latest information and given criteria.

Compare the two summaries and check if the new summary follows these rules:
* Only updates specific portions necessary to reflect new information from the lastest information
* Only includes explicitly discussed information from the session (both previous and new)
* Is factually accurate and reflects discussion nuances from both summaries
* Is detailed while being concise and clear
* Uses markdown formatting for readability
* Does not separate previous and updated summaries into sections

Analyze how the new summary incorporates information from the previous summary and the lastest information.
Give a binary score 'yes' or 'no' to indicate whether the new summary properly updates the previous summary following all criteria."""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        (
            "human",
            "previous summary: \n\n {pre_summary} \n\n latest information: \n\n {latest_info} \n\n new summary: \n\n {new_summary}"
        ),
    ]
)

def summary_grader(state):
    """
    Determines whether the retrieved documents are relevant to the question.

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Updates documents key with only filtered relevant documents
    """

    summary_grade_pipe = grade_prompt | structured_llm_grader

    print("---summary_grader(CHECK SUMMARY)---")
    print(state)
    if "summary" not in state:
        print("---summary_grader(NO PREVIOUS SUMMARY)---")
        return {"scores": None, "summary": state["new_summary"][0]}
    else:
        print("---summary_grader(PREVIOUS SUMMARY FOUND)---")
        summary = state["summary"]
        new_summary = state["new_summary"][0]
        latest_info = state["messages"][-1].content

        scores = summary_grade_pipe.invoke(
            {"pre_summary": summary, "latest_info": latest_info, "new_summary": new_summary}
        )
        return {"scores": [scores]}
