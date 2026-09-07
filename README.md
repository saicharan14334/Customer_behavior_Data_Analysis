# Customer_behavior_Data_Analysis
Customer Shopping Behavior Analysis – An end-to-end analytics project using Python, SQL, and Power BI to clean 3,900 purchase records, analyze customer segments, spending, discounts, subscriptions, and product trends, and build an interactive dashboard for actionable business insights.

## 1. Project Overview
An end-to-end Customer Shopping Behavior Analysis project that analyzes 3,900 customer purchase records to uncover spending patterns, customer segments, product preferences, discount behavior, shipping preferences, and subscription trends. The project transforms raw data into actionable business insights using Python, SQL, and Power BI.

## 2. Purpose
The goal is to understand how customer shopping behavior influences sales, engagement, loyalty, and marketing opportunities, helping businesses make data-driven decisions.

## 3. Tech Stack
Python – Data cleaning, preprocessing, EDA & feature engineering
Pandas – Data manipulation and analysis
SQL – Data storage, business analysis & SQL queries
Power BI – Interactive dashboard and data visualization
Microsoft PowerPoint – Project presentation
GitHub – Project documentation and version control

## 4. Data Source
The dataset contains 3,900 purchase transactions and 18 columns, covering customer demographics, purchase details, product information, and shopping behavior. The dataset initially contained 37 missing values in the Review Rating column.

## Key Data Fields
Customer demographics
Product and category information
Purchase amount
Subscription status
Discount usage
Purchase frequency
Review ratings
Shipping type
Previous purchases
Season and location

## 5. Features / Highlights
Python Data Preparation
Loaded and explored the dataset using Pandas.
Performed data quality checks and statistical analysis.
Handled missing review ratings using category-level median imputation.
Standardized column names.
Created age_group and purchase_frequency_days features.
Removed redundant promo_code_used data after consistency validation

## 🗄️ SQL Business Analysis

Analyzed key business questions including:
Revenue comparison by gender.
High-spending customers using discounts.
Top-rated products.
Standard vs. Express shipping spending.
Subscriber vs. non-subscriber performance.
Products with high discount dependency.
Customer segmentation into New, Returning, and Loyal.
Top products within each category.
Repeat buyers and subscription behavior.
Revenue contribution by age group.

## 📊 Power BI Dashboard

Built an interactive Customer Behavior Dashboard featuring:
Total customers
Average purchase amount
Average review rating
Subscription analysis
Revenue by category
Sales by category
Revenue by age group
Sales by age group
Interactive filters for customer and purchase attributes

## 💡 Business Insights
Identify opportunities to increase subscriptions.
Develop loyalty programs for repeat customers.
Optimize discount strategies while maintaining margins.
Promote top-rated and best-selling products.
Target high-revenue customer segments.
Analyze express-shipping customers as a higher-spending segment.

## Project Workflow
  Raw Dataset
      ↓
  Python Data Cleaning & EDA
      ↓
  Feature Engineering
      ↓
  MicroSoft SQL Database
      ↓
 SQL Business Analysis
      ↓
 Power BI Dashboard
      ↓
 Business Insights & Recommendations
 
## 7. Repository Structure
Customer-Shopping-Behavior-Analysis/
│
├── Python/
│   └── Customer_behavior_analysis.py
│
├── SQL/
│   └── SQL_Queries.sql
│
├── PowerBI/
│   └── customer_behavior_Dashboard.pbit
│
├── Documentation/
│   ├── Business Problem Document.pdf
│   └── Customer Shopping Behavior Analysis.pdf
│
├── Presentation/
│   └── Customer-Shopping-Behavior-Analysis.pptx
│
└── README.md

## 8. Key Outcome
This project demonstrates an end-to-end analytics workflow—from raw customer data preparation to SQL-based business analysis and interactive Power BI visualization—with a focus on customer segmentation, purchasing behavior, revenue drivers, and actionable business recommendations.
 
