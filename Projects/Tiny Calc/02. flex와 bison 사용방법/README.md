# flex와 bison 사용방법

<iframe width="800" height="450" src="https://www.youtube.com/embed/n5Opi1AlPS4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## flex & bison 설치

### MS-Windows

* [winflexbison 다운로드](https://github.com/lexxmark/winflexbison/releases)

### MAC OS

#### for intel chip

```
% brew install bison
```

#### for apple silicon arm64

```
% arch -arm64 brew install bison
```

### Linux (Ubuntu)

```
% sudo apt-get update
% sudo apt install flex
% sudo apt install bison
```

## flex를 이용해서 스캐너 만들기

### 코드 작성 (calc.l)

``` c
%option noyywrap
%option never-interactive

%{
#include <stdio.h>

#define T_FLOAT     1
#define T_INT       2
#define T_PLUS      3
#define T_MINUS     4
#define T_MULTIPLY  5
#define T_DIVIDE    6
#define T_LEFT      7
#define T_RIGHT     8

double fval;
int ival;
%}

%%
[ \t]           ; // ignore all whitespace
[0-9]+\.[0-9]+  {fval = atof(yytext); return T_FLOAT;}
[0-9]+          {ival = atoi(yytext); return T_INT;}
"+"             {return T_PLUS;}
"-"             {return T_MINUS;}
"*"             {return T_MULTIPLY;}
"/"             {return T_DIVIDE;}
"("             {return T_LEFT;}
")"             {return T_RIGHT;}
%%

int main(int argc, char** argv) {
    yy_scan_string("314 * (1.23 + 2)");

    int result = yylex();
    while (result) {
        switch(result) {
            case T_FLOAT: printf("  - T_FLOAT: %g \n", fval); break;
            case T_INT: printf("  - T_INT: %d \n", ival); break;
            case T_PLUS: printf("  - T_PLUS: %s \n", yytext); break;
            case T_MINUS: printf("  - T_MINUS: %s \n", yytext); break;
            case T_MULTIPLY: printf("  - T_MULTIPLY: %s \n", yytext); break;
            case T_DIVIDE: printf("  - T_DIVIDE: %s \n", yytext); break;
            case T_LEFT: printf("  - T_LEFT: %s \n", yytext); break;
            case T_RIGHT: printf("  - T_RIGHT: %s \n", yytext); break;
        }
        result = yylex();
    }
}
```

### 컴파일 및 실행

```
% flex calc.l
% gcc lex.yy.c -o calc
% ./calc
  - T_INT: 314
  - T_MULTIPLY: *
  - T_LEFT: (
  - T_FLOAT: 1.23
  - T_PLUS: +
  - T_INT: 2
  - T_RIGHT: )
```

## 사칙연산 계산기 만들기

### flex 코드 (calc.l)

``` c
%option noyywrap
%option never-interactive

%{
#include <stdio.h>
#include "calc.tab.c"
%}

%%
[ \t]           ; // ignore all whitespace
[0-9]+\.[0-9]+  {yylval.fval = atof(yytext); return T_FLOAT;}
[0-9]+          {yylval.fval = atof(yytext); return T_FLOAT;}
"+"             {return T_PLUS;}
"-"             {return T_MINUS;}
"*"             {return T_MULTIPLY;}
"/"             {return T_DIVIDE;}
"("             {return T_LEFT;}
")"             {return T_RIGHT;}
%%
```

### bison 코드 (calc.y)

``` c
%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
extern int yyparse();

void yyerror(const char* s);
%}

%union {
    float fval;
}

%token<fval> T_FLOAT
%token T_PLUS T_MINUS T_MULTIPLY T_DIVIDE T_LEFT T_RIGHT
%left T_PLUS T_MINUS
%left T_MULTIPLY T_DIVIDE

%type<fval> expression

%%
calculation:
    expression                          { printf("\tResult: %f\n", $1);}
;

expression:
    T_FLOAT                             { $$ = $1; }
    | expression T_PLUS expression      { $$ = $1 + $3; }
    | expression T_MINUS expression     { $$ = $1 - $3; }
    | expression T_MULTIPLY expression  { $$ = $1 * $3; }
    | expression T_DIVIDE expression    { $$ = $1 / $3; }
    | T_LEFT expression T_RIGHT         { $$ = $2; }
;
%%

int main() {
    return yyparse();
}

void yyerror(const char* s) {
    fprintf(stderr, "Parse error: %s\n", s);
    exit(1);
}
```

### 컴파일 및 실행

```
% flex calc.l
% bison calc.y
% gcc lex.yy.c -o calc
% ./calc
2 * (3 + 4)
[ctrl + D]
        Result: 14.000000
```
