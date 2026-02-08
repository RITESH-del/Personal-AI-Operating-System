# from app.gui import SearchBar
from pyexpat import model
from tool_kit import tools
from ollama import chat
import json

# run with python -m src

# Helper function
def parse_tool_call(text):
    try:
        data = json.loads(text)
        if "tool" in data and "arguments" in data:
            return data
    except:
        return None

# add new memory to memory_index, and save the meta data to memory_meta.json
def add_memory(text, sequence):
    new_entry = {
        "context": "user_added",
        "text": text,
        "sequence": sequence
    }



def main():
    print("Loading AI Model...", end="\r")
    
    # Lazy import to avoid startup hang being silent
    from sentence_transformers import SentenceTransformer
    import faiss

    model = SentenceTransformer("models/minilm")
    # load faiss.index file
    tool_faiss_index = faiss.read_index("faiss.index")

    memory_faiss_index = faiss.read_index("memory_faiss.index")

    with open("Memory/memory.json") as f:
        memory_meta = json.load(f)

    print("AI Model Loaded.   ")
    # app = SearchBar()
    # app.run()


    print("Connected to ollama\n")
    while True:

        try:
            user_input = str(input("Enter Prompt:"))
            query_embedding = model.encode([user_input], normalize_embeddings=True)

            tool_scores, tool_indices = tool_faiss_index.search(query_embedding, k=5)
            memory_scores, memory_indices = memory_faiss_index.search(query_embedding, k=10)

            candidate_tools = [tools[i] for i in tool_indices[0]]
            retrieved = [memory_meta[i] for i in memory_indices[0]]

            # only fetch relevant memory if the score is above a certain threshold, otherwise it may add noise
            if memory_scores[0][0] < 0.75:
                retrieved = []

            run_seq_tool = next(t for t in tools if t.name == "Shortcut.run_sequence")

            if run_seq_tool not in candidate_tools:
                candidate_tools.insert(0, run_seq_tool)



            tool_text = "\n".join([
                f"""name: {t.name}
                    description: {t.description}
                    arguments: {t.args}"""
                for t in candidate_tools
            ])

            memory_text = "\n".join([
                f"text: {m['text']}\nhotkey: {m['hotkey']}"
                for m in retrieved
            ])


            # system_prompt = f"""
            #            You are an automation agent. 
            #            You may ONLY use the tools listed below. 
            #            If no tool is appropriate, respond normally. 
                       
                        #      RULES For using tools:
                        # - You may ONLY use the tools listed below.
                        # - Output MUST be valid JSON.
                        # - Use double quotes only.
                        # - Do NOT repeat keys.
                        # - Do NOT add extra keys.
                        # - arguments MUST be an object.
                        # - No text before or after JSON.

            #            If you use a tool, your response MUST be in the following format:

            #            {{ 
            #                 "tool": "<tool_name>",
            #                 "arguments": {{ ... }} 
            #              }}
                         
            #            Return ONLY valid JSON. No text before or after JSON. Use double quotes.
            #            Never repeat keys. Never omit arguments.

            #             AVAILABLE TOOLS:
            #                 {tool_text}
            #         """
                       

            system_prompt = f"""
                    You are a computer automation agent.

                    You have TWO behaviors:

                    --------------------------------
                    1. TOOL BEHAVIOR
                    --------------------------------
                    Use this when the user wants computer actions
                    (open apps, search, type, press keys, etc.).

                    Rules:
                    - Output ONLY ONE valid JSON object.
                    - No text before or after JSON.
                    - Never output multiple JSON objects.
                    - Use double quotes only.
                    - Always include "tool" and "arguments".
                    - Never invent tools. Use only the tools listed.
                    - If multiple steps are needed, ALWAYS use Shortcut.run_sequence.

                    Format:
                    {{
                    "tool": "<tool_name>",
                    "arguments": {{ ... }}
                    }}

                    --------------------------------
                    2. CHAT BEHAVIOR
                    --------------------------------
                    Use this when the user is asking questions or chatting.
                    Respond normally. Do NOT output JSON.

                    --------------------------------
                    AVAILABLE TOOLS
                    --------------------------------
                    {tool_text}

                    --------------------------------
                    OPTIONAL MEMORY
                    --------------------------------
                    {memory_text}
"""


            
            # print(system_prompt)
           
            

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ] 

            response = chat(model="qwen3:4b-instruct", messages = messages)

            data = parse_tool_call(response["message"]["content"])

            if data is None:
                print(response["message"]["content"])
                continue
            


            tool = None
            for x in candidate_tools:
                if x.name == data["tool"]:
                    tool = x
                    break

            if tool is None:
                print("Tool not found in candidate tools")
                continue
            else:
                try:
                    result = tool.func(**data["arguments"])
                    print(result)
                except Exception as e:
                    print("Tool error:", e)

        except KeyboardInterrupt:
            print("\nExiting Program...")
            return 
        
        



if __name__ == "__main__":
    main()
