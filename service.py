# from gpt_index import SimpleDirectoryReader, GPTListIndex, VectorStoreIndex, LLMPredictor, PromptHelper
from llama_index import SimpleDirectoryReader, GPTListIndex, VectorStoreIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

# Construct the absolute file path
base_path = os.path.dirname(os.path.abspath(__file__))
    
os.environ["OPENAI_API_KEY"] = "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"

def construct_index(directory_path):
  # set maximum input size
  max_input_size = 4096
  # set number of output tokens
  num_outputs = 256
  # set maximum chunk overlap
  max_chunk_overlap = 0.2
  # set chunk size limit
  chunk_size_limit = 600

  prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

  # define LLM
  llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
  
  documents = SimpleDirectoryReader(directory_path).load_data()
  
  index = VectorStoreIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

  return index
  
def ask_bot(index, prompt):
  # response = index.query(prompt, response_mode="compact")
  # print ("Result: " + response.response + "\n")
  # return response.response
  response = index.as_query_engine()
  res = response.query(prompt)
  print(res)
  return res