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

    def _get_budget_context(self, budget: str) -> str:
        """Convert budget input to descriptive context for AI prompts with enhanced support"""
        budget_lower = budget.lower().strip()
        
        # Handle numeric budgets (assuming USD per meal)
        if budget_lower.replace('$', '').replace(',', '').isdigit():
            amount = int(budget_lower.replace('$', '').replace(',', ''))
            if amount < 15:
                return "budget-friendly (under $15 per meal)"
            elif amount < 35:
                return "mid-range ($15-35 per meal)"
            elif amount < 75:
                return "upscale ($35-75 per meal)"
            else:
                return "luxury ($75+ per meal)"
        
        # Enhanced keyword mapping for natural language
        budget_mapping = {
            # Budget-friendly variations
            'budget': 'budget-friendly (under $15 per meal)',
            'cheap': 'budget-friendly (under $15 per meal)',
            'low': 'budget-friendly (under $15 per meal)',
            'affordable': 'budget-friendly (under $15 per meal)',
            'inexpensive': 'budget-friendly (under $15 per meal)',
            'economical': 'budget-friendly (under $15 per meal)',
            'frugal': 'budget-friendly (under $15 per meal)',
            'tight': 'budget-friendly (under $15 per meal)',
            
            # Mid-range variations  
            'mid': 'mid-range ($15-35 per meal)',
            'middle': 'mid-range ($15-35 per meal)',
            'medium': 'mid-range ($15-35 per meal)',
            'moderate': 'mid-range ($15-35 per meal)',
            'average': 'mid-range ($15-35 per meal)',
            'standard': 'mid-range ($15-35 per meal)',
            'normal': 'mid-range ($15-35 per meal)',
            'regular': 'mid-range ($15-35 per meal)',
            'reasonable': 'mid-range ($15-35 per meal)',
            
            # Upscale variations
            'high': 'upscale ($35-75 per meal)',
            'expensive': 'upscale ($35-75 per meal)',
            'upscale': 'upscale ($35-75 per meal)',
            'fancy': 'upscale ($35-75 per meal)',
            'nice': 'upscale ($35-75 per meal)',
            'good': 'upscale ($35-75 per meal)',
            'quality': 'upscale ($35-75 per meal)',
            'fine': 'upscale ($35-75 per meal)',
            'elevated': 'upscale ($35-75 per meal)',
            
            # Luxury variations
            'luxury': 'luxury ($75+ per meal)',
            'premium': 'luxury ($75+ per meal)',
            'deluxe': 'luxury ($75+ per meal)',
            'exclusive': 'luxury ($75+ per meal)',
            'elite': 'luxury ($75+ per meal)',
            'top': 'luxury ($75+ per meal)',
            'best': 'luxury ($75+ per meal)',
            'finest': 'luxury ($75+ per meal)',
            'gourmet': 'luxury ($75+ per meal)',
            'michelin': 'luxury ($75+ per meal)',
            'splurge': 'luxury ($75+ per meal)',
            'extravagant': 'luxury ($75+ per meal)'
        }
        
        return budget_mapping.get(budget_lower, 'mid-range ($15-35 per meal)')

    def get_iconic_dishes(self, city: str, budget: str = "mid") -> Optional[List[str]]:
        budget_context = self._get_budget_context(budget)
        user_prompt = (
            f"List exactly 3 iconic, must-try local dishes from {city} that are suitable for a {budget_context} budget. "
            "Focus on authentic, local specialties that represent the city's culinary culture. "
            "Provide your answer as a valid JSON array of strings, like [\"Dish A\", \"Dish B\", \"Dish C\"]. "
            "Do not include any text outside of the JSON array."
        )
        try:
            session = self.client.sessions.create(agent=self.agent_id)
            chat_response = self.client.sessions.chat(session_id=session.id, messages=[{'role': 'user', 'content': user_prompt}], stream=False)
            content = chat_response.choices[0].message.content
            json_str = self._extract_json_from_response(content)
            if not json_str:
                return None
            dishes = json.loads(json_str)
            return dishes
        except Exception as e:
            print(f"ERROR: During dish discovery for {city}: {e}\nDEBUG: Raw response was: {content}")
            return None

    def find_restaurants_for_dish(self, city: str, dish_name: str, budget: str = "mid") -> Optional[Dict]:
        budget_context = self._get_budget_context(budget)
        user_prompt = (
            f'Find the single best, most highly-rated, and authentic restaurant in {city} that is famous for serving "{dish_name}" '
            f'and fits a {budget_context} budget. '
            'Provide your answer as a valid JSON object with four keys: "name" (string), "rating" (string), "reason" (a short string), and "price_range" (string). '
            'Do not include any text outside of the JSON object.'
        )
        try:
            session = self.client.sessions.create(agent=self.agent_id)
            chat_response = self.client.sessions.chat(session_id=session.id, messages=[{'role': 'user', 'content': user_prompt}], stream=False)
            content = chat_response.choices[0].message.content
            json_str = self._extract_json_from_response(content)
            if not json_str:
                return None
            return json.loads(json_str)
        except Exception as e:
            print(f"ERROR: During restaurant search for {dish_name}: {e}\nDEBUG: Raw response was: {content}")
            return None
            
    def generate_tour_narrative(self, city: str, weather: str, dining_suggestion: str, tour_data: Dict, budget: str = "mid") -> Optional[str]:
        budget_context = self._get_budget_context(budget)
        # Format the tour_data into a string for the prompt
        prompt_context = f"City: {city}\n"
        prompt_context += f"Current Weather: {weather}\n"
        prompt_context += f"Dining Suggestion: {dining_suggestion}\n"
        prompt_context += f"Budget: {budget_context}\n\n"
        prompt_context += "Here is the itinerary data:\n"
        for meal, details in tour_data.items():
            restaurant = details['restaurant']
            price_info = f" (Price range: {restaurant.get('price_range', 'N/A')})" if 'price_range' in restaurant else ""
            prompt_context += f"- {meal.capitalize()}: We'll be having {details['dish']} at {restaurant['name']}{price_info}.\n"

        user_prompt = (
            "You are writing a fun, engaging blog post for a one-day foodie tour. "
            "Use the context provided below to create a narrative. The tone should be enthusiastic and descriptive. "
            "Structure the post with headings for Breakfast, Lunch, and Dinner. "
            "Subtly weave the weather, budget considerations, and the indoor/outdoor dining suggestion into the narrative. "
            "Make the descriptions of the food sound delicious and mention value for money when appropriate.\n\n"
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
