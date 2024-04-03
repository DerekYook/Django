from django.shortcuts import render
# View에 Model(Notice) 가져오기
from .models import Notice


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def board(request):
    # board리스트를 불러오게 수정
    # return render(request,'main/board.html')
    # 모든 Notice를 가져와 list에 저장
    noticeList = Notice.objects.all()
    # board.html오픈시 모든 Notice의 list가져옴
    return render(request, 'main/board.html', {'noticeList': noticeList})
