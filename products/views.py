from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from products.forms import QuestionForm
from products.models import Product
from qna.models import Question


def product_list(request: HttpRequest):
    products = Product.objects.order_by('-id')

    return render(request, "products/product_list.html", {
        "products": products
    })

def _product_detail(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST" and request.user.is_authenticated:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.content_type = ContentType.objects.get_for_model(product)
            question.object_id = product.id
            question.user = request.user
            question.save()
            messages.success(request, "질문이 등록되었습니다")

        return redirect("products:detail", product_id=product.id)
    else:
        form = QuestionForm(request.POST)

    product_reals = product.product_reals.order_by('option_1_display_name', 'option_2_display_name')
    questions = product.questions.order_by('-id')

    return render(request, "products/product_detail.html", {
        "product": product,
        "product_reals": product_reals,
        "questions": questions,
        "question_form": form,

    })


def product_detail(request: HttpRequest, product_id):
    return _product_detail(request,product_id)


def question_create(request: HttpRequest, product_id):
    return _product_detail(request, product_id)

def question_delete(request: HttpRequest, product_id, question_id):
    question = get_object_or_404(Question, id=question_id)

    question.delete()

    messages.success(request, "질문이 삭제되었습니다")

    return redirect("products:detail", product_id=product_id)

def question_modify(request: HttpRequest, product_id, question_id):
    product = get_object_or_404(Product, id=product_id)
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            form.save()
            messages.success(request, "질문이 수정되었습니다.")
            return redirect("products:detail", product_id=product_id)
    else:
        form = QuestionForm(None, instance=question)

    return render(request, "products/question_modify.html", {
        "product": product,
        "question": question,
        "question_form": form,
    })