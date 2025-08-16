# AI Research Paper Summarizer

A beginner-friendly Django web application that uses AI to summarize research papers in different styles and lengths.

##  What This Project Does

This application helps you understand complex research papers by:
- **Selecting** from popular research papers
- **Choosing** how you want the explanation (beginner-friendly, technical, code-focused, or mathematical)
- **Picking** the length of the summary (short, medium, or long)
- **Getting** an AI-generated summary that matches your preferences

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- A Groq API key (get one for free at [groq.com](https://groq.com))

### Installation Steps

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd django-research-tool
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Create a file called `.env` in the project root
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser**
   - Go to `http://127.0.0.1:8000`
   - You should see the Research Paper Summarizer!

##  Project Structure

```
django-research-tool/
├── research_tool/          # Main Django project settings
├── summarizer/            # The main app for paper summarization
│   ├── views.py          # Handles web requests and AI processing
│   ├── prompt_generator.py # Loads AI prompts from JSON
│   ├── prompts.json      # Contains the AI instruction templates
│   └── urls.py           # Defines website URLs
├── templates/            # HTML templates for the website
│   ├── base.html         # Base template with common styling
│   └── summarizer/       # Templates for the summarizer app
├── static/              # CSS, JavaScript, and other static files
└── requirements.txt     # Python packages needed
```

##  How It Works

### 1. User Interface (Frontend)
- **HTML Templates**: Create the form and display results
- **JavaScript**: Handles form submission and shows loading states
- **CSS**: Makes everything look nice and professional

### 2. Backend Processing (Django Views)
- **Form Handling**: Collects user selections (paper, style, length)
- **AI Integration**: Sends requests to Groq's AI service
- **Response Processing**: Formats and returns the summary

### 3. AI Prompt System
- **Prompt Templates**: Stored in `prompts.json` for easy editing
- **Dynamic Content**: Templates adapt based on user choices
- **Quality Control**: Ensures consistent, helpful summaries

##  Customization

### Adding New Research Papers
Edit `summarizer/views.py` and add papers to the `papers` list:
```python
'papers': [
    "Your New Paper Title",
    "Another Research Paper",
    # ... existing papers
]
```

### Changing AI Instructions
Edit `summarizer/prompts.json` to modify how the AI writes summaries:
```json
{
    "summarization": {
        "template": "Your custom instructions here"
    }
}
```

### Adding New Styles or Lengths
Modify the `styles` and `lengths` lists in `summarizer/views.py`.

##  Troubleshooting

### Common Issues

1. **"GROQ_API_KEY not found"**
   - Make sure you created the `.env` file
   - Check that your API key is correct

2. **"Module not found" errors**
   - Run `pip install -r requirements.txt` again
   - Make sure you're in the correct directory

3. **Website not loading**
   - Check that the server is running (`python manage.py runserver`)
   - Verify the URL is correct (`http://127.0.0.1:8000`)

### Getting Help
- Check the Django documentation: https://docs.djangoproject.com/
- Look at the error messages in your terminal
- Make sure all files are in the correct locations

##  Learning Resources

- **Django Basics**: https://docs.djangoproject.com/en/stable/intro/
- **HTML/CSS**: https://developer.mozilla.org/en-US/docs/Web
- **JavaScript**: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- **AI/LLMs**: https://groq.com/docs


##  License

This project is open source and available under the MIT License.
