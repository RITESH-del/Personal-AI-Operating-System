# from app.gui import SearchBar
from .Store import model # relative package
from tool_kit import tools, System
from ollama import chat
import faiss
import json

# run with python -m src


# load faiss.index file
index = faiss.read_index("faiss.index")


# Helper function
def parse_tool_call(text):
    try:
        data = json.loads(text)
        if "tool" in data and "arguments" in data:
            return data
    except:
        return None



def main():
    # app = SearchBar()
    # app.run()


    print("Connected to ollama\n")
    while True:

        try:
            user_input = str(input("Enter Prompt:"))

            query_embedding = model.encode(
                [user_input], normalize_embeddings=True
            )

            scores, indices = index.search(query_embedding, k=5)

            candidate_tools = [tools[i] for i in indices[0]]

            tool_text = "\n".join([
                f"""name: {t.name}
                    description: {t.description}
                    arguments: {t.args}"""
                for t in candidate_tools
            ])

            system_prompt = f"""
                       You are an automation agent. 

                        You may ONLY use the tools listed below. 
                        If no tool is appropriate, respond normally. 
                       
                       if you aren't using a tool, respond to user request appropriately. 
                       If you use a tool, respond ONLY in JSON using the below given JSON schema: 

                       {{ 
                            "tool": "<tool_name>",
                            "arguments": {{ ... }} 
                         }}

                        AVAILABLE TOOLS:
                            {tool_text}
                    """
            
            # print(system_prompt)
           
            

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ] 

            response = chat(model="qwen2.5:3b", messages = messages)

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


