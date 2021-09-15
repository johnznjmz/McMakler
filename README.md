# McMakler coding challenge

Challenge to create an API with an endpoint '/get-stats', with endpoint params: 
1. field: a column from the dataset (e.g. MSZoning), 
2. method: "values" (how many unique values), "common" (most common or frequent value)
with an acceptable output is always a column "result"

For input:
{
"column": "MSZoning",
"method": "values"
}

Expected output:

{
"result": 5
}

## Requiremnets

Django==3.2.7
djangorestframework==3.12.4

## Sreenshots

![values](https://user-images.githubusercontent.com/38066495/133392953-833e542d-4559-4e52-99a6-e361b657a09a.PNG)

![common](https://user-images.githubusercontent.com/38066495/133392968-ec71cf55-33b4-42a1-948f-c8b3cdb0f995.PNG)
