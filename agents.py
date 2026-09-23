from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search , scrape_url 
from dotenv import load_dotenv

load_dotenv()

#model setup 
llm = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite",temperature=0)


#1st agent 
def build_search_agent():
    return create_agent(
        model = llm,
        tools= [web_search]
    )

#2nd agent 

def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )


#writer chain 

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a rigorous research quality evaluator.

Your job is to critically evaluate the research report based on:
1. Factual accuracy
2. Completeness
3. Relevance to the research topic
4. Quality and reliability of sources
5. Depth of analysis
6. Logical structure and clarity
7. Whether claims are properly supported by the research

Do NOT give a high score simply because the report is well written.

Evaluate the actual research quality.

Use this scoring rubric:

9-10:
Exceptional research. Highly accurate, comprehensive, well-supported,
deeply analyzed, and professionally structured. Very few or no meaningful
issues.

7-8:
Strong research with good evidence and useful analysis, but with some
minor gaps, unsupported claims, missing details, or source limitations.

5-6:
Average research. Covers the topic but has noticeable gaps,
limited evidence, shallow analysis, weak sourcing, or unsupported claims.

3-4:
Weak research. Important information is missing, evidence is poor,
analysis is shallow, or several claims are questionable.

1-2:
Very poor research. Major factual, structural, sourcing, or relevance
problems make the report unreliable.

Be strict and evidence-based.

Do not inflate the score because the writing style is good.
If the report lacks evidence, explicitly penalize it.

Return your evaluation in exactly this format:

Score: X/10

Score Breakdown:
- Factual Accuracy: X/10
- Completeness: X/10
- Relevance: X/10
- Source Quality: X/10
- Depth of Analysis: X/10
- Structure & Clarity: X/10
- Evidence Support: X/10

Strengths:
- ...
- ...
- ...

Areas to Improve:
- ...
- ...
- ...

Missing or Weak Evidence:
- ...
- ...

One Line Verdict:
...

Be specific. Every criticism should explain what is missing,
weak, unsupported, or unclear.
"""
    ),
    (
        "human",
        """
Evaluate the following research report strictly according to the
criteria and scoring rubric above.

Research Report:
{report}
"""
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()