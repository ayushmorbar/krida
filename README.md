# Krida: AI-Powered Foodie Tour Generator

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)
![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)
![Built with Julep AI](https://img.shields.io/badge/Built%20with-Julep%20AI-purple.svg)
![Foodie](https://img.shields.io/badge/Foodie-%F0%9F%8D%9E%20%F0%9F%8D%95%20%F0%9F%8D%94-orange.svg)

<p align="center">
  <!-- Logo Start -->
  <img src="assets/images/krida_logo.png" title="Krida Logo" style="border-radius:50%;margin:0 10px;" alt="Krida Logo" width="100"/>
  <!-- Logo End -->
  </p>
  <br/>
<p align="center">
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/fork-and-knife-with-plate_1f37d-fe0f.png" alt="Food Plate" width="60"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/globe-showing-asia-australia_1f30f.png" alt="Globe" width="50"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/robot_1f916.png" alt="Robot" width="50"/>
</p>

> *"Krida"* (Sanskrit: क्रीडा) means "play" or "sport" – because exploring food should be a delightful adventure!

Krida is an **open-source** Python-based AI workflow that generates a personalized, one-day "foodie tour" for any city or set of cities. It intelligently combines real-time weather data with the creative power of Julep AI to craft engaging, practical, and narrative-driven culinary itineraries.

---

## ✨ Features

- **🎨 Beautiful Terminal UI**: Rich formatting with colorful panels, emojis, and markdown rendering
- **🌤️ Weather-Smart Planning**: Suggests indoor or outdoor dining based on live weather
- **🍛 Authentic Cuisine Focus**: Discovers genuine local dishes, not generic options
- **⭐ Curated Restaurant Selection**: Finds top-rated, authentic establishments for each dish
- **📖 Narrative-Driven Tours**: Crafts engaging, blog-style stories for your day
- **🏙️ Multi-City Support**: Plan tours across multiple destinations in one go
- **🛠️ Modular & Extensible**: Easy to add new features, APIs, or cities

---

## 🚀 Workflow Logic

For each city, Krida executes the following sequence:

1. **🌤️ Weather Check**  
   Fetches current weather conditions using the OpenWeather API.
2. **🏠 Dining Suggestion**  
   Suggests indoor or outdoor dining based on temperature and weather (e.g., rain).
3. **🍽️ Dish Discovery**  
   Uses Julep AI (`gpt-4o` model) to identify three iconic local dishes.
4. **🔍 Restaurant Search**  
   For each dish, queries Julep AI to find a single, top-rated, authentic restaurant famous for that dish.
5. **📝 Narrative Generation**  
   All collected data (weather, dining style, dishes, restaurants) is passed to Julep AI, which generates a creative, blog-style tour guide narrative for a full day (Breakfast, Lunch, Dinner).

---

## 🗂️ Project Structure

```
krida/
├── LICENSE
├── README.md
├── main.py
├── requirements.txt
└── services/
    ├── inspect_julep.py
    ├── julep_service.py
    ├── weather.py
    └── __pycache__/
```

---

## 🏗️ Architecture

<p align="center">
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/brain_1f9e0.png" alt="Brain" width="50"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/gear_2699-fe0f.png" alt="Gear" width="40"/>
  <img src="https://em-content.zobj.net/source/microsoft-teams/363/rocket_1f680.png" alt="Rocket" width="40"/>
</p>

```
🤖 AI Agent (Foodie Guide)
    ↓
⚙️ YAML-based Task Workflow
    ├── 🌤️ Weather Integration (OpenWeather API)
    ├── 🍛 Local Dish Discovery (Julep AI)
    ├── ⭐ Restaurant Search (Julep AI)
    └── 📝 Tour Narrative Creation (Julep AI)
```

- **Julep Client**: Modern `Julep(api_key="...")` initialization.
- **YAML Task Definitions**: Structured, extensible workflow definitions.
- **Integration Tools**: Weather and search providers.
- **Expression Syntax**: New `$` syntax for variables in YAML.

---

## 🧑‍💻 Tech Stack

- **Language**: Python 3.9+
- **Core APIs**:
  - [Julep AI](https://julep.ai/) for all LLM-based tasks (dish discovery, restaurant search, narrative generation)
  - [OpenWeather API](https://openweathermap.org/api) for real-time weather data
- **Primary Libraries**: `requests`, `julep-ai`, `PyYAML`, `pydantic`, `rich`

---

## ⚡ Quick Start

1. **Clone and Setup**
   ```bash
   git clone https://github.com/ayushmorbar/krida.git
   cd krida
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Add your Julep API key and OpenWeather API key to .env
   ```

3. **Run Your First Tour**
   ```bash
   python main.py
   ```

---

## 🏆 Example Output

### Beautiful Terminal Experience with Rich Formatting

Krida features a stunning terminal interface with colorful panels, emojis, and markdown-rendered narratives:

**Application Startup & City Planning**
![Krida Startup](assets/images/sample_ouput_0.png)

**City Tour Generation & Narrative Output**
![Paris Tour Example](assets/images/sample_ouput_1.png)

### ✨ What You'll See:

- **🎨 Rich Terminal UI**: Colorful panels and progress indicators
- **🌍 Multi-City Planning**: Tours for Delhi, Paris, Tokyo, and New York
- **🌤️ Weather Integration**: Real-time weather affects dining suggestions
- **🍽️ Authentic Cuisine**: Local dishes like Croissants, Coq au Vin, Ratatouille for Paris
- **📖 Beautiful Narratives**: Markdown-formatted stories for each city

<details>
<summary>📜 Click to expand sample Paris narrative text</summary>

```markdown
# A Cozy Gourmet Adventure in Rainy Paris

Paris, the city of lights, love, and irresistible cuisine! Today, as the rain lightly taps on the cobblestone streets and the autumn air hugs the city at a brisk 15.5°C, we embark on an indoor culinary journey that will warm your heart and soul. Here's how to spend a deliciously cozy day in Paris.

## Breakfast: Croissants at Du Pain et des Idées

Kick-start your day with the divine flaky harmony that is the croissant. Nestled just off the Canal Saint-Martin, Du Pain et des Idées offers a perfect refuge from the rain. The bakery is a charming hideaway, complete with stunning stained-glass ceiling fixtures that sparkle even on the cloudiest mornings. As you break open the buttery shell of your croissant, an enticing aroma of toasted almonds and warm butter envelops you, beckoning you to savor each tender bite.

## Lunch: Coq au Vin at Le Procope

As the afternoon unfolds with gentle raindrops creating a romantic symphony, make your way to Le Procope for an authentic Coq au Vin experience. This historic restaurant, with its warm wooden interiors and flickering candlelight, provides the perfect sanctuary from the Parisian drizzle.

## Dinner: Ratatouille at Le Meurice

End your culinary journey at the elegant Le Meurice, where ratatouille transforms from a simple peasant dish into a work of art. As the rain continues its gentle patter against the restaurant's grand windows, you'll find yourself immersed in layers of perfectly seasoned vegetables that celebrate the essence of French countryside cooking.
```

</details>

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📝 License

Apache 2.0 License – see LICENSE file for details.

---

<p align="center">
<p align="center">
    <a href="https://github.com/Offbeatshq/" title="Offbeats Labs">
        <img src="https://avatars.githubusercontent.com/u/128445018" alt="Offbeats Labs" width="50" style="border-radius:50%;margin:0 10px;"/>
    </a>
</p>

**Built with [Julep AI](https://julep.ai) 🤖 | Crafted by [Offbeats Labs](https://github.com/Offbeatshq/) 🚀**  
Open source project by [ayushmorbar](https://github.com/ayushmorbar) 💻

*Ready to explore the world through food with the latest AI technology? Let Krida be your intelligent culinary guide!* 🌍🍽️