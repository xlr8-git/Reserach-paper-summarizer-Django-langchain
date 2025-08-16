from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from langchain_groq import ChatGroq
from .prompt_generator import load_prompt  # assuming you have this utility

def index(request):
    """Render the main research tool page"""
    context = {
        'papers': [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers", 
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis"
        ],
        'styles': [
            "Beginner-Friendly",
            "Technical", 
            "Code-Oriented",
            "Mathematical"
        ],
        'lengths': [
            "Short (1-2 paragraphs)",
            "Medium (3-5 paragraphs)", 
            "Long (detailed explanation)"
        ]
    }
    return render(request, 'summarizer/index.html', context)

@csrf_exempt
def summarize(request):
    """Handle the summarization request"""
    if request.method == 'POST':
        try:
            # Get form data
            paper_input = request.POST.get('paper_input')
            custom_paper_input = request.POST.get('custom_paper_input')
            style_input = request.POST.get('style_input') 
            length_input = request.POST.get('length_input')

            # If user chose "Other", replace with custom input
            if paper_input == "__custom__" and custom_paper_input:
                paper_input = custom_paper_input
            
            # Validate input
            if not paper_input or not style_input or not length_input:
                return JsonResponse({
                    'success': False,
                    'error': 'All fields are required.'
                })

            # Initialize ChatGroq model
            model = ChatGroq(
                groq_api_key=settings.GROQ_API_KEY,
                model_name="llama3-8b-8192"
            )
            
            # Load summarization prompt
            template = load_prompt("summarization")
            
            # Create chain and invoke
            chain = template | model
            result = chain.invoke({
                'paper_input': paper_input,
                'style_input': style_input,
                'length_input': length_input
            })
            
            return JsonResponse({
                'success': True,
                'summary_markdown': result.content  # return as markdown
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
