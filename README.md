# SPARQL to Natural Language (NL) 

An automated Semantic Web pipeline that reads 50 SPARQL queries, retrieves live knowledge graph data from the official DBpedia endpoint, and uses OpenAI's `gpt-3.5-turbo` via API to formulate natural language Question–Answer pairs.

## Project Overview

This project bridges Semantic Web querying with Large Language Models (LLMs) by:
1. **Selecting Queries:** Curating 50 diverse SPARQL queries across various fields like books, awards, geography, history, and pop culture.
2. **Endpoint Execution:** Sending parameterized HTTP requests using Python's `urllib` to the official DBpedia SPARQL API endpoint `https://dbpedia.org/sparql` and parsing JSON bindings.
3. **Natural Translation via OpenAI's API:** Leverages OpenAI's Chat Completions API (gpt-3.5-turbo) to automatically translate technical SPARQL queries into natural, human-like questions.
4. Automated Pipeline: Orchestrates the query execution and translation loop automatically with built-in sleep intervals to respect API rate limits.


## Prerequisites & Requirements
* Python 3.8+
* An active [OpenAI API Key](https://platform.openai.com/api-keys)
