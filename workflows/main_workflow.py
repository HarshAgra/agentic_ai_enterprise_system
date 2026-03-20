from utils.llm_client import call_llm
from utils.retriever import load_pdf_text, get_context

from agents.orchestrator import orchestrator_prompt
from agents.support_agent import support_prompt
from agents.hr_agent import hr_prompt
from agents.finance_agent import finance_prompt
from agents.procurement_agent import procurement_prompt
from agentic_ai_enterprise_system.utils.llm_client import call_llm


pdf_pages = load_pdf_text("data\Project Pragna at Surya Motors Limited.pdf")


def route_query(query: str) -> str:
    category = call_llm(orchestrator_prompt, query).strip().lower()
    print("DEBUG CATEGORY:", category)

    context = get_context(query, pdf_pages)

    enriched_query = f"""
You are given business context below.

Context:
{context}

Question:
{query}
"""

    if category == "customer_support":
        return call_llm(support_prompt, enriched_query)

    elif category == "hr":
        return call_llm(hr_prompt, enriched_query)

    elif category == "finance":
        return call_llm(finance_prompt, enriched_query)

    elif category == "procurement":
        return call_llm(procurement_prompt, enriched_query)

    else:
        return "Sorry, could not classify the query."
