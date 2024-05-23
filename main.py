from dotenv import load_dotenv
import os
import pandas as pd

from llama_index.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import openai
load_dotenv()

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)

population_query_engine.update_prompts({ "pandas_prompt": new_prompt })
population_query_engine.query("what is the population of England")


tools = [
    note_engine,
    QueryEngineTool(query_engine=population_query_engine, metadata=ToolMetadata(
        name="population_data",
        description="this gives information about the world population and demographics"
    ))
]

llm = openai(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)


while (prompt := input("Enter a prompt (q to quit): ") != "q"):
    result = agent.query(prompt)
    print(result)