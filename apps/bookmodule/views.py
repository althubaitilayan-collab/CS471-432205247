from django.shortcuts import render
from django.db.models import Sum, Min, Max, Avg, Count, Q
from .models import Publisher, Book

# --- Lab 4 Views ---
def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

# --- Lab 9 Task 1 View ---
def lab9_task1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookAvailability.html', {'books': books})

# --- Lab 9 Task 2 View ---
def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/publisherStock.html', {'publishers': publishers})

# --- Lab 9 Task 3 View ---
def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/oldestBookPublisher.html', {'publishers': publishers})

# --- Lab 9 Task 4 View ---
def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/publisherPriceStats.html', {'publishers': publishers})

# --- Lab 9 Task 5 View ---
def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        total_quantity=Sum('book__quantity')
    )
    return render(request, 'bookmodule/highRatedBooks.html', {'publishers': publishers})

# --- Lab 9 Task 6 (Assignment) View ---
def lab9_task6(request):
    # Filter: price > 50 AND quantity < 5 AND quantity >= 1
    publishers = Publisher.objects.annotate(
        filtered_book_count=Count(
            'book', 
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/filteredBookCount.html', {'publishers': publishers})