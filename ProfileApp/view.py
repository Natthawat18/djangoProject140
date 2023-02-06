from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")

def home(request):
    return render(request, 'home.html')

def personalRecord(request):
    return render(request, 'personalRecord.html')

def educationalRecord(request):
    return render(request, 'educationalRecord.html')

def interests(request):
    return render(request, 'interests.html')

def dreamJob(request):
    return render(request, 'dreamJob.html')

def roleModel(request):
    return render(request, 'roleModel.html')
def product(request):
    name = "ณัฐวัฒน์"
    surname = "ทองคำเหลา"
    nickname = "ปอม"
    age = "21 ปี"
    weight = "55"
    height = "165"
    color = "ดำ"
    song = "ย้ายป่าหนี"
    phoneNumber = "0627129026"
    studenCode = "65342310140-4"
    listNameProduct = [
        ["Nike Tiempo Legend 9 Academy TF ", 2700, '../../static/images/ntt.jpg'],
        ["Nike Phantom GX Academy IC ", 3300, '../../static/images/pp1.jpg'],
        ["Nike Zoom Mercurial Vapor 15 Academy TF", 2639, '../../static/images/nnm.jpg'],
        ["Nike Pegasus 39", 5100, '../../static/images/pee.jpg'],
        ["Nike Winflo 9", 3700, '../../static/images/eaa.webp'],
        ["Nike Zoom Vomero 5 SP", 6000, '../../static/images/spp.jpg'],
        ["Nike ACG Storm-FIT", 1700, '../../static/images/acg1.jpg'],
        ["Nike Sportswear Heritage 86", 700, '../../static/images/her.jpg'],
        ["Nike Everyday Cushioned", 300, '../../static/images/eee.webp'],
        ["Nike Everyday", 300, '../../static/images/ppe.webp']
    ]
    return render(request, 'product.html',
                  {'name': name, 'surname': surname, 'nickname': nickname, 'age': age, 'wight': weight,
                   'height': height,
                   'color': color, 'song': song, 'phoneNumber': phoneNumber, 'studenCode': studenCode,
                   'ListNameProduct': listNameProduct})


