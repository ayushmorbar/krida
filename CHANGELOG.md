# Changelog

All notable changes to Krida will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2025-06-09

### Added
- **Enhanced Interactive Menu System**
  - Beautiful ASCII art welcome screen with improved branding
  - Contextual city suggestions (Popular choices, Food capitals, Hidden gems)
  - Enhanced input validation with helpful error messages and tips
  - Progress tracking with spinners and status indicators

- **Smart Budget Processing**
  - Natural language support for budget input ("cheap", "expensive", "moderate", "luxury")
  - Flexible input parsing: accepts numbers, keywords, or descriptive phrases
  - Intelligent mapping to appropriate budget categories
  - Custom amount support with automatic currency symbol handling

- **Better User Interaction**
  - Enhanced confirmation screen with detailed tour summary
  - Multiple navigation options (Continue, Modify, Quit) with clear instructions
  - Improved error handling with helpful recovery suggestions
  - Graceful keyboard interrupt handling for better UX

- **Performance & Reliability Improvements**
  - Better API error handling with informative user feedback
  - Enhanced service initialization with visual status updates
  - Improved city name formatting and validation
  - More robust tour generation with fallback options

### Changed
- **User Interface Overhaul**
  - Redesigned welcome screen with comprehensive feature overview
  - Enhanced city selection with dynamic suggestions and validation
  - Improved budget selection table with detailed descriptions
  - Better progress indication during tour generation

- **Error Handling**
  - More descriptive error messages with actionable advice
  - Graceful degradation when services fail
  - Better recovery options for failed operations

- **Code Quality**
  - Enhanced natural language processing for budget keywords
  - Improved input validation and sanitization
  - Better separation of concerns in interactive components

### Fixed
- Removed hardcoded city limitations (now supports any city globally)
- Fixed budget processing edge cases with empty or invalid inputs
- Improved error handling for API failures
- Enhanced user experience flow with better navigation

## [1.0.1] - 2025-06-07

### Added
- Initial interactive menu system
- Basic city selection functionality
- Simple budget configuration options

### Changed
- Replaced hardcoded cities with user input
- Added basic error handling

### Fixed
- Initial release bug fixes

## [1.0.0] - 2025-06-06

### Added
- Initial release of Krida AI Foodie Tour Generator
- Weather integration with OpenWeather API
- AI-powered food recommendations using Julep AI
- Basic command-line interface
- Support for multiple cities (hardcoded)
- Narrative tour generation
- Beautiful terminal output with Rich library

### Features
- Weather-smart dining suggestions
- Authentic local cuisine discovery
- Budget-conscious restaurant selection
- Engaging narrative-driven tours
- Multi-city support (limited to predefined cities)

---

## Release Notes

### v1.0.2 - "Interactive Experience"
This release focuses on dramatically improving the user experience with a completely redesigned interactive interface. The most significant improvements include natural language budget processing, enhanced city selection with helpful suggestions, and a beautiful ASCII art welcome screen. Error handling has been greatly improved, making the application more robust and user-friendly.

### Key Highlights:
- 🎨 **Beautiful UI**: ASCII art, enhanced panels, and better visual hierarchy
- 🧠 **Smart Input**: Natural language budget processing ("cheap" → Budget-Friendly)
- 💬 **Better UX**: Helpful suggestions, tips, and improved error messages
- 🚀 **Robust**: Enhanced error handling and graceful degradation

### Migration Notes:
- No breaking changes from v1.0.1
- All existing functionality preserved
- Enhanced features are backward compatible
- API keys and environment setup remain the same

---

## Upcoming Features

### v1.0.3 (Planned)
- 🌐 Multi-language support
- 📱 Export tours to PDF/HTML
- 🎯 Dietary restriction support
- 🚶 Walking distance optimization
- ⭐ User rating system

### v1.1.0 (Future)
- 🗺️ Interactive map integration
- 📞 Restaurant reservation links
- 🎨 Customizable tour themes
- 📊 Analytics and insights
- 🤝 Social sharing features

---

For more information about releases, please check the [GitHub releases page](https://github.com/your-username/krida/releases).
