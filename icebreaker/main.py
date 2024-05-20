import json
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from icebreaker.agents import linkedin_lookup_agent
from icebreaker.scraping.linkedin import scrape_linkedin_profile
from icebreaker.output_parsers import Summary, summary_parser


def ice_break_with(name: str, mock=False) -> str:
    linkedin_url = linkedin_lookup_agent.lookup(name, mock=mock)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=mock)

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    
    {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    summary: Summary = chain.invoke(input={"information": linkedin_data})
    print(json.dumps(summary.dict(), indent=4))


if __name__ == "__main__":
    print("Ice breaking with Timo van Niedek")
    ice_break_with("Timo van Niedek", mock=True)
