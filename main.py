# main.py

import os
from services.weather import WeatherService
from services.julep_service import JulepService
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

console = Console()

def run_tour_for_city(city: str, weather_service: WeatherService, julep_service: JulepService):
    """
    Runs the entire foodie tour generation workflow for a single city.
    """
    # City header
    city_title = Text(f"Generating Foodie Tour for {city.upper()}", style="bold magenta")
    console.print(Panel(city_title, border_style="bright_blue", padding=(0, 2)))
    console.print()

    # 1. Weather Check
    console.print("🌤️  [bold cyan]Checking weather for[/bold cyan]", city, "...")
    weather_data = weather_service.get_weather(city)
    if not weather_data:
        console.print(f"[red]Could not get weather for {city}. Skipping.[/red]")
        return

    temp = weather_data['main']['temp']
    condition = weather_data['weather'][0]['main']
    weather_summary = f"{condition}, {temp}°C"
    dining_suggestion = "cozy indoor dining" if temp < 15 or "Rain" in condition else "delightful outdoor dining"
    console.print(f"[green]Weather is {weather_summary}. Suggesting {dining_suggestion}.[/green]")
    console.print()

    # 2. Dish Discovery
    console.print("🍽️  [bold cyan]Finding iconic dishes in[/bold cyan]", city, "...")
    dishes = julep_service.get_iconic_dishes(city)
    if not dishes or len(dishes) < 3:
        console.print(f"[red]Could not get a valid list of dishes for {city}. Skipping.[/red]")
        return
    console.print(f"[green]Found dishes:[/green] {', '.join(dishes)}")
    console.print()

    # 3. Restaurant Search for each dish
    meals = ['breakfast', 'lunch', 'dinner']
    meal_emojis = ['🥐', '🍽️', '🍷']
    tour_data = {}
    for i, meal in enumerate(meals):
        dish = dishes[i]
        console.print(f"{meal_emojis[i]}  [bold cyan]Finding a restaurant for {meal.capitalize()}[/bold cyan] ([italic]{dish}[/italic])...")
        restaurant = julep_service.find_restaurants_for_dish(city, dish)
        if not restaurant:
            console.print(f"[red]Could not find a restaurant for {dish}. Skipping city.[/red]")
            return
        tour_data[meal] = {"dish": dish, "restaurant": restaurant}
        console.print(f"[green]Found:[/green] {restaurant['name']}")
    console.print()

    # 4. Narrative Generation
    console.print("📝 [bold cyan]Generating the final tour narrative...[/bold cyan]")
    narrative = julep_service.generate_tour_narrative(city, weather_summary, dining_suggestion, tour_data)
    console.print()
    
    # 5. Final Output
    tour_header = Text(f"Your One-Day Foodie Tour in {city.upper()}", style="bold yellow")
    console.print(Panel(tour_header, border_style="bright_green", padding=(0, 2)))
    console.print()
    
    if narrative:
        # Render the narrative as markdown
        markdown_narrative = Markdown(narrative)
        console.print(markdown_narrative)
    else:
        console.print("[red]Sorry, we couldn't generate the tour narrative at this time.[/red]")
    
    console.print()
    console.print("=" * 80, style="dim")
    console.print()


def main():
    """
    Main function to run the Krida AI workflow.
    """
    # Welcome header
    welcome_text = Text("🍽️ Krida AI Foodie Tour Generator 🤖", style="bold bright_magenta")
    console.print(Panel(welcome_text, border_style="bright_cyan", padding=(1, 4)))
    console.print()
    
    # Load API keys from environment variables
    openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
    julep_api_key = os.getenv('JULEP_API_KEY')

    if not openweather_api_key or not julep_api_key:
        console.print("[bold red]FATAL ERROR:[/bold red] Make sure OPENWEATHER_API_KEY and JULEP_API_KEY are set.")
        return

    # Initialize services
    console.print("🚀 [bold green]Initializing Krida services...[/bold green]")
    try:
        weather_service = WeatherService(api_key=openweather_api_key)
        julep_service = JulepService(api_key=julep_api_key)
        console.print("[green]✅ Services initialized successfully![/green]")
        console.print()
    except Exception as e:
        console.print(f"[bold red]Failed to initialize services:[/bold red] {e}")
        return

    # Define the list of cities to process
    cities_to_tour = ['Delhi', 'Paris', 'Tokyo', 'New York']
    
    cities_text = Text(f"🌍 Planning tours for: {', '.join(cities_to_tour)}", style="bold blue")
    console.print(Panel(cities_text, border_style="blue", padding=(0, 2)))
    console.print()

    for city in cities_to_tour:
        run_tour_for_city(city, weather_service, julep_service)

if __name__ == "__main__":
    main()
