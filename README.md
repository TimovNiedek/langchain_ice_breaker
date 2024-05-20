# Ice Breaker

This repository contains my custom implementation of the first module from the [Udemy LangChain course](https://www.udemy.com/course/langchain/learn). This module implements a LLM chain that fetches the Linkedin profile of a given person and presents the user with a generated summary and list of interesting facts.

## Environment variables

The following environment variables should be added to your .env file:

```
OPENAI_API_KEY="..."
PROXYCURL_API_KEY="..."
TAVILY_API_KEY="..."

LANGCHAIN_API_KEY="..."
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT="Ice Breaker"
```

To test the code without incurring costs, the data can be mocked. To do so, supply a link to a github gist in the environment variable below. An example can be found [here](https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json).

```
MOCK_LINKEDIN_PROFILE_URL="..."
```
