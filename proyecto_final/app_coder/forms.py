from django import forms

class Jugador_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    nacimiento = forms.IntegerField()

class Equipo_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    fundacion = forms.IntegerField()

class Entrenador_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    nacimiento = forms.IntegerField()