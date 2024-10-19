# ZameenScraper

ZameenScraper is a Python-based web scraper designed to extract real estate property listings from [Zameen.com](https://www.zameen.com/), a leading online property platform in Pakistan. This tool enables users to collect detailed property information such as price, location, features, and agent details, making it suitable for real estate analysis, data-driven decision-making, and market research.

## Project Scope

The ZameenScraper project aims to provide an automated solution for extracting property data from Zameen. It supports scraping property details from multiple categories, including houses, apartments, plots, and commercial properties across various cities. The scraper can be customized to filter listings, monitor changes, and track historical data.

## Features

- **Property Details Extraction**
  - Scrapes essential details such as property type (house, apartment, plot), location, size, number of bedrooms, bathrooms, and price.
  - Extracts unique property IDs for easier tracking and duplicate detection.
  
- **Location Information**
  - Captures city, neighborhood, and locality details for each listing.
  - Includes nearby amenities such as schools, hospitals, parks, and shopping centers, if available.
  
- **Property Features and Specifications**
  - Furnishing status: furnished, semi-furnished, or unfurnished.
  - Utility availability: electricity, gas, water, internet, etc.
  - Security features such as gated community, CCTV, and security staff.
  - Parking information.
  
- **Agent/Owner Information**
  - Extracts agent/owner name, contact details, and agency information.
  - Includes reviews or ratings for agents if available.
  
- **Images and Media**
  - Downloads or saves links to property images.
  - Supports video or virtual tour URLs if available.
  
- **Listing Date and Status**
  - Records the date when the listing was posted.
  - Tracks the availability status (e.g., available, sold, under offer).
  
- **Advanced Data Handling**
  - Duplicate detection to avoid scraping the same property multiple times.
  - Historical data tracking for price changes and listing status updates.
  
- **Search Filtering and Pagination**
  - Supports keyword filters and sorting by price, date, or popularity.
  - Handles multi-page listings to scrape all available data.
  
- **Automated Alerts/Notifications**
  - Provides options for email or SMS alerts for new listings or price drops.

## Requirements

- Python 3.7+
- Required libraries:
  - `requests`
  - `BeautifulSoup`
  - `pandas`
  - `lxml`
  - `selenium` (if using a headless browser for scraping dynamic content)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ZameenScraper.git
   cd ZameenScraper
