import pandas as pd
from t1d.models import *

df = pd.read_excel('C:/Users/travi/Downloads/excludeExtrasPBRC_12-01-2020.xlsx')
subs = list(df['SubjectId'].drop_duplicates())

for s in subs:
    Subject(name=s).save()

filt = df['MealID'].str.len() == 20
meal_df = df[['MealID', 'SubjectId', 'PreDateTime', 'Meal', 'MealDescription']]

for x in range(len(meal_df)):
    Meal(id=meal_df['MealID'][x],
         date=str(meal_df['PreDateTime'][x]),
         subjectid=Subject.objects.get(name=meal_df['SubjectId'][x]),
         name=meal_df['Meal'][x],
         description=meal_df['MealDescription'][x]).save()

imgdf = pd.read_excel('D:/PycharmProjects/Work/data/T1Dexi/tested.xlsx',
                    sheet_name='Sheet1',
                    usecols=['MealID',
                             'SubjectId',
                             'Description',
                             'PreMealImageID',
                             'PreMealImageTime',
                             'PostMealImageTime',
                             'PostMealImageID'])

pre = imgdf[['MealID', 'SubjectId', 'Description', 'PreMealImageID', 'PreMealImageTime']]

post = imgdf[['MealID', 'SubjectId', 'Description', 'PostMealImageID', 'PostMealImageTime']]
filt = post['PostMealImageID'] != 'No Post Image'
post = post[filt]

pre = pre.rename(mapper={'PreMealImageID': 'Id', 'PreMealImageTime': 'Time'},  axis=1)
post = post.rename(mapper={'PostMealImageID': 'Id', 'PostMealImageTime': 'Time'},  axis=1)
imgs = pre.append(post).reset_index()


for x in range(len(imgs)):
    try:
        m = Meal.objects.get(id=imgs['MealID'][x])
        s = Subject.objects.get(name=imgs['SubjectId'][x])
        Image(id=imgs['Id'][x],
              time=imgs['Time'][x],
              mealid=m,
              subjectid=s).save()
    except:
        print(imgs['MealID'][x])
        print(imgs['SubjectId'][x])
        print(x)
