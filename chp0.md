---
title: "Chp0"
date: 2020-04-12T22:34:04+08:00
draft: true
author: bunshinn
---

## Python简介
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.



### 装饰器
```py
def bold(s):
	def wrapped():
		return '<b>' + s() + '</b>'
	return wrapped

@bold
def hw():
	return "hello,world"

```