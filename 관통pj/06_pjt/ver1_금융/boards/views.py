from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .models import Board, Comment
from .forms import BoardForm, CommentForm


def index(request):
    boards = get_list_or_404(Board)
    context = {
        'boards': boards,
    }
    return render('boadrs/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {
        'form': form,
    }
    return render(request, 'boards/create.html', context)
            


def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    commentform = CommentForm()
    comments = board.comments.all()
    context = {
        'board': board,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)


@login_required
def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    board.delete()
    return redirect('boards:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm(instance=board)
    context = {
        'board': board,
        'form': form,
    }
    return render(request, 'boards/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk= board_pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.author = request.user
        comment.board = board
        commentform.save()
        return redirect('boards:detail', board.pk)
    context = {
        'board': board,
        'commentform': commentform,
    }
    return render(request, 'boards/detail.html', context)


@login_required
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('boards:detail', board_pk)
