from django.shortcuts import render

from django.views import View

from ..users.forms import UserLoginForm

# Create your views here.

class TopicsMainPage(View):

    def get(self, request):
        topics = Topic.objects.all()
        login_form = UserLoginForm(auto_id="id_login_%s")
        return render(
            request, "topics/topics.html", {"topics": topics, 'form': form}
        )
