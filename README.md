# flaskApi
flaskApiTest

A Simple Flask API Example.

News Related
[GET] http:yourhost:5000/api/v1/News --> to get all the news that is available in Database
[POST] http:yourhost:5000/api/v1/News --> Add Some New News Json Data {"title":"xx","article":"news Article","status":1}
[PUT] http:yourhost:5000/api/v1/News --> Modify some news Data {"id":1,"title":"xx","article":"news Article","status":1}
[DELETE] http:yourhost:5000/api/v1/News --> Hard Delete Some News Data {"id":1,"title":"xx","article":"news Article","status":1}

Topic Related
[GET] http:yourhost:5000/api/v1/Topic --> to Get All the available Topic
[POST] http:yourhost:5000/api/v1/Topic --> Add Some New Topic to Database using Json Data {"topicname":"politik"}
[PUT] http:yourhost:5000/api/v1/Topic --> modify some Topic Data using Json Data {"id":1,"topicname":"politik"}
[DELETE] http:yourhost:5000/api/v1/Topic --> delete some Topic Data {"id":1,"topicname":"politik"}

Status Related
[GET] http:yourhost:5000/api/v1/Status --> to Get All the available Status
[POST] http:yourhost:5000/api/v1/Status --> Add Some New Status to Database using Json Data {"statuscode":"draft"}
[PUT] http:yourhost:5000/api/v1/Status --> modify some Status Data using Json Data {"id":1,"statuscode":"draft"}
[DELETE] http:yourhost:5000/api/v1/Status --> delete some Status Data {"id":1,"statuscode":"draft"}

Topic News (Relation Table Between Topic To News)
[POST] http:yourhost:5000/api/v1/TopicNews --> Add Some Relation Topic To News to Database using 
Json Data {"idNews":1,"idTopic":"1,2,3"} #Topic Could be More Than one

News By Topic
[GET] http:yourhost:5000/api/v1/News/<string:topic> ex: http:yourhost:5000/api/v1/News/"1,2,3" --> news by Topic Id 1,2,3

News By Status
[GET] http:yourhost:5000/api/v1/News/<int:id> ex: http:yourhost:5000/api/v1/News/1 --> news by Status Id 1

Roland Antonius Kondoy

PS : Not Uploaded Yet To Heroku
