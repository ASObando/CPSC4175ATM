from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
        
import uuid # Required for unique book instances

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    
    

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)   
        
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
        
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
        
class Account(models.Model):
    """Model representing accounts."""
    
    accountNumber = models.CharField('Account Number', max_length=10, help_text = 'Enter a 10-digit account number.')
    pin = models.CharField('PIN', max_length = 4, help_text = 'Enter a 4-digit pin.')
    accountName = models.CharField('Account Name', max_length = 30, help_text = 'Enter account name.')
    issueDate = models.CharField('Issue Date', max_length = 30, help_text = 'Enter issue date.')
    expiration_date = models.CharField('Expiration Date', max_length = 30, help_text = 'Enter expiration date.')
    address = models.CharField('Address', max_length = 30, help_text = 'Enter address')
    balance = models.DecimalField('Balance', max_digits = 20, decimal_places = 2, help_text = 'Enter balance.')
    cardNumber = models.CharField('Card Number', max_length = 16, help_text = 'Enter card number.')
    phoneNumber = models.CharField('Phone Number', max_length = 14, help_text = 'Enter phone number.')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    CARD_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )
    
    cardStatus = models.CharField(
        'Card Status',
        max_length = 1,
        choices = CARD_STATUS,
        default = 'a',
        help_text = 'Select card status.',
    )
    
    class Meta:
        ordering = ['accountNumber']
    
    def get_absolute_url(self):
        """Returns the url to access a particular instance of an account."""
        return reverse('account-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object."""
        return self.accountNumber
        
class ATM(models.Model):
    """Model representing ATMs."""
    
    ATM_UID = models.CharField('ATM UID', max_length = 15, help_text = 'Enter ATM UID')
    ATM_Address = models.CharField('ATM Address', max_length = 30, help_text = 'Enter ATM address.')
    currentBalance = models.DecimalField('Current Balance', max_digits = 20, decimal_places = 2, help_text = 'Enter current balance.')
    minimumBalance = models.DecimalField('Minimum Balance', max_digits = 20, decimal_places = 2, help_text = 'Enter minimum balance.')
    lastRefillDate = models.CharField('Last Refill Date', max_length = 30, help_text = 'Enter last refill date.')
    nextRefillDate = models.CharField('Next Refill Date', max_length = 30, help_text = 'Enter next refill date.')
    
    ATM_STATUS = (
        ('a', 'Available'),
        ('c', 'Closed'),
        ('l', 'Low'),
    )
    
    ATM_Status = models.CharField(
        'ATM Status',
        max_length = 1,
        choices = ATM_STATUS,
        default = 'a',
        help_text = 'Select ATM status.'
    )
    
    class Meta:
        ordering = ['ATM_UID']
        
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the ATM."""
        return reverse('ATM-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the ATM object."""
        return self.ATM_UID
        
class NewAccount(models.Model):
    """Model representing accounts."""
    
    accountNumber = models.CharField('Account Number', max_length=10, help_text = 'Enter a 10-digit account number.')
    pin = models.CharField('PIN', max_length = 4, help_text = 'Enter a 4-digit pin.')
    accountName = models.CharField('Account Name', max_length = 30, help_text = 'Enter account name.')
    issueDate = models.CharField('Issue Date', max_length = 30, help_text = 'Enter issue date.')
    expiration_date = models.CharField('Expiration Date', max_length = 30, help_text = 'Enter expiration date.')
    address = models.CharField('Address', max_length = 30, help_text = 'Enter address')
    balance = models.DecimalField('Balance', max_digits = 20, decimal_places = 2, help_text = 'Enter balance.')
    cardNumber = models.CharField('Card Number', max_length = 16, help_text = 'Enter card number.')
    phoneNumber = models.CharField('Phone Number', max_length = 14, help_text = 'Enter phone number.')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    CARD_STATUS = (
        ('a', 'Active'),
        ('i', 'Inactive'),
    )
    
    cardStatus = models.CharField(
        'Card Status',
        max_length = 1,
        choices = CARD_STATUS,
        default = 'a',
        help_text = 'Select card status.',
    )
    
    class Meta:
        ordering = ['accountNumber']
    
    def get_absolute_url(self):
        """Returns the url to access a particular instance of an account."""
        return reverse('account-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object."""
        return self.accountNumber