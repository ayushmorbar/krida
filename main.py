import os
from services.weather import WeatherService
from services.julep_service import JulepService
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from typing import List, Tuple

console = Console()

class InteractiveMenu:
    def __init__(self):
        self.cities_to_tour = []
        self.budget = "mid"
        self.version = "v1.0.2"
        
    def display_welcome(self):
        """Display welcome screen and app info with enhanced design"""
        # ASCII art style title
        title_art = """
╔═══════════════════════════════════════════════════╗
║  🍽️  KRIDA AI FOODIE TOUR GENERATOR v1.0.2  🤖  ║
╚═══════════════════════════════════════════════════╝
        """
        console.print(title_art, style="bold bright_magenta")
        
        # Main welcome panel
        welcome_content = Text()
        welcome_content.append("Welcome to Krida! ", style="bold cyan")
        welcome_content.append("Your AI-powered culinary adventure companion.\n\n", style="white")
        welcome_content.append("✨ Personalized foodie tours for any city worldwide\n", style="bright_green")
        welcome_content.append("🌤️ Weather-smart dining recommendations\n", style="bright_blue")
        welcome_content.append("🍛 Authentic local cuisine discovery\n", style="bright_yellow")
        welcome_content.append("💰 Budget-conscious restaurant selection\n", style="bright_red")
        welcome_content.append("📖 Beautiful narrative-driven experiences\n", style="bright_magenta")
        welcome_content.append("🌍 Support for any city globally", style="bright_cyan")
        
        console.print(Panel(
            welcome_content, 
            title="🍽️ About Krida", 
            title_align="center",
            border_style="bright_cyan", 
            padding=(1, 2)
        ))
        console.print()
        
        # Quick tip
        tip_text = Text("💡 Tip: ", style="bold yellow")
        tip_text.append("You can select multiple cities and customize your budget to create the perfect culinary journey!", style="dim white")
        console.print(Panel(tip_text, border_style="yellow", padding=(0, 1)))
        console.print()

    def get_cities(self) -> List[str]:
        """Enhanced interactive city selection with better UX"""
        console.print("🌍 [bold cyan]City Selection[/bold cyan]")
        console.print("Enter the cities you'd like to explore for your foodie adventure!")
        console.print("[dim]Examples: Paris, Tokyo, New York, Mumbai, Barcelona, Bangkok, etc.[/dim]")
        console.print()
        
        cities = []
        city_suggestions = [
            "Popular choices: Paris 🇫🇷, Tokyo 🇯🇵, New York 🇺🇸, Mumbai 🇮🇳, Barcelona 🇪🇸",
            "Food capitals: Bangkok 🇹🇭, Istanbul 🇹🇷, Lima 🇵🇪, Naples 🇮🇹, Seoul 🇰🇷",
            "Hidden gems: Penang 🇲🇾, Lyon 🇫🇷, Osaka 🇯🇵, Mexico City 🇲🇽, Tel Aviv 🇮🇱"
        ]
        
        while True:
            if len(cities) == 0:
                console.print(f"[dim]{city_suggestions[0]}[/dim]")
                city = Prompt.ask("🎯 Enter your first city")
            else:
                remaining_suggestions = city_suggestions[len(cities) % len(city_suggestions)]
                console.print(f"[dim]{remaining_suggestions}[/dim]")
                
                prompt_text = "🌟 Add another city"
                if len(cities) == 1:
                    prompt_text += f" [dim](or press Enter to continue with {cities[0]})[/dim]"
                else:
                    prompt_text += f" [dim](or press Enter to continue with {len(cities)} cities)[/dim]"
                
                city = Prompt.ask(prompt_text, default="")
            
            if city.strip() == "":
                if len(cities) > 0:
                    break
                else:
                    console.print("[red]🚫 Please enter at least one city to get started![/red]")
                    continue
            
            # Clean and format city name
            city = " ".join(word.capitalize() for word in city.strip().split())
            
            if city not in cities:
                cities.append(city)
                console.print(f"[green]✅ Added {city} to your tour![/green]")
                
                # Show current list if more than one city
                if len(cities) > 1:
                    cities_display = ", ".join(cities)
                    console.print(f"[dim]Current cities: {cities_display}[/dim]")
            else:
                console.print(f"[yellow]⚠️  {city} is already in your list![/yellow]")
                
            if len(cities) >= 5:
                console.print("[yellow]🏁 Maximum 5 cities reached for optimal experience.[/yellow]")
                break
            
            console.print()
        
        console.print()
        final_cities = ", ".join(cities)
        console.print(f"[bold green]🎉 Selected cities: {final_cities}[/bold green]")
        return cities

    def get_budget(self) -> str:
        """Enhanced interactive budget selection with natural language support"""
        console.print()
        console.print("💰 [bold cyan]Budget Selection[/bold cyan]")
        console.print("Choose how much you'd like to spend on your culinary adventure:")
        console.print()
        
        # Enhanced budget options table
        table = Table(show_header=True, header_style="bold magenta", border_style="cyan")
        table.add_column("Option", style="bold cyan", width=8, justify="center")
        table.add_column("Budget Level", style="bold white", width=18)
        table.add_column("Price Range", style="bold green", width=18)
        table.add_column("Perfect For", style="dim", width=40)
        
        table.add_row(
            "1", "Budget-Friendly", "Under $15/meal", 
            "Street food, local joints, authentic hole-in-the-wall gems"
        )
        table.add_row(
            "2", "Mid-Range", "$15-35/meal", 
            "Popular restaurants, good quality dining, tourist favorites"
        )
        table.add_row(
            "3", "Upscale", "$35-75/meal", 
            "Fine dining, trendy spots, chef-recommended establishments"
        )
        table.add_row(
            "4", "Luxury", "$75+/meal", 
            "Michelin-starred, celebrity chef venues, ultimate experiences"
        )
        table.add_row(
            "5", "Custom", "Your choice", 
            "Enter specific amount or use keywords like 'cheap', 'expensive'"
        )
        
        console.print(table)
        console.print()
        
        # Additional tips
        console.print("[dim]💡 Tips:[/dim]")
        console.print("[dim]• Budget-friendly doesn't mean less delicious - often the best local food![/dim]")
        console.print("[dim]• Mid-range offers great balance of quality and value[/dim]")
        console.print("[dim]• Custom option accepts words like 'cheap', 'moderate', 'expensive', 'luxury'[/dim]")
        console.print()
        
        while True:
            choice = Prompt.ask(
                "💳 Select your budget preference",
                choices=["1", "2", "3", "4", "5"],
                default="2"
            )
            
            if choice == "1":
                console.print("[green]🎯 Great choice! Budget-friendly often means the most authentic experiences![/green]")
                return "budget"
            elif choice == "2":
                console.print("[green]🎯 Perfect balance of quality and value![/green]")
                return "mid"
            elif choice == "3":
                console.print("[green]🎯 Excellent! You'll enjoy some fantastic upscale dining![/green]")
                return "upscale"
            elif choice == "4":
                console.print("[green]🎯 Luxury it is! Prepare for extraordinary culinary experiences![/green]")
                return "luxury"
            elif choice == "5":
                console.print("💭 You can enter:")
                console.print("• A number (like '25', '50', '$100')")
                console.print("• Keywords like: cheap, affordable, moderate, expensive, luxury, premium")
                console.print("• Descriptions like: 'mid range', 'high end', 'budget friendly'")
                console.print()
                
                custom_budget = Prompt.ask("✨ Enter your budget preference")
                processed_budget = self._process_custom_budget(custom_budget)
                
                if processed_budget:
                    # Display what was understood
                    budget_descriptions = {
                        'budget': 'Budget-Friendly (under $15/meal)',
                        'mid': 'Mid-Range ($15-35/meal)',
                        'upscale': 'Upscale ($35-75/meal)',
                        'luxury': 'Luxury ($75+/meal)'
                    }
                    
                    if processed_budget.isdigit():
                        console.print(f"[green]🎯 Got it! ${processed_budget} per meal budget set.[/green]")
                    else:
                        description = budget_descriptions.get(processed_budget, f"{processed_budget} budget")
                        console.print(f"[green]🎯 Perfect! {description} selected.[/green]")
                    
                    return processed_budget
                else:
                    console.print("[red]❌ I didn't understand that. Let's try again![/red]")
                    continue

    def _process_custom_budget(self, budget_input: str) -> str:
        """Process custom budget input with natural language understanding"""
        if not budget_input or not budget_input.strip():
            return None
            
        budget_clean = budget_input.lower().strip()
        
        # Remove common symbols and clean up
        budget_clean = budget_clean.replace('$', '').replace(',', '').replace('/', '').strip()
        
        # Try to extract number first
        import re
        number_match = re.search(r'\d+', budget_clean)
        if number_match:
            number = number_match.group()
            try:
                int(number)  # Validate it's a valid number
                return number
            except ValueError:
                pass
        
        # Natural language processing for budget keywords
        budget_keywords = {
            # Budget-friendly variations
            'cheap': 'budget', 'low': 'budget', 'budget': 'budget', 'affordable': 'budget',
            'inexpensive': 'budget', 'economical': 'budget', 'budget friendly': 'budget',
            'budget-friendly': 'budget', 'frugal': 'budget', 'tight': 'budget',
            
            # Mid-range variations  
            'mid': 'mid', 'middle': 'mid', 'medium': 'mid', 'moderate': 'mid',
            'average': 'mid', 'standard': 'mid', 'normal': 'mid', 'regular': 'mid',
            'mid range': 'mid', 'mid-range': 'mid', 'reasonable': 'mid',
            
            # Upscale variations
            'high': 'upscale', 'expensive': 'upscale', 'upscale': 'upscale',
            'fancy': 'upscale', 'nice': 'upscale', 'good': 'upscale',
            'quality': 'upscale', 'fine': 'upscale', 'elevated': 'upscale',
            'high end': 'upscale', 'high-end': 'upscale',
            
            # Luxury variations
            'luxury': 'luxury', 'premium': 'luxury', 'deluxe': 'luxury',
            'exclusive': 'luxury', 'elite': 'luxury', 'top': 'luxury',
            'best': 'luxury', 'finest': 'luxury', 'gourmet': 'luxury',
            'michelin': 'luxury', 'splurge': 'luxury', 'extravagant': 'luxury'
        }
        
        # Check for direct matches
        if budget_clean in budget_keywords:
            return budget_keywords[budget_clean]
        
        # Check for partial matches (useful for phrases)
        for keyword, category in budget_keywords.items():
            if keyword in budget_clean:
                return category
        
        return None

    def confirm_selections(self, cities: List[str], budget: str) -> bool:
        """Enhanced confirmation screen with beautiful formatting"""
        console.print()
        
        # Create a beautiful summary panel
        summary_content = Text()
        summary_content.append("🎯 Ready to create your personalized foodie tours!\n\n", style="bold bright_green")
        
        # Cities section
        summary_content.append("🌍 Destinations:\n", style="bold bright_cyan")
        for i, city in enumerate(cities, 1):
            summary_content.append(f"   {i}. {city}\n", style="bright_white")
        summary_content.append("\n")
        
        # Budget section  
        summary_content.append("💰 Budget Level:\n", style="bold bright_yellow")
        if budget.isdigit():
            summary_content.append(f"   ${budget} per meal (Custom)\n", style="bright_white")
        else:
            budget_mapping = {
                'budget': '💵 Budget-Friendly (Under $15/meal)',
                'mid': '💳 Mid-Range ($15-35/meal)', 
                'upscale': '💎 Upscale ($35-75/meal)',
                'luxury': '👑 Luxury ($75+/meal)'
            }
            budget_display = budget_mapping.get(budget, f"{budget.title()} Budget")
            summary_content.append(f"   {budget_display}\n", style="bright_white")
        
        # Add tour info
        summary_content.append("\n🍽️ What you'll get:\n", style="bold bright_magenta")
        summary_content.append("   • Weather-optimized dining recommendations\n", style="dim bright_white")
        summary_content.append("   • Authentic local cuisine discoveries\n", style="dim bright_white")
        summary_content.append("   • Budget-appropriate restaurant selections\n", style="dim bright_white")
        summary_content.append("   • Engaging narrative tour guides\n", style="dim bright_white")
        
        console.print(Panel(
            summary_content,
            title="🎉 Your Foodie Adventure Summary",
            title_align="center",
            border_style="bright_green",
            padding=(1, 2)
        ))
        console.print()
        
        # Confirmation with options
        console.print("Choose your next step:")
        console.print("  [bold green]Y[/bold green] - Let's go! Start generating tours")
        console.print("  [bold yellow]M[/bold yellow] - Modify my selections") 
        console.print("  [bold red]Q[/bold red] - Quit for now")
        console.print()
        
        while True:
            response = Prompt.ask(
                "What would you like to do?",
                choices=["y", "yes", "m", "modify", "q", "quit"],
                default="y"
            ).lower()
            
            if response in ["y", "yes"]:
                console.print("[bold bright_green]🚀 Fantastic! Let's start your culinary adventure![/bold bright_green]")
                return True
            elif response in ["m", "modify"]:
                return False
            elif response in ["q", "quit"]:
                console.print()
                goodbye_text = Text("👋 Thanks for trying Krida! Your culinary adventures await whenever you're ready.", style="bold bright_cyan")
                console.print(Panel(goodbye_text, border_style="bright_blue", padding=(1, 2)))
                console.print("🍽️ Bon appétit! Come back anytime for more foodie discoveries.")
                exit(0)

    def show_main_menu(self) -> Tuple[List[str], str]:
        """Enhanced main interactive menu with better flow"""
        self.display_welcome()
        
        while True:
            try:
                cities = self.get_cities()
                budget = self.get_budget()
                
                if self.confirm_selections(cities, budget):
                    console.print()
                    return cities, budget
                else:
                    console.print()
                    console.print("[bright_yellow]📝 Let's modify your selections...[/bright_yellow]")
                    console.print()
                    continue
                    
            except KeyboardInterrupt:
                console.print("\n\n[yellow]👋 Thanks for trying Krida! Come back anytime for foodie adventures![/yellow]")
                exit(0)
            except Exception as e:
                console.print(f"\n[red]❌ Oops! Something went wrong: {e}[/red]")
                console.print("[dim]Let's try again...[/dim]")
                console.print()
                continue


def run_tour_for_city(city: str, budget: str, weather_service: WeatherService, julep_service: JulepService):
    """Enhanced tour generation with better user experience"""
    # Beautiful city header with progress indication
    budget_display = f"${budget}/meal" if budget.isdigit() else budget.title()
    
    city_header = Text()
    city_header.append("🏙️ ", style="bright_yellow")
    city_header.append(f"Exploring {city.upper()}", style="bold bright_magenta")
    city_header.append(f" ({budget_display} Budget)", style="bright_cyan")
    
    console.print(Panel(
        city_header, 
        border_style="bright_blue", 
        padding=(1, 2),
        title="🍽️ Foodie Tour Generation",
        title_align="center"
    ))
    console.print()

    # Progress steps with enhanced messaging
    steps = [
        ("🌤️", "Checking local weather conditions", "Weather analysis"),
        ("🍽️", "Discovering iconic local dishes", "Culinary research"), 
        ("🔍", "Finding perfect restaurants", "Restaurant matching"),
        ("📝", "Crafting your tour narrative", "Story creation")
    ]
    
    try:
        # Step 1: Weather Check with enhanced feedback
        console.print(f"{steps[0][0]} [bold cyan]{steps[0][1]}[/bold cyan] for {city}...")
        
        with console.status("[bold green]Fetching weather data...", spinner="dots"):
            weather_data = weather_service.get_weather(city)
            
        if not weather_data:
            console.print(f"[red]❌ Could not get weather data for {city}. This might affect recommendations.[/red]")
            console.print("[dim]Proceeding with general dining suggestions...[/dim]")
            weather_summary = "Variable conditions"
            dining_suggestion = "flexible indoor/outdoor dining options"
        else:
            temp = weather_data['main']['temp']
            condition = weather_data['weather'][0]['main']
            weather_summary = f"{condition}, {temp}°C"
            dining_suggestion = "cozy indoor dining" if temp < 15 or "Rain" in condition else "delightful outdoor dining"
            
            console.print(f"[green]✅ Weather: {weather_summary}[/green]")
            console.print(f"[bright_blue]🎯 Recommendation: Perfect for {dining_suggestion}[/bright_blue]")
        console.print()

        # Step 2: Dish Discovery with enhanced feedback  
        console.print(f"{steps[1][0]} [bold cyan]{steps[1][1]}[/bold cyan] in {city}...")
        
        with console.status("[bold green]AI analyzing local cuisine...", spinner="dots"):
            dishes = julep_service.get_iconic_dishes(city, budget)
            
        if not dishes or len(dishes) < 3:
            console.print(f"[red]❌ Could not discover enough dishes for {city}. Skipping this city.[/red]")
            console.print("[dim]Try a different city or check your internet connection.[/dim]")
            return
            
        console.print("[green]✅ Found amazing local specialties:[/green]")
        for i, dish in enumerate(dishes, 1):
            console.print(f"   {i}. [bright_white]{dish}[/bright_white]")
        console.print()

        # Step 3: Restaurant Search with progress tracking
        console.print(f"{steps[2][0]} [bold cyan]{steps[2][1]}[/bold cyan] for your {budget_display} budget...")
        
        meals = ['breakfast', 'lunch', 'dinner']
        meal_emojis = ['🥐', '🍽️', '🍷']
        meal_names = ['Morning', 'Afternoon', 'Evening']
        tour_data = {}
        
        for i, meal in enumerate(meals):
            dish = dishes[i]
            console.print(f"   {meal_emojis[i]} [cyan]{meal_names[i]}:[/cyan] Finding restaurant for [italic]{dish}[/italic]...")
            
            with console.status(f"[bold green]Searching {meal} spots...", spinner="dots"):
                restaurant = julep_service.find_restaurants_for_dish(city, dish, budget)
                
            if not restaurant:
                console.print(f"[red]❌ Could not find a suitable restaurant for {dish}.[/red]")
                console.print("[dim]Skipping this city. Try a different location.[/dim]")
                return
                
            tour_data[meal] = {"dish": dish, "restaurant": restaurant}
            price_info = f" ({restaurant.get('price_range', 'Budget-friendly')})" if 'price_range' in restaurant else ""
            console.print(f"   [green]✅ {restaurant['name']}{price_info}[/green]")
        console.print()

        # Step 4: Narrative Generation with anticipation building
        console.print(f"{steps[3][0]} [bold cyan]{steps[3][1]}[/bold cyan] for your {city} adventure...")
        console.print("[dim]This is where the magic happens - creating your personalized tour story...[/dim]")
        
        with console.status("[bold green]AI crafting your tour narrative...", spinner="dots"):
            narrative = julep_service.generate_tour_narrative(city, weather_summary, dining_suggestion, tour_data, budget)
        
        console.print("[green]✅ Your personalized tour is ready![/green]")
        console.print()
        
        # Final Output with enhanced presentation
        tour_title = Text()
        tour_title.append("🎉 Your One-Day Foodie Adventure in ", style="bold bright_green")
        tour_title.append(city.upper(), style="bold bright_yellow")
        
        console.print(Panel(
            tour_title, 
            border_style="bright_green", 
            padding=(1, 2),
            title="✨ Tour Complete ✨",
            title_align="center"
        ))
        console.print()
        
        if narrative:
            # Add a small delay for dramatic effect
            import time
            time.sleep(0.5)
            
            # Render the narrative with beautiful formatting
            markdown_narrative = Markdown(narrative)
            console.print(Panel(
                markdown_narrative, 
                border_style="bright_white",
                padding=(1, 2)
            ))
        else:
            console.print(Panel(
                "[red]❌ Sorry, we couldn't generate the tour narrative at this time.\n"
                "Please check your internet connection and API keys.[/red]",
                border_style="red",
                padding=(1, 2)
            ))
        
        console.print()
        console.print("=" * 80, style="dim bright_blue")
        console.print()
        
    except KeyboardInterrupt:
        console.print(f"\n[yellow]⏸️  Tour generation for {city} interrupted by user.[/yellow]")
        raise
    except Exception as e:
        console.print(f"\n[red]❌ Error generating tour for {city}: {e}[/red]")
        console.print("[dim]You can try again or continue with other cities.[/dim]")
        console.print()


def main():
    """Enhanced main function with better error handling and UX"""
    try:
        # Environment check with helpful messaging
        openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
        julep_api_key = os.getenv('JULEP_API_KEY')

        if not openweather_api_key or not julep_api_key:
            error_panel = Text()
            error_panel.append("🚨 Missing API Keys!\n\n", style="bold red")
            error_panel.append("To use Krida, you need to set up these environment variables:\n", style="white")
            error_panel.append("• OPENWEATHER_API_KEY ", style="bright_yellow")
            error_panel.append("(for weather data)\n", style="dim")
            error_panel.append("• JULEP_API_KEY ", style="bright_yellow") 
            error_panel.append("(for AI-powered food recommendations)\n\n", style="dim")
            error_panel.append("💡 Check the .env.example file for setup instructions!", style="bright_cyan")
            
            console.print(Panel(
                error_panel,
                title="❌ Setup Required",
                title_align="center", 
                border_style="red",
                padding=(1, 2)
            ))
            return

        # Interactive menu system
        menu = InteractiveMenu()
        cities_to_tour, budget = menu.show_main_menu()
        
        # Initialize services with user feedback
        init_text = Text()
        init_text.append("🚀 Initializing Krida services...\n", style="bold bright_green")
        init_text.append("• Connecting to weather service\n", style="dim")
        init_text.append("• Setting up AI culinary expert\n", style="dim")
        init_text.append("• Preparing your personalized experience", style="dim")
        
        console.print(Panel(init_text, border_style="green", padding=(1, 2)))
        
        try:
            with console.status("[bold green]Starting services...", spinner="dots"):
                weather_service = WeatherService(api_key=openweather_api_key)
                julep_service = JulepService(api_key=julep_api_key)
                
            console.print("[bold green]✅ All systems ready! Let's begin your culinary journey![/bold green]")
            console.print()
        except Exception as e:
            console.print(f"[bold red]❌ Failed to initialize services:[/bold red] {e}")
            console.print("[dim]Please check your API keys and internet connection.[/dim]")
            return

        # Show comprehensive tour plan
        plan_content = Text()
        plan_content.append("🗺️ Your Culinary Journey Plan\n\n", style="bold bright_blue")
        plan_content.append("Destinations: ", style="bold bright_cyan")
        plan_content.append(f"{', '.join(cities_to_tour)}\n", style="bright_white")
        
        if budget.isdigit():
            plan_content.append("Budget: ", style="bold bright_yellow")
            plan_content.append(f"${budget} per meal (Custom)\n", style="bright_white")
        else:
            budget_names = {
                'budget': 'Budget-Friendly', 'mid': 'Mid-Range',
                'upscale': 'Upscale', 'luxury': 'Luxury'
            }
            plan_content.append("Budget: ", style="bold bright_yellow")
            plan_content.append(f"{budget_names.get(budget, budget.title())}\n", style="bright_white")
        
        plan_content.append(f"\nTotal cities: {len(cities_to_tour)}", style="dim")
        
        console.print(Panel(
            plan_content,
            title="🎯 Ready to Explore",
            title_align="center",
            border_style="bright_blue",
            padding=(1, 2)
        ))
        console.print()

        # Generate tours with enhanced progress tracking
        successful_tours = 0
        for i, city in enumerate(cities_to_tour):
            try:
                # Progress indicator
                progress_text = f"🌟 Tour {i+1} of {len(cities_to_tour)}"
                console.print(f"[bold bright_magenta]{progress_text}[/bold bright_magenta]")
                console.print()
                
                run_tour_for_city(city, budget, weather_service, julep_service)
                successful_tours += 1
                
                # Continue to next city (except for the last one)
                if i < len(cities_to_tour) - 1:
                    console.print()
                    next_city = cities_to_tour[i+1]
                    
                    # Give options for proceeding
                    console.print(f"[dim]Next up: {next_city}[/dim]")
                    console.print("Choose what to do next:")
                    console.print("  [bold green]C[/bold green] - Continue to next city")
                    console.print("  [bold yellow]P[/bold yellow] - Pause and finish here")
                    console.print("  [bold red]Q[/bold red] - Quit tour generation")
                    console.print()
                    
                    choice = Prompt.ask(
                        "What would you like to do?",
                        choices=["c", "continue", "p", "pause", "q", "quit"],
                        default="c"
                    ).lower()
                    
                    if choice in ["p", "pause"]:
                        console.print(f"[bright_yellow]⏸️  Pausing tour generation. You've completed {successful_tours} cities![/bright_yellow]")
                        break
                    elif choice in ["q", "quit"]:
                        console.print(f"[bright_red]🛑 Tour generation stopped. Completed {successful_tours} cities.[/bright_red]")
                        break
                    else:
                        console.print(f"[bright_green]➡️  Continuing to {next_city}...[/bright_green]")
                    
                    console.print()
                    
            except KeyboardInterrupt:
                console.print(f"\n[yellow]⏸️  Tour interrupted. Completed {successful_tours} out of {len(cities_to_tour)} cities.[/yellow]")
                break
            except Exception as e:
                console.print(f"[red]❌ Error with {city}: {e}[/red]")
                console.print("[dim]Continuing with remaining cities...[/dim]")
                console.print()
                continue
        
        # Final completion message
        console.print()
        completion_content = Text()
        if successful_tours == len(cities_to_tour):
            completion_content.append("🎉 All Tours Complete! 🎉\n\n", style="bold bright_green")
            completion_content.append(f"Successfully generated {successful_tours} personalized foodie tours!\n", style="bright_white")
            completion_content.append("Your culinary adventures await! Bon appétit! 🍽️✨", style="bright_cyan")
        elif successful_tours > 0:
            completion_content.append("🌟 Tours Partially Complete\n\n", style="bold bright_yellow")
            completion_content.append(f"Generated {successful_tours} out of {len(cities_to_tour)} tours.\n", style="bright_white")
            completion_content.append("Enjoy the tours you have! You can always run Krida again for more. 🍽️", style="bright_cyan")
        else:
            completion_content.append("😔 No Tours Generated\n\n", style="bold bright_red")
            completion_content.append("We couldn't complete any tours this time.\n", style="bright_white")
            completion_content.append("Please check your internet connection and try again! 🔄", style="bright_cyan")
        
        console.print(Panel(
            completion_content,
            border_style="bright_green" if successful_tours == len(cities_to_tour) else "bright_yellow" if successful_tours > 0 else "bright_red",
            padding=(1, 2),
            title="🍽️ Krida Complete",
            title_align="center"
        ))
        
    except KeyboardInterrupt:
        console.print("\n\n[bright_yellow]👋 Thanks for using Krida! Your culinary adventures await next time![/bright_yellow]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Unexpected error:[/bold red] {e}")
        console.print("[dim]Please try again or report this issue.[/dim]")


if __name__ == "__main__":
    main()
