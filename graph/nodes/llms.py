from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from graph.types import GradeSummary

# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
structured_llm_grader = llm.with_structured_output(GradeSummary)
