# datetimepicker_app/views.py
from django.shortcuts import render, redirect
from .forms import DateForm,SelectedDate

def datepicker_view(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('date_display')
    else:
        form = DateForm()
    return render(request, 'datepicker_form.html', {'form': form})

def date_display(request):
    selected_date = SelectedDate.objects.last()  # Retrieve the last selected date
    return render(request, 'date_display.html', {'selected_date': selected_date})
