from django import forms


class ProductsForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)


class DeleteItemFromCartForm(forms.Form):
    pass


class CheckoutForm(forms.Form):
    name_surname = forms.CharField()
    phone_number = forms.CharField()
    city = forms.CharField()
    email = forms.CharField()
    adress = forms.CharField()
    aditonal_information = forms.CharField(widget=forms.Textarea())


class SearchForm(forms.Form):
    CHOICES = (('all', 'all'), ('Vacuum cleaner', 'Vacuum cleaner'), ('Fridge', 'Fridge'),
               ('Flatiron', 'Flatiron'))
    keyword = forms.CharField(max_length=40, required=False)
    classification = forms.ChoiceField(choices=CHOICES)

