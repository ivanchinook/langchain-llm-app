#from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.prompts import PromtTemplate
from langchain.chains import LLMChains
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type):
    llm=OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate()
        input_variables=["animal_type"]
        template="I have a {animal_type} pet name and I want a cool name for it. Suggest me five cool names for my pet."
    name_chain=LLMChains(llm=llm,prompt=prompt_template_name)

    respone=name_chain({'animal_type': animal_type})
    return respone;

if __name__ == "__main__":
    print(generate_pet_name())
