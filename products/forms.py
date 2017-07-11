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
    CLASSIFICATION_CHOICES = (('all', 'all'), ('Vacuum cleaner', 'Vacuum cleaner'), ('Fridge', 'Fridge'),
               ('Flatiron', 'Flatiron'))
    # PRICE_CHOICES = (('dont care', 'dont care'), ('<500', '<500'), ('500-2000', '500-2000'), ('>2000', '>2000'))
    keyword = forms.CharField(max_length=40, required=False)
    classification = forms.ChoiceField(choices=CLASSIFICATION_CHOICES, required=False)
    # price = forms.ChoiceField(choices=PRICE_CHOICES, required=False)

