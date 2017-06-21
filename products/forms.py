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
