
# Library Management System 

You can do the basic library operations like add, update, read, delete , search book (CRUD operations). In this project you will also be able to access the entie book database in 2 formats csv and json also updode in both formats(make sure to uplode it in exact same formats as you download). We use PostgreSQL in this project.



## Demo

You can see a Demo of this live website at 

https://library-systems.netlify.app/

(if you are not able to access it you can install the project locally and run it by looking at setup)


## Installation

Install this project using git clone 



step 1) clone the project
```bash
git clone https://github.com/DrumilHV/Library-System.git .
```
step 2) setup you environment varaiables  for both client and server (make one .env file in each client and server directory)

.env (client)
```js
NEXT_PUBLIC_BACKEND_SERVER=
```
(you will have to put the port on which your backend will run)

.env (server)
```python
HOSTNAME=
PORT=
DATABASE=
USERNAME=
PASSWORD=
INTERNAL_DATABASE_URL=
EXTERNAL_DATABASE_URL=
PLSQ_COMMAND=
```
(if you are usign local postgresql server then you will not requre last 3 environment varaiables. but additionally you will have to connect to postgresql using usign the first 5 varaiables by looking at  I have hosted my postgresql database on https://render.com/ so I get the additional urls and psql_command)

step 3) run project

go in client directory and start frontend

```bash
npm install
npm run dev
```

now go to backend and start server

```bash
pip install -r requirements.txt
flask run
```




## Documentation

[Documentation](https://linktodocumentation)


## Components
### Book
```jsx
<Book book={book} sd={true}/>
```
The Book Component shows renders a single book which is passed in the prop book. 
```js
sd=
```
prop which is short for shortdescreption take boolen value , to render shortdescreption or not, if true renders shortdescreption else rendes long descreption.
```js
book = {
    title: string,
    isbn: string,
    pagecount: int,
    publisheddate: date,
    thumbnailurl: string,
    shortdescription: string,
    longdescription: string,
    status:  string, //either 'PUBLISHED' OR 'NOT PUBLISH'
    authors: string[],
    categories: string[],
    paid: string,// either 'PAID' OR 'FREE'
    price: int,
}
```
this is the format of book object when building a csv file or json file to uplode data in bulk please refer this once and uplode data only in the same way you downloded it. 

### Navbar

```jsx
<Navbar />
```
does not take any prop has two major Components one is logo and other is Search bar.

### Sidebar
```jsx
<SidebarCostum setEndDate={setEndDate} setStartDate={setStartDate} setGenre={setGenre} setOrder={setOrder}setPaid={setPaid} getQueryResult={getQueryResult} />
```
**setStartDate, setEndDate**: useState Components
```jsx
setStartDate(2010)
setEndDate(2013)
```
takes an useState component which sets start and end date respectively.

**setGenre**: useState Component
```jsx
setGenre("java")
```
takes a useState component which is to take user input for gener(string).

**setOrder**: useState Component
```jsx
setOrder("asc")
```
the argument it takse sets the order either ascending or decending while retreving teh query

**setPaid**:  useState Component
```jsx
setPaid('FREE')
```
the argument it takes will send either 'PAID' OR 'FREE' for querying the data

**getQueryResult**: Function which which will take all the requirements and get query result and send it to query page to show the desired result

### Searchbar

```jsx
<Searchbar />
```
does not take any proprs , when enterd a string will redirect you to results page. 


