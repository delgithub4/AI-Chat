from services.prompt_client import PromptClient
from services.agent_client import AgentClient
from services.rag_client import RAGClient
from services.vector_client import VectorClient


class ChatService:

    def __init__(self):

        self.prompt = PromptClient()

        self.agent = AgentClient()

        self.rag = RAGClient()

        self.vector = VectorClient()

    def chat(self):

        return {

            "prompt": self.prompt.get_prompt(),

            "agent": self.agent.plan(),

            "rag": self.rag.retrieve(),

            "vector": self.vector.search(),

            "response":

            "Hello from AI Chat."

        }
