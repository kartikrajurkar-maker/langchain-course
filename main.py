from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
load_dotenv()

def main():
    print("Hello from langchain-course!")
information = " Shah Rukh Khan was born and raised in New Delhi . His Muslim family is from Peshawar ; [ 1 ] the suffix 'Khan' indicates his Afghan - Pashtun heritage. [ 2 ] His mother, Fatima, was a social worker in Delhi and died of sepsis in 1991. His father, Taj Mohammed, was a lawyer and died of cancer in 1981. Shah Rukh has an older sister named Shehnaz (nickname: Lala Rukh).Shah Rukh Khan has been married to Gauri (born October 8, 1970), who comes from a Hindu family, since 1991. They have three children: two sons, Aryan and AbRam (born 1997 and 2013, respectively), and a daughter, Suhana (born 2000). Aryan has some film experience, having played the young boy Rahul, a character portrayed by his father, in the film Kabhi Khushi Kabhie Gham . AbRam appears in the end credits of Happy New Year alongside his father. AbRam was born via surrogacy, as the risk of another pregnancy was too high for Gauri Khan."

sample_template = f"Given the information {information} about a person i want you to create: 1. a short summary 2. two facts about them"

summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=sample_template)
llm = ChatGroq(model="llama-3.1-8b-instant")
if __name__ == "__main__":
    main()
chain = summary_prompt_template | llm
response = chain.invoke(input={"information": information})
print(response.content)