# Krida v1.0.2 - Quick Start Guide

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys:**
   ```bash
   export OPENWEATHER_API_KEY="your_weather_api_key"
   export JULEP_API_KEY="your_julep_api_key"
   ```

3. **Run Krida:**
   ```bash
   python main.py
   ```

## 📱 Interactive Features

### City Selection
- Enter any city name (e.g., "Paris", "Tokyo", "New York")
- Cities are automatically formatted (e.g., "new york" → "New York")
- Get helpful suggestions for popular food destinations
- Add up to 5 cities per session

### Budget Options

**Quick Select:**
- Option 1: Budget-Friendly (Under $15/meal)
- Option 2: Mid-Range ($15-35/meal) ← Default
- Option 3: Upscale ($35-75/meal)
- Option 4: Luxury ($75+/meal)

**Natural Language (Option 5):**
- Keywords: "cheap", "expensive", "moderate", "luxury"
- Numbers: "25", "$50", "100"
- Phrases: "budget friendly", "high end", "mid range"

## 🎯 Tips for Best Results

### City Names
✅ **Good:** "Paris", "Tokyo", "New York", "San Francisco"
❌ **Avoid:** Very small towns, misspelled names

### Budget Input
✅ **Good:** "moderate", "50", "luxury dining", "cheap eats"
❌ **Avoid:** Negative numbers, non-food contexts

### API Keys
- Get OpenWeather API key from: https://openweathermap.org/api
- Get Julep API key from: https://julep.ai
- Store in environment variables or .env file

## 🔧 Troubleshooting

### Common Issues

**"Missing API Keys" Error:**
- Check that both OPENWEATHER_API_KEY and JULEP_API_KEY are set
- Verify keys are valid and have proper permissions

**"Could not get weather" Message:**
- Check internet connection
- Verify city name spelling
- Some very small cities may not be in the weather database

**"Could not find restaurants" Error:**
- Try a different city with more dining options
- Check if the city is well-known for food culture
- Verify Julep API key is working

**Service Initialization Fails:**
- Check internet connection
- Verify both API keys are correct
- Try running the demo: `python demo_v1.0.2.py`

### Performance Tips
- Larger cities typically have better results
- Popular food destinations work best
- Mid-range budgets have most restaurant options

## 🎮 Demo Mode

Run the interactive demo to see all features without API keys:
```bash
python demo_v1.0.2.py
```

## 🆘 Getting Help

1. **Check the demo** - Run `python demo_v1.0.2.py`
2. **Read the README** - Comprehensive setup instructions
3. **Review CHANGELOG** - See what's new in v1.0.2
4. **Test basic functionality** - Run `python test_interactive.py`

## 🌟 Example Session

```
🍽️ KRIDA AI FOODIE TOUR GENERATOR v1.0.2 🤖

City Selection:
→ Enter "Tokyo"
→ Enter "Bangkok" 
→ Press Enter to continue

Budget Selection:
→ Select option 5 (Custom)
→ Enter "moderate"
→ System maps to Mid-Range ($15-35/meal)

Confirmation:
→ Review: Tokyo, Bangkok with Mid-Range budget
→ Select "Y" to start

Tour Generation:
→ Weather check for each city
→ Discover local dishes
→ Find perfect restaurants
→ Generate narrative tour guide

Result:
→ Beautiful, personalized foodie tours for each city!
```

Happy food exploring! 🍽️✨
