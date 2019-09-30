from django.shortcuts import render
from .forms import TestForm
from django.core import serializers
from . models import Test
import pickle
from sklearn.externals import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from django.contrib import messages
# Create your views here.

"""class TestView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializers"""

def form_view(request):
	template_name='form.html'

	if request.method=='POST':
		test_form=TestForm(request.POST)
		if test_form.is_valid():
			name=test_form.cleaned_data['name']
			age=test_form.cleaned_data['age']
			sex=test_form.cleaned_data['sex']
			sex=int(sex)
			chestpain=test_form.cleaned_data['chestpain']
			chestpain=int(chestpain)
			blood_pressure=test_form.cleaned_data['blood_pressure']
			cholestrol=test_form.cleaned_data['cholestrol']
			sugar=test_form.cleaned_data['sugar']
			sugar=int(sugar)
			restecg=test_form.cleaned_data['restecg']
			restecg=int(restecg)
			max_heart_rate=test_form.cleaned_data['max_heart_rate']
			exang=test_form.cleaned_data['exang']
			oldpeak=test_form.cleaned_data['oldpeak']
			MyDict= (request.POST).dict()
			data=pd.DataFrame(MyDict,index=[0])

			answer=get_answer(data)[0]
			answer=int(answer*100)
			if answer is not None:
				messages.info(request,"The chance of having a Heart Attack is: "+str(answer)+"%")
			print(answer)
	else:
		test_form=TestForm(request.POST)

	context={
				'test_form':test_form,
				'answer':answer,
	}
	return render(request,template_name,context)



def get_answer( data):
	X=data.drop(['name','csrfmiddlewaretoken'],axis=1)
	X=np.array(X)
	min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
	X_scaled = min_max_scaler.fit_transform(X.reshape(10,-1))
	X_test = X_scaled.reshape( -1, 10)
	mdl=joblib.load('D:/vcare/Heart_Attack_prediction.pkl')
	y_pred=mdl.predict(X_test)
	return y_pred
