from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home page.html'


class LoggedinPage(TemplateView):
    template_name = 'loggedin.html'


class LoggedoutPage(TemplateView):
    template_name = 'loggedout.html'