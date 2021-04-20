// design a libary that allows users to checkout a book up to 3 times and other small constraints

class Library {
	
	String name;
	Address location;
	List<BookItem> books;
}

class Address {
	
	int zipCode;
	String street1;
	String street2;
	String city;
	String state;

}

class Book {

	String isbn;
	String bookTitle;
	List<Author> authors;
	BookType bookType;
	Date publicationDate;

}

class BookItem extends Book {
	// one item of same book
	String barcode;
	Rack rackLocation;
	BookStatus BookStatus;
	BookFormat bookFormat;
	Date issueDate;

}

public enum BookType {
	SCI_FI, ROMANCE, FANTASY, INFORMATIVE;
}

public enum BookFormat {
	NEWSPAPER, HARDCOVER, DIGITAL, JOURNAL;
}

public enum BookStatus {
	ISSUED, AVAILABLE, RESERVED, BORROWED, LOST;
}

class Rack {
	int number;
	String locationId;
}

class Person {

	String firstName;
	String lastName;

}

class Author extends Person {

	List<Book> booksPublished;

}

class SystemUser extends Person {

	String email;
	String phoneNumber;
	Account account;

}	

class Member extends SystemUser {

	int totalBookCheckout;

	Search searchObj;
	BookIssueService issueService;
}

class Librarian extends SystemUser {

	Search searchObj;
	BookIssueService issueService;

	public void addBookItem(BookItem bookItem);
	public BookItem deleteBookItem(String barcode);
	public BookItem editBookItem(BookItem bookItem);

}

class Account {

	String userName;
	String password;
	int accountId;

}

class Search {

	public List<BookItem> getBookByTitle(String title);
	public List<BookItem> getBookByAuthor(Author author);
	public List<BookItem> getBookByType(BookType booktype);
	public List<BookItem> getBookByPublicationDate(publicationDate pubdate);
}

class BookIssueService {

	FineService fineService;

	public BookReservationDetail getReservationDetail(BookItem book);
	public void updateReservationDetail(BookReservationDetail bookReservationDetail);
	public BookReservationDetail reserveBook(BookItem book, Member user);
	public BookIssueDetail issueBook(BookItem book, Librarian user);

	// it will internally call the issueBook function after basic validation
	public BookIssueDetail renewBook(BookItem book, Librarian user);
	public void returnBook(BookItem book, Member user);
}

class BookLending {

	BookItem book;
	Date startDate;
	SystemUser user;
}

class BookReservationDetail extends BookLending {

	ReservationStatus reservationStatus;

}

class BookIssueDetail extends BookLending {
	
	Date duedate;
}

class FineService {

	public Fine calculateFine(BookItem book, SystemUser user, int days);
}

class Fine {

	Date fineDate;
	BookItem book;
	SystemUser user;
	Double fineValue;
}