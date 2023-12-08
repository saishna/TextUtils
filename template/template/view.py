from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Saishna Budhathoki', 'place': 'The Universe'}
    return render(request, 'index.html', params)


def analyzer(request):
    # Get the text
    text = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
     #check which box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Return analyze.html with the text
        text= analyzed
        #return render(request, 'analyze.html', params)


        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in text:
            analyzed= analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Return analyze.html with the text
        # return render(request, 'analyze.html', params)
        text=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLine ', 'analyzed_text': analyzed}
        # Return analyze.html with the text
        # return render(request, 'analyze.html', params)
        text = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        is_space = False  # Flag to keep track of extra spaces
        for char in text:
            if char == " ":
                if not is_space:
                    analyzed += char
                    is_space = True
            else:
                analyzed += char
                is_space = False

        params = {'purpose': 'Removed ExtraSpace', 'analyzed_text': analyzed}
        text = analyzed

    if (charcount == "on"):
        character_count = len(text)  # Calculate the character count
        analyzed = str(character_count)  # Convert it to a string
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        # Return analyze.html with the text
        # return render(request, 'analyze.html', params)
        text = analyzed
    if(removepunc !="on" and fullcaps !="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Select Operation and Try Again!")

    return render(request, 'analyze.html', params)

