from datetime import date

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, Borrowing, Member


def home(request):
    return render(request, "library/home.html")


def book_list(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()
    if query:
        books = books.filter(Q(title__icontains=query) |
                             Q(author__icontains=query))
    return render(request, "library/book_list.html", {
        "books": books,
        "members": Member.objects.all(),
        "query": query,
    })


def book_create(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"].strip(),
            author=request.POST["author"].strip(),
            year=int(request.POST["year"]),
        )
        return redirect("book_list")
    return render(request, "library/book_form.html", {"book": None})


def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST["title"].strip()
        book.author = request.POST["author"].strip()
        book.year = int(request.POST["year"])
        book.save()
        return redirect("book_list")
    return render(request, "library/book_form.html", {"book": book})


def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
    return redirect("book_list")


def member_list(request):
    return render(request, "library/member_list.html", {"members": Member.objects.all()})


def member_create(request):
    error = None
    if request.method == "POST":
        name = request.POST["name"].strip()
        email = request.POST["email"].strip()
        if Member.objects.filter(email=email).exists():
            error = "A member with this email already exists."
        else:
            Member.objects.create(name=name, email=email)
            return redirect("member_list")
    return render(request, "library/member_form.html", {"error": error})


def borrow_book(request, book_id, member_id):
    book = get_object_or_404(Book, id=book_id)
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST" and book.available:
        book.available = False
        book.borrow_count += 1
        book.save()
        Borrowing.objects.create(
            book=book, member=member, borrowed_at=date.today())
    return redirect("book_list")


def return_book(request, book_id):
    if request.method == "POST":
        borrowing = (
            Borrowing.objects
            .filter(book_id=book_id, returned_at__isnull=True)
            .order_by("-borrowed_at")
            .first()
        )
        if borrowing:
            borrowing.returned_at = date.today()
            borrowing.save()
            borrowing.book.available = True
            borrowing.book.save()
    return redirect("book_list")


def member_history(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    history = member.borrowings.select_related("book").order_by("-borrowed_at")
    return render(request, "library/history.html", {
        "member": member,
        "history": history,
    })


def statistics(request):
    return render(request, "library/statistics.html", {
        "total_books": Book.objects.count(),
        "available_books": Book.objects.filter(available=True).count(),
        "borrowed_books": Book.objects.filter(available=False).count(),
        "total_members": Member.objects.count(),
        "active_borrowings": Borrowing.objects.filter(returned_at__isnull=True).count(),
        "most_popular": Book.objects.order_by("-borrow_count").first(),
    })
