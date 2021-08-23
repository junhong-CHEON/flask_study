# 02-Parameter

## 1) 개요

클라이언트(프론트엔드)로부터 변수를 전송받는 방법

| 전송 방법 | 의미 | 동작 | 관련 SQL | HTML 전송 가능 여부 |
| ---- | --- | --- | --- | --- |
| GET | URL에 `?`이후 `key=value`&`key=value` 형식으로 전송. | READ | SELECT | O |
| POST | HTTP Header에 데이터를 포함시켜 전송 | CREATE | INSERT | O |
| PUT | HTTP Header에 데이터를 포함시켜 전송 | UPDATE | UPDATE | X |
| DELETE | HTTP Header에 데이터를 포함시켜 전송 | DELETE | DELETE | X |

## 2) GET 전송 방법

### Link에 의한 전송

```html
<a href='http://localhost:9901/parameter/get?num1=100&num2=200'>click</a>
```

### `<form>`에 의한 전송

```html
<form method='get' action='http://localhost:9901/parameter/get'>
    <input type='text' name='num1' />
    <input type='text' name='num2' />
    <button type='submit'>submit</button>
</form>
```

### jQuery Ajax에 의한 전송

```js
$.get('http://localhost:9901/parameter/get', {
    num1: 100,
    num2: 200
}, function(req) { ... });
```

## 3) POST 전송 방법

### `<form>`에 의한 전송

```html
<form method='post' action='http://localhost:9901/parameter/get'>
    <input type='text' name='num1' />
    <input type='text' name='num2' />
    <button type='submit'>submit</button>
</form>
```

### jQuery Ajax에 의한 전송

```js
$.post('http://localhost:9901/parameter/post', {
    name: 'foo',
    email: 'bar'
}, function(req) { ... });
```

## 4) PUT, DELETE 전송 방법

Link나 `<form>`에 의한 전송은 불가능함.

jQuery Ajax의 경우도 특수한 코드를 먼저 적용한 후에나 가능함.

### jquery-method-override.js
```js
jQuery.each([ "put", "delete" ], function(i, method) {
    jQuery[method] = function(url, data, callback, type) {
        if (jQuery.isFunction(data)) {
            type = type || callback;
            callback = data;
            data = undefined;
        }
 
        return jQuery.ajax({
            url : url,
            type : method,
            dataType : type,
            data : data,
            success : callback
        });
    };
});
```

위의 코드를 html에서 jquery 다음으로 참조

```html
<script src='//code.jquery.com/jquery.min.js'></script>
<script src='{path}/jquery-method-override.js'></script>
```

그 후 `$.put`, `$.delete` 함수 사용 가능함

```js
$.put('http://localhost:9901/parameter/put', {
    num1: 100,
    num2: 200
}, function(req) { ... });
```

```js
$.delete('http://localhost:9901/parameter/delete', {
    num1: 100,
    num2: 200
}, function(req) { ... });
```

## 5) 데이터 전송 도구 사용하기

매번 post, put, delete를 테스트 할 때 마다 html 페이지를 작성하는 번거로움을 피하기 위한 도구

> https://insomnia.rest/