scoring_prompt = f"""
You are evaluating a student's induction proof for a discrete math problem.

Reference proofs (showing correct structure):
{retrieved_examples}

Student's answer:
{student_answer}

Evaluate based on:
- Base case properly stated and proved (0-2 points)
- Inductive hypothesis clearly stated (0-2 points)  
- Inductive step logically valid (0-2 points)
- Overall clarity and completeness (0-1 point)

Return JSON: {{"score": total, "feedback": "specific feedback", "missing_components": []}}
"""