"""
Строитель - это пораждающий патер проектирования, когда вознимает такая ситуация
что конструктор класса очень большой и у него есть много условий. тоесть создания обьекта
сложный и опцыональный прцоесс. Тогда используеться патер проектирования строитель

Думаю не самый лучшый примерно, но +- пойдет, все примеры которые встречал очень абстрактные
а SQL конструктор +- что то с области релаьного

"""


"""SQL запрос"""
class SQLQuery:
    def __init__(self):
        self.select_clause = ''
        self.from_clause = ''
        self.where_clause = ''
        self.goup_by_clause = ''
        self.order_by_clause = ''
        self.limit_clause = ''
        self.query_clause = ''

    def __str__(self):
        return self.query_clause
    
"""Строитель запросов"""
class SQLBilder:
    def __init__(self):
        self.sql_query = SQLQuery()

    def select(self, columns):
        "columns = [] or '*' "
        if columns == '*':
            self.sql_query.select_clause = 'SELECT * '
        if type(columns) == list:
            self.sql_query.select_clause = f'SELECT {', '.join(columns)}'

        return self
    
    def from_table(self, name_table):
        self.sql_query.from_clause = f'FROM {name_table}'
        return self

    def where(self, condition):
        self.sql_query.where_clause = f'WHERE {condition}'
        return self
    
    def goup_by(self, columns):
        self.sql_query.goup_by_clause = f'GROUP BY {columns}'
        return self

    def order_by(self, column, order='ASC'):
        self.sql_query.order_by_clause = f'ORDER BY {column} {order}'
        return self
        
    def limit(self, limit):
        self.sql_query.limit_clause = f'LIMIT {str(limit)}'
        return self
    
    def bild(self):
        self.sql_query.query_clause = self.sql_query.select_clause

        if self.sql_query.from_clause:
            self.sql_query.query_clause += f' {self.sql_query.from_clause}'

        if self.sql_query.where_clause:
            self.sql_query.query_clause += f' {self.sql_query.where_clause}'

        if self.sql_query.goup_by_clause:
            self.sql_query.query_clause += f' {self.sql_query.goup_by_clause}'

        if self.sql_query.order_by_clause:
            self.sql_query.query_clause += f' {self.sql_query.order_by_clause}'

        if self.sql_query.limit_clause:
            self.sql_query.query_clause += f' {self.sql_query.limit_clause}'

        return self.sql_query


# SELECT name, year FROM users WHERE name = "yura" LIMIT 10
bildersql = SQLBilder()
sqlquery = bildersql.select(['name', 'year']).from_table('users').where('name = "yura"').limit(10).bild()

# SELECT *  FROM Users
bildersql = SQLBilder()
sqlquery2 = bildersql.select('*').from_table('Users').bild()

print(sqlquery)
print(sqlquery2)


# Второй пример, использования строителя для HTTP запросов (method, url, headers, params, body)
import requests

class HttpRequest:
    def __init__(self):
        self.method = 'GET'
        self.url = ''
        self.headers = {}
        self.params = {}
        self.body = None

    def send(self):
        response = requests.request(
            method=self.method,
            url=self.url,
            headers=self.headers,
            params=self.params,
            json=self.body
        )
        return response
    
class HttpRequestBuilder:
    def __init__(self):
        self.request = HttpRequest()

    def set_method(self, method):
        self.request.method = method
        return self

    def set_url(self, url):
        self.request.url = url
        return self

    def add_headers(self, kay, value):
        self.request.headers[kay] = value
        return self

    def add_params(self, kay, value):
        self.request.params[kay] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def bild(self):
        return self.request


# Пример использования
bilderHttp = HttpRequestBuilder()
http_requrst = (bilderHttp
    .set_method('GET')
    .set_url('https://jsonplaceholder.typicode.com/posts')
    .add_headers('Content-Type', 'application/json')
    .set_body({
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    })
    .bild())


response = http_requrst.send()
print("Статус код:", response.status_code)
print("Ответ:", response.json())



