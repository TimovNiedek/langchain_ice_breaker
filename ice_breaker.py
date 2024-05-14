from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain

if __name__ == "__main__":

    print("Hello, LangChain!")
    information = """
Daniel Craig Schreiber (born 1984) is an Australian radio producer, writer, podcaster, and comedian based in London. He co-created the BBC Radio 4 panel show The Museum of Curiosity with host John Lloyd and co-producer Richard Turner[1] and co-hosts the podcast No Such Thing As A Fish.[2]
Early life

Schreiber was born c. 1984 in British Hong Kong to an Australian father and a British mother, both of whom worked as celebrity hairdressers.[3][4][5][6][7] He became proficient in Mandarin.[8] The Schreibers moved to Sydney, Australia around the time Hong Kong changed from British rule to Chinese rule.[7] He moved to the UK at age 19 after QI creator John Lloyd offered him a job while Schreiber was visiting family in Oxford.[7] He has a sister, Chyna, and a brother.[9][10]
Career

Schreiber began at the television panel game show QI as a researcher, or "elf", shortly after moving to England.[11][6] He co-created and co-produces The Museum of Curiosity starting in 2008;[6][12] co-hosts the cryptozoology-focused podcast The Cryptid Factor with Rhys Darby, David Farrier and producer Leon 'Buttons' Kirkbeck starting in 2013;[13][14] and co-created, co-hosts, and co-produces the podcast No Such Thing As A Fish alongside James Harkin, Andrew Hunter Murray and Anna Ptaszynski starting in 2014.[15][16] Schreiber also appeared as a panelist and presenter on the BBC panel show No Such Thing as the News, a spin-off of the No Such Thing As a Fish podcast. The program's two series aired in 2016.[17][18] While staying at his in-laws' house during the COVID-19 pandemic, Schreiber created Show Us Your Shit (also known as Show Us Your Shit (or: Some Shakespeare, A Pair of Pyjamas & A Mutton Chop)), an Instagram Live series. Each episode features a different guest who shows Schreiber and the audience a selection of interesting objects from around their home.[19] On 6 June 2020, Schreiber was featured on the BBC Radio 4 series Loose Ends to discuss Show Us Your Shit.[19] In 2021, The Tournament, a show devised by Schreiber along with James Rawson and Simon Urwin, aired on BBC hosted by Alex Scott.[20][21]

After five seasons working for QI, Schreiber started as head of development for ComedyBox,[22][23] an online channel from Warner, which financially supported comedy projects and provided a forum for comedians to share their content.[24][25][26][27] There, he executive produced Ken Russell's short Christmas film A Kitten for Hitler[28] and Flight of the Conchords star Rhys Darby's ComedyBox clips[29] and stand-up DVD Imagine That! As a stand-up comedian in his own right,[30] Schreiber has toured with FolkFace from Radio 1's Chris Moyles Show and was a regular panelist on the E4 show Dirty Digest. Schreiber's comic debut at the Edinburgh Festival Fringe was his show Cockblocked From Outer Space in 2014.[31] In 2015, he was the presenter in the Channel 4 documentary The Great UFO Conspiracy, which examined beliefs about aliens in the UK.[31][32] Since hosting the cancelled pilot of his own radio show, which featured guests Rhys Darby, John Lloyd, Ismo Leikola, and John Gribbin in 2009[33] Schreiber has also been a guest on BBC Radio 4's Don't Make Me Laugh with David Baddiel and Fresh From The Fringe as well as a variety of podcasts including Judge John Hodgman and Richard Herring's Leicester Square Theatre Podcast.[34][35][36][37]

Schreiber has also contributed to a number of books, including The Naked Jape by Jimmy Carr; the QI spinoffs The Book of General Ignorance and G Annual; and No Such Thing as a Fish's The Book of the Year series.[38][39][40] He released his first stand-alone book, The Theory of Everything Else: A Voyage Into the World of the Weird, in October 2022.
    """

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": information})

    print(res['text'])
