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
            """),
        ("human", """
            [ARTICLE]:
            {input}
            """)
        ])
    __summarization_chain = None