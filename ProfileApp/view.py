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
    height = "165" \
             ""
    color = "ดำ"
    song = "ย้ายป่าหนี"
    phoneNumber = "0627129026"
    studenCode = "65342310140-4"
    listNameProduct = [
        ['มาร์คมะขามน้ำผึ้ง', 190, '../../static/images/add.jpg'],
        ["มาร์คมะกู้ด", 199, '../../static/images/add.jpg'],
        ["ยาสีฟันนมแพะ", 199, '../../static/images/add.jpg'],
        ["น้ำหอม JANUA กลิ่น flower shop", 290, '../../static/images/add.jpg'],
        ["น้ำหอม JANUA กลิ่น wood sand and fresh vibe", 290, '../../static/images/add.jpg'],
        ["น้ำหอม JANUA กลิ่น srxy on the beach", 290, '../../static/images/add.jpg'],
        ["น้ำหอม JANUA กลิ่น sweetie picnic", 290, '../../static/images/add.jpg'],
        ["กลอสดอกไม้ 01-poppy pink", 199, '../../static/images/add.jpg'],
        ["กลอสดอกไม้ 02-sunny flower", 199, '../../static/images/add.jpg'],
        ["กลอสดอกไม้ 03-ruby tulip", 199, '../../static/images/add.jpg']
    ]
    return render(request, 'product.html',
                  {'name': name, 'surname': surname, 'nickname': nickname, 'age': age, 'wight': weight,
                   'height': height,
                   'color': color, 'song': song, 'phoneNumber': phoneNumber, 'studenCode': studenCode,
                   'ListNameProduct': listNameProduct})


