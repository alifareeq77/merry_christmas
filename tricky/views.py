from django.shortcuts import render

def index(request, n):
    message = None
    if int(n) >= 45:
        return render(request, 'tricky/oops.html')

    context = range(1, 21)
    if int(n) > 20:
        message = f'you moved the tree by {int(n)-20}px'
    return render(request, 'tricky/index.html', {
        'cont': context,
        'n': str(n),
        'message': message,
    })


def about(request):
    return render(request, 'tricky/about.html', {})
