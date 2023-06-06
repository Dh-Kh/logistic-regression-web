from django.shortcuts import render
from .forms import ChoiceForm
from .prediction_system import make_user_prediction
from django.contrib import messages

def prediction_view(request):
    form1 = ChoiceForm(prefix="form1")
    form2 = ChoiceForm(prefix="form2")
    form3 = ChoiceForm(prefix="form3")
    form4 = ChoiceForm(prefix="form4")
    form5 = ChoiceForm(prefix="form5")
    form6 = ChoiceForm(prefix="form6")
    mapping_list = []
    context={
       "form1": form1,
       "form2": form2,
       "form3": form3,
       "form4": form4,
       "form5": form5,
       "form6": form6,
       }
    if request.method == "POST":
        form1 = ChoiceForm(request.POST, prefix="form1")
        form2 = ChoiceForm(request.POST, prefix="form2")
        form3 = ChoiceForm(request.POST, prefix="form3")
        form4 = ChoiceForm(request.POST, prefix="form4")
        form5 = ChoiceForm(request.POST, prefix="form5")
        form6 = ChoiceForm(request.POST, prefix="form6")
        if form1.is_valid():
            mapping_data1 = form1.cleaned_data["choice"]
            mapping_list.append(mapping_data1)
        if form2.is_valid():
            mapping_data2 = form2.cleaned_data["choice"]
            mapping_list.append(mapping_data2)
        if form3.is_valid():
            mapping_data3 = form3.cleaned_data["choice"]
            mapping_list.append(mapping_data3)

        if form4.is_valid():
            mapping_data4 = form4.cleaned_data["choice"]
            mapping_list.append(mapping_data4)
        if form5.is_valid():
            mapping_data5 = form5.cleaned_data["choice"]
            mapping_list.append(mapping_data5)
        if form6.is_valid():
            mapping_data6 = form6.cleaned_data["choice"]
            mapping_list.append(mapping_data6)
            messages.success(request, make_user_prediction(mapping_list))
            return render(request, "logic_prediction/prediction_view.html" , context=context)
        
    return render(request, "logic_prediction/prediction_view.html" , context=context)


    
