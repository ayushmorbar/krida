import json
import re
from typing import Optional, List, Dict
from julep import Julep

class JulepService:
    def __init__(self, api_key: str):
        self.client = Julep(api_key=api_key)
        self.agent_id = self._create_culinary_agent()

    def _create_culinary_agent(self) -> str:
        agent_name = "Krida Culinary Expert"
        system_prompt = (
            "You are a world-class culinary expert, food historian, and engaging travel guide. "
            "Your goal is to provide accurate, structured data in JSON format when asked, "
            "and to write captivating, blog-style narratives when prompted for a tour."
        )
        try:
            agent = self.client.agents.create(name=agent_name, about=system_prompt, model='gpt-4o')
            print(f"INFO: Created Julep agent '{agent_name}' with ID: {self.client.api_key[:5]}...{agent.id[-5:]}")
            return agent.id
        except Exception as e:
            print(f"ERROR: Failed to create Julep agent: {e}")
            raise

    def _extract_json_from_response(self, content: str) -> Optional[str]:
        match = re.search(r'``````', content, re.DOTALL)
        if match:
            return match.group(1)
        match = re.search(r'(\{.*\}|\[.*\])', content, re.DOTALL)
        if match:
            return match.group(0)
        return None

    def get_iconic_dishes(self, city: str) -> Optional[List[str]]:
        user_prompt = (
            f"List exactly 3 iconic, must-try local dishes from {city}. "
            "Provide your answer as a valid JSON array of strings, like [\"Dish A\", \"Dish B\", \"Dish C\"]. "
            "Do not include any text outside of the JSON array."
        )
        try:
            session = self.client.sessions.create(agent=self.agent_id)
            chat_response = self.client.sessions.chat(session_id=session.id, messages=[{'role': 'user', 'content': user_prompt}], stream=False)
            content = chat_response.choices[0].message.content
            json_str = self._extract_json_from_response(content)
            if not json_str: return None
            dishes = json.loads(json_str)
            return dishes
        except Exception as e:
            print(f"ERROR: During dish discovery for {city}: {e}\nDEBUG: Raw response was: {content}")
            return None

    def find_restaurants_for_dish(self, city: str, dish_name: str) -> Optional[Dict]:
        user_prompt = (
            f'Find the single best, most highly-rated, and authentic restaurant in {city} that is famous for serving "{dish_name}". '
            'Provide your answer as a valid JSON object with three keys: "name" (string), "rating" (string), and "reason" (a short string). '
            'Do not include any text outside of the JSON object.'
        )
        try:
            session = self.client.sessions.create(agent=self.agent_id)
            chat_response = self.client.sessions.chat(session_id=session.id, messages=[{'role': 'user', 'content': user_prompt}], stream=False)
            content = chat_response.choices[0].message.content
            json_str = self._extract_json_from_response(content)
            if not json_str: return None
            return json.loads(json_str)
        except Exception as e:
            print(f"ERROR: During restaurant search for {dish_name}: {e}\nDEBUG: Raw response was: {content}")
            return None
            
    def generate_tour_narrative(self, city: str, weather: str, dining_suggestion: str, tour_data: Dict) -> Optional[str]:
        # Format the tour_data into a string for the prompt
        prompt_context = f"City: {city}\n"
        prompt_context += f"Current Weather: {weather}\n"
        prompt_context += f"Dining Suggestion: {dining_suggestion}\n\n"
        prompt_context += "Here is the itinerary data:\n"
        for meal, details in tour_data.items():
            prompt_context += f"- {meal.capitalize()}: We'll be having {details['dish']} at {details['restaurant']['name']}.\n"

        user_prompt = (
            "You are writing a fun, engaging blog post for a one-day foodie tour. "
            "Use the context provided below to create a narrative. The tone should be enthusiastic and descriptive. "
            "Structure the post with headings for Breakfast, Lunch, and Dinner. "
            "Subtly weave the weather and the indoor/outdoor dining suggestion into the narrative. "
            "Make the descriptions of the food sound delicious.\n\n"
            f"--- CONTEXT ---\n{prompt_context}"
        )

        try:
            session = self.client.sessions.create(agent=self.agent_id)
            chat_response = self.client.sessions.chat(
                session_id=session.id,
                messages=[{'role': 'user', 'content': user_prompt}],
                stream=False
            )
            return chat_response.choices[0].message.content
        except Exception as e:
            print(f"ERROR: During narrative generation for {city}: {e}")
            return None
