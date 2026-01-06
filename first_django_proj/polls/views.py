import os
from email.policy import default
import logging

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Question, Contact
from .forms import ContactForm
from django.template import loader

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     context = {"lq": latest_question_list}
#     # return HttpResponse(template.render(context, request))
#     return render(request, "polls/index.html", context)

# class IndexView(View):
#     number_of_tasks = 5
#
#     def get(self, request):
#         latest_question_list = Question.objects.order_by("-pub_date")[:self.number_of_tasks]
#         context = {"lq": latest_question_list}
#         return render(request, "polls/index.html", context)
logger = logging.getLogger('polls')

class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        logger.error('List of Questions viewed by user.')
        return Question.objects.order_by('-pub_date')
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        return latest_question_list

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context["num_questions"] = Question.objects.count()
        context["students"] = [10,20,30,40]
        logger.info("Question list")
        return context

# def detail(request, q_slug):
#     # question = Question.objects.filter(id=question_id)
#     # if question:
#     #     return HttpResponse(question[0].question_text)
#     # else:
#     #     return HttpResponse("Question does not exist.")
#
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#
#     question = get_object_or_404(Question, q_slug=q_slug)
#     return render(request, "polls/question_detail.html", {"question": question})

class QuestionDetailView(DetailView):
    model = Question


def results(request, question_id):
    response = _("You're looking at the results of question %s.")
    print(request.session.items())
    request.COOKIES['test'] = 'hello world'
    return HttpResponse(response % question_id)

def about(request, language):
    return HttpResponse("About us: ...")


class NewQuestionView(CreateView):
    model = Question
    fields = ["question_text", 'pub_date', 'name']
    success_url = "/polls/success/"
    success_message = "Question created successfully."

# def success(request):
#     return HttpResponse("Success!")

class SuccessView(TemplateView):
    template_name = "polls/success.html"


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["question_text", 'pub_date', 'name']
    success_url = "/polls/success/"
    template_name = "polls/question_form.html"


class QuestionDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.delete_question'
    model = Question
    success_url = "/polls/success/"
    template_name = "polls/question_delete.html"


class ContactUsView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "polls/contact_us.html", {"form": form})

    def post(self, request):
        # contact = Contact(name=request.POST["name"], email=request.POST["email"], message=request.POST["message"])
        # contact.save()
        form = ContactForm(request.POST)
        if form.is_valid():
            # contact = Contact(name=form.cleaned_data["name"], email=form.cleaned_data["email"], message=form.cleaned_data["message"])
            # contact.save()
            form.save()
            return render(request, "polls/success.html")
        else:
            return render(request, "polls/contact_us.html", {"form": form})