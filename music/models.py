from django.db import models

# Create your models here.
class Album(models.Model):
    albumid = models.IntegerField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase. This field type is a guess.
    artistid = models.IntegerField(db_column='ArtistId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Album'


class Artist(models.Model):
    artistid = models.IntegerField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Artist'


class Customer(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    supportrepid = models.IntegerField(db_column='SupportRepId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'


class Employee(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True)  # Field name made lowercase. This field type is a guess.
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True)  # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True)  # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True)  # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Employee'


class Genre(models.Model):
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Genre'


class Invoice(models.Model):
    invoiceid = models.IntegerField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    billingaddress = models.TextField(db_column='BillingAddress', blank=True)  # Field name made lowercase. This field type is a guess.
    billingcity = models.TextField(db_column='BillingCity', blank=True)  # Field name made lowercase. This field type is a guess.
    billingstate = models.TextField(db_column='BillingState', blank=True)  # Field name made lowercase. This field type is a guess.
    billingcountry = models.TextField(db_column='BillingCountry', blank=True)  # Field name made lowercase. This field type is a guess.
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True)  # Field name made lowercase. This field type is a guess.
    total = models.TextField(db_column='Total')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Invoice'


class Invoiceline(models.Model):
    invoicelineid = models.IntegerField(db_column='InvoiceLineId', primary_key=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='InvoiceId')  # Field name made lowercase.
    trackid = models.IntegerField(db_column='TrackId')  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceLine'


class Mediatype(models.Model):
    mediatypeid = models.IntegerField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MediaType'


class Playlist(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Playlist'


class Playlisttrack(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    trackid = models.IntegerField(db_column='TrackId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaylistTrack'


class Track(models.Model):
    trackid = models.IntegerField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    albumid = models.IntegerField(db_column='AlbumId', blank=True, null=True)  # Field name made lowercase.
    mediatypeid = models.IntegerField(db_column='MediaTypeId')  # Field name made lowercase.
    genreid = models.IntegerField(db_column='GenreId', blank=True, null=True)  # Field name made lowercase.
    composer = models.TextField(db_column='Composer', blank=True)  # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Track'
