from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from langchain_groq import ChatGroq
from .prompt_generator import load_prompt 

def index(request):
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
    if request.method == 'POST':
        try:
            paper_input = request.POST.get('paper_input')
            custom_paper_input = request.POST.get('custom_paper_input')
            style_input = request.POST.get('style_input') 
            length_input = request.POST.get('length_input')

            if paper_input == "__custom__" and custom_paper_input:
                paper_input = custom_paper_input
            
            if not paper_input or not style_input or not length_input:
                return JsonResponse({
                    'success': False,
                    'error': 'All fields are required.'
                })

            model = ChatGroq(
                groq_api_key=settings.GROQ_API_KEY,
                model_name="llama3-8b-8192"
            )
            
            template = load_prompt("summarization")
            
            chain = template | model
            result = chain.invoke({
                'paper_input': paper_input,
                'style_input': style_input,
                'length_input': length_input
            })
            
            return JsonResponse({
                'success': True,
                'summary_markdown': result.content  
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
