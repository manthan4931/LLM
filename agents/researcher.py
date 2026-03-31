def research_task(query,retriever):
    docs=retriever.invoke(query)
    context="\n\n".join(doc.page_content for doc in docs)


    return context