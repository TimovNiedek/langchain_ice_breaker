from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from icebreaker.scraping.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://linkedin.com/in/timo-van-niedek/", mock=True
    )
    res = chain.invoke(input={"information": linkedin_data})

    print(res["text"])
