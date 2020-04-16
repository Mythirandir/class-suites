from django.shortcuts import render

# Homepage
def homepage(request):
    return render(request=request,
                  template_name="index.html",
                  )

# Blog entries

def blog(request):
    return render(request=request,
                  template_name="blog.html",
                  )

def about(request):
    return render(request=request,
                  template_name="about.html",
                  )


def rooms(request):
    return render(request=request,
                  template_name="rooms.html",
                   )


def contact(request):
    return render(request=request,
                  template_name="contact.html",
                  )
