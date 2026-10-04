import openai
import urllib
import json
from time import sleep

openai_api_key = "sk-U503K0......."   # Your OpenAI API key

client = openai.Client(api_key=openai_api_key)


def run_sparql_query(query):
    url = f"https://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query={urllib.parse.quote_plus(query)}&format=application%2Fsparql-results%2Bjson&timeout=30000&signal_void=on&signal_unconnected=on"
    response = urllib.request.urlopen(url)
    data = response.read()
    values = json.loads(data)
    results = values["results"]["bindings"]
    value = []
    for result in results:
        for key in result:
            value.append(result[key]["value"])
    value = ", ".join(value)
    return value


def ask_chatgpt_about_sparql_result(question, sparql_result):
    formatted_result = str(sparql_result)
    prompt = f"Question: {question}\n\nAnswer:"
    print(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content


queries = []
with open("sparql_queries.txt", "r") as f:
    for line in f:
        queries.append(line.strip())

for query in queries:
    question_for_gpt = f"Based on this sparql query, {query}, create a possible question as if you were asking a human. Do not refer at all at the DBpedia database. After you create the question, please proceed to create an answer for it using info from the sparql result. \n"
    sparql_result = run_sparql_query(query)
    gpt_response = ask_chatgpt_about_sparql_result(question_for_gpt, sparql_result)
    print(gpt_response)
    print("------------------")
    sleep(2)  # to avoid rate limit
