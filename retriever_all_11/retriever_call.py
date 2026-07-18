from langchain_community.retrievers import WikipediaRetriever

from retriever_all_11.model.retriever_model import SimpleQuery


async def do_rerieve_from_wikipedia(simpleQuery: SimpleQuery):
    query = simpleQuery.query_str
    retriever = WikipediaRetriever(top_k_results=1)
    retrieved_docs = retriever.invoke(query)
    return {"model_response": retrieved_docs[0].page_content}
