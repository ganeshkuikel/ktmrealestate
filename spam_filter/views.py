from django.shortcuts import redirect
from sklearn.metrics import accuracy_score
from .models import Spam_filtering
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from sklearn.externals import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os
from sklearn.metrics import confusion_matrix 


vectorizer = CountVectorizer()
modulePath = os.path.dirname(__file__)  # get current directory
print(modulePath)
filePath = os.path.join(modulePath, 'spam_model.pkl')
with open(filePath, 'rb') as f:
    mdl=joblib.load(f)
xlfile = os.path.join(modulePath, 'test.xlsx')
with open(xlfile, 'rb') as g:
    X=pd.read_excel(g)
X=X[['result','comments']]
DF = pd.DataFrame(X)
y_pred=vectorizer.fit_transform(DF['comments'])
mdl.fit(y_pred,DF['result'])
y_test=mdl.predict(y_pred)
accuracy=accuracy_score(y_test, DF['result'])
print("Comfusion:",confusion_matrix(y_test,DF['result']))
print('Accuracy: %f' % (accuracy*100))


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
def Convert(string):
    li = list(string.split("-"))
    return li

# Create your views here.
# def api_sentiment_pred(request):
#     comment = request.GET['comments']
#     example_counts = vectorizer.transform(Convert(comment))
#     listToString(comment)
#     predictions = mdl.predict(example_counts)
#     print(predictions)
#     confusion_matrix(y_test, predictions)
#     return (JsonResponse(listToString(predictions), safe=False))

@login_required(login_url="/account/login")
def detect_spam(request,listing_id):
        # Save data
        listing = Listing.objects.get(pk=listing_id)
        if request.method == 'POST':
            listing_id = request.POST['listing_id_value']
            comments = request.POST['message']
            type = request.POST['type']
            example_counts = vectorizer.transform(Convert(comments))
            listToString(comments)
            predictions = mdl.predict(example_counts)
            predict = listToString(predictions)
            spam_detection = Spam_filtering( comments=comments,type=predict,user=request.user,listing=listing)
            spam_detection.save()
            print(listToString(type))
            if predict=='spam':
                messages.error(request,"Looks like you have posted something that is spam in comment so your comment cannot be posted! Thank you!")
            else:
                messages.success(request, "Your comment has been posted thank you for your response")


            return redirect('/listings/'+listing_id )
















