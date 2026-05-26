# Personal-Assistant

An AI-powered automation assistant built using n8n and deployed with Streamlit.  
This project allows users to perform multiple productivity and automation tasks using natural language prompts.

## Features

The Personal-Assistant automation workflow can perform the following tasks automatically:

### Email Automation
- Send emails
- Summarize emails
- get emails

### Google Docs Automation
- Create Google Docs
- Update existing Google Docs
- Retrieve Google Docs content

### Google Tasks Automation
- Create Google Tasks
- Delete tasks
- Retrieve tasks

### Google Calendar Automation
- Create calendar events
- Create calendar tasks
- Retrieve calendar events and tasks

### Google Sheets Automation
- Perform calculations
- Add data to sheets
- Edit/update Google Sheets

---

# Tech Stack

## Backend Automation
- n8n

## Frontend
- Streamlit

## APIs & Integrations
- Google Calendar API
- Google Docs API
- Google Sheets API
- Google Tasks API
- Gmail API
- Gemini AI API

---

# Project Architecture

```text
User Prompt
     ↓
Streamlit UI
     ↓
n8n Webhook
     ↓
AI Agent + Automation Workflows
     ↓
Google Services / Email / Sheets / Docs
