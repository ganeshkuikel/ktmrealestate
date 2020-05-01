from django.shortcuts import redirect
from sklearn.metrics import accuracy_score
from .models import Spam_filtering
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from .serializers import Spam_filteringSerializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from sklearn.externals import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer =self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        return Response(token.key)




# data=pd.read_csv("C:/Users/Ganesh/Documents/fyp/spam.csv",encoding='latin',error_bad_lines=False)
# newdata=data[['v1','v2']]
# # Replacing columns names
# newdata.rename(columns={
#     'v1':'result',
#     'v2': 'comments'
# },inplace=True)

vectorizer = CountVectorizer()
mdl=joblib.load('C:/Users/Ganesh/Documents/fyp/spam_model.pkl')
X=pd.read_excel('C:/Users/Ganesh/Documents/fyp/test.xlsx')
X=X[['result','comments']]
DF = pd.DataFrame(X)
y_pred=vectorizer.fit_transform(DF['comments'])
mdl.fit(y_pred,DF['result'])
y_test=mdl.predict(y_pred)
accuracy=accuracy_score(y_test, DF['result'])
print('Accuracy: %f' % (accuracy*100))


# newdata['numerical_label'] = newdata.result.map({'ham':0, 'spam':1})
#
# model_var=['result','comments','numerical_label']
# datas=newdata[model_var]
#
# data_relevant_method=pd.get_dummies(datas)


# def preprocessing_tech(text):
#     data = text.lower()
#
#     data = ''.join([t for t in text if t not in string.punctuation])
#
#     data = [t for t in text.split() if t not in stopwords.words('english')]
#
#     st = Stemmer()
#     data = [st.stem(t) for t in text]

#     return data
# newdata['comments'].apply(preprocessing_tech)
# x_train, x_test, y_train, y_test = train_test_split(newdata['comments'], newdata['result'], test_size=0.2,
#                                                             random_state=21)
#
# vectorizer = CountVectorizer()
#
# vectorized_text = vectorizer.fit_transform(x_train)
#
# classifier = MultinomialNB()
# classifier.fit(vectorized_text, y_train)
#
# convert_to_vector = vectorizer.transform(y_test)
# predictions_test_class = classifier.predict(convert_to_vector)
#
# print(classification_report(predictions_test_class, y_test))
#
# accuracy_score(y_test, predictions_test_class)
#
# print(y_test.shape)
# confusion_matrix(y_test, predictions_test_class)




# newdata.groupby('numerical_label').describe()

# newdata.head()

# ham = newdata[newdata.numerical_label==0]
# spam = newdata[newdata.numerical_label==1]




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
def api_sentiment_pred(request):
    comment = request.GET['comments']
    example_counts = vectorizer.transform(Convert(comment))
    listToString(comment)
    predictions = mdl.predict(example_counts)
    print(predictions)
    return (JsonResponse(listToString(predictions), safe=False))

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

            # if request.user.is_authenticated:
            #
            #     user_id = request.user.id
                # has_contacted = Contact.objects.all().filter(user_id=user_id,listing_id=listing_id)
                # if has_contacted:
                #     messages.error(request, "You have already commented for this listing")
                #     return redirect('/listings/'+listing_id)
            # else :
            #     messages.error(request, "You Need to first login")
            #     return redirect('/login/')
            # if not request.user.is_authenticated:
            #     messages.error(request, "You Need to first login")
            #     return redirect('/login/')

                # user_firstname = request.user.first_name
                # user_lastname = request.user.last_name
            spam_detection = Spam_filtering( comments=comments,type=predict,user=request.user,listing=listing)
            spam_detection.save()
            print(listToString(type))
            if predict=='spam':
                messages.error(request,"Looks like you have posted something that is spam in comment so your comment cannot be posted! Thank you!")
            else:
                messages.success(request, "Your comment has been posted thank you for your response")


            return redirect('/listings/'+listing_id )









class SpamView(viewsets.ModelViewSet):

    queryset = Spam_filtering.objects.all()
    serializer_class = Spam_filteringSerializers




class SpamList(APIView):

    def get(self,request):
        model = Spam_filtering.objects.all()
        serializer = Spam_filteringSerializers(model,many=True)
        return Response(serializer.data)




    def post(self,request):
        serializer = Spam_filteringSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

















