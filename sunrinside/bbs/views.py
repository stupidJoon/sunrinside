import logging
from django.shortcuts import render, redirect
from .models import Board, Article, Comment

def index(request):
  if request.method == "GET":
    boards = Board.objects.order_by('id')
    return redirect(str(boards.first().id) + '/')

def board(request, board_id):
  if request.method == "GET":
    boards = Board.objects.order_by('id')
    articles = Article.objects.filter(board=Board.objects.filter(id=board_id)[0]).order_by('id').reverse()
    context = { 'id': board_id, 'boards': boards, 'articles': articles, 'now_board': boards.filter(id=board_id)[0] }
    return render(request, 'index.html', context)

def article(request, board_id, article_id):
  if request.method == "GET":
    article = Article.objects.filter(id=article_id)[0]
    comments = Comment.objects.filter(article=article)
    context = { 'article': article, 'comments': comments, 'boards': Board.objects.order_by('id'), 'board_id': board_id }
    return render(request, 'article.html', context)

def addBoard(request):
  if request.method == "POST":
    title = request.POST["title"]
    description = request.POST["description"]
    board = Board.objects.create(creator=request.user, title=title, description=description)
    return redirect('/' + str(board.id) + '/')

def addArticle(request):
  if request.method == "POST":
    author = request.user
    board = Board.objects.filter(id=request.POST["board_id"])[0]
    title = request.POST["title"]
    text = request.POST["text"]
    Article.objects.create(author=author, board=board, title=title, text=text)
    return redirect('/' + str(request.POST["board_id"]) + '/')

def addComment(request):
  if request.method == "POST":
    author = request.user
    article = Article.objects.filter(id=request.POST["article_id"])[0]
    text = request.POST["text"]
    Comment.objects.create(author=author, article=article, text=text)
    return redirect('/' + str(request.POST["board_id"]) + '/' + str(request.POST["article_id"]) + '/')