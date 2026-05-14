# ask.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def load_qa_chain():
    # 1. Load the existing ChromaDB
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    # 2. Set up the retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 3. Custom prompt so it stays focused on the resume
    template = """
    You are a helpful assistant that answers questions about a candidate's resume.
    Use ONLY the context below to answer. If the answer is not in the resume, say
    "I couldn't find that in the resume."

    Context:
    {context}

    Question: {question}
    Answer:
    """

    prompt = ChatPromptTemplate.from_template(template)

    # 4. Use cheapest model — works great for resume Q&A
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 5. Build the RAG chain using LCEL
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    qa_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return qa_chain


def main():
    print("🤖 Resume Q&A Bot")
    print("=" * 40)
    print("Type your question or 'quit' to exit\n")

    qa_chain = load_qa_chain()

    while True:
        question = input("You: ").strip()

        if question.lower() in ["quit", "exit", "q"]:
            print("Bye!")
            break

        if not question:
            continue

        answer = qa_chain.invoke(question)
        print(f"\n🤖 Bot: {answer}\n")
        print("-" * 40)


if __name__ == "__main__":
    main()