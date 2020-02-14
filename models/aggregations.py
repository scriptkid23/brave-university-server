
GROUP_SCORE = [
    {
        '$group': {
            '_id': '$years', 
            'count': {
                '$sum': 1
            }
        }
    }
]

GET_LIST_SCORE = [
    {
        '$match': {
            'years': '2018-2019', 
            'hk': 1
        }
    }, {}
]
