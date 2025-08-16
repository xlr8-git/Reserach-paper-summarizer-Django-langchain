import json
import os
from langchain_core.prompts import PromptTemplate

def load_prompt(prompt_name: str) -> PromptTemplate:
    """
    Load a prompt template from prompts.json by name.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompts_path = os.path.join(base_dir, "prompts.json")

    with open(prompts_path, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    if prompt_name not in prompts:
        raise ValueError(f"Prompt '{prompt_name}' not found in prompts.json")

    prompt_data = prompts[prompt_name]
    return PromptTemplate(
        input_variables=prompt_data["input_variables"],
        template=prompt_data["template"]
    )
