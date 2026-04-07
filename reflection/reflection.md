# Application: [Wysa] 
- Most important difference between pipelines: [The manual pipeline produced the clearest personas and the most useful requirements as personas were more detailed and requirements had the lowest ambiguity ratio 0.3 so they were mostly easily verifiable. Automated pipeline tests had high ambiguity and personas were more generic. But automated and hybrid pipelines did provide greater review coverage due to the quick speed at which LLMs can process data, they also provided the most traceability links. But all pipelines had a traceability ratio of 1.0]
- Most useful pipeline: [The hybrid pipeline proved most useful as it had the greatest balance achieving the high review coverage of the automated pipeline while creating acceptable detailed personas and verifiable tests that effectively test requirements.] 
- Most surprising finding: [LLMs were very sensitive to prompts. Possibly because the model we had to use was not as effective. For example, I had to be careful which template to provide to LLM as it may have limited detail to match the template rather than instructions. Also had to explicitly instruct the mdoel to create detailed personas that could be used to derive requirements before I got acceptable output]
- Observed weakness in the automated pipeline: [More than half of tests in the automated pipeline were not verifiable]

- A key trade-off was between quality and scalability. The manual pipeline yielded quality outputs (lower ambiguity, clearer personas), but required significantly more time and effort. The automated pipeline improved efficiency and coverage but at the cost of precision and verifiability. The hybrid approach balanced these trade-offs effectively.

- Although all pipelines achieved a testability ratio of 1.0, this metric alone was misleading as many automated tests were not practically verifiable due to vague or ambiguous wording. This highlights the limitation of relying solely on quantitative metrics without qualitative validation.

- LLMs are highly dependant on prompt engineering. Small variations of wording or structure significantly impacted output quality. This indicates that automated pipelines are not truly autonomous and still require careful human oversight to guide output generation effectively.

- Overall, this project reinforced that while LLMs are powerful tools for accelerating software specification tasks, human judgement remains essential for ensuring clarity, correctness and usability of outputs.

