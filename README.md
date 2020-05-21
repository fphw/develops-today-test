# develops-today-test
Task deploing on next url: https://developtodaytest.herokuapp.com/

All API code stored in folder newsBoard/news
1.Using CURD API for manage post:
  1) Get all posts '/api/v1/news/articles/'
  2) Create new post '/api/v1/news/articles/create/'
  3) Update post '/api/v1/news/articles/update/id' id - id of concreet post
  
2. Using CURD API for manage coments:
  1) Get all posts '/api/v1/news/comments/'
  2) Create new post '/api/v1/news/comments/create/'
  3) Update post '/api/v1/news/comments/update/id' id - id of concreet comment
  
Examples of JSON add new article:

{
	"title": "New article from another author asdad1111",
	"link":"http://www.somerandlink.com",
	"creation_date": "2020-05-21T09:34:38.898985+03:00",
	"author":1,
	"likes":2
}
