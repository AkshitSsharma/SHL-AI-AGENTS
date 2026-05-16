from retriever import search_assessments

query = "Java developer with communication skills"

results = search_assessments(query)

for item in results:

    print("\n===================")

    print("NAME:", item.get("name"))

    print("URL:", item.get("link"))

    print("SKILLS:", item.get("keys"))