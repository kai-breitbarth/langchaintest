import os
from langchain.llms import OpenAI


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    print(f"API key: %s" % api_key)

    llm = OpenAI(openai_api_key="OPENAI_API_KEY")
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))


if __name__ == "__main__":
    main()