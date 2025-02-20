def summary_grader_edge(state):
    if state["scores"] is None:
        print("---summary_grader_edge(NO SCORES)---")
        return "qualified"
    else:
        scores = state["scores"][0]
        if scores.updates_specific_portions and \
            scores.explicit_information and \
            scores.factually_accurate and \
            scores.concise_and_clear:
            print("---summary_grader_edge(SCORES ARE GOOD)---")
            return "qualified"
        else:
            print("---summary_grader_edge(SCORES ARE BAD)---")
            return "unqualified"
