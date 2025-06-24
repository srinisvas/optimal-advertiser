interests_target_grouping = {

"young adults" : {"gaming", "music", "business and entrepreneurship", "finance and investments", "fashion", "beauty"},
"family oriented" : {"gardening", "social causes and activism", "art", "history", "movies", "cooking", "pets", "parenting and family", "politics", "art", "diy and crafts"},
"travel lovers" : {"photography", "travel", "food and dining"},
"fitness lovers" : {"outdoor activities", "health and wellness", "nature", "sports", "fitness"},
"tech enthusiasts" : {"education and learning", "technology", "books", "science", "cars and automobiles"}

}

lookup_target = {
    interest.lower(): group
    for group, interests in interests_target_grouping.items()
    for interest in interests
}

interests_topic_grouping = {

"travel" : {"photography", "travel", "food and dining", "books"},
"fashion" : {"fashion", "beauty", "art"},
"electronics" : {"gaming", "music", "movies"},
"health" : {"outdoor activities", "health and wellness", "nature", "sports", "fitness"},
"automotive" : {"technology", "science", "cars and automobiles"}

}

lookup_topic = {
    interest.lower(): group
    for group, interests in interests_topic_grouping.items()
    for interest in interests
}