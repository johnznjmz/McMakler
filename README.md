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

Epected output:

{
"result": 5
}

## Requiremnets

Django==3.2.7
djangorestframework==3.12.4
