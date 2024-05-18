from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from icebreaker.agents import linkedin_lookup_agent
from icebreaker.scraping.linkedin import scrape_linkedin_profile

def ice_break_with(name: str, mock=False) -> str:
    linkedin_url = linkedin_lookup_agent.lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=mock)

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": linkedin_data})
    print(res.content)


if __name__ == "__main__":
    print("Ice breaking with Timo van Niedek")
    ice_break_with("Timo van Niedek", mock=True)
