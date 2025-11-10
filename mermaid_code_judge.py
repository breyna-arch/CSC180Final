from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from agents import Agent, ItemHelpers, Runner, TResponseInputItem, trace

@dataclass
class EvaluationFeedback:
    feedback: str
    score: Literal["pass", "needs_improvement", "fail"]

evaluator = Agent[None](
    name="evaluator",
    instructions=(
        "You are an expert Mermaid syntax reviewer."
        "Your task is to evaluate Mermaid diagram code to determine whether it will successfully render using the latest stable Mermaid.js version (v11.x)."
        "If the code is invalid, ambiguous, or non-optimal, you must: Explain why it may fail, Suggest or provide corrected code, and, Optionally, give clarity or layout improvements (without changing semantics)."
        "Remember you cannot have parentheses inside of a statement. NOT like this: 'D2 --> E2[Action: Increase local marketing (social media, flyers, partnerships)]'"
        "Also NO double quotes inside a statement."
    ),
    output_type=EvaluationFeedback
    )

class codeJudge:
    async def main(insert_prompt_result) -> None:
        latest_code: str | None = None

        with trace("Mermaid Code Judge"):
            while True:
                input_items = insert_prompt_result.to_input_list()
                latest_code = ItemHelpers.text_message_outputs(insert_prompt_result.new_items)

                evaluator_result = await Runner.run(evaluator, input_items)
                result: EvaluationFeedback = evaluator_result.final_output

                print(f"Evaluator score: {result.score}")

                if result.score == "pass":
                    print("Good!")
                    break

                print("Re-running with feedback")

                input_items.append({"content": f"Feedback: {result.feedback}", "role": "user"})

        print(f"Final story outline: {latest_code}")
        return latest_code