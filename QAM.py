import torch
from transformers import pipeline

# Load the question answering model
qa_model = pipeline("question-answering")


# Function to interact with the model
def answer_question(context, question):
    # Generate an answer to the question
    answer = qa_model(question=question, context=context)
    return answer['answer']


if __name__ == "__main__":
    # Example context and question
    context = """
    Transformers (formerly known as pytorch-transformers and pytorch-pretrained-bert) provides general-purpose architectures (BERT, GPT-2, RoBERTa, XLM, DistilBert, XLNet…) for Natural Language Understanding (NLU) and Natural Language Generation (NLG) with over 32+ pretrained models in 100+ languages and deep interoperability between TensorFlow 2.0 and PyTorch.
    """

    question = "What does Transformers provide?"

    # Get the answer
    answer = answer_question(context, question)

    print("Question:", question)
    print("Answer:", answer)