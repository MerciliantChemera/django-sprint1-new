from django.shortcuts import render

def about(request):
    template_name = 'pages/about.html'
    title = 'О проекте'
    context = {
        'title': title
    }
    return render(request, template_name, context)

def rules(request):
    template_name = 'pages/rules.html'
    title = 'Наши правила'
    context = {
        'title': title
    }
    return render(request, template_name, context)
