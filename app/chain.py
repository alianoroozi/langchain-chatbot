from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI


OPENAI_MODEL_NAME = "gpt-4-turbo-preview"
llm = ChatOpenAI(model=OPENAI_MODEL_NAME)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

basic_chain = prompt | llm

message_history = ChatMessageHistory()
chain = RunnableWithMessageHistory(
    basic_chain,
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# chain.invoke(
#     {"input": "Hi!"},
#     {"configurable": {"session_id": "unused"}},
# )