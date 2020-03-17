from django import forms
import flightradar24

fr = flightradar24.Api()
airlines = fr.get_airlines()
airlines = airlines['rows']
airlines = [(airline['ICAO'], "{} | {}".format(airline['Name'], airline['ICAO'])) for airline in airlines]
class AirlineForm(forms.Form):
    choose_airline = forms.IntegerField(label="Choose an Airline",
                                    widget=forms.Select(choices=airlines))
