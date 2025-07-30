from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class Summarizer:

    __PROMPT_TEMPLATE = ChatPromptTemplate.from_messages([
        ("system", """
            [RESUME CONFIG]:
            - Resumo com uma linguagem informativa para todo o público de TI.
            - O resumo deve conter todo o **CONTEÚDO CHAVE** do artigo da notícia.
            - Utilize de trocadilhos engraçados da área de TI (quando necessário, sem exageros).
            - O resumo deve conter pelo menos 1/4 (um quarto) do artigo.

            [INSTRUCTION]:
            1. Faça uma análise do artigo em [ARTICLE].
            2. Entenda todo o contexto.
            3. Elabore um resumo baseado na [RESUME CONFIG].

            [OUTPUT CONFIG]:
            - **NUNCA** mencione que é um resumo.
            """),
        ("human", """
            [ARTICLE]:
            {input}
            """)
        ])

    __summarization_chain = None
    __summary = None

    def __init__(self, llm):
        self.__summarization_chain = self.__PROMPT_TEMPLATE | llm | StrOutputParser()

    def summarize(self, article):
        output = self.__summarization_chain.invoke({
            "input":
                f"""
                [ARTICLE]:
                {article}
                """
        })

        self.__summary = output

    def get_summary(self):
        return self.__summary