# SPARQL to Natural Language (NL) 

An automated Semantic Web pipeline that reads 50 SPARQL queries, retrieves live knowledge graph data from the official DBpedia endpoint, and uses OpenAI's `gpt-3.5-turbo` via API to formulate natural language Question–Answer pairs.

## Project Overview

This project bridges Semantic Web querying with Large Language Models (LLMs) by:
1. **Selecting Queries:** Curating 50 diverse SPARQL queries across various fields like books, awards, geography, history, and pop culture.
2. **Endpoint Execution:** Sending parameterized HTTP requests using Python's `urllib` to the official DBpedia SPARQL API endpoint `https://dbpedia.org/sparql` and parsing JSON bindings.
3. **Natural Translation via OpenAI's API:** Leverages OpenAI's Chat Completions API (gpt-3.5-turbo) to automatically translate technical SPARQL queries into natural, human-like questions.
4. Automated Pipeline: Orchestrates the query execution and translation loop automatically with built-in sleep intervals to respect API rate limits.


## Workflow 

1. **SPARQL Execution (`run_sparql_query`)**  
   The script queries the DBpedia endpoint via HTTP GET and parses the resulting RDF data into structured JSON bindings.

2. **Prompt Formulation**  
   The query and its results are packaged into a guided prompt directing OpenAI's model to act as a human communicator:
   > *"Based on this sparql query, `{query}`, create a possible question as if you were asking a human. Do not refer at all to the DBpedia database. After you create the question, please proceed to create an answer for it using info from the sparql result."*

3. **Natural Language Generation**  
   The LLM synthesizes the intent of the SPARQL code into an intuitive question and formats the raw graph entity labels into a fluent answer.

---

## End-to-End Example

###  Input SPARQL Query

SELECT ?winnerName 
WHERE {
  ?winner dbo:award dbr:Nobel_Prize_in_Literature ;
          foaf:name ?winnerName .
} 
LIMIT 10

### Generated Conversational Output

> **💬 Question**  
> *“Can you provide me with the names of the winners of the Nobel Prize in Literature?”*

> **ChatGPT's Answer**  
> *“Sure! Here are the names of some winners of the Nobel Prize in Literature:*  
> 1. Ernest Hemingway  
> 2. Gabriel Garcia Marquez  
> 3. Toni Morrison  
> 4. Alice Munro  
> 5. Orhan Pamuk  
> 6. Doris Lessing  
> 7. J.M. Coetzee  
> 8. Mario Vargas Llosa  
> 9. Mo Yan  
> 10. Alice Munro*”*


## Prerequisites & Requirements
* Python 3.8+
* An active [OpenAI API Key](https://platform.openai.com/api-keys)
