from abc import ABC, abstractmethod
from agno.agent import Agent

class AgentLike(ABC):

    @property
    @abstractmethod
    def agent(self) -> Agent:
        """
        Get the agent instance.
        
        Returns:
            Agent: The agent instance.
        """