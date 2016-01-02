from django.http import HttpResponse
from kegbot.models import Tap


def main(request):
    t1, t2 = Tap.objects.all()
    return HttpResponse('t1: {}\nt2: {}'.format(t1.current_volume, t2.current_volume))
