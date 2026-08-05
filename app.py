from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings = OpenAIEmbeddings()

db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever()

llm = ChatOpenAI(
    temperature=0
)

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""

Answer ONLY using the context below.

If the answer is not in the document, reply:

"I couldn't find that information in the document."

Context:

{context}

Question:

{question}

"""

    answer = llm.invoke(prompt)

    print("\nAnswer:\n")

    print(answer.content)
