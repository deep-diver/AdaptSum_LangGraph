# AdaptSum (LangGraph)

This is a spin-off project of [AdaptSum](https://github.com/deep-diver/AdaptSum) whose purpose is to demonstrate the usefulness of progressive summarization. This project brings that idea into Agentic Workflow, hence language model itself checks if the summarization is well written based on the pre-defined crieteria. 

## Project structure

```bash
.
├── graph
│   ├── __init__.py
│   ├── edges
│   │   ├── __init__.py
│   │   └── from_summary_grader.py
│   ├── graph.py
│   ├── nodes
│   │   ├── __init__.py
│   │   ├── chatbot.py
│   │   ├── grader.py
│   │   ├── llms.py
│   │   └── summarizer.py
│   └── types
│       ├── __init__.py
│       └── grader.py
├── main.py
├── requirements.txt
└── state
    ├── __init__.py
    └── state.py
```

- `graph`: everything about building LangGraph graph including nodes, edges, and tools.
  - `graph/nodes/chatbot.py`: chatbot node that allows users to communicate with LLM
- `state`: everything about state data structure.
- `main.py`: the entry point of this project. See below how to run this project.

## Instructions

```bash
$ export GOOGLE_API_KEY=<your_api_key>
$ python main.py
```

# Acknowledgments
This is a project built during the Vertex sprints held by Google's ML Developer Programs team. We are thankful to be granted good amount of GCP credits to do this project. 
